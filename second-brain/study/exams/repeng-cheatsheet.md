---
title: "Reproducibility Engineering — Definitions & Formulas Cheatsheet"
tags: [exam-prep, cheatsheet, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
exam_date: "2026-07-30"
status: current
last_updated: "2026-07-28"
---

# Reproducibility Engineering — Cheatsheet

> Definitions and formulas only. No explanations. For context, see [[repeng-exam-prep-condensed]].

---

## Terminology

| Term | Definition |
|------|-----------|
| Repeat | Same team, same experimental setup, same data |
| Reproduce | Different team, same experimental setup, same/similar data |
| Replicate | Different team, different experimental setup, new data |
| Computational reproducibility | Same code + data + environment → same result |
| Empirical reproducibility | Same setup, different team → same result |
| Statistical reproducibility | Same analysis method on same/similar data → same conclusions |
| Reproducibility crisis | 52% of researchers agree there is a significant crisis (Nature survey, 1,576 respondents) |

## Artifact Badging (ACM)

| Badge | Meaning |
|-------|---------|
| Artifacts Available | Artifact is publicly archived (green) |
| Artifacts Functional | Runs, documented, reusable (blue) |
| Artifacts Reusable | Functional + exceeds minimal requirements (gold) |

## Types of Reproducibility

| Type | Scope |
|------|-------|
| Computational | Same code, data, environment |
| Empirical | Same experimental setup, different team |
| Statistical | Same analysis method, same/similar data |

## Research Artifacts (ACM Taxonomy)

Data, code, workflows, models, documentation

---

## Levels of Reproducibility (VisTrails, Freire et al.)

| Dimension | Question |
|-----------|----------|
| Availability | What can you access? (nothing → data → code → workflow → all) |
| Repeatability/Reproducibility/Replicability | Same/different team, same/different method |
| Confirmability | Can you reach the same conclusion? |

## Provenance Types

| Type | What it captures |
|------|-----------------|
| Prospective | Workflow specification (what SHOULD happen) |
| Execution | What actually ran (steps, parameters, timing) |
| Version | Which versions of data/code were used |

## Heil et al. Bronze/Silver/Gold (ML Reproducibility)

| Level | Requirement |
|-------|-------------|
| Bronze | Share: data + code + model + documentation |
| Silver | Bronze + detailed config + environment + hyperparameters |
| Gold | Silver + containerized + automated re-run from scratch |

---

## Hypotheses (Zobel)

| Property | Requirement |
|----------|-------------|
| Precise | No vague terms |
| Specific | State what is claimed AND what is NOT claimed |
| Unambiguous | One interpretation only |
| Falsifiable | An experiment could disprove it |

### Levels of Equivalence (increasing strictness)

| Level | Definition |
|-------|-----------|
| Bitwise identity | Byte-for-byte identical (SHA-256 match) |
| Structural equivalence | Same structure, different representation |
| Functional equivalence | Same I/O, different internals |
| Behavioral equivalence | Same observable behavior over time, different internals |

### Occam's Razor

If two hypotheses explain the same observations, prefer the simpler one (fewer assumptions). Does NOT say the simpler one is correct.

---

## Git

### Object Types

| Object | Content |
|--------|---------|
| Blob | File content |
| Tree | Directory listing |
| Commit | Snapshot + metadata + parent pointer |
| Tag | Named label |

### Key Git Rules

| Rule | Definition |
|------|-----------|
| Atomic commits | One logical change per commit |
| Imperative subject | "Add feature X" not "Added feature X" |
| Golden rule of rebasing | Never rebase commits pushed to a shared branch |
| DCO | Signed-off-by trailer = trail of responsibility |

### Three Strategies for Upstream Code

| Strategy | Description |
|----------|-------------|
| Snapshot | Copy code at a specific version |
| Clone + patches | Clone repo, maintain local patches on top |
| Fork | Full repo with GitHub PR workflow |

---

## Reproducible Builds

### Formal Definition

A build is reproducible if given the same source code, build environment, and build instructions, any party can recreate bit-for-bit identical copies of all specified artifacts.

### Sources of Non-Determinism

| Source | Example | Fix |
|--------|---------|-----|
| Timestamps | `__TIME__`, `__DATE__` | `SOURCE_DATE_EPOCH` env var |
| File ordering | `$(wildcard *.c)` | `$(sort $(wildcard *.c))` |
| Embedded paths | `__FILE__` | Relative paths or `--debug-prefix-map` |
| Parallelism | Race conditions | Pin thread count, serialize critical steps |
| Randomness | Uninitialized memory, ASLR | Zero-initialize, pin ASLR off |
| Locale | Different locale → different output | `LC_ALL=C` |
| Compiler version | Different compiler → different binary | Pin in Dockerfile |

### C Preprocessor Macros

| Macro | What it embeds | Breaks reproducibility? |
|-------|---------------|------------------------|
| `__TIME__` | Compilation time | Yes |
| `__DATE__` | Compilation date | Yes |
| `__FILE__` | Source file path | Yes (path-dependent) |
| `__LINE__` | Source line number | No (deterministic) |
| `SOURCE_DATE_EPOCH` | Fixed timestamp from env | Fixes `__TIME__`/`__DATE__` |

### diffoscope

Deep structural comparison of two builds. Disassembles binaries, compares ELF headers, recurses into embedded archives.

---

## Database Architectures

| Architecture | Examples | Reproducibility |
|-------------|----------|----------------|
| File-based / serverless | SQLite | Copy the file → done |
| Client/server | PostgreSQL, MySQL | More moving parts (server, network, config) |
| Embedded | SQLite library, BerkeleyDB | Engine linked into app |

### SQLite Features

Serverless, zero-config, single-file, self-contained, ACID, SQL92-compatible, public domain (no license)

### PostgreSQL Foreign Tables

Access external data as local tables. Use case: capture system info during experiments.

### Docker Compose

`compose.yaml` declares services with pinned versions. `docker compose up` = same stack everywhere.

---

## Tidy Data (Wickham)

### Three Rules

1. Each variable forms a column
2. Each observation forms a row
3. Each value forms a cell

All three must hold simultaneously.

### Common Untidy Patterns

| Pattern | Example |
|---------|---------|
| Column headers are values | `male`, `female` as columns |
| Multiple variables in one column | `180cm` in one cell |
| Variables in both rows and columns | Patients × dates grid |
| Multiple types in one table | Demographics + lab results mixed |
| One variable in multiple columns | `first_name`, `last_name` for `name` |

### SQL Pivoting

**Unpivot (wide → tall):** UNION ALL of SELECT per value column
**Pivot (tall → wide):** `SUM(CASE WHEN year=X THEN val END) AS col_X ... GROUP BY key`

### Data Transformations

| Transformation | Definition |
|----------------|-----------|
| Discretization | Continuous → categorical (binning) |
| Binarization | Convert to 0/1 |
| Dummy variables | One-hot encoding for categorical data |

---

## Hierarchical Data Formats

### Format Comparison

| Format | Structure | Schema | Size |
|--------|-----------|--------|------|
| Relational | Flat tables | Strict (upfront) | Small-medium |
| XML | Tree (elements) | Optional (XSD/DTD) | Verbose |
| JSON | Tree (objects/arrays) | Optional (JSON Schema) | Medium |
| HDF5 | Tree (groups/datasets) | Self-describing (attributes) | Large (binary) |

### JSON Schema Keywords

| Keyword | Function |
|---------|----------|
| `type` | `"string"`, `"object"`, `"array"`, `"integer"`, `"number"`, `"boolean"`, `"null"` |
| `properties` | Object keys and their schemas |
| `required` | Array of keys that must be present |
| `items` | Schema for array elements |
| `additionalProperties` | `false` = no extra keys |
| `enum` | Fixed set of allowed values |
| `pattern` | Regex on strings |
| `minimum` / `maximum` | Numeric bounds |
| `minLength` / `maxLength` | String length bounds |

### JSON Schema Combinators

| Keyword | Logic | Match requirement |
|---------|-------|-------------------|
| `allOf` | AND | Must satisfy ALL sub-schemas |
| `anyOf` | OR | At least ONE |
| `oneOf` | XOR | EXACTLY ONE |
| `not` | NOT | Must NOT satisfy |

### HDF5

| Concept | Definition |
|---------|-----------|
| Group | Like a directory, contains datasets and other groups |
| Dataset | Multi-dimensional array |
| Attribute | Metadata attached to group/dataset (max 64 KB) |
| `h5py` | Python library: `create_group()`, `create_dataset()`, `d.attrs[...]` |

---

## LLMs and Reproducibility

### Reproduction Package Must Pin

1. Model identifier + version (commit hash or API version)
2. Exact prompts (decomposed by role: system, user, assistant)
3. Parameters: `temperature`, `seed`, `max_tokens`, `top_p`, `top_k`
4. Sample outputs from original run
5. Client library version (e.g., `openai==1.30.0`)

### Local vs Remote LLM

| Property | Local (container) | Remote API |
|----------|-------------------|-----------|
| Self-contained | Yes | No |
| Container size | Large (GBs) | Small |
| Bitwise reproducible | Possible but hard | No (provider controls model) |
| Version drift | You control it | Provider may update silently |

### Key LLM Facts

| Fact | Detail |
|------|--------|
| `temperature=0` | Greedy decoding, NOT bitwise deterministic |
| Constrained decoding | Mask tokens that produce invalid JSON at each step |
| Structured outputs | `response_format: { type: "json_schema", json_schema: {...} }` |

---

## Remote Experiments (Mauerer & Scherzinger, ICDE 2021)

### Five Stages

```
1. Build artifacts → 2. Experiment execution package → 3. Run experiments → 4. Measured data → 5. Generate graphs + paper
```

### Dependency Types

| Type | Meaning |
|------|---------|
| Integration (A → B) | B incorporates A |
| Production (A ⇒ B) | A produces B |

### Multi-Stage Docker Build

| Stage | Contains |
|-------|---------|
| Build stage | Compiler + source + build tools |
| Runtime stage | Binary + minimal OS only |

---

## FAIR Principles (Wilkinson et al., 2016)

| Letter | Principle | Meaning |
|--------|-----------|---------|
| F | Findable | Persistent identifiers (DOIs), rich metadata, indexed |
| A | Accessible | Open or clear access protocol, authentication if needed |
| I | Interoperable | Common formats, shared vocabularies, standard ontologies |
| R | Reusable | Clear license, detailed provenance, community standards |

### Legal Frameworks

| Framework | Protects | Key distinction |
|-----------|----------|----------------|
| Copyright | Creative expression (code, papers, figures) | Facts are NOT copyrightable |
| GDPR | Personal data of EU residents | Requires consent + anonymization |
| Trade secrets | Confidential business information | Sharing under NDA breaks it |
| Database sui generis (EU) | Investment in database compilation | Protects selection/arrangement, not facts |

---

## Docker Quick Reference

| Command | Purpose |
|---------|---------|
| `docker build -t name .` | Build image from Dockerfile |
| `docker run -it name` | Run container interactively |
| `docker exec -it name bash` | Enter running container |
| `docker cp src cont:path` | Copy file to container |
| `docker run -v host:cont` | Bind mount |
| `docker secret create` | Create secret (mounted at `/run/secrets/`) |
| `docker compose up` | Start multi-service stack |

---

## Key Trap: Terminology Pairs

| Wrong | Right |
|-------|-------|
| "Reproduce = replicate" | Reproduce = same method, different team. Replicate = different method, different team |
| "FAIR = open access" | FAIR = findable + accessible (can be restricted with protocol) |
| "Copyright protects datasets" | Facts aren't copyrightable; selection/arrangement may get sui generis right |
| "SQLite = open source" | SQLite = public domain (no license at all) |
| "Bronze/Silver/Gold = quality" | Levels of reproducibility documentation: share → document → automate |