# Generates StudyMate_report_draft.docx from a content spec via the docx skill.
import json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
SKILL = Path(r"C:\Users\quiescent\AppData\Local\hermes\skills\productivity\docx\scripts\docx_create.py")

B = []  # blocks
def h(level, text): B.append({"type": "heading", "level": level, "text": text})
def p(text): B.append({"type": "paragraph", "text": text})
def bullets(items): B.append({"type": "bullet_list", "items": items})
def table(header, rows): B.append({"type": "table", "header": header, "rows": rows, "style": "Table Grid"})
def meta(text): B.append({"type": "paragraph", "runs": [{"text": text, "italic": True}]})

# ---------------------------------------------------------------- title/authors
h(1, "StudyMate: Agent Loop and Memory Handling in a From-Scratch ReAct Harness")
p("Bagus Trilaksono  |  AI Engineering Lab, Chair of AI Engineering, University of Passau  |  SoSe 2026  |  Individual written report, September 2026")

# ---------------------------------------------------------------- I
h(2, "I. Introduction")
p("StudyMate is an agent harness built from scratch in Python 3.12 during a three-week lab at the University of Passau. It serves one domain: a computer science student drops lecture slides, PDFs, and exercise sheets into a read-only folder, and the agent turns that material into an Obsidian-style knowledge base of interlinked concept notes, lecture summaries, flashcards, and Mermaid mind maps, and can afterwards lint the vault for broken links and quiz the student about the material. The lab brief describes an agentic system as an LLM plus the infrastructure around it, the harness, decomposed into loop, context, tools, skills, long-term memory, hooks, permission management, sandboxing, and sub-agents. StudyMate implements every one of those components without using a framework; the only third-party runtime pieces are an OpenAI-compatible client library and a stdio MCP bridge.")
p("This report has two halves. The first half explains the control loop of the system (Section II) and then its memory handling, both short-term and long-term (Section III), which is the focus assigned to me. The second half describes where the team exceeded the minimum requirements of the lab (Section IV) and which extensions we considered and did not pursue, with our reasons (Section V). All code claims in this report refer to the repository as delivered at the end of week 3, roughly 7,800 lines of Python under src/study_agent plus a pytest suite of the same size class.")

# ---------------------------------------------------------------- II
h(2, "II. The Agent Loop")
h(3, "II.A. States and transitions")
p("The control structure lives in one file, core/engine.py (693 lines), and is a bounded state machine in the sense the lab background text uses it. A run starts when the REPL hands the engine a user message; the engine appends it to the context and enters a while-loop capped by max_iterations, configured at 50. Each iteration has four steps.")
bullets([
    "Guard. Before calling the model, the engine estimates the size of the next request and, if it passes the compaction threshold, folds the history (Section III.B). This runs before the call, never as a reaction to a failed call, except on the overflow retry path described below.",
    "Reason. The LLM client is called with the full message list and the tool schemas. The response is either a text answer, tool calls, or a malformed or empty reply.",
    "Act. Every requested tool call is dispatched through one ToolRegistry.execute(), never directly to a tool object.",
    "Observe. Each tool output is appended to the context as a TOOL message and the loop continues.",
])
p("A text response with no tool calls is the normal exit: the engine closes the run, records metrics and a trace, and returns. The exit statuses are success, max_iterations, empty, and error, chosen deliberately so the Prometheus counters can separate \"the model gave up\", \"the model looped\", and \"infrastructure failed\". Two recovery paths are worth naming. If the response is empty, the engine injects a synthetic user message (\"Your last response was empty. Continue the requested task now.\") and keeps looping instead of returning a blank answer. If the provider rejects the request because the context overflowed anyway, the engine forces one compaction and retries the iteration exactly once; a second overflow terminates the run.")
h(3, "II.B. The registry as the single choke point")
p("The tool layer is a contract, not a collection of functions. BaseTool requires a name, a description, and a JSON-schema for parameters, which to_openai_schema() renders for the model; a tool's execute() returns a string and, by convention, failures come back as strings starting with \"Error\" rather than exceptions. ToolRegistry.execute() enforces that. It looks the tool up, runs the permission gate, executes inside a try/except that converts any surviving exception into an error observation, and emits latency and status metrics. The model therefore always receives an observation it can read and act on, which the lab text calls communicating failures upstream, and the loop can never crash mid-iteration because a tool raised.")
p("The same method is also where the Week 3 permission system attaches. When a policy is configured, each call is evaluated against an ordered rule list (first match wins, unmatched calls default to require-user-confirmation), and three outcomes exist: allow proceeds, deny and user-refusal return error observations addressed to the model, and one detail matters for safety: if a confirmation is required but no interactive handler exists (tests, non-interactive runs, or a handler that itself throws), the call is treated as denied. Fail-closed, as the brief describes for the full-access tier.")
h(3, "II.C. Hooks around the loop")
p("Instrumentation is bolted on, not woven in. The engine exposes a list of telemetry callbacks that fire run_start, run_end, tool_start, tool_end events; the registry exposes an on_permission_decision seam; and metrics, JSONL traces, and Langfuse export subscribe to those seams at assembly time in the CLI. Listener exceptions are caught and logged at the seam, so a broken listener cannot break a run. This is the decoupled lifecycle-hook mechanism the week 3 brief asks for, and it has a practical payoff for us: the same engine code runs uninstrumented inside unit tests and fully instrumented inside the Docker compose stack.")
h(3, "II.D. Termination guarantees")
p("Every path through the loop returns. The iteration cap bounds the common case; LLM exceptions propagate to the REPL after closing the live trace span; empty responses re-enter the loop but the cap still applies; denial observations tell the model not to retry the exact call, which is a small prompt-engineering measure against the loop spending its whole budget retrying a refused tool. In our experience with the qwen-agentworld-35b-a3b model the cap is rarely reached; delegation runs (Section IV) are the case where long iteration counts actually happen.")
meta("[Editor notes: figure 1 = loop state-machine diagram (states: guard, reason, act, observe; exits: success/empty/max-iterations/error). Insert before submission. Optional: a real run excerpt from observability/traces.jsonl once fresh runs are generated.]")

# ---------------------------------------------------------------- III
h(2, "III. Memory Handling")
h(3, "III.A. What counts as memory in this harness")
p("We split memory the way the lab background text does. Short-term memory is the context window itself: system prompt, conversation history, tool schemas, everything the model sees on the next call. Long-term memory lives outside the window and survives restarts. The interesting engineering is at the boundary between them: what to write out, what to read back in, when, and how much budget each is allowed. StudyMate keeps three long-term stores, matching the taxonomy of episodic records, declarative facts, and procedural skills, in one SQLite database and one directory of Markdown files.")
h(3, "III.B. Short-term memory: context assembly and compaction")
p("ContextManager (core/context.py) maintains a leading SYSTEM message assembled from config/soul.md (persona, sandbox directives, storage and recall rules), the current date, and an injectable note slot. One implementation detail we found the hard way: injected memory cannot be appended as a second SYSTEM message, because strict chat templates on the serving stack reject that (\"System message must be at the beginning\"). So every injection, and there are several per session (recent facts at startup, matched routines per turn), merges into messages[0] by re-rendering it. A stale per-turn block is explicitly reset so a routine matched on one turn cannot leak into the next.")
p("Compaction (core/compaction.py) fights context rot within a single thread. The trigger is a size estimate of the next request: all message content plus serialized tool schemas, at four characters per token. That is a heuristic, and we treat it as one: it is cheap, deterministic, and conservative in the right direction, and its residual risk is covered by the overflow retry path in the loop. The threshold fires at 80% of the model window, but the window itself is resolved per model through a precedence chain we kept from a design note: an explicit config table wins, otherwise a best-effort gateway lookup against a model-info route, otherwise a [Nm] suffix parsed from the model id, otherwise a conservative 128k default with a startup warning. Which layer answered is logged and shown in /config, because a wrong window silently misplaces every later threshold.")
p("When compaction fires it works in two tiers, cheapest first. Tier one blanks TOOL observations older than the recent window in place, replacing them with a placeholder that says where the output went (the artifacts directory); this costs no API call and is often enough, since a PDF dump or a search result dominates the budget. Tier two, if the estimate is still over the line, serializes the old turns, asks the same LLM (tools disabled) for a structured summary under fixed headings (Goals, Decisions, Artifacts created with exact paths, Pending work, Referenced memory topics), and rebuilds the history as SYSTEM, summary, last ten messages. Two properties are deliberate. The summary is marked \"historical context, not new instructions\", because it enters as a user message and we did not want the model treating a compressed past directive as live. And the free tier exists because a summarizer call inside every long run is both money and a second failure mode; a per-run once-only guard plus a two-failure cross-run circuit breaker bound that mode.")
p("Nothing in this design deletes. The compacted turns are not lost: the full transcript lives in the thread database (III.C), and the summary itself is persisted to the thread. Compaction trades window space, not history.")
h(3, "III.C. Long-term, episodic: threads")
p("Every user, assistant, and tool message is appended to a per-thread table in workspace/artifacts/memory/memory.db while the session runs, so the store doubles as the replay source for compaction. Threads are named from their first message, browsable with an arrow-key picker (/threads), resumable (/thread 3 continues with the transcript restored into the context), and archivable with a tombstone flag, never deleted, consistent with the harness-wide no-delete invariant. The practical test we hold it to: quit the application, restart, resume the thread, and say \"continue where we left off\"; the agent should still know which lecture it was ingesting without being re-told.")
h(3, "III.D. Long-term, semantic: facts with hybrid recall")
p("The lab brief asks specifically for the write and read policies of long-term memory, so we state them exactly.")
p("Writing. Two channels exist. The model calls the memory_store tool when the student says \"remember ...\" or when a durable preference, struggle, or goal emerges; soul.md restricts this to information worth surviving a restart and forbids storing ephemeral chat. The harness stamps provenance (active thread id and name) itself; the tool schema exposes no thread fields, so the model cannot forge where a fact came from. The store enforces a UNIQUE(topic, fact) constraint inside one transaction; an exact duplicate does not insert a second row but revives the original if it had been archived and backfills a missing embedding. Text over 2000 characters is refused, which keeps the auto-injected recall block from being hijacked by a dump.")
table(
    ["Trigger", "Path", "What we measure or decide"],
    [
        ["Startup", "top 5 recent facts merged into system prompt", "fixed budget, max_inject=5"],
        ["Per turn", "approved routines matching the user text", "substring triggers, max 2 routines, 4000-char cap"],
        ["Model-initiated", "memory_recall tool", "hybrid: LIKE page first, vector page second, reranker reorders"],
    ],
    # header row counts as table content (excluded from word count)
)
p("Reading happens on three triggers, summarized in the table. The just-in-time path is the interesting one. hybrid_recall (memory/retrieval.py) runs a keyword LIKE query first because exact matches are precise and free, then embeds the query against sqlite-vector cosine search to catch paraphrases that share no words with the stored fact, unions the two pages up to a limit, and hands the merged candidates to the InnKube qwen3-reranker-4b endpoint, which reorders by cross-encoder relevance to the query. Recall is thus three models deep: an 8B embedder at write time, a 4B reranker at read time, the chat model at use time. One API key covers all three because grants are per model server-side.")
p("Graceful degradation is a design requirement, not a nicety, because the embedding and reranker grants are per model and can be missing. No embedder configured, or an embedding call that fails: recall returns keyword hits and tells the model \"vector search unavailable\" in the observation, so the model knows the difference between \"no facts exist\" and \"semantic search could not run\". No reranker or a failed rerank call: the hybrid order is kept. Facts stored before embeddings existed get backfilled lazily, one hundred per recall, so a user who upgrades a database mid-term converges to fully embedded without a migration step. Each of these paths has a test.")
h(3, "III.E. Long-term, procedural: routines as files")
p("Skills live as Markdown bundles in workspace/artifacts/procedures/, committed to git and reviewable like code. A procedure has frontmatter (name, triggers, scope, version, status, supersedes) and body sections (steps, rationale, pitfalls, example), parsed by study/procedures.py. Matching is deliberately stupid: case-insensitive substring overlap between the user message and the name, triggers, and scope of non-archived procedures, sorted by name, capped at two routines and 4000 characters of injected text. Status controls disclosure. Approved routines are injected and followed. Drafts, which is where every agent-distilled routine starts, are surfaced for confirmation but never followed silently; a human promotes them by editing the status field. Versioning is git plus a supersedes field, because files can be edited but not deleted by policy.")
p("The split between facts and routines follows the declarative/procedural line in the lab text. Facts answer \"what is true about this student\", routines answer \"how do we do X here\", and only facts go through the vector machinery. Routines are short enough that a substring trigger plus a size cap is adequate retrieval, and keeping them as plain files means a student can audit what the agent has taught itself.")
h(3, "III.F. Why this design, and what it costs")
p("The alternative we did not take was one external vector store (Chroma, or the Postgres already running for Langfuse) with a proper ANN index. We chose SQLite plus sqlite-vector because the whole memory subsystem then lives inside the existing artifacts jail, needs zero new services to run the agent itself, and inherits the append-only, no-delete semantics of the filesystem policy. The cost is honest: the cosine search is a linear scan over the facts table. At the scale of one student's semester, a few hundred facts, that is invisible; we never stress-tested past low thousands, and it would be the first thing to replace in a multi-user deployment.")
meta("[Editor notes: figure 2 = memory architecture (context window / compaction tiers / threads+facts+procedures / embed+rerank loop). Re-verify the store/read table against final code before submission.]")

# ---------------------------------------------------------------- IV
h(2, "IV. Beyond the Minimum Requirements")
p("The lab states plainly that meeting the weekly minimums caps the grade, and that students should identify and build beyond them. This section lists what our team built that no bullet in the brief requires, with the evidence for each. Everything below is on main at the end of week 3.")
h(3, "IV.A. Building a domain, not just a harness")
p("The minimum Week 1 is a file-navigating agent. We spent part of the same week turning it into a study assistant: the concept and lecture templates with YAML frontmatter in study/templates.py, the VaultLinter that walks the artifact directory and reports broken wikilinks, orphan pages, missing frontmatter, and open questions (the generate-then-verify pattern the background text describes, applied to a knowledge graph instead of a test suite), and the three-level Socratic grilling prompt in study/griller.py. The /ingest, /lint, /grill slash-commands are prompt-rewrites into the same engine loop, which keeps the persona layer thin.")
h(3, "IV.B. Depth in the components themselves")
p("Several minimum requirements have a plain reading that we exceeded. The Week 2 memory minimum is \"store in one session, retrieve in a later one\" with a stated mechanism; we shipped three memory types (Section III) where the minimum requires one, and the recall path adds vector search and a cross-encoder reranker. The Week 2 MCP minimum is one connected server with runtime discovery plus one extension tool; we run an external DuckDuckGo search server over a stdio bridge and wrote our own nine-tool Obsidian MCP server (anchored section edits, backlink and outgoing-link queries) that the harness consumes through the same registry and permission gate as built-ins. The Week 3 permission minimum is the three outcomes; our policy adds tier labels, argument-pattern matching with fnmatch, session-scoped \"always\" allowances recorded as their own observability dimension, and the fail-closed default that auto-covers runtime-discovered MCP tools nobody wrote a rule for. The Week 3 sub-agent minimum is delegation on the same harness with its own limits and permissions; we added per-sub-agent tool profiles (the examiner is read-only by construction, so it cannot corrupt the vault while grading the student) and parent_run_id trace correlation, so a delegation shows up as one tree in Langfuse rather than two unrelated runs. The Week 3 observability minimum is Prometheus, a scrape config, and any dashboard; we added per-run JSONL traces, best-effort async Langfuse export, a background health heartbeat for the MCP servers, and a provisioning script that rebuilds the dashboard widgets so the stack is reproducible on a TA machine.")
p("Context compaction and thread resumption are not minimum requirements at all. In the lab taxonomy they are the \"context\" component done properly, and in practice they changed how the agent behaves on long sessions more than any single tool did.")
h(3, "IV.C. Engineering practices beyond the call")
p("Three smaller items we consider part of the deliverable. The MockLLMClient, MockEmbedder, MockReranker, and MockMCP path lets the full suite of 261 tests run offline and deterministically, which is what makes instrumenting the loop safe to touch. Tool descriptions and soul.md directives encode model-behavior findings from our own runs (for example, search-discipline rules that stop the model from baking hallucinated years into web queries) and are treated as part of the system under test, edited and reviewed like code. And the no-delete invariant is enforced across every subsystem at once: files, tombstoned threads and facts, superseded rather than removed procedures, and a compaction tier that prunes views instead of data.")
meta("[Editor notes: every claim here is checkable in code; pull 1-2 numbers from freshly generated runs (e.g. token savings from a compaction event, a delegation trace screenshot) to make this section evidence-backed rather than list-shaped. Team attribution: Bagus (git: putra01) owns [FILL IN modules] and can vouch for the rest through code review.]")

# ---------------------------------------------------------------- V
h(2, "V. Extensions Considered but Not Pursued")
p("The brief asks what we left out and why. This section separates items with a concrete team decision behind them from items we simply never got to. Where a decision exists, the reason is ours; where it does not, we say so.")
table(
    ["Extension", "Status", "Reason"],
    [
        ["True tokenizer-based token counting", "Considered, rejected for now", "InnKube serves the chat models without exposing their tokenizers; a server-side count call per iteration adds latency for a threshold estimate that the overflow-retry path already backstops. Cost/benefit was wrong at lab scale."],
        ["External vector database (Chroma, pgvector)", "Considered, rejected", "New service or dependency for a table we scan linearly at a few hundred rows. Would only pay off with many users or heavy vaults. See III.F."],
        ["Explicit up-front planning phase", "Considered, not pursued", "The background text mentions planning as a loop extension. We tested prompt-level planning early and the 35B model's plans drifted from its actions within a few iterations; soul.md directives plus the observation loop gave us more reliable behavior for the effort."],
        ["LLM-judged promotion of draft routines", "Not pursued", "Approval is a human edit deliberately. Procedural memory silently rewriting what the agent does next is the failure mode most worth preventing in a study tool."],
        ["Memory consolidation and decay", "Deferred", "Facts deduplicate on exact text but never merge or age out; near-duplicate facts accumulate. Needs an offline job with a quality bar we could not test in three weeks."],
        ["Write-back / correction of memories", "Deferred", "Append-only is a safety invariant here; a correction path means deciding what overwrites what, which is a design discussion, not a feature."],
        ["Semantic (not substring) procedure triggering", "Deferred", "Cheaper to keep triggers explicit and reviewable; the reranker stack already exists and could be reused later."],
        ["Session state offloading to sub-agents", "Never reached", "Sub-agents isolate context for work; handing the parent's own overflow to a summarizing subagent was on our list and lost to the dashboard work."],
    ],
)
meta("[Editor notes: the first four rows are drafted from repo evidence (code comments, docs) and need your confirmation against real team decisions from standups/daily reports; the rest are honest deferrals inferred from what is absent in code. Please dictate corrections before submission. Daily_reports/ mining still pending.]")

# ---------------------------------------------------------------- VI
h(2, "VI. Conclusion")
p("Building the harness from scratch was the point of the lab, and the parts where that mattered most were the boring ones: one choke point for every tool call where errors become observations and permissions become observations' gatekeepers; hooks bolted to the loop instead of woven into it; and a memory model that separates what happened (threads), what is true (facts), and how we work (routines) rather than one undifferentiated retrieval blob. The compaction tiers and hybrid recall are the pieces we would design the same way again. The token estimate and the linear vector scan are the pieces we would revisit first, and Section V records why we did not get there in three weeks.")

# ---------------------------------------------------------------- refs
h(2, "References")
refs = [
    "[1] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, Y. Cao, \"ReAct: Synergizing reasoning and acting in language models,\" ICLR 2023.",
    "[2] P. Rajasekaran, E. Dixon, C. Ryan, J. Hadfield, \"Effective context engineering for AI agents,\" Anthropic engineering blog, Sep. 2025.",
    "[3] Model Context Protocol, \"What is the Model Context Protocol?\", modelcontextprotocol.io.",
    "[4] L. Pan, L. Zou, S. Guo, J. Ni, H.-T. Zheng, \"Natural-language agent harnesses,\" arXiv:2603.25723, 2026.",
    "[5] V. Trivedy, \"The anatomy of an agent harness,\" LangChain blog, Mar. 2026.",
    "[6] StudyMate team repository, group-11, git.fim.uni-passau.de, week 3 final, 2026.",
]
for r in refs: p(r)

spec = {
    "page": {"size": "a4", "margins_mm": {"top": 25, "bottom": 25, "left": 25, "right": 25}},
    "footer_page_numbers": True,
    "blocks": B,
}
spec_path = HERE / "report_spec.json"
spec_path.write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")

r = subprocess.run([sys.executable, str(SKILL), str(spec_path), str(HERE / "StudyMate_report_draft.docx")],
                   capture_output=True, text=True)
print(r.stdout[-2000:]); print(r.stderr[-1500:])

# word count excluding tables and editor notes
words = 0
for blk in B:
    if blk.get("type") == "table":
        continue
    if blk.get("type") == "paragraph" and blk.get("runs") and blk["runs"][0]["text"].startswith("[Editor"):
        continue
    t = blk.get("text") or " ".join(blk.get("items", []))
    words += len(re.findall(r"\S+", t))
print("BODY WORD COUNT (excl. tables, captions-as-editor-notes, headings counted):", words)
