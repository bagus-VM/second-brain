---
title: Agent Harness Explained Plainly
status: active
tags: [ai-engineering-lab, studymate, oral-exam]
---

Companion to [[Oral Exam Study Guide]]. The big guide is the detailed reference for each week's code.
This file explains the same system in plain words, one concept at a time. It follows the order our
study conversations went: harness first, then the model, then the loop, then lint vs grill, memory,
permissions, and the rest. Each section ends with a short line you can actually say out loud.

> **Read time:** about 15 minutes. Re-read it right before the exam, not the 1500-line guide.

---

## 1. What an "agent harness" is

A harness is the **program you write around an LLM to let it actually do things**.

The LLM itself can only do one thing: take some text, return some text. It cannot read your files,
search the web, or run a command. The harness is the code that:

1. decides what the model is allowed to touch,
2. writes down the model's requests,
3. performs them with normal Python,
4. feeds the results back as text,
5. repeats until the model says it is done.

**One-line answer:** "The model only produces text. The harness turns that text into file operations,
checks whether those operations are allowed, and shows the model what happened."

In this project, the harness is `src/study_agent/` — about 7,700 lines of Python. The model is not
ours; it runs on the university's InnKube server and we call it over HTTP.

---

## 2. What StudyMate does for a student

Plainly, it turns messy lecture material into a tidy note vault.

| Student does | Program does |
|---|---|
| drops PDFs in `workspace/data/` | reads them, never writes there |
| asks for notes on a lecture | writes concept notes, summaries, flashcards, mind maps into `workspace/artifacts/` |
| types `/lint` | checks the links between notes and fixes the broken ones |
| types `/grill <topic>` | quizzes them, getting harder each round |
| says "remember that I struggle with X" | saves it in a database and uses it in later sessions |
| starts a new session | can resume the old conversation with its history |

---

## 3. Who the "model" is here, and what it never sees

The chat model is `qwen-agentworld-35b-a3b`. We never download it; we POST to
`https://llms.innkube.fim.uni-passau.de`.

**What the model sees:**

- one text file that tells it who it is (`config/soul.md`)
- the list of tools (names, descriptions, expected arguments, as JSON)
- the conversation so far

**What the model never sees, and this matters for the exam:**

- file paths outside the sandbox — it cannot even ask for `C:\` correctly, it is told to stay in
  `workspace/`
- the API key
- the permission rules
- the trace log (traces are written by the harness, outside the model's writable area, so the model
  cannot forge its own logs)
- whether the user said "hello" or "/grill regex" — commands reach it as plain text

**One-line answer:** "The model is a stateless text function living on a remote server. Everything
called 'agent behaviour' is the harness: context assembly, tool dispatch, sandboxing, and the loop."

---

## 4. The ReAct loop, in plain steps

`AgentEngine.run(user_message)` in `core/engine.py` (707 lines). One turn:

1. Add the user's message to the history.
2. Ask the model: "here is the conversation, here are your tools, what now?"
3. Two possible answers:
   - **Text, no tool requested** → that is the final answer. Return it. Done.
   - **A tool request** → run that tool with normal Python, append the result to the history, go back
     to step 2.
4. Never more than 50 rounds. If it runs out, return a failure message instead of looping forever.

That is the entire design. The model does not execute anything; it *asks*, the harness *does*.

```
user:  create a note about gradient descent
model: I need to check the lecture first      -> tool: read_file("workspace/data/lecture.txt")
harness: [returns 40 lines of text]
model: now I can write it                     -> tool: write_file("workspace/artifacts/concept-....md")
harness: [returns "File written successfully"]
model: Here is your note: gradient descent...  -> final answer, loop exits
```

Three small guards worth mentioning because they were real design decisions:

- **Empty answer** → the harness injects "your last response was empty, continue" and retries once
  instead of returning nothing (`engine.py:516-561`).
- **Answer cut off by the token limit** (`finish_reason == "length"`) → same: ask it to continue,
  do not present half a sentence as finished work.
- **Context full** → compact before calling, not after the server rejects the request (`engine.py:356-371`).

**One-line answer:** "Reason, act, observe, repeat, with a hard budget of 50 iterations and a
terminal condition of 'the model answered without requesting a tool'."

---

## 5. `/lint` vs `/grill` — the best example of where the model is used

These two look similar from the terminal. They are opposite in design, and that contrast is a strong
exam answer.

### `/lint` — code finds, model fixes

1. `VaultLinter` (plain Python, regex) walks every `.md` file, collects all `[[wikilinks]]`, and
   reports any link pointing at a note that does not exist. Zero model involvement.
2. If problems exist, the harness builds a prompt listing the exact defects and calls `engine.run()`
   with it. Now the model works: read the broken note, guess what the author meant, either point the
   link at a real note or remove the brackets while keeping the words.
3. After the model finishes, the harness runs `linter.lint()` **again**. If the model claimed to fix
   something and did not, the second pass proves it.

Why split it this way: finding a broken link is set arithmetic — a loop does it perfectly, an LLM does
it expensively and sometimes wrongly. Deciding what a dead link *was supposed to mean* needs judgment.
So the deterministic part is code, the judgment part is the model, and code verifies the model at the end.

Deliberate limits in the repair prompt: no deleting files, no inventing new notes, and **orphan pages
are reported but never auto-repaired** — "fixing" an orphan means making up a link to it, which is
exactly the kind of invention that should stay with a human.

### `/grill` — no new machinery, only a rewritten sentence

`/grill regex` does not call a special grilling engine. The CLI replaces your input with a longer
prompt (`SocraticGriller.create_initial_prompt`) that says "act as a demanding examiner, start with a
Level 1 recall question", and then runs the **normal** `engine.run()`. The engine cannot tell the
difference between a slash command and typed chat. Difficulty levels, one-question-at-a-time, and
"do not give the answer" are only instructions in that text.

Honest weakness to volunteer: `create_evaluation_prompt()` exists in `griller.py` but **nothing in the
codebase calls it**. Turn-by-turn evaluation is improvised by the model from the persona, not driven by
code.

**One-line answer:** "`/lint` uses code to measure and the model to repair, then code re-checks.
`/grill` uses no new code at all — it is a prompt rewrite through the same loop. Rule of thumb:
deterministic work goes in Python, judgment goes to the model."

---

## 6. Context, and what happens when it fills up

`ContextManager` (`core/context.py`, 163 lines) just holds the message list:
one system message, then user / assistant / tool messages in order. It grows forever inside one
session, which eventually exceeds the model's window (262,144 tokens for our default model).

Compaction (`core/compaction.py`) solves that in two cheap-to-expensive tiers:

1. **Free tier:** overwrite old tool results with the placeholder `"[Older tool output cleared — see
   artifacts/]"`. No LLM call. The information is usually still on disk anyway.
2. **Summary tier:** if still too big, take all old turns except the most recent 10, send them to the
   model *without* tools, and ask for a structured summary: Goals, Decisions, Artifact paths, Pending
   work, Memory topics referenced. Then the history becomes: system message + that summary + last 10
   messages.

Details that show care:

- The system prompt (index 0) is never summarized away.
- The summary is marked "historical context, not new instructions" — otherwise a summary containing
  "user asked to delete X" would read like an order.
- Circuit breaker: if summarizing fails twice in a row, stop trying.
- Trigger points: automatic at 80 % of the window, reactive once if the server rejects with an
  overflow error, and manual via `/compact`.

**One-line answer:** "The context is a plain list of messages. When it gets large, we drop old tool
output for free, and only if that is not enough do we pay for one summarizing call — with the system
prompt and the last 10 turns always kept."

---

## 7. Memory: two kinds, three search methods

Storage is one SQLite file: `workspace/artifacts/memory/memory.db`.

- **Episodic** = threads and messages (what we talked about, when). Lets you resume with `/thread`.
- **Semantic** = facts: short statements like `topic: "preferences"`, `fact: "struggles with backprop"`.

A fact is written only when the *model decides* to call the `memory_store` tool, but the harness pins
the provenance (which thread, which date) so a fact can always be traced back.

**Nothing is ever deleted — only archived.** A tombstone `archived` flag, plus an explicit SQL
`BEGIN` before the DDL so a half-created schema cannot survive a crash.

Searching happens through `hybrid_recall` (`memory/retrieval.py`) and it merges three signals:

| Method | Finds | Fails on |
|---|---|---|
| SQL `LIKE` on text | exact keyword | "the thing where gradients vanish" |
| Vector (embed the fact, cosine distance) | paraphrase, same meaning | exact identifiers |
| Reranker (cross-encoder) | reorders the merged hits by true relevance | — |

Keyword hits come first, vector hits fill the rest, the reranker reorders. If the embedding server is
down, it degrades to keyword-only and never raises, because a tool must never throw at the model.

Also: the 5 most recent facts are injected into the system prompt automatically at session start, so
the agent already "knows" them without searching.

**One-line answer:** "Two kinds of memory in SQLite, never deleted only archived; recall is keyword
first, then semantic vectors for paraphrases, then an optional reranker — and every failure degrades
to the cheaper method instead of breaking the run."

---

## 8. Facts vs procedures (skills)

Facts above are *what the student is*. Procedures are *how to do a job*.

- A procedure is a markdown file in `workspace/artifacts/procedures/` with frontmatter
  (`name`, `triggers`, `scope`, `status`, `version`) and sections: Steps, Rationale, Pitfalls, Example.
- Before each turn, `match_procedures` looks for trigger words in the user's message and injects the
  matching routine into the system note. So the agent follows a proven workflow instead of improvising.
- `status` controls trust: **`approved`** injects automatically; **`draft`** is surfaced ("I have a
  draft routine for this — use it?") and never followed silently; **`archived`** is dead.
- The agent may *draft* a procedure after a clearly successful multi-step task, but a human promotes
  it by flipping the status field. Never distilled mid-failure.

This is the project's version of "a skill" — and it is different from `griller.py`/`linter.py`, which
are fixed code shipped in the package.

**One-line answer:** "Facts are learned statements about the student; procedures are reusable
routines as markdown with a trust status. Both are append-only, and a draft never runs without asking."

---

## 9. Permissions: three files, one system

This question is worth answering as a chain, because people confuse the layers.

```
config/config.yaml        what the operator wrote        (data, human-edited)
        ↓ loader.py
PermissionsConfig         Pydantic schema + defaults     (validated)
        ↓ policy_from_config()
PermissionPolicy (Rule,   the runtime decision function  (pure, no I/O)
  Decision, evaluate)
        ↓
ToolRegistry.execute() → _check_permission() on EVERY call
```

- **`config.yaml`** is the only thing a user edits: which tool names get which decision, and the
  fallback.
- **`PermissionsConfig` in `settings.py`** is not a second system — it is the *type* the YAML has to
  satisfy. It catches `decision: "maybe"` or a string where a list belongs at startup, so a malformed
  security policy fails loudly instead of silently allowing things.
- **`PermissionPolicy` in `security/policy.py`** is the executable one: first matching rule wins
  (fnmatch on tool name, optionally on argument values), else `default_decision`.

The three tiers:

| Tier | Decision | Examples | Why |
|---|---|---|---|
| `observe` | allow | `read_file`, `list_files`, `memory_recall`, `research_topic` | read-only, no side effects |
| `sandbox-edit` | allow | `write_file`, `edit_file`, `rename_file`, `memory_store` | writes are already jailed to `artifacts/` — two layers compose |
| `consequential` | confirm | `web_search`, `fetch_web_content`, `delegate_task` | leaves the machine, or spawns a whole sub-agent |

**Fail-closed everywhere:** default is `require-user-confirmation`, which means a newly discovered MCP
tool with no rule needs a human automatically — you never have to remember to write a rule for
something you did not know existed. If there is no interactive user (tests, non-TTY), a confirmation
*becomes a denial*. If the confirmation prompt itself throws, that is also a denial.

One detail: subagents **inherit the same policy object by reference**, so a child agent cannot escape
the gate its parent is under.

**One-line answer:** "Permissions are declared in YAML, typed and validated by a Pydantic model, and
executed by a pure policy object the tool registry consults before every call. Default is ask-a-human,
so anything unknown is treated as dangerous."

---

## 10. The three security layers

1. **The path jail** (`PathSecurityManager`, `tools/filesystem.py:44-116`): every path is resolved
   against the base directory with `Path.resolve()` (which flattens `../`), then checked with
   `relative_to` against the allowed roots. Reads must be inside `workspace/`, writes only inside
   `workspace/artifacts/`. Failure raises `PermissionError`, which the registry converts to an
   `"Error: ..."` string so the loop survives.
2. **The permission gate** (section 9): decides *whether a tool may run at all*.
3. **No deletion**: there is no delete tool, so the model cannot request one. This is **structural**,
   not a flag — worth knowing: `allow_delete: false` in the config is never actually read by runtime
   code; the guarantee is that no tool exists, plus a test asserting it. Related: `write_file` is the
   only overwrite vector, and writes are crash-atomic (temp file + `os.replace`) so a crash mid-write
   cannot leave a truncated note.

**One-line answer:** "Path validation blocks escaping, permissions block dangerous tools, and
deletion is impossible because we simply never built the capability."

---

## 11. Subagents, in plain terms

`delegate_task` looks exotic but is not: **it is one more tool.** When the model calls it, the tool's
`execute()` builds a *second `AgentEngine`* and runs its own little loop. The child's final text is
returned as a plain tool result string, and the parent continues.

What the child gets:

| | Parent agent | Child subagent |
|---|---|---|
| Context | your whole conversation | brand empty; only the `task` string |
| System prompt | `soul.md` | its own persona (Examiner / Researcher) |
| Tools | everything | an allowlist (examiner: 3 read-only tools; researcher: 1) |
| Iterations | 50 | 8 / 12 |
| Permissions | the policy | the *same* policy object, inherited |
| Traces | `parent_run_id = None` | stamped with the parent's run id |

So it is recursion, not a special engine. Two things were added late (Day 5 of Week 3) and are useful
as an honest "what went wrong" story:

- `research_topic` was whitelisted for the researcher but **never registered in the parent registry**,
  so every research delegation failed with "tool not registered" until it was wired up.
- Input sanitization (`strip().lower()` before lookup) because the model sometimes sends
  `" Researcher "`.

And the delegation rule in `soul.md` says: **do not delegate by default** — answer simple things
directly, only delegate when the student explicitly asks or names a subagent.

**One-line answer:** "Delegation is an ordinary tool call that starts a second, isolated engine:
fresh context, allowlisted tools, smaller budget, inherited permission policy, and a parent run id so
the trace shows the hierarchy."

---

## 12. MCP in one paragraph

MCP (Model Context Protocol) is a standard for exposing tools to any agent, not just ours. StudyMate
does both sides. **As a server** (`tools/mcp/server.py`): it publishes the local Obsidian vault tools
so Claude or Cursor could use them over stdio. **As a client** (`tools/mcp/external.py`): it starts the
external `duckduckgo-mcp-server` on demand over stdio, keeps it alive between calls, and adapts each
remote tool into a local `BaseTool`. Remote tools that were discovered at runtime and have no
permission rule fall into the confirm tier automatically. The internal `web_search` implementation is
our own HTML scraping service (`services.py`), separate from the external MCP path.

---

## 13. Observability, plainly

Three switches, all off by default and toggled by environment variables:

- **Prometheus** (`metrics_enabled`) → a `/metrics` HTTP endpoint with counters and histograms for
  runs, LLM calls, tool calls, memory operations, compactions, permissions, subagents, MCP health.
- **JSONL traces** (`trace_file`) → one line per finished run with the whole turn history, token
  totals, timings, and every tool call. Written by the harness under `./observability/`, deliberately
  **outside** the agent's writable jail.
- **Langfuse** (`langfuse_enabled`) → the same events pushed to a self-hosted trace UI so you can
  click through parent/child spans. Keys are env-only, never in YAML.

The one design rule that gets asked about: **nothing in observability can break a run.** Every
listener, span, and exporter is wrapped so failures are logged and swallowed. Truncation at
`trace_max_chars` (4000) is intentional — traces are a lossy audit log, not a transcript.

Plus a background health heartbeat that probes the MCP bridge and vault every 60 s so the dashboard
can show "last 30 min" status.

**One-line answer:** "Metrics for aggregation, JSONL for local audit, Langfuse for interactive
inspection — all opt-in, all failure-isolated, and all written outside the sandbox so the agent cannot
tamper with its own record."

---

## 14. Ten sentences that carry the whole project

If you remember nothing else, say these:

1. The LLM only emits text; the harness executes everything.
2. The loop is: ask → run requested tools → append results → ask again, capped at 50 rounds.
3. A turn ends when the model answers without asking for a tool.
4. All file access goes through a path resolver that blocks `../` and confines writes to
   `workspace/artifacts/`.
5. There is no delete tool, so deletion is impossible by construction, not by permission.
6. Permissions are YAML-declared, Pydantic-validated, and evaluated by a pure policy before every
   tool call, with fail-closed as the default.
7. Context is compacted by dropping old tool output first and paying for a summary only if that is
   not enough.
8. Memory is SQLite, append-only, recalled by keyword then vector then rerank, and it degrades to the
   cheaper method on failure.
9. A subagent is a second instance of the same engine with a fresh context and a tool allowlist.
10. Telemetry never raises into the agent loop, and traces live outside the sandbox so they cannot be
    forged.

---

## 15. Vocabulary you are expected to use correctly

| Term | Plain meaning here |
|---|---|
| harness | the Python program wrapping the LLM |
| ReAct | ask-then-act loop, not a framework |
| observation | the text a tool returns into the history |
| terminal answer | a model reply with no tool request |
| context window | how many tokens the model can be shown at once |
| compaction | replacing old turns with a summary to save window |
| tombstoning | marking archived instead of deleting |
| embedding | a list of numbers representing meaning, for similarity search |
| cross-encoder / reranker | a model that scores query-vs-document relevance directly |
| jail | the directory the agent is not allowed to escape |
| fail-closed | when in doubt, deny or ask; never allow |
| provenance | where a fact or run came from (thread id, parent run id) |
| circuit breaker | stop retrying an operation after N failures |
| MCP | protocol for plugging external tools into agents |
| atomic write | temp file + rename, so a crash cannot leave a half-written file |
| idempotent | safe to call twice (registration, health ticks) |

---

Related: [[oral-exam-study-guide|Oral Exam Study Guide]] (full reference with line numbers),
[[memory-architecture]], [[call-graph]].
