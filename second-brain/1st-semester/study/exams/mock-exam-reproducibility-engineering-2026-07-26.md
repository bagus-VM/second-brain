---
title: "Mock Exam — Reproducibility Engineering (Antwort-Wahl-Verfahren)"
tags: [exam-prep, mock-exam, reproducibility-engineering, multiple-choice, semester-1]
course: "Reproducibility Engineering"
exam_date: "2026-07-30"
format: "Antwort-Wahl-Verfahren (single-best-answer + multiple-select)"
status: current
last_updated: 2026-07-26
prerequisites: []
---

# Mock Exam — Reproducibility Engineering

> *40 questions. Einfachauswahl (single-best-answer) unless marked **[Mehrfachauswahl]** (zero, one, or more correct). 90 minutes. No notes.*
>
> Scope: 11 lectures, 11 exercise sheets, 11 in-class exercises. One central question: how do we make computational research reproducible?

---

## Section 1 — Reproducibility Crisis & Terminology

### Q1. Alice runs her own experiment three times on the same machine, same script, same day. This is:

a) Repeatability
b) Reproduction
c) Replication
d) Repetition

> [!note]- Solution
> **a)** Repeatability = same team, same setup, same location. ACM terminology: the experimenter can reproduce their own results with the same equipment and inputs.

---

### Q2. Bob reads Alice's paper, downloads her Docker container from Zenodo, and runs it on his own server. This is:

a) Repeatability
b) Reproduction
c) Replication
d) Repetition

> [!note]- Solution
> **b)** Reproduction = different team, same experimental setup (the container preserves the setup). Bob got Alice's container, so the experimental setup is preserved; only the team and location changed.

---

### Q3. Carol builds a new benchmarking framework from scratch, following Alice's methodology description, to test whether she gets the same conclusions. This is:

a) Repeatability
b) Reproduction
c) Replication
d) None of the above

> [!note]- Solution
> **c)** Replication = different team, different setup, same research question. Carol built a new framework — the experimental setup differs from Alice's. She tests whether Alice's conclusions hold under her own implementation.

---

### Q4. [Mehrfachauswahl] Which of the following are types of reproducibility distinguished in the course?

a) Computational reproducibility — same code, same data, same environment, recompute outputs
b) Empirical reproducibility — collect new data with the same methods, look for consistent results
c) Statistical reproducibility — robustness of statistical conclusions (study design, sample sizes, no p-hacking)
d) Computational reproducibility — only possible when running on identical hardware

> [!note]- Solution
> **a), b), c).** Three main types: computational (re-run code on data), empirical (re-collect data with same methods), statistical (robustness of conclusions). (d) is wrong — computational reproducibility is about code/data/environment, not identical hardware; containers abstract away hardware differences.

---

### Q5. The reproducibility crisis refers to:

a) A decline in scientific publishing rates
b) A substantial fraction of published studies fail to reproduce when independently re-run — Nature survey found ~52% significant failures across fields
c) A hardware shortage in academic labs
d) The collapse of the peer-review system

> [!note]- Solution
> **b)** Nature's 2016 survey reported that >50% of researchers across fields were unable to reproduce others' published experiments. The crisis motivates the entire course — reproducibility engineering is the response.

---

## Section 2 — Levels, Provenance & Standards

### Q6. Correct ordering of reproducibility levels (Bronze/Silver/Gold from Heil et al. 2021) weakest to strongest:

a) Gold, Silver, Bronze
b) Silver, Bronze, Gold
c) Bronze, Silver, Gold
d) Bronze, Gold, Silver

> [!note]- Solution
> **c)** Bronze < Silver < Gold. The levels reflect increasing requirements for the reproduction artifact — findable archive (bronze), runnable container (silver), bitwise-identical build with pinned environment (gold). Higher tiers subsume lower.

---

### Q7. Correct order of equivalence hierarchy from strongest to weakest:

a) Behavioral, Functional, Structural, Bitwise
b) Bitwise, Structural, Functional, Behavioral
c) Bitwise, Functional, Structural, Behavioral
d) Structural, Bitwise, Behavioral, Functional

> [!note]- Solution
> **b)** Bitwise identity ⊂ Structural equivalence ⊂ Functional equivalence ⊂ Behavioral equivalence. Bitwise = identical bytes. Structural = same AST/structure. Functional = same output for same input. Behavioral = same externally observable behavior. Each level is weaker (covers more cases) than the one before.

---

### Q8. Two Docker images built from the same Dockerfile on the same machine, consecutively, with all packages pinned. Strongest equivalence that holds:

a) Behavioral
b) Functional
c) Bitwise identity
d) Structural

> [!note]- Solution
> **c)** Bitwise identity — same source, same build environment, same machine, pinned packages → identical layers. The strongest equivalence holds because every variable that affects the build is fixed.

---

### Q9. `{"name":"Alice","age":30}` and `{"age":30,"name":"Alice"}` — strongest equivalence:

a) Bitwise identity
b) Structural equivalence
c) Functional equivalence
d) Behavioral equivalence

> [!note]- Solution
> **b)** Structural — same key/value pairs but different byte sequences (key order differs in source). JSON objects are semantically unordered, so structurally these encode the same structure. Not bitwise because the bytes differ.

---

### Q10. A Python script and a Java script that both compute and print the median of a list. Strongest equivalence:

a) Bitwise identity
b) Structural equivalence
c) Functional equivalence
d) Behavioral equivalence

> [!note]- Solution
> **c)** Functional — same output for same input, but completely different implementations (different languages, different code structures). They agree on the function output(x) → median. Behavioral equivalence would also hold but is weaker.

---

### Q11. [Mehrfachauswahl] Which of the following are provenance types distinguished in the course?

a) Prospective provenance — the workflow plan (what was supposed to run)
b) Execution (retrospective) provenance — what actually ran, with parameter values and timestamps
c) Version provenance — which versions of data, code, and tools were used
d) Hardware provenance — the exact CPU model used

> [!note]- Solution
> **a), b), c).** Three provenance types: prospective (the plan), execution / retrospective (what actually ran), version (data/code/tool versions). Hardware model could be part of version provenance but isn't a distinct type. Provenance is the metadata trail that enables reproducing the *same* experiment.

---

## Section 3 — Hypotheses & Equivalence

### Q12. A good research hypothesis must be (best answer):

a) Precise, specific, unambiguous, falsifiable
b) Broad enough to cover many scenarios
c) Opinionated and persuasive
d) Proven by the time it's written

> [!note]- Solution
> **a)** The four canonical properties: precise, specific, unambiguous, falsifiable. A hypothesis that can't be falsified isn't testable. "Code with more comments is more readable" is vague; "Code with over 30% comment density has higher readability scores (p<0.05) on the Scalabrino benchmark" is specific and falsifiable.

---

### Q13. `f(x)=x*2` vs `g(x)=x+x` — for which input type are they NOT functionally equivalent?

a) Integers
b) Floats (IEEE 754)
c) Booleans
d) Strings

> [!note]- Solution
> **b)** Floats. Floating-point: x*2 is exact (exponent bump); x+x involves addition, and non-associativity can cause different rounding for some values. For integers, x*2 and x+x both give 2x. The functional-equivalence check is type-dependent.

---

### Q14. Occam's Razor in hypothesis formulation prefers:

a) The hypothesis with the most assumptions (more detailed)
b) The simplest hypothesis that explains the data (fewest assumptions)
c) The most counter-intuitive hypothesis
d) The first hypothesis that comes to mind

> [!note]- Solution
> **b)** Occam's Razor: prefer the hypothesis that explains the data with the fewest assumptions. Simplicity reduces the surface for confounding variables and makes the hypothesis more testable.

---

### Q15. [Mehrfachauswahl] Which of the following are signs of statistical malpractice explored in the reproducibility crisis?

a) p-hacking — trying many analyses and reporting only the significant ones
b) HARKing — Hypothesizing After Results are Known
c) Bonferroni correction for multiple comparisons
d) Failing to report effect sizes

> [!note]- Solution
> **a), b), d).** (a) and (b) are the two canonical malpractices the course emphasizes. (d) is also malpractice — statistical significance doesn't imply importance; effect size (Cohen's d) matters. (c) is NOT malpractice — it's the correct countermeasure for multiple comparisons. The course showcases PPV (Positive Predictive Value) collapsing under p-hacking.

---

## Section 4 — Git Internals

### Q16. In git, `Author` and `Committer` differ when:

a) They never differ — they're always the same user
b) Someone other than the original author applies the commit — e.g., cherry-picking a patch from a mailing list, or a maintainer rebasing another developer's commits
c) The commit is the first in the repo
d) The commit has no parents

> [!note]- Solution
> **b)** Author wrote the code; Committer applied the commit to the repo. They differ when a maintainer rebases or cherry-picks someone else's commits. The two fields preserve attribution to the original author even when the commit is rewritten in the history.

---

### Q17. You've made 5 messy commits ("WIP", "fix typo", "actually fix the bug", "oops forgot a file", "final version"). The clean approach is:

a) `git revert` each commit individually
b) `git rebase -i HEAD~5` to squash or fixup the commits into 1–2 logical commits
c) Delete the repo and start over
d) `git cherry-pick` each commit onto a new branch

> [!note]- Solution
> **b)** Interactive rebase (`git rebase -i HEAD~5`) opens an editor listing the last 5 commits. Mark commits as `squash` (fold into previous, keep message) or `fixup` (fold, discard message). The original commits become unreachable — recoverable via reflog for ~30 days.

---

### Q18. You accidentally ran `git reset --hard HEAD~3`. You lost 3 commits. Recovery command:

a) `git pull`
b) `git reflog` to find the lost commit hash, then `git reset --hard <hash>`
c) `git stash pop`
d) The commits are gone permanently — no recovery

> [!note]- Solution
> **b)** reflog records every HEAD movement including destructive operations like `reset --hard`. Find the hash of the commit that was HEAD before the reset, then `git reset --hard <hash>`. reflog is the safety net for history rewriting. It persists ~30 days for unreachable commits.

---

### Q19. The Developer Certificate of Origin (DCO) is:

a) A license like MIT or GPL
b) A sign-off ("Signed-off-by:") asserting that the contributor has the right to submit the code under the project's license
c) A replacement for CLAs (Contributor License Agreements)
d) A cryptographic signature for tamper detection

> [!note]- Solution
> **b)** DCO is a developer's assertion: "I wrote this, or have the right to submit it." Sign-off line (`Signed-off-by: Name <email>`) on each commit. Unlike a CLA (which can grant extra rights to the project owner), the DCO only attests to origin — it's lighter weight. Linux kernel uses DCO.

---

### Q20. [Mehrfachauswahl] Which of these are recommended git hygiene practices from the course?

a) Each commit is a single logical, working unit (atomic)
b) Use trailers like `Signed-off-by:` for DCO compliance
c) Commit messages should be vague to allow flexibility
d) Squash WIP commits before merging to the main branch via interactive rebase
e) Force-push directly to the main branch without coordination

> [!note]- Solution
> **a), b), d).** Atomic commits (each compile and pass tests), trailers for DCO, and rebase-squash before merge are all taught. (c) is wrong — messages should be precise. (e) is wrong — force-push to shared main without coordination destroys history. Force-push is acceptable on personal feature branches but not on shared refs.

---

## Section 5 — Reproducible Builds

### Q21. A C program contains `printf("Built at %s %s\n", __TIME__, __FILE__);`. Why does it break bitwise reproducibility?

a) `__TIME__` and `__FILE__` are runtime values
b) `__TIME__` embeds the current time (changes every second) and `__FILE__` embeds the full source path (differs across machines) at compile time — both go into the binary's data section, so any byte difference breaks bitwise identity
c) `__TIME__` is invalid C syntax
d) They're computed at runtime, not compile time

> [!note]- Solution
> **b)** Both macros expand at *compile time*: `__TIME__` → "HH:MM:SS" (changes per second), `__FILE__` → the full source path (changes across machines or build directories). Both strings land in the binary's data section. So two builds at different times or on different paths produce different bytes.

---

### Q22. [Mehrfachauswahl] Which of the following C preprocessor macros break bitwise reproducibility across rebuilds on different machines?

a) `__TIME__`
b) `__DATE__`
c) `__FILE__`
d) `__LINE__`

> [!note]- Solution
> **a), b), c).** `__TIME__` changes per second. `__DATE__` changes per day. `__FILE__` includes full path — differs across machines. `__LINE__` is the source line number, which is fixed as long as the source file is the same — it doesn't break reproducibility across rebuilds of unchanged source.

---

### Q23. `gcc -O0 hello.c -o hello_O0` vs `gcc -O2 hello.c -o hello_O2` — the binaries are:

a) Bitwise identical
b) Functionally equivalent (same behavior for same input) but NOT bitwise identical (different optimization choices, loop unrolling, inlining, instruction selection)
c) Different in behavior — O2 may produce wrong results
d) Completely unrelated — they're different programs

> [!note]- Solution
> **b)** Same source → same external behavior → functionally equivalent. Different optimization levels → different machine code → different bytes → NOT bitwise identical. The pair (functionally equiv, NOT bitwise identical) is the canonical build-reproducibility case.

---

### Q24. `gcc hello.c -o hello_g` and `clang hello.c -o hello_clang` — the binaries are:

a) Bitwise identical
b) Functionally equivalent but NOT bitwise identical
c) Behaviorally different (different output)
d) Bitwise identical except for a few bytes

> [!note]- Solution
> **b)** Both compile the same source with default flags — same external behavior → functionally equivalent. Different compilers produce different object code (instruction selection, register allocation, padding, metadata).

---

### Q25. Compiling with `-g` (debug info) changes the binary by:

a) Adding debug sections (DWARF data, line tables) — binary is larger and different from the build without `-g`, even though executable code is unchanged
b) Optimizing the code
c) Nothing — `-g` has no effect
d) Linking additional shared libraries

> [!note]- Solution
> **a)** Debug info adds `.debug_info`, `.debug_line` sections containing line tables and DWARF data. Executable code is unchanged; binary file is larger and different. DWARF can include paths and timestamps, further breaking bitwise identity.

---

### Q26. `SOURCE_DATE_EPOCH` is an environment variable that:

a) Records the git commit hash
b) Provides a deterministic substitute for build timestamps — set to the date of the last source modification, so all builds produce the same `__TIME__`/`__DATE__` values
c) Disables optimization
d) Points to the source file to compile

> [!note]- Solution
> **b)** `SOURCE_DATE_EPOCH` is a convention reproducible-build tools use: it pins the "current time" to a fixed Unix timestamp (typically last source commit). GCC, clang, and many tools substitute it for `__TIME__`/`__DATE__`, decoupling the binary from the wall clock at build time.

---

### Q27. ReproTest is best described as:

a) A static analysis tool
b) A tool that builds a program twice in different (simulated) environments and compares the resulting binaries to check reproducibility
c) A unit testing framework
d) A Docker alternative

> [!note]- Solution
> **b)** ReproTest runs the build twice in varying environments (different paths, different timestamps) and reports differences between the binaries. It exposes non-determinism sources: `__TIME__`, paths in debug info, random filename suffixes. Tests for the reproducible-build property without manual effort.

---

### Q28. Make rebuilds a target `T` when:

a) The recipe says so
b) ANY prerequisite of `T` is newer (has a more recent mtime) than `T`, OR `T` does not exist
c) The user passes `-f` to force
d) All prerequisites are older than `T`

> [!note]- Solution
> **b)** Make uses mtime comparison: if any prerequisite is newer than the target, OR the target file doesn't exist, the target's recipe runs. If all prerequisites are older, nothing happens. `.PHONY` targets always run (don't correspond to files).

---

### Q29. [Mehrfachauswahl] Given:
```makefile
experiment.pdf: experiment.tex results/chart.pdf
	pdflatex experiment.tex
results/chart.pdf: generate_chart.py results/results.csv
	python3 generate_chart.py
results/results.csv: run_experiment.sh recipe.txt
	bash run_experiment.sh
```
After `make`, you modify **only** `generate_chart.py` and run `make` again. Which targets are rebuilt?

a) `results/results.csv`
b) `results/chart.pdf`
c) `experiment.pdf`
d) Nothing — nothing important changed

> [!note]- Solution
> **b), c).** `results/chart.pdf` depends directly on `generate_chart.py` (changed) → rebuild. `experiment.pdf` depends on `results/chart.pdf` (which got rebuilt) → rebuild. `results/results.csv` does NOT depend on `generate_chart.py` → NOT rebuilt. The transitive cascade is the exam's favorite trap — forgetting that downstream targets also rebuild.

---

### Q30. The `.PHONY` declaration in a Makefile is used for:

a) Targets that don't correspond to files (e.g. `all`, `clean`) — they always run regardless of file existence
b) Targets that produce no output
c) Targets that are experimental
d) Targets that depend on the network

> [!note]- Solution
> **a)** `.PHONY` declares targets that aren't files. Without `.PHONY`, if a file named "clean" happened to exist in the directory, `make clean` would think the target is up-to-date and skip the recipe. Declaring `.PHONY: clean` forces the recipe to always run.

---

## Section 6 — Database Architectures

### Q31. SQLite's architecture is best described as:

a) Client-server with a separate server process
b) Embedded (serverless, zero-config, single-file, ACID) — the database library is linked into the application
c) Distributed with sharding
d) Document-oriented NoSQL

> [!note]- Solution
> **b)** SQLite is the canonical embedded database: serverless, zero-config, single-file. The library is linked directly into the application. ACID-compliant. Public domain. For reproducibility: trivially portable — just copy the file.

---

### Q32. PostgreSQL uses MVCC. MVCC stands for Multi-Version Concurrency Control, which means:

a) Multiple database files versioned by git
b) Readers don't block writers and vice versa — each transaction sees a consistent snapshot, avoiding lock contention
c) Multiple schemas in one database
d) The server is redundant across machines

> [!note]- Solution
> **b)** MVCC = Multi-Version Concurrency Control. Each transaction sees a snapshot of the database at a consistent point in time. Writers create new row versions rather than overwriting in place. Readers see the version valid at their snapshot's commit time. No read/write locks → good concurrency for mixed workloads. PostgreSQL, Oracle, and others use MVCC.

---

### Q33. A Docker Compose `depends_on` without `condition: service_healthy` means:

a) The dependent service starts only after the dependency passes its healthcheck
b) The dependent service starts after the dependency container starts, but NOT waiting for the application inside to be ready — the dependency may still be initializing
c) The dependent service starts at the same time as the dependency
d) `depends_on` is deprecated

> [!note]- Solution
> **b)** Without `condition: service_healthy`, Compose only waits for the container's main process to start, not for the app to be ready. If your app has a slow startup (e.g. PostgreSQL loading), clients will fail connecting. The fix: add a `healthcheck` to the dependency and `condition: service_healthy` to `depends_on`.

---

## Section 7 — Tidy Data & SQL

### Q34. The three rules of tidy data (Wickham) are:

a) Each variable = column, each observation = row, each value = cell
b) All data in one table
c) No missing values
d) Each row has a unique identifier

> [!note]- Solution
> **a)** Wickham's three rules: (1) each variable forms a column, (2) each observation forms a row, (3) each type of observational unit forms a table. A fourth sometimes added: each value is a cell. Tidy data enables consistent manipulation and analysis tooling.

---

### Q35. The table below is NOT tidy. Why?

| country | 1999 | 2000 |
|---------|------|------|
| Afghanistan | 745 | 2666 |
| Brazil | 37737 | 80488 |

a) It contains missing values
b) Column headers (1999, 2000) are values (years), not variable names — `year` should be a variable in its own column
c) Mixed numeric and text data
d) It's too small to analyze

> [!note]- Solution
> **b)** The headers "1999" and "2000" are values of the `year` variable, not separate variables. The tidy version stacks them into a single `year` column with a `cases` column for values: `country | year | cases`.

---

### Q36. [Mehrfachauswahl] Which operations are common tidy-data transformations?

a) PIVOT (rows → columns)
b) UNPIVOT (columns → rows)
c) Splitting compound columns (e.g. "745/19987071" → cases + population)
d) Joining tables on unrelated keys
e) Discretization (continuous → bins)
f) One-hot encoding (categorical → multiple binary columns)

> [!note]- Solution
> **a), b), c), e), f).** Pivoting and unpivoting reshape wide ↔ long. Splitting handles compound columns. Discretization and one-hot encoding transform feature representations. (d) is wrong — joining on unrelated keys produces nonsense merges, not a tidy-data transform.

---

### Q37. The difference between "destructive" and "non-destructive" data transformations is:

a) Destructive transformations alter the source table; non-destructive create a new table, leaving the source intact
b) Destructive transformations are irreversible; non-destructive are reversible
c) Destructive transformations delete rows; non-destructive keep them
d) They're synonyms

> [!note]- Solution
> **a)** Destructive = the transformation overwrites the source (e.g. SQL `UPDATE`). Non-destructive = produces a new table, keeping the original intact (e.g. `SELECT` with transformations into a new view). Reversibility is a related but distinct property — a transformation can be destructive yet reversible (e.g. UPDATE with a known undo).

---

## Section 8 — Hierarchical Data (XML, JSON, HDF5)

### Q38. Which is true about JSON object keys and array ordering?

a) JSON object keys are ordered; arrays are unordered
b) JSON object keys are unordered; arrays are ordered
c) Both are ordered
d) Both are unordered

> [!note]- Solution
> **b)** JSON object keys are an unordered set (object = map). Arrays are ordered sequences (indexed). The difference matters for equivalence: `{"a":1,"b":2}` and `{"b":2,"a":1}` are structurally equivalent (same object). Arrays `[1,2,3]` and `[3,2,1]` are NOT equivalent (different order).

---

### Q39. `oneOf` in JSON Schema requires that the instance:

a) Matches ALL sub-schemas (AND)
b) Matches AT LEAST ONE sub-schema (OR)
c) Matches EXACTLY ONE sub-schema (XOR)
d) Matches NO sub-schemas

> [!note]- Solution
> **c)** oneOf = XOR — exactly one sub-schema matches. If two sub-schemas match, the instance is INVALID under oneOf. anyOf = OR (at least one). allOf = AND (all). The classic trap: a short string matching two sub-schemas is invalid under oneOf but valid under anyOf.

---

### Q40. `anyOf` in JSON Schema requires the instance match:
a) All sub-schemas
b) At least one sub-schema
c) Exactly one sub-schema
d) Zero sub-schemas

> [!note]- Solution
> **b)** anyOf = OR — at least one sub-schema must match. If two match, still valid (unlike oneOf). The common confusion: anyOf vs oneOf. anyOf is the permissive version; oneOf is the strict (exactly-one) version.

---

### Q41. Given schema:
```json
{
  "type": "object",
  "required": ["id", "name"],
  "additionalProperties": false,
  "properties": {
    "id": {"type": "integer", "minimum": 1},
    "name": {"type": "string"}
  }
}
```
Which instance is VALID?

a) `{"id":0,"name":"Bob"}`
b) `{"id":5,"name":"Alice","extra":true}`
c) `{"id":5,"name":"Alice"}`
d) `{"name":"Alice"}`

> [!note]- Solution
> **c)** Valid. `id=5` is an integer ≥1 ✓, `name` is a string ✓, no extra fields ✓, both required present ✓. (a) invalid: id=0 violates `minimum:1`. (b) invalid: `extra` rejected by `additionalProperties:false`. (d) invalid: missing required `id`.

---

### Q42. HDF5 differs from JSON/XML in that:

a) HDF5 is text-based; JSON and XML are binary
b) HDF5 is a binary format supporting groups, datasets, and attributes — efficient for large multi-dimensional scientific data with partial I/O (read slices without loading the whole file)
c) HDF5 cannot store metadata
d) HDF5 is human-readable

> [!note]- Solution
> **b)** HDF5 is binary, not human-readable, but supports: groups (folders) containing datasets (n-dim typed arrays) and attributes (metadata up to 64 KB per object). Designed for large scientific data with chunking, compression, and partial I/O. Human-readable tools: `h5ls -r`, `h5dump -H`. Contrast JSON/XML: text, must parse the whole file.

---

## Section 9 — LLMs & Reproducibility

### Q43. With `temperature=0.0`, which statement about LLM output is most accurate?

a) Outputs are bitwise identical on all hardware
b) Outputs are bitwise identical on a CPU but not guaranteed bitwise identical on a GPU due to non-deterministic floating-point reduction order
c) Outputs are bitwise identical on a GPU but not on a CPU
d) Temperature has no effect; only the seed matters

> [!note]- Solution
> **b)** Temperature=0 → greedy decoding (always pick highest-probability token). CPU floating-point operations are deterministic (same input → same bits). GPU parallel reductions can differ across runs due to non-deterministic ordering. Seed is irrelevant when temperature=0 because there's no sampling. The takeaway: temperature=0 reduces variability but doesn't eliminate hardware-level non-determinism.

---

### Q44. Local LLM in container vs. remote API for reproducibility:

a) Remote API is more reproducible (provider manages version)
b) Local container is more reproducible — model weights are preserved in the image; remote providers can silently update the model without version bumps
c) They are equally reproducible
d) Only remote APIs are reproducible

> [!note]- Solution
> **b)** Local container: weights are frozen in the image, fully self-contained. Remote API: provider may deprecate, silently change the model, or change quotas. Even with date-stamped version names (e.g. `gpt-4o-2024-08-06`), providers update without warning. Cost trade-off: local needs GPU + electricity, remote needs per-token payments.

---

### Q45. [Mehrfachauswahl] Which must a reproduction package for an LLM-based experiment include?

a) Model identifier and pinned version (e.g. `gpt-4o-2024-08-06`)
b) Exact prompts, decomposed by role (system, user, constraint, output format)
c) The training corpus of the LLM
d) Parameters (temperature, seed, max_tokens, top_p)
e) Cached sample outputs from the original run
f) API client version (e.g. `openai` Python package version)

> [!note]- Solution
> **a), b), d), e), f).** Ship version, prompts, parameters, cached outputs, and client version. (c) is wrong — you don't have the training corpus for closed models. For local models, ship the weights (or a DOI to them). Cached outputs are first-class artifacts because bitwise re-execution isn't guaranteed — they let consumers compare even when re-runs differ.

---

### Q46. Constrained decoding (structured outputs) guarantees:

a) Syntactic validity — output conforms to the declared JSON Schema tokens at the grammar level
b) Semantic correctness — generated facts are true
c) No hallucinations
d) Any JSON Schema keyword will be honored by any provider

> [!note]- Solution
> **a)** Constrained decoding restricts the model at the token level — it cannot emit tokens that violate the schema. Only SYNTACTIC correctness is guaranteed. Hallucinations and semantic wrongness still possible. Different providers support different JSON Schema subsets (e.g. `oneOf` mutual exclusivity, `minimum/maximum` range — support varies; test before relying).

---

### Q47. Pasting a JSON Schema into the LLM prompt (no constrained decoding) is:

a) Equivalent to constrained decoding
b) A hint — the model may follow the schema, but enforcement is not guaranteed; can still emit invalid JSON or extra fields
c) Guaranteed to produce valid JSON
d) More efficient than constrained decoding

> [!note]- Solution
> **b)** Putting the schema text in the prompt gives guidance, not enforcement. The model may ignore parts, emit invalid JSON, or add fields. Only constrained decoding forces token-level compliance. The bowschrift principle: `strict: true` in OpenAI's API flips the flag that activates grammar-level restriction; otherwise the schema is just a suggestion embedded as text.

---

### Q48. Secret handling gradient from LEAST to MOST visible against `docker inspect`:

a) Mounted secret file (least) → `.env` file → `-e OPENAI_API_KEY` (most)
b) `-e OPENAI_API_KEY` (most visible — full value in inspect) → `.env` file → mounted secret file (least visible — inspect shows only mount path)
c) `.env` → mounted file → `-e`
d) All equally visible

> [!note]- Solution
> **b)** `-e VAR` makes the full value appear verbatim in `docker inspect`. `--env-file` still materializes as env vars, visible in inspect. Mounted secret file: inspect only shows the mount source/destination, not file contents. Security gradient (most → least visible): env-var → env-file → mounted-file → secret never inside container.

---

### Q49. `.gitignore` and `.dockerignore` differ in that:

a) `.gitignore` is the same file as `.dockerignore`
b) `.gitignore` prevents files from being committed to Git; `.dockerignore` prevents files from being copied into the Docker build context — both should list secrets because a `COPY . .` in the Dockerfile would embed `.env` files or secrets into image layers where they persist even if deleted later
c) `.gitignore` is for source code; `.dockerignore` is only for binaries
d) `.dockerignore` is a subset of `.gitignore`

> [!note]- Solution
> **b)** `.gitignore` — git excludes listed files from commits. `.dockerignore` — Docker excludes listed files from the build context (the `COPY . .` sends to docker daemon). Both should list secret patterns; otherwise secrets get baked into image layers and persist even if a later layer deletes them (layers are additive). Same patterns should appear in both.

---

### Q50. The dispatcher script for remote experiments (e.g. `doall.sh` in the SQPolite case study) should record which environment metadata before execution?

a) Only the hostname
b) At least: hostname, /etc/os-release, /proc/config.gz (kernel config), /proc/cmdline (boot args), /proc/cpuinfo (CPU), loaded modules (/proc/modules), git commit of source
c) Only /etc/hostname
d) The dispatcher doesn't need to record anything

> [!note]- Solution
> **b)** Environment metadata for reproducibility on a remote target: OS release, kernel config, boot args, CPU info, loaded modules, git commit. The workflow separately tracks: (1) build artifacts (compile in Docker), (2) execution package (binary + scripts), (3) measured data, (4) analysis. If the target doesn't support Docker (clusters, HPC), the environment record is the *only* way to interpret/replicate the results.

---

### Q51. The "experiment execution package" workflow separates build, execute, analyze into distinct phases because:

a) It's required by Docker
b) The target platform (cluster, HPC) may not support Docker — separating lets the build/analysis run in reproducible Docker containers while only the execution step runs on the specialized target hardware
c) It speeds up the build
d) It avoids needing to commit code

> [!note]- Solution
> **b)** The key insight: not every target runs Docker (HPC clusters often forbid it). By separating, the build and analysis stay in reproducible containers while only execution depends on the target's specific hardware. The environment record (Q50's metadata) bridges the gap — it documents the one non-containerized step.

---

### Q52. SSH disconnects kill a long-running experiment on the remote server. The fix uses:

a) GNU screen — but `tmux` is the canonical answer in the course. Start `tmux new -s experiment`, detach with `Ctrl-b d`, reattach with `tmux a` (or `tmux attach -t experiment`). The session survives the SSH disconnect because it runs on the server, not the SSH process
b) `nohup` — but no output stream management
c) Running via `&` in bash — loses SSH disconnect protection
d) Nothing can be done

> [!note]- Solution
> **a)** tmux is the canonical tool taught. The session lives on the server independent of the SSH client. Reconnect via SSH, then `tmux a` to reattach. `Ctrl-b d` detaches. Screen is older and equivalent. Long-running jobs should NOT run in the bare SSH session — disconnect kills them.

---

### Q53. The `scp` and `ssh` commands use different flag casing for port specification:

a) Both use `-p` for port
b) Both use `-P` for port
c) `ssh -p PORT` (lowercase) vs `scp -P PORT` (uppercase). Mixing them fails silently.
d) Neither supports custom ports

> [!note]- Solution
> **c)** `ssh -p 2222 user@host` (lowercase p), but `scp -P 2222 file user@host:` (uppercase P). Inconsistent Unix heritage; easy to confuse in scripts. For reproducibility, the dispatcher should record and use the correct flag.

---

## Section 10 — FAIR Principles

### Q54. FAIR stands for:

a) Findable, Accessible, Interoperable, Reusable
b) Free, Accessible, Interoperable, Reusable
c) Findable, Available, Interoperable, Reproducible
d) Fast, Accessible, Interoperable, Reusable

> [!note]- Solution
> **a)** Findable, Accessible, Interoperable, Reusable. Distinguishing FAIR from "Open Data": FAIR doesn't mean free — data can be access-controlled but still FAIR (Accessible category includes auth restrictions). The hot concept: machine-actionability (FAIR targets computational agents, not only humans).

---

### Q55. A central goal of FAIR is that digital objects are:

a) Open and free
b) Machine-actionable — computational agents can autonomously discover, access, and reuse data with minimal human intervention
c) Stored in physical archives
d) Only accessible by humans

> [!note]- Solution
> **b)** Machine-actionability is the distinguishing feature of FAIR vs. earlier data-management guidelines. The principles are designed so that computational agents can autonomously discover, interpret, access, and reuse data — not only humans. This is why persistent identifiers, vocabularies, and machine-readable metadata matter.

---

### Q56. "Meta(data) are assigned a globally unique and persistent identifier" belongs to which FAIR category?

a) Findable
b) Accessible
c) Interoperable
d) Reusable

> [!note]- Solution
> **a)** Findable — persistent identifiers (e.g. DOIs) enable discovery. The four F principles: globally unique persistent identifier, rich metadata, metadata explicitly includes the data's identifier, registered/indexed in a searchable resource.

---

### Q57. "Metadata remain accessible even when the data are no longer available" belongs to which FAIR category?

a) Findable
b) Accessible
c) Interoperable
d) Reusable

> [!note]- Solution
> **b)** Accessible — the metadata must persist even if the underlying data is gone, so the record of existence and context isn't lost. The four A principles: retrievable by identifier using a standard protocol, protocol is open/free/universal, allows auth/authz where needed, metadata persists after data disappears.

---

### Q58. "Meta(data) use vocabularies that follow FAIR principles" belongs to which FAIR category?

a) Findable
b) Accessible
c) Interoperable
d) Reusable

> [!note]- Solution
> **c)** Interoperable — uses FAIR-compliant vocabularies so different systems can work with the same data. The four I principles: uses a formal, accessible, shared, broadly applicable language; vocabularies themselves follow FAIR; includes qualified references to other (meta)data.

---

### Q59. "Meta(data) are released with a clear and accessible data usage license" belongs to which FAIR category?

a) Findable
b) Accessible
c) Interoperable
d) Reusable

> [!note]- Solution
> **d)** Reusable — license tells others how they can (re)use the data. The four R principles: richly described with accurate attributes, clear data usage license, detailed provenance, meets domain-relevant community standards.

---

### Q60. [Mehrfachauswahl] Which of the following are stakeholders in FAIR (explicitly listed in the course)?

a) Researchers who produced the original data
b) Researchers who reuse each other's data
c) Professional data publishers (repositories)
d) Funding agencies (increasingly mandating FAIR compliance)
e) Computational agents that discover and process data autonomously

> [!note]- Solution
> **a), b), c), d), e).** All five are stakeholders. The inclusion of (e) — computational agents — distinguishes FAIR from earlier guidelines. FAIR is about machine-actionable data: agents can autonomously find, access, and reuse data without human intervention.

---

## Section 11 — Legal Aspects

### Q61. The EU Database Directive (96/9/EC) protects:

a) The creative expression in a database
b) The substantial investment in obtaining, verifying, or presenting the contents of a database (sui generis right)
c) Personal data
d) Software source code

> [!note]- Solution
> **b)** The sui generis database right protects investment in obtaining, verifying, or presenting existing data — not creative expression (copyright), not personal data (GDPR), and not software. Key qualifier (exam trap): the right protects *obtaining* existing data, not *creating* new data.

---

### Q62. In BHB v. William Hill, the ECJ ruled BHB's database was NOT protected because:

a) BHB made no financial investment
b) BHB *created* the data (horse race listings) as part of its normal business, rather than *obtaining* data from external sources — the sui generis right protects obtaining, not creating
c) William Hill copied only one record
d) The database was not digital

> [!note]- Solution
> **b)** The court distinguished "creating" from "obtaining": BHB generated the race listings as its business activity. The sui generis right protects investment in obtaining/verifying/presenting *existing* data, not in generating new data. (a) is wrong — investment was substantial, just in the wrong activity. (c) is wrong (extraction was bulk). The exam's classic trap: thinking any database qualifies.

---

### Q63. In Toll Collect, the BGH ruled the toll records database was NOT protected because:

a) The data was personal
b) The toll records were generated as a byproduct of running the toll system — not obtained through a substantial investment independent of the system's operation
c) The database was too small
d) The data was encrypted

> [!note]- Solution
> **b)** The toll records were an automatic byproduct of operating the toll system — not collected via a substantial investment separate from the system's main purpose. Same principle as BHB: the sui generis right protects obtaining existing data, not generating new data as a side effect of operations.

---

### Q64. [Mehrfachauswahl] Which of the following actions can violate the sui generis database right?

a) Extracting a single record once
b) Repeatedly extracting individual records until effectively copying the whole database
c) Extracting all records at once
d) A French research team reproducing data for non-commercial scientific comparison

> [!note]- Solution
> **b), c).** Extracting a single record is fine (not a "substantial part"). Repeatedly extracting individual records until the whole is copied IS a violation (systematic extraction counts as substantial). Bulk extraction is a clear violation. (d) is permitted — the Directive includes a research and educational exception for non-commercial scientific use.

---

### Q65. A German university invests 3 years in compiling a research database. A US company scrapes and republishes it. The university:

a) Has no protection because databases can't be copyrighted
b) Is protected under the EU sui generis right — substantial investment in obtaining/verifying/presenting the data gives rise to protection; enforcement against a US entity may require international legal cooperation, but the right exists automatically (no registration needed)
c) Can only protect the database via GDPR
d) Has protection only if the database contains personal data

> [!note]- Solution
> **b)** The university made a substantial investment — sui generis right applies automatically (no registration, unlike some IP rights). The right is EU-wide and applies even when the infringer is outside the EU, though enforcement is more complex. GDPR doesn't apply here (weather data, no personal data). Copyright doesn't cover the data contents (only original creative selection/arrangement).

---

### Q66. For a database containing personal information about identifiable living individuals, which legal framework applies?

a) Copyright
b) Trade secret law
c) GDPR (General Data Protection Regulation)
d) Sui generis database right

> [!note]- Solution
> **c)** GDPR applies to personal data of identifiable living individuals — data protection (privacy) is separate from copyright/sui generis/trade secret. GDPR requires a legal basis (consent, contract, legitimate interest, public task), data minimization, purpose limitation, and right-to-erasure ("right to be forgotten").

---

### Q67. Copyright protects:

a) The facts contained in a database
b) The original creative expression in a work (e.g. the database schema if it reflects original creative choices, or software source code)
c) The investment in compiling the database
d) Personal data

> [!note]- Solution
> **b)** Copyright protects *creative expression*, not facts or investment. A database schema may be copyrightable if its structure reflects original creative choices (not trivial like `firstName | lastName`). Source code is copyrightable as a literary work. Facts (e.g. weather measurements) are not copyrightable. Sui generis is the separate right that protects investment.

---

### Q68. [Mehrfachauswahl] Which of the following artifacts are generally copyrightable?

a) A novel database schema with carefully crafted partitioning (original creative choices)
b) A trivial schema with `firstName | lastName`
c) Complex stored procedure source code
d) An original graphical user interface
e) An image of Bart Simpson stored as a BLOB

> [!note]- Solution
> **a), c), d), e).** (a) original creative schema → copyrightable literary work. (c) software source → copyrightable. (d) original GUI → copyrightable creative work. (e) the Bart Simpson image is owned by Fox — copyright of the original creator; storing it in a DB doesn't change that. (b) trivial schema lacks the originality threshold → NOT copyrightable (any developer would design it the same way).

---

### Q69. Trade secret protection requires:

a) Public disclosure of the secret
b) Reasonable steps to keep information confidential (NDAs, access restrictions) — protection lasts as long as confidentiality is maintained
c) Registration with a government body
d) The secret be a software algorithm

> [!note]- Solution
> **b)** Trade secret: information is protected as long as it's kept confidential with reasonable measures (NDAs, access controls, physical/digital barriers). No registration. Protection evaporates once the secret becomes public. NDAs are the classic mechanism; customer lists kept under access restrictions are the typical example.

---

### Q70. The FAIR "Reusable" principle regarding licenses means:

a) All FAIR data must be licensed under CC0 (public domain)
b) (Meta)data are released with a clear and accessible data usage license — the license tells others how they can (re)use the data; the choice of license is the data provider's, not mandated by FAIR
c) Licenses are optional for FAIR data
d) Only open-source licenses qualify

> [!note]- Solution
> **b)** Reusable requires a clear, accessible usage license. The license choice is the provider's — could be CC-BY, CC0, or a restrictive license. FAIR ≠ Open Data: data can be access-restricted (e.g. sensitive medical data) but still license-clear and thus Reusable in the FAIR sense. The principle ensures users know what reuse is permitted.

---

*Let's cook. 🔬*

> *Self-check: Can you recite the equivalence hierarchy? Explain why `__TIME__` breaks builds but `__LINE__` doesn't? What's the difference between reproduction and replication? Why is `oneOf` stricter than `anyOf`? What does the BHB ruling tell us about "obtaining" vs "creating" data?*