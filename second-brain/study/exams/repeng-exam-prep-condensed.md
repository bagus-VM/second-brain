---
title: "Reproducibility Engineering — Condensed Exam Prep"
tags: [exam-prep, reproducibility-engineering, condensed, semester-1]
course: "Reproducibility Engineering"
exam_date: "2026-07-30"
status: current
last_updated: 2026-07-28
prerequisites: []
---

# Reproducibility Engineering — Condensed Exam Prep

> All 10 lectures + 11 lab sheets + 11 in-class exercises, distilled to what matters for the exam.
> Each unit: key concepts, formulas/definitions you must know, and the trap questions.

---

## L1 — Reproducibility Basics & Terminology

**Sheets:** Lab 1 (Docker setup, image comparison), IC 1 (crisis survey, terminology)

### Core vocabulary — know the difference cold

| Term | Who | Same team? | Same method? | Same data? |
|------|-----|-----------|-------------|-----------|
| **Repeat** | Same team, same setup | Yes | Yes | Yes |
| **Reproduce** | Different team, same setup | No | Yes | Same/similar |
| **Replicate** | Different team, different setup | No | Similar but own | New data |

**Reproducibility crisis:** 1,576 researchers surveyed (Nature, 2016). 52% agreed there is a significant crisis. 90% of scientists have failed to reproduce someone else's experiments. 70% failed to reproduce their own.

**ACM Artifact Badging:**
- Artifacts Available (Badge: green) — artifact is publicly archived
- Artifacts Functional (Badge: blue) — artifact runs, documented, reusable
- Artifacts Reusable (Badge: gold) — functional + exceeds minimal requirements

**Three types of reproducibility:**
1. Computational — same code, same data, same environment → same result
2. Empirical — same experimental setup, different team → same result
3. Statistical — same analysis method on same/similar data → same conclusions

**Research artifacts (ACM taxonomy):** data, code, workflows, models, documentation.

**Docker basics (Sheet 1):**
- Image = read-only template (blueprint). Container = running instance.
- Dockerfile = script to build an image. Layered architecture: app container → Docker engine → host OS kernel.
- `docker build`, `docker run -it`, `docker exec`, `docker cp`, `docker run -v` (bind mount).
- SHA-256 checksums detect hidden differences (steganography example: fox.jpg vs fox_secret.jpg looked identical, hashes differed).
- Pearson correlation on pixel arrays: close to 1.0 = nearly identical. Formula: r = Σ(xi - x̄)(yi - ȳ) / √(Σ(xi - x̄)² × Σ(yi - ȳ)²).

**Trap:** "Reproduce" and "replicate" are NOT synonyms. Reproduce = same method, different team. Replicate = different method, different team.

---

## L2 — Levels of Reproducibility & Provenance

**Sheets:** Lab 2 (randomness, levels), IC 2 (VisTrails, Bronze/Silver/Gold)

### Framework 1: VisTrails three dimensions (Freire et al.)

| Dimension | Question | Levels |
|-----------|----------|--------|
| Availability | What can you access? | Nothing → data → code → workflow → all |
| Repeatability/Reproducibility/Replicability | Same/different team, same/different method | Repeat (same) → Reproduce (diff team) → Replicate (diff all) |
| Confirmability | Can you reach the same conclusion? | Low → medium → high |

### Three provenance types

| Type | What it captures | Example |
|------|-----------------|---------|
| **Prospective** | The workflow specification (what SHOULD happen) | A script / pipeline definition |
| **Execution** | What actually ran — steps, parameters, timing | Log of actual runs with timestamps |
| **Version** | Which versions of data/code were used | Git commit hashes, data snapshots |

### Framework 2: Heil et al. Bronze/Silver/Gold (ML reproducibility)

| Level | Requirement | What you share |
|-------|-------------|----------------|
| **Bronze** | Share | Data + code + model + documentation |
| **Silver** | Document | Bronze + detailed config + environment + hyperparameters |
| **Gold** | Automate | Silver + containerized pipeline + automated re-run from scratch |

**Trap:** "Gold" in Heil et al. means automated reproducibility, not "best results." A Bronze variant might be enough if your paper is about method X, not about the pipeline.

### Handling randomness (Sheet 2)
- Seeding RNGs: `np.random.seed(42)`, `torch.manual_seed(42)`.
- Non-determinism sources: GPU floating-point, parallel data loading, atomic operations.
- Ex: training a model twice with the same seed on the same GPU → should get same weights. On different GPU architectures → might differ.
- Fixed seeds make runs repeatable (same team). For full reproduction by others, you also need: exact library versions, hardware specs, runtime flags.

**Trap:** `temperature=0` and a fixed seed do NOT guarantee bitwise-identical LLM output across hardware runs. But they do help.

---

## L3 — Hypotheses & Experimental Design

**Sheets:** Lab 3 (experiment dispatching), IC 3 (Zobel's guidelines, equivalence levels)

### Good hypothesis properties (Zobel)

- **Precise** — no vague terms. "Runs faster" → "runs 20% faster on benchmark X."
- **Specific** — state what is claimed and what is NOT claimed.
- **Unambiguous** — one interpretation only.
- **Falsifiable** — there must exist an experiment that could disprove it.
- **Contradictory** hypotheses are bad — if your hypothesis contradicts your stated limitation, it's invalid.

### Presenting experiments

Structure: **Setup** (datasets, baselines, metrics, hardware) → **Results** (tables/figures, what happened) → **Discussion** (interpretation, limitations, threats to validity).

### Levels of equivalence — by increasing strictness

1. **Bitwise identity** — byte-for-byte identical outputs. Strongest. Ex: SHA-256 hash match.
2. **Structural equivalence** — same structure, possibly different representation. Ex: two JSON files with same key-value pairs but different key order.
3. **Functional equivalence** — same input → same output, different internals. Ex: two sort implementations producing the same sorted list.
4. **Behavioral equivalence** — same observable behavior over time, different internals. Ex: two database engines returning the same query results but with different execution plans.

**Comparing methods:** Use precise comparatives. "Method A is faster than Method B" → "Method A runs 23% faster than Method B on average across 5 trials." Single runs are insufficient — statistical comparison needs multiple trials, error bars, significance tests.

**Experiment dispatching (Sheet 3):**
- Dispatching = running experiment in a controlled container.
- Binary containers: strip everything except what's needed to run the experiment.
- Dependency management: pin all versions in Dockerfile, `pip freeze > requirements.txt`, isolate build env.
- Passing extra Dockerfiles into a running container for additional setup.

**Trap (Occam's Razor):** If two hypotheses explain the same observations, prefer the simpler one (fewer assumptions). But Occam's Razor does NOT say the simpler one is correct — it says don't add complexity without evidence.

---

## L4 — Git for Reproducibility

**Sheets:** Lab 4 (LaTeX in Docker, structural equivalence), Lab 5 (Git basics, rebasing, patches), IC 4 (commit hygiene, history)

### Git internals (content-addressable storage)

- Four object types: **blob** (file content), **tree** (directory listing), **commit** (snapshot + metadata + parent), **tag** (named label).
- SHA-1 (or SHA-256 in newer Git) hash of content → object ID.
- Commits form a **DAG** (directed acyclic graph). Each commit points to parent(s) + tree.
- Tamper-evident: changing any content changes the hash, which cascades to all ancestor commits.

### Commit hygiene (Norm's cautionary tale)

- **Atomic commits** — one logical change per commit. Don't mix "add feature X" with "fix bug in Y."
- **Imperative subject** — "Add feature X" not "Added feature X" or "Adds feature X."
- **No WIP commits** on shared branches. Use `git commit --fixup` + `git rebase -i --autosquash` to clean up before pushing.
- Trailer blocks: `Signed-off-by`, `Reviewed-by`, `Tested-by` — the **trail of responsibility** (DCO).

### Rebasing and history rewriting

- `git rebase -i HEAD~N` — squash, reorder, edit, drop commits in the last N.
- `git rebase --autosquash` with `fixup!` / `squash!` commits → auto-reorders them next to the original.
- **Golden rule:** Never rebase commits that have been pushed to a shared branch. Rewrite local history only.

### Patches and diffs

- Unified diff format: `@@ -old_start,old_count +new_start,new_count @@`
- `git format-patch` produces email-able `.patch` files.
- `git am` applies patches from mailbox format.
- Three strategies for using upstream code:
  1. Snapshot — copy code at a specific version. Simplest, no upstream connection.
  2. Clone + patches — clone the repo and maintain local patches on top. Patches can be sent upstream.
  3. Fork — full repo with GitHub PR workflow. Best for active collaboration.

### Structural equivalence in LaTeX (Sheet 4)

- Two LaTeX documents with different whitespace, comments, or formatting → different source files → but same compiled PDF.
- Structural equivalence = same content tree, different surface representation.
- Automated reporting: generate LaTeX from scripts, not by hand. `latexmk` automates compilation.
- XPath: query XML documents (e.g., experiment configs) by path expressions.

**Trap:** "git merge" and "git rebase" both combine branches but produce different commit histories. Merge preserves history (merge commit). Rebase rewrites history (linear, no merge commit). Don't rebase public branches.

---

## L5 — Reproducible Builds

**Sheets:** Lab 6 (binary builds, Make, diffoscope), IC 5 (C compilation, preprocessor, heisenbugs)

### What is a reproducible build?

Given the same source + build instructions + build environment → byte-for-byte identical artifact.

**Formal criteria (reproducible-builds.org):** Any party can recreate bit-identical copies of all specified artifacts.

### Sources of non-determinism (learn the full list)

| Source | Example | Fix |
|--------|---------|-----|
| Timestamps embedded | `__TIME__`, `__DATE__` macros | Use `SOURCE_DATE_EPOCH` env var |
| Filesystem ordering | `$(wildcard *.c)` order varies | Sort explicitly: `$(sort $(wildcard *.c))` |
| Embedded paths | `__FILE__` includes absolute build path | Use relative paths or `--debug-prefix-map` |
| Parallelism | Race conditions in build steps | Pin thread count, or serialize critical steps |
| Randomness | uninitialized memory, ASLR | Pin ASLR off, zero-initialize |
| Locale | Different locale → different output | `LC_ALL=C` |
| Compiler version | Different compiler → different binary | Pin compiler version in Dockerfile |

### C compilation pipeline

```
Source (.c) → Preprocessor → Compiler → Assembler → Linker → Binary
```

- Preprocessor: `#include`, `#define`, `#if` / `#ifdef` / `#ifndef`.
- `__TIME__`, `__DATE__`, `__FILE__`, `__LINE__` — preprocessor macros that inject non-determinism.
- Make: `make -j4` for parallel builds. `$(wildcard *.c)` for file globbing (non-deterministic order!).

### diffoscope

Tool for comparing two builds at a deep structural level. Disassembles binaries, compares ELF headers, compares embedded archives recursively. Pinpoints exactly WHERE and HOW two builds differ.

### SOURCE_DATE_EPOCH

Standard environment variable (defined by the Reproducible Builds project) that replaces `__TIME__` and `__DATE__` with a fixed timestamp (e.g., the git commit time). This is THE standard fix for timestamp non-determinism.

### Heisenbug

A bug that disappears or changes behavior when you try to observe it (e.g., adding print statements, running under a debugger, or changing the build configuration). Classic example: linking order changes due to filesystem ordering cause a latent bug to surface on one machine but not another. Fix: deterministic build environment (pin everything: compiler, flags, file ordering, environment variables).

**Trap:** `$(wildcard)` returns files in directory-entry order, which is filesystem-dependent. Two developers on different filesystems get different file lists → different link orders → potentially different binaries.

---

## L6 — Database Architectures & Reproducibility

**Sheets:** Lab 7 (BenchBase: SQLite vs PostgreSQL), IC 6 (architectures, foreign tables)

### Three DB architectures

| Architecture | Examples | Reproducibility tradeoff |
|-------------|----------|--------------------------|
| File-based / serverless | SQLite | Copy the file → done. Simplest to reproduce. |
| Client/server | PostgreSQL, MySQL | More moving parts (server process, network, config). Harder to reproduce. |
| Embedded | SQLite library, BerkeleyDB | DB engine linked into app. Medium difficulty. |

### SQLite features (know for MC)

- Serverless (no separate process), zero-config, single-file, self-contained, ACID, SQL92-compatible, public domain.
- Public domain = no license restrictions, unlike PostgreSQL (BSD) or MySQL (GPL).
- Limitations: no user management (unlike PostgreSQL), limited concurrency (database-level locking), no network access built in.

### Docker Compose for reproducible DB stacks

- `compose.yaml` declares multiple services (e.g., DB server + benchmark client).
- Each service is a container with pinned versions, configs, and network setup.
- Reproducible across machines: `docker compose up` gives the same DB stack everywhere.
- Version pinning: `image: postgres:16.3-alpine` (not `postgres:latest`).

### PostgreSQL foreign tables

- Feature: access data from external sources as if they were local tables.
- Use case: capture system information (OS version, CPU, memory) during experiments by exposing them as foreign tables inside the database.
- `CREATE FOREIGN TABLE ... SERVER ...` — foreign server wraps a data source (file, API, another DB).

### BenchBase (Sheet 7)

- Benchmarking framework for DBMS performance testing.
- Exercise: compare SQLite vs PostgreSQL on same workload.
- Throughput, latency, scalability metrics.
- Different DB architectures → different performance profiles → different reproducibility requirements.

**Trap:** SQLite uses database-level write locking (one writer at a time). PostgreSQL uses MVCC (multi-version concurrency control, multiple writers). This affects concurrency but NOT the reproducibility of a single run.

---

## L7 — Tidy Data

**Sheets:** Lab 8 (DuckDB, tidy data), IC 7 (Wickham's rules, metadata)

### Wickham's three rules of tidy data

1. Each **variable** forms a column.
2. Each **observation** forms a row.
3. Each **value** forms a cell.

All three must hold simultaneously. Violate ANY → untidy.

### Common untidy patterns

| Pattern | Example | Fix |
|---------|---------|-----|
| Column headers are values | `male`, `female` as columns | Unpivot (melt): create `sex` column + `count` column |
| Multiple variables in one column | `180cm` in one column | Split into `height` + `unit` |
| Variables in both rows and cols | Patients × dates grid | Melt into `date` + `temperature` |
| Multiple types in one table | Demographics + lab results mixed | Split into separate tables |
| One variable in multiple columns | `first_name`, `last_name` for full name | Combine or keep depending on analysis |

### Pivoting and unpivoting in SQL

**Unpivot (wide → tall):** Turn many columns into one + a key column.
```sql
SELECT patient, '1995' AS year, mag_1995 AS magnitude FROM quakes
UNION ALL
SELECT patient, '1996' AS year, mag_1996 FROM quakes ...
```

**Pivot (tall → wide):** Turn one column's values into multiple columns.
```sql
CREATE TABLE pivoted AS
SELECT patient,
  SUM(CASE WHEN year=1995 THEN magnitude END) AS mag_1995,
  SUM(CASE WHEN year=1996 THEN magnitude END) AS mag_1996
FROM tidy GROUP BY patient;
```

### DuckDB (Sheet 8)

- In-process analytical SQL engine (like SQLite for analytics).
- No server, no installation, reads CSV/Parquet directly.
- `INSTALL` / `LOAD` extensions, `PRAGMA` for settings.

### Metadata and workflow reproducibility

- Data exploration is a workflow — every transformation should be **reversible** (undo) or **destructive-but-logged** (trace provenance).
- Discretization: convert continuous to categorical (binning).
- Binarization: convert to 0/1.
- Dummy variables: one-hot encoding for categorical data.

**Trap:** "80% of data analysis is cleaning" (Wickham). Tidying is not optional cleanup — it's the FIRST step that makes all downstream operations composable and reproducible.

---

## L8 — Hierarchical Data Formats

**Sheets:** Lab 9 (JSON + JSON Schema), IC 8 (JSON, XML, HDF5, comparisons)

### XML, JSON, HDF5 comparison

| Feature | Relational | XML | JSON | HDF5 |
|---------|-----------|-----|------|------|
| Structure | Flat tables | Tree (nested elements) | Tree (objects/arrays) | Tree (groups/datasets) |
| Schema | Strict (upfront) | Optional (XSD/DTD) | Optional (JSON Schema) | Self-describing (attributes) |
| Size | Small-medium | Verbose | Medium | Large (binary) |
| Use case | Transactional DBs | Document exchange | APIs, config | Scientific data |

### JSON Schema

Validates JSON structure. Key keywords:

| Keyword | What it does |
|---------|-------------|
| `type` | `"string"`, `"object"`, `"array"`, `"integer"`, `"number"`, `"boolean"`, `"null"` |
| `properties` | Defines object keys and their schemas |
| `required` | Array of keys that must be present |
| `items` | Schema for array elements |
| `additionalProperties` | `false` = no extra keys allowed |
| `enum` | Fixed set of allowed values |
| `pattern` | Regex constraint on strings |
| `minimum` / `maximum` | Numeric bounds |
| `minLength` / `maxLength` | String length bounds |

### Composition keywords

| Keyword | Logic |
|---------|-------|
| `allOf` | Must satisfy ALL sub-schemas (logical AND) |
| `anyOf` | Must satisfy AT LEAST ONE (logical OR) |
| `oneOf` | Must satisfy EXACTLY ONE (logical XOR) |
| `not` | Must NOT satisfy the sub-schema |

**Trap:** `oneOf` = exactly one match, not "at least one." `anyOf` = at least one. If you use `oneOf` where you mean `anyOf`, valid data matching two sub-schemas will FAIL validation.

### HDF5

- Hierarchical Data Format v5. Stores large multi-dimensional scientific datasets.
- Structure: **Groups** (like directories) contain **Datasets** (multi-dimensional arrays) and other Groups.
- **Attributes**: metadata attached to groups/datasets. Max 64 KB per attribute.
- Self-describing: metadata lives inside the file.
- `h5py` Python library: `f.create_group()`, `f.create_dataset()`, `d.attrs['unit'] = 'meters'`.
- Visitor pattern: traverse the HDF5 tree by visiting each node.

### Bowtie (JSON Schema meta-validator)

- Meta-validator for JSON Schema implementations.
- Runs multiple validators in pinned containers, exposes implementation differences.
- Useful for finding validators that silently ignore keywords like `oneOf` mutual exclusivity.

### Pretty-printing JSON (Sheet 9)

- `python -m json.tool` — pretty-prints JSON (indented).
- `jq` — command-line JSON processor. `jq -c` compacts; `jq -S` sorts keys.
- Sorted keys are important for reproducible comparisons: `{a:1, b:2}` and `{b:2, a:1}` are structurally equivalent but byte-different.

---

## L9 — LLMs and Reproducibility

**Sheets:** Lab 10 (LLM reproducibility, secrets), IC 9 (local vs remote, structured output)

### Why LLMs are hard to reproduce

LLMs are probabilistic sampling engines over learned distributions. Even with `temperature=0` and a fixed `seed`, outputs can differ across:
- GPU model / driver version
- Framework version (PyTorch, CUDA, cuDNN)
- Batching and parallelism settings
- Silent model updates by API providers (OpenAI may update `gpt-4` without notice)

### Reproduction package for LLM experiments

Must pin:
1. Model identifier + version (commit hash for local, API version for remote)
2. Exact prompts (decomposed by role: system, user, assistant)
3. Parameters: `temperature`, `seed`, `max_tokens`, `top_p`, `top_k`
4. Sample outputs from the original run (for comparison)
5. Client library version (e.g., `openai==1.30.0`)

### Local vs Remote LLM trade-off

| Property | Local (container) | Remote API |
|----------|-------------------|-----------|
| Self-contained | Yes (weights in image) | No (depends on external service) |
| Container size | Large (GB to hundreds of GB) | Small (just client code) |
| Bitwise reproducible | Possible but hard | No (provider controls model version) |
| Cost | High upfront (GPU + storage) | Pay per token |
| Version drift | You control it | Provider may update silently |

### Structured outputs

- Constrain LLM to output valid JSON matching a schema.
- **Constrained decoding**: at each generation step, mask tokens that would produce invalid JSON.
- **JSON Schema**: same schema format as hierarchical data (L8). LLM can only produce JSON that validates against the schema.
- OpenAI structured outputs: `response_format: { type: "json_schema", json_schema: {...} }`.

### Secrets in containers (Sheet 10)

- Docker secrets: `docker secret create`, mounted at `/run/secrets/<name>`.
- Environment variables are NOT secure (visible in `docker inspect`).
- Multi-stage builds: build stage has tools + source, runtime stage has only the binary. Smaller image, fewer attack surfaces.

**temperature=0 precision fix:**
- On **CPU**: bitwise identical (greedy decoding + deterministic floating-point). Seed is irrelevant.
- On **GPU**: NOT guaranteed (parallel floating-point non-determinism, even at temperature=0).
- For true determinism: CPU + fixed seed + pinned library versions.

**Trap:** `temperature=0` on GPU does NOT guarantee determinism. On CPU it does. The exam tests this distinction.

---

## L10 — Remote Experiments & Artifact Packaging

**Sheets:** Lab 11 (multi-stage builds, HDF5, remote containers), IC 10 (workflow stages, SQPolite)

### The remote experiment workflow (Mauerer & Scherzinger, ICDE 2021)

Five stages with clear dependency ordering:

```
1. Build artifacts         →  compile the software (may run on different machine)
2. Experiment execution    →  bundle binary + config + scripts into executable package
3. Run experiments         →  execute on target platform (cluster, cloud, lab machine)
4. Measured data           →  collect results (CSV, logs, measurements)
5. Generate graphs + paper  →  analyze data, produce figures, compile LaTeX
```

Dependencies: `Source → Build → Execution Package → Experiments → Data → Analysis → Paper`

- **Integration** (A → B): B incorporates A (e.g., execution package includes build artifacts)
- **Production** (A ⇒ B): A produces B (e.g., running experiments produces measured data)

### Why remote experiments break reproducibility

- Target platform may not support Docker (e.g., HPC clusters, some cloud instances).
- Different hardware (CPU architecture, memory) → different floating-point results.
- No root access → can't install packages or configure system.
- Solution: ship a self-contained execution package with pinned dependencies.

### Multi-stage Docker builds (Sheet 11)

```dockerfile
# Build stage
FROM gcc:13 AS builder
COPY src/ /src/
RUN cd /src && make

# Runtime stage
FROM debian:bookworm-slim
COPY --from=builder /src/myapp /usr/local/bin/myapp
CMD ["myapp"]
```

- Build stage has compiler + source + build tools.
- Runtime stage has ONLY the binary + minimal OS.
- Result: smaller image, fewer vulnerabilities, no build tooling leaked into production.
- Reproducibility benefit: runtime environment is minimal and fully controlled.

### HDF5 for experiment data (Sheet 11)

- Store measured data in HDF5: hierarchical, self-describing, efficient for large arrays.
- Attach provenance metadata as HDF5 attributes (experiment ID, timestamp, hardware info).
- Inspect with `h5dump`, `h5ls`, or `h5py` in Python.

### Practical remote experiment tools (Sheet 11)

- **tmux**: terminal multiplexer. Keeps sessions alive after SSH disconnect.
  - `tmux new -s name` — create named session
  - `Ctrl-b d` — detach (session keeps running)
  - `tmux a -t name` — reattach
- **SSH vs SCP port flag**: `-p` (lowercase) for ssh, `-P` (uppercase) for scp.
- **Environment recording**: before running, record hostname, `/etc/os-release`, `/proc/cpuinfo`, `/proc/cmdline`, `/proc/config.gz`, `/proc/modules`, system load.
- **Static binaries**: `FROM scratch` for runtime stage with statically linked binary = minimal image.

### SQPolite case study (IC 10)

- Real-world example of the remote experiment workflow.
- Git for source code provenance (snapshot, clone+patches, fork strategies).
- Build artifacts reproduced from same source + same toolchain.
- Patches encode modifications to upstream code → tracked and version-controlled.

---

## L11 — FAIR Principles & Legal Aspects

**Sheets:** IC 11 (FAIR, copyright, GDPR, trade secrets, sui generis)

### FAIR principles (Wilkinson et al., 2016)

| Letter | Principle | Meaning |
|--------|-----------|---------|
| **F**indable | Data is discoverable | Persistent identifiers (DOIs), rich metadata, indexed in searchable resources |
| **A**ccessible | Data can be retrieved | Open access or clear access protocol, authentication if needed |
| **I**nteroperable | Data works with other systems | Common formats, shared vocabularies, standard ontologies |
| **R**eusable | Data can be reused | Clear license, detailed provenance, community standards |

**What FAIR applies to:** research data, algorithms, software tools, workflows.
**What FAIR does NOT guarantee:** openness. FAIR data can be restricted (authenticated access) but must be accessible with clear protocols.

### Legal frameworks for research data

| Framework | What it protects | Relevance to research |
|-----------|------------------|----------------------|
| **Copyright** | Creative expression (code, papers, figures) | Code is copyrighted; datasets of facts generally are not |
| **GDPR** | Personal data of EU residents | If your dataset contains personal data, need consent + anonymization |
| **Trade secrets** | Confidential business information | If data is under NDA, sharing it breaks the agreement |
| **Database sui generis right** (EU) | Investment in database compilation | EU grants rights to database MAKERS for substantial investment in collecting/verifying data |

**Trap:** Copyright protects expression, not facts. A dataset of temperature measurements is not copyrightable, but the specific arrangement or selection might be (sui generis right). Code is copyrightable. Papers are copyrightable. The IDEA behind an algorithm is not copyrightable (but might be patentable).

---

## Quick-Reference: All Formulas & Definitions

| Concept | Formula / Definition |
|---------|---------------------|
| Repeat | Same team, same setup |
| Reproduce | Different team, same setup |
| Replicate | Different team, different setup |
| Bitwise equivalence | SHA-256 hashes match |
| Structural equivalence | Same tree structure, different surface |
| Functional equivalence | Same I/O, different internals |
| Repeatability levels (VisTrails) | Availability × RRR × Confirmability |
| Provenance types | Prospective (spec), Execution (log), Version (commit hash) |
| Heil Bronze | Share artifacts |
| Heil Silver | Document everything |
| Heil Gold | Automate the pipeline |
| Reproducible build | Same source + env + instructions → bit-identical artifact |
| SOURCE_DATE_EPOCH | Replaces `__TIME__`/`__DATE__` with fixed timestamp |
| `$(wildcard)` fix | `$(sort $(wildcard *.c))` |
| Tidy data | Variables=columns, observations=rows, values=cells |
| JSON Schema oneOf | Exactly one sub-schema must match |
| JSON Schema anyOf | At least one must match |
| JSON Schema allOf | All must match |
| HDF5 attribute limit | 64 KB per attribute |
| LLM reproduction package | Model version + prompt + params + sample outputs + client version |
| `temperature=0` | Greedy decoding but NOT bitwise deterministic |
| FAIR | Findable, Accessible, Interoperable, Reusable |
| Multi-stage build | Build stage (tools+source) → runtime stage (binary only) |
| Remote experiment stages | Build → Execution package → Run → Data → Analysis |

---

## Top 10 Trap Questions

1. **"Reproduce = replicate"** — NO. Reproduce = same method, different team. Replicate = different method, different team.
2. **"`temperature=0` makes LLM output deterministic"** — NO. Greedy decoding but floating-point non-determinism on GPU. Even CPU can differ across library versions.
3. **"`$(wildcard)` is deterministic"** — NO. Returns files in filesystem-dependent order. Use `$(sort ...)`.
4. **"`oneOf` = at least one match"** — NO. Exactly one. `anyOf` = at least one.
5. **"SQLite is open source"** — It's PUBLIC DOMAIN. No license at all. PostgreSQL is open source (PostgreSQL License, BSD-like).
6. **"FAIR means open access"** — NO. FAIR means findable and accessible (with clear access protocol). Data can be FAIR and restricted.
7. **"Copyright protects datasets"** — Facts are not copyrightable. But the selection/arrangement might get a sui generis database right in the EU.
8. **"Bronze/Silver/Gold = better/worse quality"** — NO. It's levels of reproducibility documentation: share → document → automate.
9. **"Git merge and rebase produce the same result"** — Same final content, different commit history. Merge preserves, rebase rewrites.
10. **"Tidy data = clean data"** — NO. Tidy = specific structural property (3 rules). Clean = no errors/duplicates. A tidy dataset can have dirty values.

---

## Connections

- [[reproducibility-engineering-lecture-1]] through [[reproducibility-engineering-lecture-10]]
- [[reproducibility-engineering-sheet-1]] through [[reproducibility-engineering-sheet-11]]
- [[repeng-prof-ic01]] through [[repeng-prof-ic11]]
- [[reproducibility-crisis]], [[repeat-reproduce-replicate]], [[types-of-reproducibility]]
- [[levels-of-reproducibility]], [[provenance-in-reproducibility]], [[reproducibility-standards-bronze-silver-gold]]
- [[containerization-for-builds]], [[deterministic-builds]], [[diffoscope]]
- [[git-dag-structure-and-internals]], [[git-rebasing-and-history-rewriting]], [[git-commit-hygiene]]
- [[sqlite-architecture]], [[docker-compose]], [[foreign-tables-postgresql]]
- [[tidy-data]], [[json-schema]], [[hdf5]]
- [[artifact-packaging]], [[workflow-reproducibility]], [[data-provenance]]

---

## Open Questions

- None remaining — all exercises and lectures are fully ingested.