# Builds the plain-language (non-specialist audience) variant of the IEEE
# report from an embedded spec, writing report_spec_plain.json alongside.
# Same layout code as build_report_ieee.py; different content strings.
import json, re
from pathlib import Path
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, Inches
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = Path(__file__).parent

TITLE = "StudyMate: How a From-Scratch AI Study Assistant Reasons, Remembers, and Stays in Its Lane"
AUTHOR = ("Bagus Trilaksono  |  AI Engineering Lab, Chair of AI Engineering, University of Passau  |  "
          "SoSe 2026  |  Individual written report, September 2026")

ABSTRACT = ("StudyMate is an AI study assistant built from scratch in Python 3.12 for the AI Engineering Lab "
            "at the University of Passau. A student drops lecture slides and exercise sheets into a folder, and "
            "the assistant reads them and produces organized, interlinked notes, flashcards, and summaries. "
            "This report explains, for a non-specialist reader, how the assistant decides what to do step by "
            "step inside a sandboxed tool environment, how it manages memory in both senses: the working "
            "context it keeps for the current conversation and the long-term record it keeps across sessions, "
            "what the team built beyond the minimum requirements of the lab, and which extensions were "
            "considered and deliberately not pursued, with reasons.")
INDEX_TERMS = ("agent harness, ReAct, long-term memory, context compaction, retrieval-augmented generation, "
               "Model Context Protocol, observability.")

B = []
def H(level, text): B.append({"type": "heading", "level": level, "text": text})
def P(text): B.append({"type": "paragraph", "text": text})
def NOTE(text): B.append({"type": "paragraph", "runs": [{"text": text, "italic": True}]})
def BL(items): B.append({"type": "bullet_list", "items": items})
def TBL(header, rows): B.append({"type": "table", "header": header, "rows": rows, "style": "Table Grid"})

H(1, TITLE)
P(AUTHOR)

H(2, "I. Introduction")
P("StudyMate is a study assistant for one job. A computer science student puts lecture slides, PDFs, and "
  "exercise sheets into a folder that the assistant can read but never change. The assistant reads the "
  "material and returns a small library of organized notes: concept pages that cross-reference each other, "
  "lecture summaries, flashcards, and diagrams. Afterwards it can check its own work for broken cross-"
  "references, and it can quiz the student on the material until weak spots surface. The parts that do the "
  "thinking are a rented commodity; the interesting system is everything we built around them. That "
  "everything is what an agent harness is: the memory, the toolbox, the ground rules, and the record-keeping "
  "that turn a raw text-generating model into a worker you would let near your files.")
P("We wrote the harness ourselves in Python, without an agent framework; the only third-party runtime pieces "
  "are the model's API client and a standard bridge to external plugins. The lab brief breaks such a system "
  "into loop, context, tools, skills, long-term memory, hooks, permission management, sandboxing, and sub-"
  "agents. StudyMate implements all of them, which is why we can say honestly that we know how it works: we "
  "made every part.")
P("This report has two halves. The first half explains the assistant's decision loop (Section II) and its "
  "memory handling, both the working kind and the keeping kind (Section III); memory was the part assigned to "
  "me. The second half describes where the team exceeded the minimum requirements of the lab (Section IV) and "
  "which extensions we considered and did not pursue, with our reasons (Section V). All claims refer to the "
  "repository as delivered at the end of week 3: roughly 7,800 lines of Python under src/study_agent, with a "
  "test suite of the same size class.")

H(2, "II. The Decision Loop")
H(3, "II.A. One step at a time, with a hard budget")
P("All of the assistant's self-discipline lives in one file, core/engine.py (693 lines). A run starts when "
  "the user types something. The engine adds it to the running record of the conversation and enters a loop "
  "that repeats at most 50 times, the budget set in configuration. Fifty steps sounds generous until you "
  "have watched a model spend twenty of them chasing a mistake; the number is there so that a confused "
  "assistant stops and reports rather than working forever. Each round through the loop has five stages.")
BL([
  "Guard. Before consulting the model, the engine checks whether the conversation is getting too big for the "
  "model's attention and, if so, compresses the older parts first (Section III.B). Housekeeping happens "
  "before the work, not after a failure, with one exception on the overflow-retry path below.",
  "Reason. The model is asked, with the full conversation plus a catalog of available tools, what should "
  "happen next. The answer is either a text reply, a batch of requested actions, or a reply so broken or "
  "empty we treat it as its own case.",
  "Gate. A requested action never reaches a tool directly. Every one of them passes through one front door, "
  "ToolRegistry.execute(), which first checks it against the permission rules. An allowed action proceeds "
  "silently. A denied one, or one the user declines to approve, comes back to the model as a readable error "
  "that also tells it not to retry that exact action (Section II.B).",
  "Act. Actions that clear the gate are carried out. If one crashes anyway, the engine catches the crash "
  "and converts it into an error message rather than letting the run fall over.",
  "Observe. The result of each action, good or bad, is appended to the conversation, and the loop starts "
  "the next round with the model seeing what just happened.",
])
P("A plain text reply ends the run; that is the normal, successful exit. The engine records which of four "
  "exits happened (success, out of budget, empty reply, or error) because those need answering to different "
  "people: \"the model gave up\", \"the model looped\", and \"the plumbing broke\" look very different in "
  "the monitoring dashboards of Section IV. Two recovery paths are built in. If the model sends an empty "
  "message, the engine injects a synthetic user message (\"Your last response was empty. Continue the "
  "requested task now.\") and keeps looping rather than handing the student a blank answer. If the provider "
  "rejects a request because the conversation outgrew the model's context window despite the compression "
  "check, the engine forces one compaction and retries that step exactly once; a second rejection ends the "
  "run.")
H(3, "II.B. One front door for every action")
P("The toolbox is a contract, not a pile of functions. Every capability the model may use (read a file, "
  "extract text from a PDF, create a folder, search inside documents) must register with a name, a "
  "description the model can read, and a declared list of arguments it accepts. A tool answers in plain "
  "text, and by convention it reports failure by returning a message that starts with \"Error\" instead of "
  "crashing. The front door enforces the rules of the contract: lookup, permission gate, execution with a "
  "catch-all net that turns surviving crashes into readable error messages, and timing metrics. The benefit "
  "is that the model always gets something it can read and act on (the lab materials call this communicating "
  "failures upstream), and the loop cannot die mid-step because a tool threw an exception.")
P("The same front door is where the permission system we added in week 3 attaches. When rules are "
  "configured, each action is checked against an ordered list (first match wins, and anything unmatched "
  "defaults to asking the user). Allowance proceeds silently; denial and user-refusal return error "
  "observations telling the model not to retry. One detail matters for safety: if the rules call for a human "
  "confirmation and no human is available to answer (an automated test run, or a dialog that itself broke), "
  "the action is treated as denied, never as approved. Fail-closed, in the brief's word.")
H(3, "II.C. Watching the loop without touching it")
P("The instrumentation is bolted on, not woven in. The engine offers a list of callbacks that fire when a "
  "run starts and ends and when each tool starts and finishes; the registry offers one for permission "
  "decisions. The monitoring pieces (counters, per-run log files, the Langfuse exporter) subscribe to those "
  "hooks when the program is assembled. If a listener crashes, the failure is caught and logged at the seam: "
  "a broken monitor cannot break a run. This is the decoupled lifecycle-hook mechanism the week 3 brief "
  "lists, and it pays off in our daily work: the same engine code runs unmonitored inside unit tests and "
  "fully watched inside the Docker compose stack, without a single if-statement about which world it is in.")
H(3, "II.D. It always ends")
P("Every path through the loop returns something. The step budget bounds the common case; infrastructure "
  "errors travel up to the command line after the current trace is closed; empty replies re-enter the loop "
  "but remain bounded by the budget; denials are phrased so the model learns not to knock on the same door "
  "again, which quietly stops it from spending the entire budget retrying a refused action. In practice, "
  "with the qwen-agentworld-35b-a3b model, we rarely bump the cap. Delegation is the exception: when one "
  "agent assigns a subtask to another (Section IV), long runs with large step counts genuinely happen.")
NOTE("[Editor notes: figure 1 = loop state-machine diagram (states: guard, reason, gate, act, observe; "
     "exits: success/empty/max-iterations/error). Insert before submission. Optional: a real run excerpt "
     "from observability/traces.jsonl once fresh runs are generated.]")

H(2, "III. Memory")
H(3, "III.A. The two kinds, and the filing cabinet between them")
P("We split memory the way the lab materials do. Short-term memory is the conversation window itself: the "
  "standing instructions, the message history, the tool catalog, everything the model \"sees\" on the next "
  "call. Long-term memory is everything filed outside that window, which survives a restart. The design "
  "work happens at the boundary: what is worth writing out, when to read it back in, and how much room each "
  "kind gets inside the window. StudyMate keeps three long-term stores, matching the standard taxonomy of "
  "episodic records (what happened), declarative facts (what is true), and procedural skills (how we work), "
  "in one SQLite database file and one folder of text files.")
H(3, "III.B. The attention span: assembling it, then compressing it")
P("ContextManager (core/context.py) keeps one leading instructions message: the assistant's persona and "
  "house rules from config/soul.md, the current date, and a slot for injected memories. One implementation "
  "detail we found the hard way: the serving stack rejects a second instructions block (\"System message "
  "must be at the beginning\"), so every injection, and there are several per session (recent facts at "
  "startup, matched routines per turn), re-renders that first message instead of adding new ones. An "
  "injected per-turn block is explicitly cleared afterward, so a routine matched on one exchange cannot "
  "leak into the next.")
P("Compaction (core/compaction.py) is the fight against context rot: the slow decay of an assistant that "
  "forgets what it said thirty messages ago once its window fills with noise. The trigger is an estimate of "
  "the next request's size, counting all message text plus the serialized tool catalog at four characters "
  "per token. That is a heuristic, and we treat it as one: cheap, deterministic, and wrong in the safe "
  "direction, with the loop's overflow-retry path as the backstop. The check fires at 80% of the model's "
  "window; the window itself is resolved through a precedence chain we kept from a design note (an explicit "
  "entry in the configuration file wins; failing that, a best-effort lookup against the gateway's model-info "
  "route; failing that, a size suffix parsed from the model's name; failing that, a conservative 128k "
  "default with a startup warning). Which layer answered gets logged and shown in /config, because a wrong "
  "window silently misplaces every later threshold.")
P("When compaction runs, it tries the cheap trick first. Tier one blanks out old, bulky tool outputs, "
  "keeping only the recent window, and replaces each with a placeholder that says where the full text was "
  "filed. This costs no API call, and it is often enough, because a PDF dump or a search result usually "
  "dominates the budget. Tier two, if the estimate is still over the line, hands the old turns to the same "
  "model (tools switched off) with a request to summarize them under fixed headings (Goals, Decisions, "
  "Artifacts created with exact paths, Pending work, Referenced memory topics), and rebuilds the "
  "conversation as: instructions, that summary, the last ten messages. Two properties are deliberate. The "
  "summary is labeled \"historical context, not new instructions\", because it enters as a user message and "
  "a compressed past directive must not masquerade as a live order. And because a summarizer call inside "
  "every long run costs money and adds a second failure mode, there is a once-per-run limit and a breaker "
  "that disables the call after two consecutive failures.")
P("Nothing is lost: the compacted turns stay in the thread database (III.C), which holds the full "
  "transcript, and the summary is archived there too. Compression trades attention space, not history.")
H(3, "III.C. Episodic: conversations that can be resumed")
P("Every message of every run is appended to a per-thread table in workspace/artifacts/memory/memory.db "
  "while the session is live, so the store doubles as the replay source the compaction archive points at. "
  "Threads are named from their first message, browsable with an arrow-key picker (/threads), resumable "
  "(/thread 3 restores the transcript into the conversation), and archived with a flag rather than deleted, "
  "which keeps the whole harness on one rule it never breaks: nothing gets thrown away. The practical test "
  "we hold it to: quit the application, restart, resume the thread, and say \"continue where we left off\"; "
  "the assistant should still know which lecture it was processing without being re-told.")
H(3, "III.D. Facts: what is true about the student")
P("The lab brief asks specifically how long-term memory is written and read, so we state the policies "
  "exactly. Writing has two channels. The model calls the memory_store tool when the student says "
  "\"remember ...\" or when a lasting preference, struggle, or goal surfaces; the assistant's standing "
  "instructions forbid storing conversation ephemera and limit it to things worth surviving a restart for. "
  "The harness stamps provenance (thread id and name) itself, and the tool offers no fields for it, so the "
  "model cannot forge where a fact came from. The store enforces, inside one database transaction, that the "
  "same topic-plus-fact pair cannot exist twice: an exact duplicate does not add a second copy but revives "
  "the archived original if there is one, and fills in a missing meaning-fingerprint. Facts longer than "
  "2000 characters are refused, so no single dump can hijack the block of memories injected into every "
  "future conversation.")
TBL(["Trigger", "What happens", "Budget"],
    [["Startup", "The five most recent facts are merged into the instructions block", "fixed slot, five facts"],
     ["Per turn", "Approved routines whose trigger phrases match the user's text are injected", "max 2 routines, 4000 characters"],
     ["Model-initiated", "The assistant calls memory_recall: keyword search first, meaning-based search second, a reranking model reorders the merged list", "page size, then candidate limit"]])
P("Reading happens on the three triggers in the table. The model-initiated path deserves the most "
  "attention. Recall runs a keyword search first, because exact matches are precise and free; then a "
  "meaning-based search, in which every stored fact carries a numeric fingerprint (an embedding) computed at "
  "write time and the question gets one too, so facts that paraphrase the idea without sharing a single "
  "word still surface. The two result pages are merged and handed to a third model, a reranker, which "
  "reorders candidates by true relevance to the question. Recall thus involves three models: the "
  "8-billion-parameter embedder at write time, the 4-billion reranker at read time, and the chat model at "
  "use time. One API key covers all three because the provider grants access per model server-side.")
P("Graceful degradation is load-bearing, because the embedding and reranker access are per-model grants "
  "that can be missing. Without an embedder, configured or merely failing, recall falls back to keyword "
  "hits and tells the model in the observation that vector search is unavailable, so the assistant can tell "
  "the difference between \"no facts exist\" and \"the semantic search could not run\". Without a reranker, "
  "the merged order stands. Facts stored before embeddings existed are backfilled lazily, one hundred per "
  "recall, so a mid-term database upgrade converges to fully embedded without a migration step. Every "
  "fallback path has a test.")
H(3, "III.E. Routines: how we do things here")
P("The procedural memory, routines the assistant teaches itself, is deliberately boring: plain Markdown "
  "files in workspace/artifacts/procedures/, committed to git and reviewed like code. A routine has a header "
  "block (name, trigger phrases, scope, version, status, what it supersedes) and a body (steps, rationale, "
  "pitfalls, example), parsed by study/procedures.py. Matching is case-insensitive substring search of the "
  "user's message against the name, triggers, and scope of non-archived routines, sorted by name and capped "
  "at two routines and 4000 characters of injected text. We kept it that simple on purpose: cheap, "
  "reviewable, and it never surprises anyone. Status controls disclosure. Approved routines are injected and "
  "followed. Drafts (where every agent-distilled routine starts) are surfaced for confirmation but never "
  "followed silently, and only a human promotes them, by editing one field. Versioning is git plus a "
  "supersedes field, because files can be edited but not deleted by policy.")
P("The line between facts and routines follows the declarative/procedural split in the lab materials. "
  "Facts answer \"what is true about this student\"; routines answer \"how do we do X here\". Only facts go "
  "through the fingerprinting machinery: routines are short enough that a trigger phrase and a size cap are "
  "adequate search, and keeping them as plain files means the student can read, and audit, everything the "
  "assistant has taught itself.")
H(3, "III.F. Why this design, and what it costs")
P("The alternative we did not take was a dedicated external vector database (Chroma, or the Postgres "
  "already running for Langfuse) with a proper search index. We chose SQLite plus the sqlite-vector "
  "extension because the entire memory subsystem then lives inside the existing sandbox, needs no new "
  "service to operate, and inherits the same append-only, no-delete policy as the filesystem. The tradeoff: "
  "meaning-based search is a linear scan over the facts table. At one student's scale (a few hundred facts) "
  "that is invisible; we never stress-tested past the low thousands, and it is the first thing we would "
  "replace in a multi-user deployment.")
NOTE("[Editor notes: figure 2 = memory architecture (context window / compaction tiers / threads+facts+"
     "procedures / embed+rerank loop). Re-verify the store/read table against final code before submission.]")

H(2, "IV. Beyond the Minimum Requirements")
P("The lab states plainly that meeting the weekly minimums caps the grade. This section lists what the team "
  "built that no bullet in the brief requires, with the evidence for each. Everything below is on the main "
  "branch as delivered at the end of week 3.")
H(3, "IV.A. Building a product, not just plumbing")
P("The Week 1 minimum is an assistant that can walk a filesystem. We spent part of the same week turning it "
  "into an actual study product: the note templates that give every generated page a consistent shape, the "
  "vault linter that walks the finished library and reports broken cross-references, orphan pages, missing "
  "metadata, and open questions (the generate-then-verify pattern from the background text, applied to a "
  "knowledge base instead of a test suite), and the three-level Socratic quiz engine in study/griller.py. "
  "The /ingest, /lint and /grill commands are canned instructions to the same assistant, which keeps the "
  "product layer thin over the engine.")
H(3, "IV.B. Depth inside the required components")
P("Several minimum requirements look small on paper; we did not read them that way. The Week 2 memory "
  "minimum is store-once, retrieve-later in one stated mechanism; we shipped three kinds of long-term "
  "memory (Section III) with two-stage, meaning-aware search behind them. The Week 2 plugin minimum is one "
  "connected external server plus one added tool; we run an external DuckDuckGo search server over a "
  "standard bridge and wrote our own nine-tool server for the note library (anchored section edits, "
  "backlink and outgoing-link queries), which the assistant consumes through the same front door and "
  "permission gate as the built-in tools. The Week 3 permission minimum is the three outcomes; our policy "
  "adds rule tiers, pattern matching on arguments, session-scoped \"always\" allowances recorded as their "
  "own metric, and the fail-closed default that automatically covers every future plugin nobody wrote a "
  "rule for. The sub-agent minimum is delegation on the same harness with its own limits and permissions; "
  "we added per-role tool profiles (the examiner agent is read-only by construction, so it cannot tamper "
  "with the work it grades) and trace correlation, so a delegation shows up as one tree in the dashboard "
  "rather than two unrelated runs. The observability minimum is Prometheus, a scrape config, and any "
  "dashboard; we added per-run JSON log files, best-effort export to hosted Langfuse, a background health "
  "check for the external servers, and a provisioning script that rebuilds the dashboard widgets, so the "
  "whole monitoring stack is reproducible on a teaching-assistant machine.")
P("Context compaction and thread resumption are not required at all. In the lab's taxonomy they are the "
  "\"context\" component done properly, and on long sessions they changed the assistant's day-to-day "
  "behavior more than any single feature did.")
H(3, "IV.C. Engineering practices we were not asked for")
P("Mock versions of the model, the embedder, the reranker, and the plugin path let all 261 automated tests "
  "run offline and deterministically, which is what makes touching the instrumented loop safe. Tool "
  "descriptions and the assistant's standing instructions encode behavior lessons from our own runs (for "
  "example, search-discipline rules that stop the model from baking invented years into web queries) and are "
  "treated as part of the product: edited, reviewed, and tested like code. And the no-delete rule holds "
  "across every subsystem at once: files are never deleted, threads and facts archive with tombstone flags, "
  "routines are superseded rather than removed, and the cheap compaction tier prunes the assistant's view "
  "rather than the data.")
NOTE("[Editor notes: every claim here is checkable in code; pull 1-2 numbers from freshly generated runs "
     "(e.g. token savings from a compaction event, a delegation trace screenshot) to make this section "
     "evidence-backed rather than list-shaped. Team attribution: Bagus (git: putra01) owns [FILL IN modules] "
     "and can vouch for the rest through code review.]")

H(2, "V. Extensions Considered but Not Pursued")
P("The brief asks what we left out and why. Every item below was either rejected on purpose or never "
  "reached; the status column says which, and where a decision exists, the reason is ours.")
TBL(["Extension", "Status", "Reason"],
    [["Exact token counting instead of our size estimate", "Considered, rejected for now",
      "The provider serves the chat models without exposing their tokenizers; a server-side count call per "
      "step adds latency to protect a threshold the overflow-retry path already backstops. Cost/benefit was "
      "wrong at lab scale."],
     ["Autonomous ingestion watcher (a new file dropped into the folder starts the ingest by itself)",
      "Wanted from week 1, not pursued",
      "The blocker turned out to be our own safety model. Ingestion is a long, file-writing run, and in an "
      "unattended context the fail-closed gate denies every action that needs a confirmation, so an "
      "autonomous watcher would either be inert or require weakening exactly the gate we built in week 3. On "
      "top of that, naive folder polling fires on half-copied files, and every unattended run spends real "
      "quota on a shared cluster with nobody watching. We preferred a human deciding what enters the "
      "knowledge base, but we never designed the review-on-completion flow that would make unattended runs "
      "acceptable; that is the missing piece, not the watcher."],
     ["External vector database (Chroma, pgvector)", "Considered, rejected",
      "A new service to operate, in place of one table we scan linearly at a few hundred rows. Would only "
      "pay off with many users or heavy vaults. See III.F."],
     ["Explicit up-front planning phase", "Considered, not pursued",
      "The background text mentions planning as a loop extension. We tested prompt-level planning early and "
      "the 35B model's plans drifted from its actions within a few iterations; standing instructions plus "
      "the observe-and-adjust loop gave us more reliable behavior for the effort."],
     ["Automatic approval of new routines by another model", "Not pursued",
      "Approval is a human edit deliberately. Procedural memory silently rewriting what the assistant does "
      "next is the failure mode most worth preventing in a study tool."],
     ["Memory consolidation and decay", "Deferred",
      "Facts deduplicate on exact text but never merge or age out; near-duplicates accumulate. Needs an "
      "offline job with a quality bar we could not test in three weeks."],
     ["Correcting or overwriting stored memories", "Deferred",
      "Append-only is a safety invariant here; a correction path means deciding what overwrites what, which "
      "is a design discussion, not a feature."],
     ["Meaning-based (not substring) routine triggering", "Deferred",
      "Cheaper to keep triggers explicit and reviewable; the reranker stack already exists and could be "
      "reused later."],
     ["Handing the assistant's own overflow to a summarizing sub-agent", "Never reached",
      "Sub-agents isolate context for assigned work; offloading the parent's overflow was on the list and "
      "lost to the dashboard work."]])
NOTE("[Editor notes: the first four rows are drafted from repo evidence (code comments, docs) and need your "
     "confirmation against real team decisions from standups/daily reports; the rest are honest deferrals "
     "inferred from what is absent in code. Please dictate corrections before submission. Daily_reports/ "
     "mining still pending.]")

H(2, "VI. Conclusion")
P("Building the assistant from scratch was the point of the lab, and the parts where that mattered most "
  "were the boring ones: one front door for every action, where failures and permissions come back as "
  "readable outcomes instead of crashes; monitoring bolted to the loop rather than woven into it; and a "
  "memory model that separates what happened (threads), what is true (facts), and how we work (routines) "
  "instead of one undifferentiated pile of searchable text. The compaction tiers and the two-stage recall "
  "are pieces we would design the same way again. The size heuristic and the linear search are the pieces "
  "we would revisit first, and Section V records why three weeks was not enough to get there.")

H(2, "References")
P("[1] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, Y. Cao, \"ReAct: Synergizing reasoning and "
  "acting in language models,\" ICLR 2023.")
P("[2] P. Rajasekaran, E. Dixon, C. Ryan, J. Hadfield, \"Effective context engineering for AI agents,\" "
  "Anthropic engineering blog, Sep. 2025.")
P("[3] Model Context Protocol, \"What is the Model Context Protocol?\", modelcontextprotocol.io.")
P("[4] L. Pan, L. Zou, S. Guo, J. Ni, H.-T. Zheng, \"Natural-language agent harnesses,\" arXiv:2603.25723, "
  "2026.")
P("[5] V. Trivedy, \"The anatomy of an agent harness,\" LangChain blog, Mar. 2026.")
P("[6] StudyMate team repository, group-11, git.fim.uni-passau.de, week 3 final, 2026.")

spec = {"blocks": B}
(HERE / "report_spec_plain.json").write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")

# ---- word count (body prose; excludes tables and editor notes) ----
words = 0
for blk in B:
    if blk.get("type") == "table" or blk.get("runs"):
        continue
    t = blk.get("text") or " ".join(blk.get("items", []))
    words += len(re.findall(r"\S+", t))
print("spec written; approx body words (excl. tables/notes):", words)
