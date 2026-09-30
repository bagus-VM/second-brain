# StudyMate Memory Architecture

How the agent's short-term (working context) and long-term (persistent) memory
work, and how they interact across a session. All references are to the code
as of this commit.

## Two memory tiers

| | Short-term (working context) | Long-term (persistent) |
|---|---|---|
| What | Live message list sent to the LLM each turn | `workspace/artifacts/memory/memory.db` (SQLite) |
| Owner | `ContextManager` (`core/context.py`) | `MemoryStore` (`memory/store.py`) |
| Lifetime | One process run; survives thread switches via load/restore | Survives restarts; append-only, tombstoned never deleted |
| Contents | SYSTEM prompt (+ injected note) + user/assistant/tool messages | `threads` + `messages` (episodic), `facts` + embeddings (semantic) |
| Written by | Engine appends each ReAct step | Harness persists each turn; LLM calls `memory_store` tool |
| Read by | Every LLM call | Thread restore (`/threads`, `/thread`), `memory_recall` tool, start-of-session injection |

## Diagram

```
                            ┌──────────────────────────────────────────────┐
                            │        LONG-TERM MEMORY (SQLite)             │
                            │   workspace/artifacts/memory/memory.db       │
                            │                                              │
                            │  episodic              semantic              │
                            │  ┌──────────────┐     ┌───────────────────┐  │
                            │  │ threads      │     │ facts             │  │
                            │  │ messages     │     │  topic/fact/tags  │  │
                            │  │ (tool calls  │     │  provenance:      │  │
                            │  │  json too)   │     │   source_thread   │  │
                            │  └──────▲───┬───┘     │  embedding BLOB   │  │
                            └─────────┼───┼─────────┴────────▲──────────┘  │
              persist turn   ┌────────┘   │ restore thread   │ store/recall│
              (after engine. │  (harness, │ (load_history,   │  via LLM    │
               run returns)  │  REPL)     │  /threads,       │  tools      │
                             │            │  /thread)        │             │
   ══════════════════════════╪════════════╪═══════════════════╪═════════════╪══
                             │            │                   │             │
                            ┌┴────────────┴───────────────────┴─────────────┐ │
                            │        SHORT-TERM MEMORY (in-process)        │ │
                            │               ContextManager.messages        │ │
                            │                                              │ │
                            │  [0] SYSTEM: soul.md + date                  │ │
                            │      + injected note ──┐                     │ │
                            │                        │ re-injected per turn│ │
                            │  [1..n] user /         │ (facts + approved   │ │
                            │        assistant /     │  procedures)        │ │
                            │        tool msgs       │                     │ │
                            │        ▲               │                     │ │
                            └────────┼───────────────┼─────────────────────┘ │
                                     │               │                       │
                    auto-compact ────┤               │                       │
                    (prune old tool  │               │                       │
                     outputs, then   │        ┌──────┴───────────┐           │
                     LLM summary     │        │ AgentEngine ReAct│           │
                     checkpoint msg) │        │ loop (engine.py) │           │
                            (core/   │        │                  │           │
                            compac-   │        │  chat(messages,  │           │
                            tion.py) ─┘        │      tools) ────┼──► InnKube LLM
                                               │  execute()  ◄───┼──┐
                                               └───────▲─────────┘  │ tool calls
                                                       │            ▼
                                     memory_store /    │  ┌─────────────────────┐
                                     memory_recall ◄───┼──│ ToolRegistry        │
                                     tools (tools.py)  │  │ memory tools +      │
                                                       │  │ filesystem tools    │
                                                       │  └─────────────────────┘
                                                       │
                                        harness stamps thread provenance
                                        (set_thread_context, per turn —
                                         never LLM-supplied)
```

## Short-term memory: `ContextManager`

`src/study_agent/core/context.py`

- One in-process list `messages: List[ChatMessage]`; index 0 is always the
  SYSTEM message rendered as `soul.md + "Current date: <iso>" + injected note`.
- The engine appends assistant messages, tool calls, and TOOL observations
  every ReAct iteration; `get_messages()` is the exact payload of the next
  LLM call. There is no token truncation of the list itself — window
  pressure is handled by compaction (below).
- `inject_system_note(content)` folds a small high-value block into
  `messages[0]` instead of appending a second SYSTEM message (strict chat
  templates on vLLM/LiteLLM reject a SYSTEM message anywhere but at the
  start). The note is idempotent-replaced each turn and cleared by
  `reset_injected_note()` so a stale per-turn block never leaks forward.
- `clear(keep_system_prompt=True)` (the `/clear`, `/new`, post-archive path)
  drops everything but the system prompt.

### Context-window pressure: compaction

`src/study_agent/core/compaction.py`, called from the engine loop and `/compact`

- Token budget estimated at 4 chars/token over serialized messages + tool
  schemas; the window size resolves via config table > gateway probe >
  `[Nm]` model-id suffix > conservative default.
- When usage passes `threshold` (default 0.8 of window) — or when the
  provider returns a context-overflow error (retry-once path) —
  `maybe_compact()` runs two tiers:
  1. Free tier: prune older TOOL outputs in place to
     `[Older tool output cleared — see artifacts/]` (DB untouched).
  2. Summary tier: one tool-less LLM call summarizes old turns into a
     bullet checkpoint (Goals / Decisions / Artifacts / Pending /
     Referenced memory topics — topics only, never verbatim facts), which
     replaces them ahead of the kept recent tail.
- Guards: once per run, circuit breaker on consecutive failures. After an
  auto/manual compaction the summary message is persisted into the thread,
  so the long-term record carries the checkpoint.

## Long-term memory: `MemoryStore` (SQLite)

`src/study_agent/memory/store.py` — one DB file, four tables:

Episodic (what happened):
- `threads(id, name, created_at, updated_at, archived)` — a conversation
  container; names generated heuristically from the first user message
  (`memory/threads.py:generate_thread_name`, no LLM call).
- `messages(thread_id, role, content, tool_calls_json, tool_call_id, name,
  created_at, archived)` — full turn-by-turn history including tool calls
  and observations, serialized ChatMessages.

Semantic (what was learned):
- `facts(topic, fact, tags, source_thread, source_thread_name, created_at,
  archived, embedding, embedding_model)` with `UNIQUE(topic, fact)`.
  Duplicate stores revive/dedupe instead of duplicating; provenance is
  filled in, never overwritten.
- `vector_meta(model, dim)` — records each embedding space so a model
  rotation makes stale vectors simply invisible to the vector query
  (LIKE recall still sees them).

Invariants:
- Append-only with tombstones: `archived = 1` hides rows from every default
  read; there is no DELETE anywhere — consistent with the harness-wide
  `allow_delete=False` rule. Writing to an archived thread raises inside the
  transaction (guard is in-transaction to beat a concurrent archiver).
- The DB lives under `workspace/artifacts/` so it stays inside the path jail.

## The write path (harness → store)

`src/study_agent/cli/terminal.py` (main loop)

1. First task message lazily creates a thread (`ensure_thread`);
   `/new <name>` creates one explicitly; `/threads` and `/thread <id|name|#>`
   switch into one — `get_messages(limit=memory.max_load)` restores the last
   N messages and `context.load_history()` swaps them into short-term memory
   behind the existing system prompt.
2. Before `engine.run()`, the harness stamps the active thread onto the
   `memory_store` tool via `set_thread_context(id, name)` — facts the LLM
   stores this turn carry provenance the model itself cannot forge (the
   tool schema exposes no thread fields).
3. After the run, the REPL persists the delta: every message appended to
   the context during this turn (`context.get_messages()[pre_len:]`) is
   `add_message`'d into the thread. So short-term state flows to long-term
   storage wholesale, once per user turn, without the LLM doing anything.

## The read paths (store → context)

Two modes, one automatic, one just-in-time:

1. Auto-injection at session start: the top `memory.max_inject` (default 5)
   non-archived facts are formatted as "Relevant long-term memory" and
   folded into the system note via `inject_system_note`. The note is
   re-applied (or refreshed with matched approved procedures) every turn so
   `clear()` and thread switches never silently drop it.
2. Just-in-time recall: the LLM calls `memory_recall(query, limit)` when
   personalizing. `hybrid_recall` (`memory/retrieval.py`) returns:
   - LIKE page: case-insensitive substring over topic/fact/tags (precise,
     always available), then
   - vector page: cosine nearest-neighbors via the `sqlite-vector`
     extension over facts embedded with the active model
     (`recall_semantic_vector`), unioned in after the LIKE hits,
     deduped by fact id; then
   - optional rerank: InnKube `qwen3-reranker-4b` rescores the merged set
     (`memory/rerank.py`), order kept on any failure.
   - lazy backfill: before each vector query, up to 100 facts missing an
     embedding for the active model are embedded and attached
     (`_backfill_missing_vectors`).

Every degradation is graceful and never raises to the LLM (tools return
error strings / fall back): missing sqlite-vector extension → LIKE-only;
embedder API failure at store time → text-only fact; semantic query failure
→ LIKE results; reranker failure → hybrid order. Observability counts each
mode via `observe_memory("recall", "semantic"|"keyword"|"empty")`.

## The semantic write path (LLM → store)

The LLM calls `memory_store(topic, fact, tags)` when it judges something
worth persisting across restarts (the tool description steers it away from
ephemeral chat content). `MemoryStoreTool.execute` embeds
`"topic: fact"` via `InnKubeEmbedder` (`octen-embedding-8b`, best-effort),
stamps harness-provided provenance, and calls `store_fact`. Metrics record
`created` vs `deduplicated`.

## End-to-end turn lifecycle

```
user input
  │
  ├─ slash commands? (threads: restore history → context)
  ├─ inject note: recent facts (+ approved procedures)
  ├─ ensure_thread(); stamp set_thread_context()
  │
  ├─ engine.run(): ReAct loop
  │     chat(messages, tools) ──► assistant msg / tool calls
  │     memory_store ──► facts(+embedding) ──► SQLite        (LLM-driven write)
  │     memory_recall ──► hybrid_recall ──► SQLite           (LLM-driven read)
  │     over budget or overflow error ──► maybe_compact()    (short-term trim)
  │     TOOL observations appended to context each iteration
  │
  └─ persist context[pre_len:] ──► messages table            (harness write)
```

## Module map

| File | Role |
|---|---|
| `core/context.py` | Short-term memory: message list, system prompt, injected note, load_history |
| `core/compaction.py` | Window-pressure management: prune + LLM summary checkpoint |
| `core/engine.py` | ReAct loop; triggers auto-compact and overflow retry |
| `memory/store.py` | SQLite long-term store: threads/messages/facts/vectors, tombstones |
| `memory/threads.py` | Thread naming heuristic + id/prefix/name resolution |
| `memory/retrieval.py` | hybrid_recall: LIKE ∪ vector, backfill, rerank hook |
| `memory/embeddings.py` | InnKube/Mock embedders, sqlite-vector loading, pack/pack cosine utils |
| `memory/rerank.py` | InnKube/Mock rerankers, defensive payload parsing |
| `memory/tools.py` | `memory_store` / `memory_recall` LLM tools + thread-context stamping |
| `cli/terminal.py` | Harness: thread lifecycle commands, per-turn persist, note injection |
| `config/settings.py` | `MemoryConfig` (`enabled`, `db_path`, `max_load=50`, `max_inject=5`) |
