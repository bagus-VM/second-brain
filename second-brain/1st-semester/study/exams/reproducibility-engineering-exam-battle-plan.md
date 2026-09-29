---
title: "Reproducibility Engineering — Exam Battle Plan"
tags: [exam-prep, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
exam_date: "2026-07-30"
created: 2026-07-19
status: current
---

# Reproducibility Engineering — Exam Battle Plan

> *"You clearly don't know who you're talking to, so let me clue you in. I am the one who studies."*

**Exam:** 30 July 2026
**Days remaining:** 10 (July 20–29, with July 29 as rest day)
**Scope:** 11 lectures, 11 exercise sheets, 11 in-class exercises

---

## 1. Topic Coverage Map

### What's in scope

The course covers **one central question:** How do we make computational research reproducible? Every topic feeds into this.

| # | Topic | Lab Sheet | IC Sheet | Vault Pages | Flashcards | Coverage |
|---|-------|-----------|----------|-------------|------------|----------|
| 1 | Reproducibility Crisis & Terminology | Sheet 1 | IC 1 | ✅ 5 concepts | ✅ | **Strong** |
| 2 | Levels, Provenance & Standards | Sheet 2 | IC 2 | ✅ 6 concepts | ✅ | **Strong** |
| 3 | Hypotheses & Equivalence | Sheet 3 | IC 3 | ✅ 3 concepts | ✅ | **Strong** |
| 4 | Git Internals & Best Practices | Sheets 4+5 | IC 4+5 | ✅ 6 concepts | ✅ | **Strong** |
| 5 | Reproducible Builds (C, Make) | Sheets 5+6 | IC 5 | ✅ 8 concepts | ✅ | **Strong** |
| 6 | Database Architectures | Sheet 7 | IC 6 | ✅ 4 concepts | ✅ | **Strong** |
| 7 | Tidy Data & SQL | Sheet 8 | IC 7 | ⚠️ 2 concepts | ❌ | **Moderate** |
| 8 | Hierarchical Data (JSON/XML/HDF5) | Sheet 9 | IC 8 | ⚠️ 3 concepts | ❌ | **Moderate** |
| 9 | LLMs & Reproducibility | Sheet 10 | IC 9 | ⚠️ 2 concepts | ❌ | **Moderate** |
| 10 | Remote Experiments & Packaging | Sheet 11 | IC 10 | ⚠️ 1 concept | ❌ | **Weak** |
| 11 | FAIR Principles & Legal | — | IC 11 | ❌ | ❌ | **Weak** |

### Gap Assessment

**Strong coverage (vault + flashcards + practice):** Topics 1–6. You've been through these thoroughly. Flashcards exist. Concept pages are built. You can recall and apply.

**Moderate coverage (practice exists, no flashcards):** Topics 7–9. You've done the exercises and IC sheets, but flashcards are missing. The practice material is solid — you need active recall drilling.

**Weak coverage (no flashcards, sparse vault):** Topics 10–11. Remote experiments and FAIR/legal are newer. The exercise sheets exist but you haven't built the spaced-repetition layer. These are your highest-risk topics.

### Priority Queue (likelihood × weakness)

| Priority | Topic | Why |
|----------|-------|-----|
| 🔴 **P0** | FAIR Principles & Legal (IC 11) | Newest, no flashcards, highly testable (definitions, categorization, case law) |
| 🔴 **P0** | LLMs & Reproducibility (Sheet 10, IC 9) | Timely topic, professor clearly interested, no flashcards, conceptual traps (temperature=0, constrained decoding) |
| 🟡 **P1** | Remote Experiments & HDF5 (Sheet 11, IC 10) | Workflow labeling, tmux, environment recording — specific facts that are easy to test |
| 🟡 **P1** | Tidy Data & SQL (Sheet 8, IC 7) | PIVOT/UNPIVOT, tidying messy data — hands-on SQL that could appear as a practical question |
| 🟡 **P1** | Hierarchical Data & JSON Schema (Sheet 9, IC 8) | allOf/anyOf/oneOf distinctions, jq, HDF5 vs JSON — tricky validation semantics |
| 🟢 **P2** | Database Architectures (Sheet 7, IC 6) | SQLite vs PostgreSQL, MVCC, Docker Compose — solid coverage, quick review |
| 🟢 **P2** | Reproducible Builds (Sheets 5+6, IC 5) | Make, C preprocessor, __TIME__/__FILE__, ReproTest — well-practiced |
| 🟢 **P2** | Git (Sheets 4+5, IC 4) | Interactive rebase, patches, blame, commit hygiene — strong coverage |
| 🟢 **P3** | Hypotheses & Equivalence (Sheet 3, IC 3) | Equivalence levels, hypothesis formulation — conceptual, easy to review |
| 🟢 **P3** | Levels & Provenance (Sheet 2, IC 2) | Bronze/Silver/Gold, VisTrails — well-covered |
| 🟢 **P3** | Reproducibility Crisis (Sheet 1, IC 1) | Repeatability/Reproduction/Replication — foundational, well-covered |

---

## 2. Day-by-Day Study Schedule

### July 20 (Day 1) — 🔴 FAIR & Legal + LLMs (P0 Sprint)

**Morning (2h):** FAIR Principles & Legal
- Read IC 11 thoroughly. This is the freshest and least-reinforced material.
- Create flashcards for:
  - The 4 FAIR categories (Findable, Accessible, Interoperable, Reusable) — 4 principles each
  - Sui generis database right — what it protects, BHB v William Hill, Toll Collect
  - GDPR scope — personal data of identifiable living individuals
  - Copyright vs trade secret vs sui generis — which applies when
  - Stakeholders in FAIR (including computational agents!)
- Work through IC 11 Exercises 1–11 without looking at solutions.

**Afternoon (2h):** LLMs & Reproducibility
- Read Sheet 10 + IC 9 thoroughly.
- Create flashcards for:
  - Temperature=0 → deterministic on CPU, seed irrelevant
  - Temperature>0 → seed alone doesn't guarantee reproducibility
  - Constrained decoding vs schema-in-prompt
  - oneOf vs anyOf — mutual exclusivity
  - Secret handling: env var → .env → mounted file (visibility gradient)
  - .gitignore AND .dockerignore for secrets
  - Prompt components (role, task, constraint, output format, context, style)
- Work through Sheet 10 Exercises 3–5 and IC 9 Exercises 4–10.

**Evening (30min):** Quiz yourself on both topics using newly created flashcards.

---

### July 21 (Day 2) — 🟡 Remote Experiments & HDF5 + Tidy Data

**Morning (2h):** Remote Experiments & HDF5
- Read Sheet 11 + IC 10 thoroughly.
- Create flashcards for:
  - Experiment execution package pattern
  - tmux: `Ctrl-b d` (detach), `tmux a` (attach), `tmux new -s name`
  - SSH vs SCP: `-p` (lowercase) for ssh, `-P` (uppercase) for scp
  - HDF5: groups, datasets, attributes, `h5ls -r`, `h5dump -H`
  - Multi-stage builds: `FROM scratch` for static binaries
  - Environment recording: hostname, os-release, cpuinfo, kconfig
  - Workflow labels: build → binary → run → measured data → graphs/paper
- Work through Sheet 11 Exercises 2–5 and IC 10 Exercises 1–3.

**Afternoon (2h):** Tidy Data & SQL
- Read Sheet 8 + IC 7 thoroughly.
- Create flashcards for:
  - Tidy data rules: variable=column, observation=row, value=cell
  - PIVOT (rows→columns) vs UNPIVOT (columns→rows)
  - CASE/SUM for manual pivot, UNION ALL for manual unpivot
  - Splitting compound columns (STRPOS, LEFT, SUBSTRING)
  - Discretization vs binarization vs one-hot encoding
  - Destructive vs non-destructive vs reversible transformations
- Practice: given a messy table, write the SQL to tidy it. Do IC 7 Exercise 5 (earthquakes) from scratch.

**Evening (30min):** Flashcard review — all new cards from Days 1–2.

---

### July 22 (Day 3) — 🟡 Hierarchical Data & JSON Schema Deep Dive

**Morning (2h):** JSON Schema Mastery
- Read Sheet 9 + IC 8 thoroughly.
- Create flashcards for:
  - JSON object keys are unordered; arrays are ordered
  - `allOf` = all must match; `anyOf` ≥1 must match; `oneOf` = exactly 1 must match
  - `additionalProperties: false` rejects extra keys
  - `minimum`, `maximum`, `exclusiveMinimum` — numeric constraints
  - `enum` restricts to specific values
  - `required` lists mandatory properties
  - `jq .` (pretty), `jq -c` (compact), `jq -S` (sorted keys)
  - Bowtie: meta-validator, pinned containers, exposes implementation differences
  - HDF5 vs JSON vs XML — when to use which

**Afternoon (1.5h):** Practice JSON Schema validation
- Write schemas from scratch: given a description, produce the JSON Schema
- Given schemas and instances, determine validity by hand
- IC 8 Exercises 5–9 without solutions

**Evening (30min):** Flashcard review — all cards.

---

### July 23 (Day 4) — 🟢 Database Architectures & Reproducible Builds Review

**Morning (1.5h):** Database Architectures
- Review Sheet 7 + IC 6 flashcards.
- Key distinctions to lock in:
  - Embedded (SQLite) vs Client-Server (PostgreSQL)
  - SQLite features: serverless, zero-config, single-file, ACID, public domain
  - MVCC and why it matters for mixed workloads
  - Foreign tables are lazy (not validated at creation)
  - Multi-stage Docker builds for benchmarking
  - Docker Compose: healthcheck + depends_on condition

**Afternoon (1.5h):** Reproducible Builds
- Review Sheets 5+6 + IC 5 flashcards.
- Key distinctions:
  - `__TIME__` and `__FILE__` break bitwise reproducibility; `__LINE__` does not (if source unchanged)
  - `gcc` vs `clang` → functionally equivalent, NOT bitwise identical
  - `-O0` vs `-O2` → functionally equivalent, NOT bitwise identical
  - `-g` adds debug sections → NOT bitwise identical
  - Make dependency chains: which targets rebuild when X changes?
  - Heisenbug: side effects in `assert()` disappear with `-DNDEBUG`
  - ReproTest: builds twice in different environments, compares binaries

**Evening (30min):** Do the MC questions from Sheets 6 and 7 without looking.

---

### July 24 (Day 5) — 🟢 Git Deep Review + Hypotheses

**Morning (1.5h):** Git
- Review Sheets 4+5 + IC 4 flashcards.
- Key distinctions:
  - Author vs Committer
  - `git rebase -i`: squash, reword, edit, drop
  - `git reflog` as safety net
  - `git blame` for tracking contributions
  - Patches: `diff -u` → `patch <`
  - `.gitignore` vs `.dockerignore`
  - DCO (Developer Certificate of Origin)
  - Snapshot vs Clone vs Fork — when to use which
  - Commit hygiene: each commit = logical, working unit

**Afternoon (1h):** Hypotheses & Equivalence
- Review Sheet 3 + IC 3 flashcards.
- Key distinctions:
  - Equivalence hierarchy: bitwise > structural > functional > behavioral
  - f(x)=x*2 vs g(x)=x+x — functionally equivalent for integers, NOT for floats
  - Good hypothesis: precise, specific, unambiguous, falsifiable
  - Occam's Razor

**Evening (30min):** MC questions from Sheets 3, 4, 5 without looking.

---

### July 25 (Day 6) — 🔴 Full P0/P1 Rehearsal

**Morning (2h):** Timed practice — all MC questions from Sheets 8–11 and IC 8–11
- Set a timer. 2 minutes per question. No notes.
- After each section, check answers. Note what you got wrong.
- For every wrong answer: WHY was it wrong? Conceptual gap or careless mistake?

**Afternoon (2h):** Gap drilling
- For every gap found in the morning session:
  - Re-read the relevant exercise sheet section
  - Create a new flashcard if one doesn't exist
  - Explain the concept out loud (the Feynman test)

**Evening (30min):** Review ALL flashcards. Focus on ones you keep getting wrong.

---

### July 26 (Day 7) — Full Mock Exam Day

**Morning (2h):** Professor White Mock Exam (see Section 3 below)
- Sit down. No notes. No phone. Timer at 2 hours.
- Write answers as if this were the real exam.

**Afternoon (1.5h):** Self-grading
- Go through each answer against the solutions.
- Be brutally honest. German academic standards: vague = wrong.
- Identify the 3 weakest areas.

**Evening (30min):** Write down the 3 weakest areas on a piece of paper. These are your focus for tomorrow.

---

### July 27 (Day 8) — Targeted Weakness Day

**Full day:** Focus exclusively on the 3 weakest areas from the mock exam.
- For each area:
  1. Re-read the relevant exercise sheets and IC sheets
  2. Re-do the flashcards
  3. Write a one-page summary from memory
  4. Do the MC questions again

**Evening:** Final flashcard run — ALL cards, no exceptions.

---

### July 28 (Day 9) — Light Review & Exam Logistics

**Morning (1h):** Skim all 11 lecture topic summaries in `vault/topics/`
- Don't deep-dive. Just refresh the mental map.
- Check: can you name the key concept from each lecture without looking?

**Afternoon (1h):** Exam logistics
- Where is the exam? What time? What can you bring?
- Review the mock exam one more time. Don't redo it — just read through your answers and corrections.

**Evening:** Stop studying. Go for a walk. You're ready.

---

### July 29 (Day 10) — REST DAY

No studying. Your brain consolidates during rest. Trust the process.

---

## 3. Professor White Mock Exam

> *10 questions. 2 hours. No notes. This is not a half-measure.*

---

### Question 1 — Reproducibility Terminology (8 points)

Classify each scenario as **Repeatability**, **Reproduction**, or **Replication** according to the ACM definitions. Justify each answer in one sentence.

**(a)** (2 pts) Alice runs her own experiment three times on the same machine, using the same script, on the same day.

**(b)** (2 pts) Bob reads Alice's paper, downloads her Docker container from Zenodo, and runs it on his own server.

**(c)** (2 pts) Carol builds a new benchmarking framework from scratch, following Alice's methodology description, to test whether she gets the same conclusions.

**(d)** (2 pts) Dave asks Eve to come to his lab, use his computer, and re-run his experiment using his exact script.

> **Solution:**
> (a) **Repeatability** — same team, same setup, same location.
> (b) **Reproduction** — different team, same experimental setup (via container).
> (c) **Replication** — different team, different setup, same research question.
> (d) **Repetition** — different person, but same equipment, same procedure, same location.

---

### Question 2 — Levels of Equivalence (6 points)

For each pair, identify the **strongest equivalence relationship** that holds: bitwise identity, structural equivalence, functional equivalence, or behavioral equivalence. Briefly justify.

**(a)** (2 pts) Two Docker images built from the same Dockerfile on the same machine, consecutively, with all packages pinned.

**(b)** (2 pts) `{"name":"Alice","age":30}` and `{"age":30,"name":"Alice}` — two JSON documents.

**(c)** (2 pts) A Python script and a Java script that both compute the median of a list and print it to stdout.

> **Solution:**
> (a) **Bitwise identity** — same source, same build environment, same machine, pinned packages → identical layers.
> (b) **Structural equivalence** — same key-value pairs, different key order. JSON objects are unordered.
> (c) **Functional equivalence** — same output for same input, different implementations.

---

### Question 3 — Docker & Reproducibility (8 points)

**(a)** (3 pts) A student's Dockerfile begins with `FROM ubuntu:latest`. Explain three specific reasons why this undermines long-term reproducibility.

**(b)** (3 pts) Compare environment variable injection (`-e OPENAI_API_KEY`) vs mounted secret file (`/run/secrets/openai_api_key`) for passing API keys to a Docker container. Which is more secure against `docker inspect`, and why?

**(c)** (2 pts) What is the difference between a `.gitignore` and a `.dockerignore`? Why should both list the same secret patterns?

> **Solution:**
> (a) `FROM ubuntu:latest`: (1) Pulls whatever the latest version is at build time — a new Ubuntu release changes all packages. (2) Unpinned packages in `apt-get install` may resolve to different versions. (3) The image is not reproducible across time — building today vs next month yields different results.
> (b) Mounted secret file is more secure. `docker inspect` reveals the full value of environment variables in plain text, but for mounted files it only shows the mount point (source/destination paths), not the file contents.
> (c) `.gitignore` prevents files from being committed to Git. `.dockerignore` prevents files from being copied into the Docker build context. Both should list secrets because a `COPY . .` in the Dockerfile would embed `.env` files or secret directories into image layers, where they persist even if deleted in a later layer.

---

### Question 4 — Git Internals (8 points)

**(a)** (2 pts) In `git log`, you see `Author` and `Committer` as separate fields. When would they differ? Give one concrete example.

**(b)** (3 pts) A developer has 5 messy commits: "WIP", "fix typo", "actually fix the bug", "oops forgot a file", "final version". Describe the git command to clean this into 1–2 logical commits. What happens to the original commits?

**(c)** (3 pts) You accidentally ran `git reset --hard HEAD~3` and lost 3 commits. How do you recover them? Name the exact command and explain what it accesses.

> **Solution:**
> (a) They differ when someone other than the original author applies the commit — e.g., when cherry-picking a patch from a mailing list, or when a maintainer rebases another developer's commits. The Author wrote the code; the Committer applied it to this repository.
> (b) `git rebase -i HEAD~5`. In the interactive editor, mark the last 4 commits as `squash` (or `fixup`) to fold them into the first. The original commits are replaced by the new squashed commit(s). The old commit hashes become unreachable (but recoverable via reflog for 30 days).
> (c) `git reflog` to find the hash of the commit that was HEAD before the reset, then `git reset --hard <hash>`. The reflog records all HEAD movements, including destructive operations. It's the safety net for history-rewriting mistakes.

---

### Question 5 — Reproducible Builds (10 points)

**(a)** (3 pts) A C program contains `printf("Built at %s on %s\n", __TIME__, __DATE__);`. Explain why this program can never produce bitwise-identical binaries across two builds, even with the same source, same compiler, and same flags.

**(b)** (3 pts) You compile `hello.c` with `gcc -O0 hello.c -o hello_O0` and `gcc -O2 hello.c -o hello_O2`. Are the two binaries functionally equivalent? Bitwise identical? Justify both answers.

**(c)** (4 pts) Given this Makefile:

```makefile
experiment.pdf: experiment.tex results/chart.pdf
	pdflatex experiment.tex
results/chart.pdf: generate_chart.py results/results.csv
	python3 generate_chart.py
results/results.csv: run_experiment.sh pplease.py recipe.txt
	bash run_experiment.sh
```

After running `make`, you modify only `generate_chart.py` (fix a typo in the legend). You run `make` again. Which targets are rebuilt? Which are NOT rebuilt? Explain the dependency reasoning.

> **Solution:**
> (a) `__TIME__` expands to the current time at compile time (e.g., "14:32:07"). `__DATE__` expands to the current date. Two builds at different times produce different strings, which are embedded in the binary's data section. Even a single byte difference means the binaries are not bitwise identical.
> (b) **Functionally equivalent:** Yes — same source, same behavior (same output for same input). **Bitwise identical:** No — different optimization levels produce different machine code (different instruction selection, loop unrolling, inlining).
> (c) `results/chart.pdf` IS rebuilt (depends on `generate_chart.py`, which changed). `experiment.pdf` IS rebuilt (depends on `results/chart.pdf`, which was rebuilt). `results/results.csv` is NOT rebuilt (does NOT depend on `generate_chart.py`). Make only rebuilds targets whose prerequisites have changed.

---

### Question 6 — Tidy Data & SQL (10 points)

**(a)** (3 pts) The following table is NOT tidy. Explain why, and write the tidy version.

| country | 1999 | 2000 |
|---------|------|------|
| Afghanistan | 745 | 2666 |
| Brazil | 37737 | 80488 |

**(b)** (3 pts) Write a SQL query using `CASE`/`SUM` (no PIVOT) to convert the tidy version back to wide format.

**(c)** (4 pts) A table has a column `rate` with values like `"745/19987071"`. Write a SQL query to split this into two separate columns: `cases` (integer before the slash) and `population` (integer after the slash). Use DuckDB syntax.

> **Solution:**
> (a) The column headers `1999` and `2000` are **values** (years), not variable names. Year should be a variable in its own column. Tidy version:
>
> | country | year | cases |
> |---------|------|-------|
> | Afghanistan | 1999 | 745 |
> | Afghanistan | 2000 | 2666 |
> | Brazil | 1999 | 37737 |
> | Brazil | 2000 | 80488 |
>
> (b)
> ```sql
> SELECT country,
>        SUM(CASE WHEN year = 1999 THEN cases END) AS y1999,
>        SUM(CASE WHEN year = 2000 THEN cases END) AS y2000
> FROM countries_tidy
> GROUP BY country;
> ```
>
> (c)
> ```sql
> SELECT
>     CAST(LEFT(rate, STRPOS(rate, '/') - 1) AS INTEGER) AS cases,
>     CAST(SUBSTRING(rate, STRPOS(rate, '/') + 1) AS INTEGER) AS population
> FROM countries_rate;
> ```

---

### Question 7 — JSON Schema (10 points)

**(a)** (3 pts) Write a JSON Schema that validates an object with:
- `id`: integer, minimum 1, required
- `name`: string, required
- `score`: number, 0–100, required
- No additional properties allowed

**(b)** (4 pts) Given the schema from (a), which of these instances are valid? Justify each.

1. `{"id":1,"name":"Ada","score":90}`
2. `{"id":0,"name":"Bob","score":50}`
3. `{"id":3,"name":"Cy","score":80,"extra":true}`
4. `{"id":4,"score":100}`

**(c)** (3 pts) Explain the difference between `oneOf` and `anyOf` in JSON Schema. Give an example where they produce different results.

> **Solution:**
> (a)
> ```json
> {
>   "type": "object",
>   "required": ["id", "name", "score"],
>   "additionalProperties": false,
>   "properties": {
>     "id": {"type": "integer", "minimum": 1},
>     "name": {"type": "string"},
>     "score": {"type": "number", "minimum": 0, "maximum": 100}
>   }
> }
> ```
>
> (b)
> 1. **Valid** ✓ — all required present, types correct, score in range.
> 2. **Invalid** ✗ — `id: 0` violates `minimum: 1`.
> 3. **Invalid** ✗ — `extra: true` rejected by `additionalProperties: false`.
> 4. **Invalid** ✗ — missing required property `name`.
>
> (c) `anyOf` requires the instance to match **at least one** sub-schema. `oneOf` requires the instance to match **exactly one** sub-schema. Example where they differ: schema `oneOf: [{type: string}, {maxLength: 5}]`. The string `"foo"` matches BOTH sub-schemas (is a string AND length ≤ 5). Under `oneOf`, this is **invalid** (matches more than one). Under `anyOf`, this is **valid** (matches at least one).

---

### Question 8 — LLMs & Reproducibility (8 points)

**(a)** (2 pts) You run the same LLM prompt 10 times with `temperature=0.0` on a CPU-based local server. Are the outputs bitwise identical? What about on a GPU?

**(b)** (3 pts) Explain why constrained decoding (structured outputs) is more reliable than putting the JSON Schema in the prompt for ensuring valid LLM output. What limitation does constrained decoding still have?

**(c)** (3 pts) A research paper uses GPT-4 to classify 10,000 abstracts. List three things the authors must include in the reproduction package to make this step reproducible.

> **Solution:**
> (a) On **CPU**: Yes, bitwise identical. Temperature=0 means greedy decoding (always pick the highest-probability token). CPU floating-point operations are deterministic — same input, same bits. Seed is irrelevant. On **GPU**: Not guaranteed. GPU parallel floating-point operations can have non-deterministic ordering, causing slight differences even at temperature=0.
>
> (b) Constrained decoding enforces the schema at the **grammar level** — the model physically cannot generate tokens that violate the schema. Schema-in-prompt is a *hint* — the model may ignore it, produce malformed JSON, or add extra fields. However, constrained decoding only guarantees **syntactic** validity (correct structure), not **semantic** correctness (factual accuracy). Also, tools may not support all JSON Schema features (e.g., oneOf mutual exclusivity may be silently ignored).
>
> (c) (1) The exact model name and version (e.g., "gpt-4-turbo-2024-04-09"). (2) All parameters: temperature, top_p, seed, max_tokens, system prompt. (3) The raw LLM outputs (cached responses) — since exact reproduction is impossible on a remote API, archive the outputs as data artifacts.

---

### Question 9 — FAIR Principles & Legal (10 points)

**(a)** (4 pts) Match each principle to its FAIR category:
1. "Data are assigned a globally unique and persistent identifier"
2. "Metadata remain accessible even when the data are no longer available"
3. "Meta)data use vocabularies that follow FAIR principles"
4. "Meta)data are released with a clear and accessible data usage license"

**(b)** (3 pts) A German university creates a research database by collecting and curating 50,000 weather measurements over 3 years. A US company scrapes the entire database and republishes it. Does the university have legal protection? Under which law? Explain.

**(c)** (3 pts) Under the EU Database Directive, explain the ruling in **BHB v. William Hill**. Why was the database NOT protected by the sui generis right?

> **Solution:**
> (a)
> 1. **Findable** — persistent identifiers enable discovery.
> 2. **Accessible** — metadata persists even when data is gone.
> 3. **Interoperable** — FAIR vocabularies enable cross-system compatibility.
> 4. **Reusable** — licensing enables reuse.
>
> (b) Yes. The university is protected under the **sui generis database right** (EU Database Directive 96/9/EC). The university made a substantial investment in obtaining, verifying, and presenting the data over 3 years. The US company's bulk extraction constitutes unauthorized extraction of a substantial part. The right applies because the database was created in the EU. However, enforcement against a US entity may require international legal cooperation.
>
> (c) The European Court of Justice ruled that BHB (British Horse Racing Board) **created** the data as part of its normal business activities (organizing races, selecting participants). The sui generis right protects investment in **obtaining existing data**, not in **generating new data**. Since BHB created the data rather than collecting it from external sources, the investment was in data *creation*, not data *obtaining* — and therefore not protected.

---

### Question 10 — Remote Experiment Workflows (7 points)

**(a)** (3 pts) The "experiment execution package" pattern separates build, execution, and analysis. Draw (or describe) the workflow showing which steps happen inside a Docker container and which happen on the target platform. Why is this separation important?

**(b)** (2 pts) You SSH into a remote server and start a long-running experiment. Your SSH connection drops. The experiment is killed. What tool prevents this, and what is the key command to reattach?

**(c)** (2 pts) What environment metadata should a dispatcher script record before running an experiment on a remote machine? Name at least 4 items.

> **Solution:**
> (a) Workflow:
> 1. **Docker container (build):** Compile binary from source → produce statically linked executable
> 2. **Copy to target:** Ship binary + dispatch script to remote server
> 3. **Target platform (run):** Execute experiment on actual hardware
> 4. **Copy back:** Transfer measured data (CSV) to analysis environment
> 5. **Docker container (analysis):** Generate graphs, compile paper
>
> Separation is important because: (1) the target platform may not support Docker (specialized hardware, shared clusters); (2) the build environment is reproducible (Docker); (3) the analysis is reproducible (same Docker); (4) only the execution depends on hardware — and we record the hardware environment for later comparison.
>
> (b) **tmux** (terminal multiplexer). Start experiment inside tmux: `tmux new -s experiment`. Detach: `Ctrl-b`, then `d`. Reattach: `tmux a` (or `tmux attach -t experiment`). tmux keeps the session alive independently of the SSH connection.
>
> (c) (Any 4 of): hostname, OS release (`/etc/os-release`), kernel config (`/proc/config.gz`), boot command line (`/proc/cmdline`), CPU info (`/proc/cpuinfo`), loaded kernel modules (`/proc/modules`), cgroup info, system load.

---

## 4. Quick-Reference Cheat Sheet

### Equivalence Hierarchy
```
Bitwise Identity ⊂ Structural Equivalence ⊂ Functional Equivalence ⊂ Behavioral Equivalence
```

### FAIR (one word per principle)
- **F**indable → identifiers, metadata, searchable
- **A**ccessible → protocol, auth, metadata persists
- **I**nteroperable → standards, vocabularies, references
- **R**eusable → license, provenance, community standards

### JSON Schema Combinators
- `allOf` = AND (all must match)
- `anyOf` = OR (≥1 must match)
- `oneOf` = XOR (exactly 1 must match)

### Tidy Data Rules
1. Each variable = column
2. Each observation = row
3. Each value = cell
4. Each type of observational unit = table

### Docker Security Gradient
```
Environment variable (-e) → .env file → Mounted secret file
  MOST VISIBLE                                    LEAST VISIBLE
  (docker inspect sees value)              (docker inspect sees path only)
```

### Reproducibility Breakers in C
- `__TIME__` → changes every build ✗
- `__DATE__` → changes every day ✗
- `__FILE__` → changes with path ✗
- `__LINE__` → constant if source unchanged ✓
- Different compiler → different binary ✗
- Different flags (`-O0` vs `-O2`) → different binary ✗
- `-g` (debug info) → adds sections, different binary ✗

### Make Logic
- Target rebuilt if: ANY prerequisite is newer than target
- Target NOT rebuilt if: all prerequisites are older than target
- `.PHONY` targets always run (don't correspond to files)

### Git Safety Nets
- `git reflog` — records all HEAD movements (including before reset/rebase)
- `git reset --hard <hash>` — recover to any reflog entry
- `git stash` — save WIP without committing
- `git commit --amend` — fold changes into last commit

---

## 5. Vault Asset Inventory

### Practice Files (all ingested ✅)
- `study/practice/reproducibility-engineering-sheet-{1..11}.md` — 11 lab sheets
- `study/practice/repeng-prof-ic{01..11}.md` — 11 in-class exercises

### Flashcards
- `study/flashcards/reproducibility-engineering-sheet-{1..7}-flashcards.md` — 7 decks ✅
- Sheets 8–11: **MISSING** — created during this prep cycle (Days 1–3)

### Vault Concept Pages
- `vault/concepts/`: 12 pages (reproducibility-crisis, types-of-reproducibility, levels-of-reproducibility, provenance-in-reproducibility, etc.)
- `vault/topics/`: 10 lecture pages (lectures 1–10)
- Missing: FAIR principles, legal aspects, structured outputs concepts

### Recommended Actions After Exam
- File flashcards for Sheets 8–11 permanently
- Create vault pages for FAIR principles, sui generis right, constrained decoding
- Update `courses/reproducibility-engineering.md` to reflect all 11 lectures

---

*This is what you don't know yet. These are your weak points. That's where we start.*
*Say it back to me — what's the difference between `oneOf` and `anyOf`? What does `temperature=0` actually guarantee? What did BHB get wrong?*

*Let's cook.* 🔬
