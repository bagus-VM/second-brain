---
title: "Make Dependency Tracking"
tags: [concept, reproducibility-engineering, semester-1, make, dependencies, incremental-build]
course: "Reproducibility Engineering"
source_count: 2
status: current
last_updated: 2026-06-14
prerequisites: ["[[make-and-build-systems]]", "[[out-of-source-build]]"]
---

## One-line Summary
Make's dependency tracking uses file mtimes to decide what to rebuild — if any prerequisite (a `.c` file, a header, a generated data file) is newer than its target, the target's recipe is rerun — and the lecture's exercise shows that a single edit to `generate_chart.py` triggers a precisely-scoped cascade (rebuild chart, then PDF) but NOT the upstream data regeneration.

## Core Intuition
Make's algorithm is simple but precise: a target is out-of-date iff *any* of its prerequisites has been modified more recently than the target itself. The recipe is run only for out-of-date targets. For an up-to-date project, `make` does nothing.

The lecture's example (task 5 and 6b):
```makefile
experiment.pdf: experiment.tex results/chart.pdf
    latexmk -pdf -interaction=nonstopmode -halt-on-error experiment.tex

results/chart.pdf: generate_chart.py results/results.csv
    python3 generate_chart.py results/results.csv 10 results/chart.pdf

results/results.csv: run_experiment.sh pplease.py pplease_split.py \
                     pplease_stats.py recipe.txt
    bash run_experiment.sh recipe.txt 10 42 make_run
```

The dependency graph is:
```
results/results.csv ← run_experiment.sh, pplease.py, ..., recipe.txt
results/chart.pdf ← generate_chart.py, results/results.csv
experiment.pdf ← experiment.tex, results/chart.pdf
```

Question: "If you modify `generate_chart.py` and run `make all` again, which targets are recreated?"
- `results/chart.pdf` — out of date (generate_chart.py is newer)
- `experiment.pdf` — out of date (its prerequisite, chart.pdf, is newer)
- `results/results.csv` — up to date (its prerequisites are unchanged)

Answer: **only `results/chart.pdf` and `experiment.pdf`** are recreated. The expensive experiment run (`results/results.csv`) is NOT re-executed, because none of its prerequisites changed.

This is the whole point of Make's dependency tracking: *rebuild the minimum necessary, never more, never less*.

## Formal Definition / Statement

### The Make algorithm
For each target T:
1. If T does not exist, T is out-of-date.
2. For each prerequisite P of T:
   - If P does not exist, error: missing prerequisite.
   - If P is newer than T (mtime(P) > mtime(T)), T is out-of-date.
   - If P is out-of-date, T is out-of-date.
3. If T is out-of-date, execute the recipe.
4. Process prerequisites in the correct order (depth-first traversal of the dependency DAG).

### Edge cases
- **Missing target with no recipe**: Make errors out.
- **Circular dependency**: Make errors out.
- **Phony targets** (`.PHONY`): always out-of-date, even if a file with that name exists. Used for `clean`, `all`, `test`, etc.
- **Parallel builds** (`make -j N`): Make builds independent targets concurrently. The order within a recipe is still sequential.
- **Order-only prerequisites** (`|`): prerequisite must exist before target is built, but its mtime does not trigger a rebuild. Used for directory creation.

### The mtime assumption
Make's correctness depends on the file system's mtime being a reliable proxy for "this file is newer than that file". This breaks when:
- The mtime is wrong (e.g., file copied with `cp -p` preserves mtime, but `cp` without `-p` does not).
- The mtime is in the future (system clock changed, DST shift, VM clock skew).
- The granularity is too coarse (FAT32 has 2-second granularity; two files in the same second are "equal").
- The build tool writes to a file with an older mtime (e.g., a generator that preserves mtime from the input).

## Key Properties

### What Make gives you
- **Incremental builds**: change one file, rebuild only what's downstream.
- **Parallelism**: independent branches of the DAG can build in parallel.
- **Declarative dependencies**: the Makefile *describes* the DAG, doesn't prescribe the build order.
- **Cross-platform**: every Unix-like system has Make.

### What Make does NOT give you
- **Remote execution** (use distcc, icecream, or build clusters).
- **Content-based dependency tracking** (use Bazel, please, or Buck — they hash file contents, not mtime).
- **Automatic dependency discovery** (you have to write `gcc -M` rules or use `auto-depend`).
- **Reproducibility across machines** (mtime is not portable; content-based tools are).

## Worked Example

The lecture's task 5f–h: incremental rebuild scenarios.

**Scenario 1: change the sample size in `gen_df_sin.py` to 2048.**
- The dependency for `results/results.csv` includes `gen_df_sin.py` (via the `run_experiment.sh` script, which calls the Python script). So `results/results.csv` is out of date.
- The chart depends on the CSV, so the chart is out of date.
- The PDF depends on the chart, so the PDF is out of date.
- `make` reruns: `run_experiment.sh` → chart generation → `latexmk`.

**Scenario 2: change the noise strength in `csv_noisy_sin.py` to 0.4.**
- Same as above: the Python script is a transitive dependency of the CSV.

**Scenario 3 (the one the lecture asks): modify `generate_chart.py` only.**
- The CSV's prerequisites do NOT include `generate_chart.py` (the script that *generates* the chart is separate from the script that *reads* the CSV to make the chart).
- So the CSV is up-to-date; the chart is out of date; the PDF is out of date.
- `make` reruns: chart generation → `latexmk`. The experiment itself is NOT rerun.

This is the central efficiency point: the experiment is expensive, the chart is cheap, the PDF is cheap. The dependency graph puts the expensive step at the root, and a downstream edit doesn't propagate up.

## Common Pitfalls
- **Forgetting a dependency in the Makefile**: if `experiment.tex` includes a file that's not listed as a prerequisite, editing that file won't trigger a rebuild. Symptom: stale PDF. Fix: re-run the dependency scan, or use `latexmk`'s automatic dependency discovery.
- **mtime skew after `git checkout`**: Git updates mtimes, but the files you just checked out may all have the same checkout time. Make sees them as "all up-to-date" even if the contents changed. Fix: use `git checkout --` with `--no-fsync` or run `find . -exec touch {} \;` after checkout.
- **Generator scripts that don't update mtime**: a Python script writes `output.csv` but uses `os.utime` to preserve the source's mtime. Make sees the output as "older than the source" and rebuilds forever. Fix: have the generator write the current mtime, or use a sentinel.
- **Confusing `=` and `:=` in Make**: `VARIABLE = $(shell date)` is evaluated *every* time the variable is referenced, giving different values on different invocations. `VARIABLE := $(shell date)` is evaluated once. Use `:=` for fixed values.
- **Parallel builds with shared resources**: `make -j` runs recipes concurrently, but if two recipes write to the same intermediate file, you have a race. Symptom: non-deterministic build failures. Fix: serialise the conflicting recipes.
- **Phony targets that look like files**: if you have a file named `clean` in the directory, `make clean` would think the target is up-to-date (file exists, no prerequisites). Always declare phony targets with `.PHONY: clean`.

## Connections
- [[make-and-build-systems]] — the broader topic
- [[out-of-source-build]] — the standard hygiene practice that pairs with Make
- [[reproducible-builds]] — Make's mtime-based tracking is *not* reproducible across machines; for that, use content-based tools
- [[deterministic-builds]] — Make + out-of-source + content-based deps = reproducible
- [[source-date-epoch]] — for making mtimes deterministic
- [[latexmk]] — the lecture's example of a tool that auto-tracks LaTeX dependencies

## Open Questions
- For very large C++ projects, can Make's mtime-based tracking be made as reliable as Bazel's content-based tracking? (Use `ccache` for content-based caching of compilations; the dependency graph itself remains mtime-based.)
- For builds that span multiple machines (CI, build clusters), how do you keep mtime semantics consistent? (Distcc, icecream, or migrate to a content-based system.)
- Can Make be extended to *prove* that its dependency graph is a DAG at parse time? (Make itself doesn't check; tools like `makedepend` and `compiledb` can verify post hoc.)
