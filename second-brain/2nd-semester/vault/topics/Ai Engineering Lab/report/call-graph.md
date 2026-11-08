# StudyMate — Call Graph

> Who calls what, where. Every arrow is a real function call; `file:line` refs are to the current
> checkout. Read together with `docs/oral-exam-study-guide.md`.
>
> Legend: solid `-->` = direct call · dashed `-.->` = callback / hook / telemetry · `-->|cond|` =
> conditional branch.

---

## 0. Module-level dependency map

Who imports whom (arrows = "calls into"):

```mermaid
flowchart TD
    CLI["cli/terminal.py<br/>(REPL)"] --> CFG["config/loader.py"]
    CLI --> CTX["core/context.py"]
    CLI --> ENG["core/engine.py"]
    CLI --> TB["tools/base.py<br/>ToolRegistry"]
    CLI --> MEM["memory/store.py + tools.py"]
    CLI --> STU["study/linter.py<br/>griller.py / procedures.py"]
    CLI --> OBS["observability/*"]

    ENG --> LLMB["llm/base.py ABC"]
    ENG --> CTX
    ENG --> TB
    ENG --> CMP["core/compaction.py"]
    ENG --> OBS

    TB --> SEC["security/policy.py<br/>(pure, no I/O)"]
    TB --> TOOL["tools/filesystem.py<br/>delegation.py<br/>mcp/tools.py"]
    TOOL --> PS["tools/filesystem.py<br/>PathSecurityManager"]
    TOOL --> MEM
    TOOL --> MCP["tools/mcp/external.py<br/>services.py"]
    TOOL --> ENG

    CMP --> LLMB
    MEM --> LLMB["embeddings.py / rerank.py"]

    CFG -.->|YAML + .env| CLI
    OBS -.->|observe_* hooks| ENG
```

**Key rule:** `security/policy.py` imports nothing from engine/CLI (pure & unit-testable).
`core/engine.py` does **not** import `memory` (persistence is the CLI's job).

---

## 1. Bootstrap — `main()` → `run_cli()`

`study_agent/cli/terminal.py`

```mermaid
flowchart TD
    M["main() <b>terminal.py:1381</b>"] -->|--inline / non-TTY| RC["run_cli() <b>:786</b>"]
    M -->|"LAUNCH_NEW_TERMINAL"| NW["launch_in_new_window() <b>:1341</b><br/>wt.exe / start → re-invoke --inline"]
    NW --> M

    RC --> A1["load_config() <b>loader.py:42</b>"]
    A1 --> A2["_load_env_file() <b>:8</b>"]
    A1 --> A3["yaml.safe_load → AppConfig(**data)"]
    A1 --> A4["os.getenv INNKUBE_API_KEY <b>:55</b>"]

    RC --> B1["OpenAICompatibleLLMClient(cfg.llm) <b>:795</b>"]
    RC --> B2["ContextManager(system_prompt_path) <b>:796</b>"]
    B2 --> B3["_init_system_prompt() <b>context.py:42</b><br/>custom → soul.md → DEFAULT"]
    B2 --> B4["_render_system_message() <b>:31</b><br/>+ Current date + injected note"]

    RC --> C1["init_metrics(True, host, port) <b>:800</b>"]
    C1 --> C2["prometheus start_http_server :8000"]

    RC --> D1["ToolRegistry(policy=policy_from_config(...)) <b>:803</b>"]
    D1 --> D2["policy_from_config() <b>policy.py:137</b><br/>→ PermissionPolicy(rules) or None"]
    RC --> D3["registry.on_permission_decision.append(<br/>_log_permission_event) <b>:834</b>"]
    RC --> D4["registry.confirmation_handler =<br/>make_confirmation_handler() <b>:832</b>"]

    RC --> E1["register_filesystem_tools() <b>:846</b>"]
    E1 --> E2["PathSecurityManager(...) <b>filesystem.py:41</b>"]
    E1 --> E3["register × 8 tools"]
    RC --> E4["register_mcp_tools() <b>:858</b>"]
    E4 --> E5["ExternalMCPService(command, args)"]
    E4 --> E6["ObsidianVaultService(vault_path)"]
    RC --> E7["register_delegation_tools() <b>:878</b>"]
    RC --> E8["HealthHeartbeat.start() <b>:886</b><br/>daemon thread, tick every 60s"]

    RC --> F1["AgentEngine(llm, registry, cfg, compaction) <b>:930</b>"]
    RC --> G1["MemoryStore(cfg.memory.db_path) <b>:942</b>"]
    G1 --> G2["_init_db() store.py:102 → BEGIN + CREATE TABLE"]
    G1 --> G3["load_sqlite_vector() embeddings.py:12"]
    RC --> G4["InnKubeEmbedder / InnKubeReranker <b>:950</b>"]
    RC --> G5["register_memory_tools() <b>:966</b>"]
    RC --> G6["recall_facts('', limit=5) →<br/>context.inject_system_note(facts) <b>:975</b>"]

    RC --> H1["print_banner() + prompt_toolkit session <b>:1010</b>"]
    H1 --> LOOP{"REPL while True <b>:1023</b>"}
```

---

## 2. REPL turn — dispatch table

```mermaid
flowchart TD
    IN["read_student_input() <b>:240</b><br/>session.prompt / console.input"] --> Q{"input?"}
    Q -->|"empty"| IN
    Q -->|"exit / quit"| OUT["memory_store.close() → break <b>:1031</b>"]

    Q -->|"/help /templates /config /permissions"| DISP["display-only → continue<br/>print_help/print_templates/print_config/print_permissions"]

    Q -->|"/threads"| T1["pick_thread_interactive() <b>:449</b> → get_messages() →<br/>context.load_history() <b>:1052</b> → render_history()"]
    Q -->|"/thread arg"| T2["get_thread / find_threads → load_history() <b>:1092</b>"]
    Q -->|"/new"| T3["context.clear() <b>:1101</b>"]
    Q -->|"/archive-this|-all"| T4["archive_thread()/archive_all() <b>:1115,1131</b><br/>(tombstone, no DELETE)"]
    Q -->|"/clear"| T5["context.clear() <b>:1183</b> — in-memory only"]

    Q -->|"/lint"| L1["run_vault_lint() <b>:569</b><br/>→ VaultLinter.lint()"]
    L1 --> L2{"broken links / metadata issues?"}
    L2 -->|yes| L3["engine.run(repair_prompt, context) <b>:585</b> → re-lint"]
    L2 --> no["render report tables"]

    Q -->|"/grill topic"| G1["user_input = SocraticGriller<br/>.create_initial_prompt(topic) <b>:1158</b>"] --> NORMAL
    Q -->|"/ingest path"| G2["user_input = ingestion prompt<br/><b>:1163-1180</b>"] --> NORMAL
    Q -->|"/compact"| C1["maybe_compact(force=True) <b>:1193</b><br/>→ observe_compaction('manual') → add_message(summary) <b>:1206</b>"]

    Q -->|"plain text"| NORMAL["NORMAL TURN PATH ↓"]
```

---

## 3. Normal turn — before the engine

`terminal.py:1234-1311`

```mermaid
flowchart TD
    N0["user_input (plain text)"] --> P1["match_procedures(dir, input) <b>:1236</b><br/>study/procedures.py:144"]

    P1 -->|"approved found"| P2["format_procedures_block() :194 →<br/>context.inject_system_note(facts + routines) <b>:1240</b>"]
    P1 -->|"none, facts exist"| P3["context.inject_system_note(facts) <b>:1242</b>"]
    P1 -->|"none at all"| P4["context.reset_injected_note() <b>:1244</b>"]
    P2 --> P5["match_procedures(statuses=DRAFT) <b>:1245</b><br/>→ hint only, never auto-followed"]

    P2 --> S1["ensure_thread(user_input) <b>:1253</b><br/>→ generate_thread_name() threads.py:8 → create_thread()"]
    P3 --> S1
    P4 --> S1
    P5 --> S1

    S1 --> S2["pre_len = len(context.get_messages()) <b>:1255</b>"]
    S2 --> S3["registry.get('memory_store')<br/>.set_thread_context(id, name) <b>:1264</b>"]

    S3 --> S4["console.status('StudyMate is thinking...')<br/>spinner_ref['live'] = thinking._live <b>:1267</b>"]
    S4 --> RUN["engine.run(...) <b>:1275</b>"]
```

---

## 4. The ReAct loop — `AgentEngine.run()` (`core/engine.py:254-693`)

```mermaid
flowchart TD
    R["run(user_message, context, on_tool_start, on_tool_end,<br/>thread_id, thread_name) <b>:254</b>"] --> A["run_id = new_run_id() <b>:268</b>"]
    A --> A2{"context is None?"}
    A2 -->|yes — subagent| A3["ContextManager(custom_system_prompt) <b>:270</b>"]
    A2 -->|no — main REPL| A4["reuse long-lived context"]
    A3 --> A5["delegate_task.parent_run_id = run_id <b>:277</b>"]
    A4 --> A5
    A5 --> A6["context.add_user_message(msg) <b>:279</b>"]
    A6 --> A7["emit run_start telemetry <b>:281</b>"]
    A7 --> A8["schemas = registry.list_schemas() <b>:301</b><br/>+ live_handle = start_langfuse_run() <b>:316</b>"]

    A8 --> LOOP{"while iterations &lt; max_iterations <b>:337</b>"}

    LOOP -->|"budget left"| INC["iterations += 1 <b>:339</b>"]
    INC --> Z0{"compaction.enabled?<br/>estimate_tokens &gt; fire_line? <b>:341-356</b>"}
    Z0 -->|yes| Z1["maybe_compact(state) <b>:346</b><br/>→ observe_compaction('threshold') <b>:355</b>"]
    Z0 -->|no| Z2
    Z1 --> Z2["start_langfuse_generation('llm-turn-n') <b>:379</b>"]

    Z2 --> L1["response = llm_client.chat(messages, tools=schemas) <b>:388</b>"]
    L1 -->|raises| L2{"is_context_overflow(e) &&<br/>!overflow_retried <b>:407</b>"}
    L2 -->|yes| L3["maybe_compact(force=True) <b>:414</b><br/>observe_compaction('overflow') → continue"]
    L2 -->|no| L4["observe_llm(status) <b>:405</b> → abort_langfuse_run → <b>raise</b> <b>:429</b>"]
    L1 -->|ok| L5["observe_llm('ok') + observe_component_latency('llm') <b>:431-439</b><br/>finish_langfuse_generation() <b>:450</b>"]

    L5 --> B1["context.add_assistant_message(content, tool_calls) <b>:495</b>"]
    B1 --> B2{"response.tool_calls?"}

    B2 -->|"no — terminal"| B3{"content empty?"}
    B3 -->|"yes, budget left"| B4["context.add_user_message(nudge) <b>:504</b> → continue"]
    B3 -->|"yes, no budget"| B5["_finish(status='empty') <b>:516</b>"]
    B3 -->|"no"| B6{"finish_reason == 'length'?"}
    B6 -->|yes| B7["context.add_user_message('Continue...') <b>:547</b> → continue"]
    B6 -->|no| B8["_finish(status='success') <b>:553</b> → return"]
    B4 --> LOOP

    B2 -->|"yes — Act"| T1["for tool_call in response.tool_calls <b>:581</b>"]
    T1 --> T2["on_tool_start(tool_call) <b>:584</b> &nbsp;emit tool_start <b>:587</b>"]
    T2 --> T3["start_langfuse_tool() <b>:609</b>"]
    T3 --> T4["observation = tool_registry.execute(name, arguments) <b>:615</b>"]
    T4 --> T5["status = 'error' if startswith('Error') <b>:621</b><br/>finish_langfuse_tool, tool_records.append <b>:634</b>"]
    T5 --> T6["on_tool_end(tool_call, observation) <b>:646</b> &nbsp;emit tool_end <b>:649</b>"]
    T6 --> T7["context.add_tool_result(id, name, observation) <b>:657</b>"]
    T7 --> LOOP

    LOOP -->|"exhausted"| FIN["_finish(status='max_iterations') <b>:665</b>"]
```

### 4a. `_finish()` — the single exit point (`engine.py:148-236`)

```mermaid
flowchart LR
    F["_finish(status, final_response, error_message...) <b>:148</b>"] --> F1["duration_s = perf_counter - run_start"]
    F1 --> F2["observe_run(status, duration, iterations) <b>:177</b>"]
    F2 --> F3{"_obs_active()<br/>metrics or langfuse <b>:106</b>"}
    F3 -->|yes| F4["build_run_event() tracing.py:100 →<br/>append_trace() :207"]
    F4 --> F5{"live_handle?"}
    F5 -->|yes| F6["finish_langfuse_run() :210"]
    F5 -->|no| F7["export_langfuse_async() :212"]
    F3 -->|no| F8
    F6 --> F8["AgentRunResult(is_success = status=='success') <b>:218-236</b> → return"]
    F7 --> F8
```

---

## 5. One tool call — registry → policy → jail → tool

```mermaid
flowchart TD
    X1["engine: tool_registry.execute(name, arguments) <b>engine.py:615</b>"] --> X2["ToolRegistry.execute() <b>base.py:128</b>"]

    X2 --> X3{"tool registered?<br/><b>:135</b>"}
    X3 -->|"no"| X4["return 'Error: Tool not registered.'<br/>observe_tool(not_found)"]

    X3 -->|yes| X5["gate = _check_permission(name, args) <b>:141</b>"]
    X5 --> X6{"policy is None?<br/><b>:169</b>"}
    X6 -->|"yes — disabled"| X8
    X6 -->|no| X7["policy.evaluate(name, arguments) <b>policy.py:125</b><br/>session_allow → rules[0 match] → default"]
    X7 --> X9{"decision?"}
    X9 -->|"ALLOW"| X10["emit PermissionEvent(executed=True) <b>base.py:177</b>"] --> X8
    X9 -->|"DENY"| X11["return 'Error: ... denied by permission policy'<br/>emit PermissionEvent(executed=False) <b>:184</b>"]
    X9 -->|"CONFIRM"| X12{"confirmation_handler?<br/><b>:192</b>"}
    X12 -->|"no"| X13["fail-closed → return 'Error: ... no interactive user'"]
    X12 -->|"yes"| X14["approved = handler(name, args, rule) <b>:203</b>"]
    X14 -->|"<b>handler throws</b>"| X15["catch → approved=False (fail closed) <b>:205</b>"]
    X14 -->|"True"| X16["allow_for_session if 'always' <b>terminal.py:750</b>"] --> X10
    X14 -->|"False"| X17["return 'Error: User denied ... Do not retry.' <b>:215</b>"]

    X10 --> X8["tool.execute(**arguments) <b>base.py:147</b>"]
    X8 -->|"<b>raises</b>"| X20["catch → 'Error executing tool: ...' <b>:154</b>"]
    X8 -->|ok| X21["status = 'error' if startswith('Error') <b>:157</b><br/>observe_tool + observe_component_latency('tool')"]
    X20 --> X21

    X8 --> Y1["e.g. ReadFileTool.execute() filesystem.py:179"]
    X8 --> Y2["WriteFileTool.execute() :139"]
    X8 --> Y3["ExternalMCPTool.execute() mcp/tools.py:42"]
    X8 --> Y4["MemoryRecallTool.execute() memory/tools.py:151"]
    X8 --> Y5["DelegateTaskTool.execute() delegation.py:73"]

    Y1 --> J["PathSecurityManager.validate_read_path(path) <b>filesystem.py:81</b>"]
    Y2 --> JW["validate_write_path(path) <b>:93</b>"]
    J --> J2["target = (base_dir / raw).resolve()"]
    JW --> J2
    J2 --> J3{"_is_subpath(target, allowed_root)?<br/>relative_to() <b>:73</b>"}
    J3 -->|no| J4["raise PermissionError → becomes Error string"]
    J3 -->|yes| J5["real FS / pypdf / sqlite operation<br/>(write_file → _atomic_write_text :10)"]
```

---

## 6. Delegation → child engine

```mermaid
flowchart TD
    D1["LLM emits delegate_task tool call"] --> D2["ToolRegistry.execute → permission gate (§5)"]
    D2 --> D3["DelegateTaskTool.execute(subagent_name, task) <b>delegation.py:73</b>"]
    D3 --> D4{"params valid?<br/>subagent registered? <b>:79-91</b>"}
    D4 -->|no| D5["return 'Error: Subagent x not registered...'"]

    D4 -->|yes| D6["subagent_registry.create_engine(name, llm_client,<br/>base_registry=parent, parent_run_id) <b>:95</b>"]
    D6 --> D7["SubagentRegistry.create_engine() <b>subagents.py:85</b>"]
    D7 --> D8["child_tools = ToolRegistry() <b>:104</b>"]
    D8 --> D9["for name in config.allowed_tools:<br/>child_tools.register(same instance) <b>:106</b>"]
    D9 --> D10["child_tools.policy / confirmation_handler /<br/>on_permission_decision ← inherited by reference <b>:111-119</b>"]
    D10 --> D11["return AgentEngine(tools=child_tools,<br/>system_prompt=config.system_prompt,<br/>max_iterations=8|12, parent_run_id) <b>:123-131</b>"]

    D11 --> D12["child_result = child_engine.run(task) <b>delegation.py:103</b>"]
    D12 -.->|"fresh context = None"| RL["<b>§4 ReAct loop (recursion)</b>"]
    RL -.-> D13

    D13{"child_result.is_success?"}
    D13 -->|yes| D14["return child_result.final_response <b>:116</b>"]
    D13 -->|no| D15["return 'Subagent x failed: ...' <b>:120</b>"]
    D13 -->|"TimeoutError"| D16["return 'Error: Subagent timed out' <b>:121</b>"]
    D14 --> D17["→ becomes a TOOL observation in the PARENT history"]
    D15 --> D17
    D16 --> D17

    D14 -.-> D18["_record_run() <b>:142</b> → observe_subagent() +<br/>build_subagent_event() → trace / Langfuse"]
```

---

## 7. Memory paths

### 7a. Store a fact (LLM-initiated)

```mermaid
flowchart LR
    M1["LLM calls memory_store(topic, fact, tags)"] --> M2["permission gate (tier sandbox-edit)"]
    M2 --> M3["MemoryStoreTool.execute() <b>memory/tools.py:80</b>"]
    M3 --> M4["embedder.embed(['topic: fact']) <b>:90</b>"]
    M4 -->|"API down"| M5["log warning → store text-only"]
    M3 --> M6["store.store_fact(...) <b>store.py:391</b>"]
    M6 --> M7{"UNIQUE(topic,fact) conflict?"}
    M7 -->|yes| M8["revive archived row + COALESCE provenance<br/>+ backfill embedding <b>:454-476</b>"]
    M7 -->|no| M9["INSERT + pack_embedding Float32 BLOB"]
    M8 --> M10["observe_memory('store_fact', created|deduplicated) <b>:230</b>"]
    M9 --> M10
    M10 --> M11["return 'Stored fact #12 under topic x.'"]
```

### 7b. Recall (hybrid) — `memory/retrieval.py:39`

```mermaid
flowchart TD
    R1["LLM calls memory_recall(query, limit)"] --> R2["MemoryRecallTool.execute() <b>tools.py:151</b>"]
    R2 --> R3["hybrid_recall(store, query, embedder, limit, reranker) <b>retrieval.py:39</b>"]

    R3 --> R4["1. store.recall_facts(query, limit) <b>store.py:483</b><br/>SQL LIKE '%q%' on topic/fact/tags, id DESC"]
    R3 --> R5{"2. embedder present && query non-empty?"}
    R5 -->|no| R6["return (like_hits, semantic_used=False)"]
    R5 -->|yes| R7["3. _backfill_missing_vectors() :12<br/>≤100 rows/run → embedder.embed()"]
    R7 --> R8["4. store.recall_semantic_vector(pack(qv), model, limit) <b>store.py:541</b><br/>vector_full_scan → JOIN facts, archived=0, model match"]
    R8 -->|"exception"| R9["warn → keyword-only, flag False"]
    R8 --> R10["5. merge: LIKE first, semantic fills slots, dedup by id <b>:65</b>"]
    R10 --> R11{"6. reranker && len ≥ 2?"}
    R11 -->|yes| R12["_apply_rerank() <b>:22</b> → InnKubeReranker.rerank()<br/>httpx.post /rerank rerank.py:84"]
    R12 -->|"exception"| R13["keep hybrid order (warn)"]
    R11 -->|no| R13
    R12 -->|ok| R14["reorder by score desc"]
    R13 --> R15["7. return (records, semantic_used)"]
    R14 --> R15
    R15 --> R16["format_fact_line() :13 + optional<br/>'(vector search unavailable)' note"]
    R15 -.-> R17["observe_memory('recall', semantic|keyword|empty)"]
```

### 7c. Thread persistence & resume (CLI-driven)

```mermaid
flowchart LR
    W1["engine.run returns <b>terminal.py:1275</b>"] --> W2["for msg in context.get_messages()[pre_len:]:<br/>memory_store.add_message(thread_id, msg) <b>:1309</b>"]
    W2 --> W3["store.add_message() <b>store.py:278</b><br/>json.dumps(tool_calls) + touch thread.updated_at"]

    R1["/threads or /thread <b>:1042,1061</b>"] --> R2["pick_thread_interactive / get_thread / find_threads"]
    R2 --> R3["memory_store.get_messages(id, limit=50) <b>store.py:342</b><br/>ORDER BY id DESC → reversed()"]
    R3 --> R4["context.load_history(history) <b>context.py:94</b><br/>messages = [SYSTEM] + history"]
    R4 --> R5["render_history() <b>terminal.py:380</b>"]
```

---

## 8. Compaction — three triggers, one algorithm

```mermaid
flowchart TD
    T1["A. proactive <b>engine.py:341-356</b><br/>before each llm.chat"] --> M
    T2["B. reactive overflow <b>engine.py:414</b><br/>on is_context_overflow(e)"] --> M
    T3["C. manual /compact <b>terminal.py:1193</b>"] --> M

    M["maybe_compact(messages, client, cfg, force, state)<br/><b>compaction.py:136</b>"] --> G1{"guards: enabled / leading SYSTEM /<br/>has tail / compacted_this_run /<br/>consecutive_failures ≥ 2"}
    G1 -->|"blocked"| OUT1["return (False,0,0) — never raises"]
    G1 -->|"force=True skips some"| G2["before = estimate_tokens() = chars//4 <b>:28</b>"]
    G2 --> P1["<b>TIER 1 (free)</b> _prune_old_tool_outputs() <b>:112</b><br/>blank old TOOL contents in place"]
    P1 --> P2["split: recent = tail[-10:], old = rest <b>:170</b>"]
    P2 --> P3{"old turns exist?"}
    P3 -->|no| OUT1
    P3 -->|yes| P4["<b>TIER 2</b> serialize turns (_serialize_turn :124, 2000 chars each)"]
    P4 --> P5["client.chat([USER summary_prompt], tools=None) <b>:176</b>"]
    P5 -->|"empty summary"| P6["raise RuntimeError → caught"]
    P5 -->|ok| P7["hard-truncate to summary_max_tokens*4 chars <b>:184</b>"]
    P7 --> P8["del messages[1:] → append summary(USER) → extend(recent) <b>:185-191</b>"]
    P8 --> P9["state.compacted_this_run = True;<br/>consecutive_failures = 0 <b>:192</b>"]
    P6 --> P10["consecutive_failures += 1 <b>:197</b>"]
    P9 --> OUT2["return (True, before, after)"]
    P10 --> OUT1
```

Window resolution used by the threshold: `resolve_context_window()` (`compaction.py:72`) →
**config map → gateway `/model/info` → model-id suffix regex → default 128000**.

---

## 9. Observability fan-out

```mermaid
flowchart TD
    subgraph ENGINE["Engine hooks"]
        E1["run_start/tool_start/tool_end/run_end<br/>_emit_telemetry() <b>engine.py:93</b>"]
        E2["observe_run / observe_llm / observe_tool /<br/>observe_compaction / observe_component_latency"]
        E3["start/finish_langfuse_run, _generation, _tool"]
        E4["build_run_event → append_trace"]
    end

    subgraph REG["Registry hooks"]
        R1["ToolRegistry._emit() <b>base.py:101</b><br/>on_permission_decision listeners"]
    end

    subgraph CLI["CLI listeners"]
        C1["_log_permission_event <b>terminal.py:834</b><br/>observe_permission + buffer"]
        C2["_flush_permission_buffer <b>:809</b><br/>per turn → build_permission_event"]
        C3["on_tool_start/on_tool_end → Rich ⚙/✓/✗ lines <b>:1218</b>"]
        C4["on_subagent_run → build_subagent_event <b>:867</b>"]
    end

    subgraph HEALTH["Health thread"]
        H1["HealthHeartbeat.tick() <b>health.py:201</b>"]
        H2["probe_external_bridge() :69 (stdio MCP)<br/>probe_obsidian_vault() :111"]
    end

    E1 -.-> C3
    E1 -.-> C4
    R1 -.-> C1
    C1 -.-> C2
    H1 --> H2
    H1 -.-> H3["observe_mcp_health() + build_heartbeat_event()"]

    E2 --> P["Prometheus client<br/>:8000/metrics ← scraped by prometheus.yml (2 jobs)"]
    C1 --> P
    H1 --> P
    E4 --> J["./observability/traces.jsonl<br/>(plain I/O, OUTSIDE the write jail)"]
    C2 --> J
    H3 --> J
    E3 --> L["Langfuse v4 (OTel SDK)<br/>root → generation → tool spans"]
    C2 --> L
    C4 --> L
    H3 --> L
```

---

## 10. Study-layer flows

### `/lint` with auto-repair

```mermaid
flowchart LR
    A["/lint [path] <b>terminal.py:1153</b>"] --> B["run_vault_lint(target, engine, context) <b>:569</b>"]
    B --> C["VaultLinter(target).lint() <b>linter.py:40</b>"]
    C --> D["os.walk *.md → slug map <b>:59</b>"]
    D --> E["per file: frontmatter check :78<br/>wikilink check :94<br/>open-questions check :110"]
    E --> F["orphan check :121 (exclude index/readme/topics/connections)"]
    F --> G{"broken_links or metadata_issues?"}
    G -->|yes| H["engine.run(constrained repair prompt) <b>:585</b><br/>→ tools read_file/edit_file inside the jail"]
    H --> I["re-lint → render tables <b>:601</b>"]
    G -->|no| I
```

### `/grill` and `/ingest` — prompt rewrites, same engine path

```mermaid
flowchart LR
    A["/grill topic <b>:1158</b>"] --> B["user_input =<br/>SocraticGriller.create_initial_prompt(topic) <b>griller.py:24</b>"]
    C["/ingest path <b>:1163</b>"] --> D["user_input = list→read→write→link prompt"]
    B --> E["falls through to the normal turn path (§3)"]
    D --> E
    E --> F["engine.run(user_input, context) — the engine only ever sees TEXT"]
    F -.-> G["GRILL_SYSTEM_PROMPT directives drive<br/>L1 recall → L2 tracing → L3 edge case"]
```

---

## 11. LLM client call — `llm/client.py:104`

```mermaid
flowchart TD
    A["engine: llm_client.chat(messages, tools) <b>engine.py:388</b>"] --> B["OpenAICompatibleLLMClient.chat() <b>client.py:104</b>"]
    B --> C["payload = [m.to_dict() for m in messages]<br/>types.py:37 — json.dumps for tool args"]
    B --> D["if tools: kwargs['tools']=tools; tool_choice='auto' <b>:121</b>"]
    B --> E["openai.ChatCompletion create(model, temperature, max_tokens)"]
    E --> F["parse tool_calls: json.loads(arguments)<br/>→ on JSONDecodeError keep raw string <b>:131</b>"]
    E --> G["_split_think_blocks() :53 + _reasoning_content() :33"]
    E --> H["usage + completion_tokens_details.reasoning_tokens :149"]
    F --> I["LLMResponse(content, reasoning_content, tool_calls,<br/>finish_reason, token counts) types.py:63"]
    G --> I
    H --> I
```

`MockLLMClient.chat()` (`llm/mock.py`) returns the next scripted response from `_current_index`
(incremented per call) — **enqueue exactly as many responses as the loop will make iterations**.

---

## 12. Call index — "where is X defined / who calls it"

| Function | Defined at | Called by |
|---|---|---|
| `main` | `cli/terminal.py:1381` | console script `studymate` |
| `run_cli` | `cli/terminal.py:786` | `main` |
| `load_config` | `config/loader.py:42` | `run_cli:794` |
| `ContextManager._init_system_prompt` | `core/context.py:42` | `ContextManager.__init__`, `clear()` |
| `ContextManager.inject_system_note` | `core/context.py:102` | `run_cli:975,1240,1242` |
| `ContextManager.load_history` | `core/context.py:94` | `/threads`, `/thread` (`:1052,1092`) |
| `AgentEngine.run` | `core/engine.py:254` | `run_cli:1275`, `run_vault_lint:585`, `DelegateTaskTool:103` |
| `AgentEngine._finish` | `core/engine.py:148` | `run` (success/empty/max_iterations exits) |
| `llm_client.chat` | `llm/client.py:104` | `engine.py:388`, `compaction.py:176` |
| `ToolRegistry.execute` | `tools/base.py:128` | `engine.py:615` |
| `ToolRegistry._check_permission` | `tools/base.py:162` | `execute:141` |
| `PermissionPolicy.evaluate` | `security/policy.py:125` | `_check_permission:172` |
| `ConfirmationHandler` (y/n/always) | `cli/terminal.py:708` | `_check_permission:203` |
| `PathSecurityManager.validate_read_path` | `tools/filesystem.py:81` | every read tool, `search_text` walk |
| `PathSecurityManager.validate_write_path` | `tools/filesystem.py:93` | `create_folder/write_file/edit_file/rename_file` |
| `_atomic_write_text` | `tools/filesystem.py:10` | `write_file` |
| `DelegateTaskTool.execute` | `tools/delegation.py:73` | `ToolRegistry.execute` |
| `SubagentRegistry.create_engine` | `core/subagents.py:85` | `DelegateTaskTool.execute:95` |
| `MemoryStore.store_fact` | `memory/store.py:391` | `MemoryStoreTool.execute:94` |
| `hybrid_recall` | `memory/retrieval.py:39` | `MemoryRecallTool.execute:155` |
| `MemoryStore.add_message` | `memory/store.py:278` | `run_cli:1309` (after each run), `:1206` (`/compact`) |
| `maybe_compact` | `core/compaction.py:136` | `engine.py:346,414`, `run_cli:1193` |
| `resolve_context_window` | `core/compaction.py:72` | `engine._window:238`, `print_context_usage` |
| `match_procedures` | `study/procedures.py:144` | `run_cli:1236,1245` |
| `VaultLinter.lint` | `study/linter.py:40` | `run_vault_lint:573` |
| `SocraticGriller.create_initial_prompt` | `study/griller.py:24` | `/grill` handler `:1158` |
| `format_concept_note` | `study/templates.py:66` | agent tool calls / e2e tests |
| `policy_from_config` | `security/policy.py:137` | `run_cli:803` |
| `init_metrics` | `observability/metrics.py:65` | `run_cli:800` |
| `build_run_event` / `append_trace` | `observability/tracing.py:100/158` | `engine._finish:184-207`, CLI error path |
| `observe_permission` / `observe_subagent` | `observability/metrics.py:246/254` | `_log_permission_event`, `_record_run` |
| `HealthHeartbeat.tick` | `observability/health.py:201` | daemon thread `mcp-health-heartbeat` |
| `ExternalMCPService.call_tool` | `tools/mcp/external.py:58` | `ExternalMCPTool.execute:42` |
| `ObsidianVaultService._resolve` | `tools/mcp/services.py:371` | all 9 `obsidian_*` tools + MCP server |

---

*Line numbers verified against the current checkout; re-check after any refactor.*
