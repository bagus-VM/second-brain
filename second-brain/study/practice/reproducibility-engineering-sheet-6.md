---
title: "Exercise Sheet 6 — Reproducible Binary Builds & Make"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-14
---

# Exercise Sheet 6 — Reproducible Binary Builds & Make

## Exercises

### 2. Challenges in Reproducing Binary Builds

**2.2 Comparing different Compilers**

Compile the same `hello.c` with `gcc` and `clang`, then compare the binaries.

- **Functionally equivalent?** Yes — both print "Hello World". The source code is the same, the runtime behaviour is the same.
- **Bitwise identical?** No — different compilers produce different object code (different code generation strategies, different default settings, different versions, different ABI). The binaries will differ in instruction selection, register allocation, padding, and metadata.
- **Implication for reproducibility**: the compiler is part of the build environment. To get reproducible binaries, you must pin the compiler version *and* the compilation flags. Using a different compiler (even for the same source) gives different bytes.

**2.3 Comparing different Compile Options**

Compile with different optimisation levels (e.g., `-O0` vs `-O2`).

- **Functionally equivalent?** Yes — same source, same external behaviour.
- **Bitwise identical?** No — different optimisation levels produce different code (loop unrolling, inlining, instruction scheduling). Even a single `-O0` vs `-O2` flag changes the entire binary.
- **Implication**: build flags must be pinned for reproducibility. A "reproducible build" requires not just the same source but the same build environment *and* build commands.

**2.4 Debug Information and Preprocessors**

Compile with `-g` (debug info) vs without:
- **Bitwise identical?** No — debug info adds sections to the binary (DWARF data, line tables, etc.). The executable code is the same, but the binary file is larger and different.

Preprocessor macros (`__TIME__`, `__FILE__`, `__LINE__`):
- These macros expand to the current time, source file path, and line number at compile time
- If the macro is used, the binary *will* differ across builds (because time, file path, or line may differ)
- **Implication**: programs that use `__TIME__` in their output are *intrinsically non-reproducible* — you cannot get bitwise-identical binaries without removing the macro

### 3. Reproducible Toolchains: Compiling Python

Building Python from source in an "out of source" (out of tree) build:
- Out-of-source build: build artifacts go in a separate directory, not mixed with the source
- The `configure --prefix=$HOME/Python-3.12.3-custom` step sets the installation location
- `make -j $(nproc)` uses all available cores
- **Why is out-of-source build good practice?**
  - **Clean separation**: source tree stays clean; you can delete the build dir without affecting the source
  - **Multiple builds**: you can have multiple build directories with different configurations (debug, release, etc.) sharing the same source
  - **Reproducibility**: the build artifacts are clearly separated, making it easier to reason about what was produced
  - **Tooling support**: many build systems (CMake, Meson, Autoconf) explicitly support out-of-source builds

### 4. ReproTest

ReproTest is a tool that builds a program twice in different, simulated environments and checks whether identical binaries are produced.

- **`reprotest 'gcc hello-line.c -o hello-line' hello-line`**: tests whether the build is reproducible across different environments
- **Output**: ReproTest reports the differences between the two binaries (file size, section differences, etc.)
- **Without `-g`**: the build may be reproducible if no macros inject timestamps or paths
- **With `-g`**: ReproTest typically finds differences in the debug info section (DWARF contains paths, timestamps, etc.)
- **C memory terminology for the differences**:
  - **Stack**: local variable storage; not embedded in the binary
  - **Heap**: dynamic memory; runtime, not in the binary
  - **Globals**: global variables; in `.data` or `.bss` sections of the binary
  - **Constants**: read-only data; in `.rodata` section
  - **Code**: compiled instructions; in `.text` section
- The debug info differences appear in the debug sections (typically `.debug_info`, `.debug_line`), not in the runtime memory regions

### 5. Make

Make is a build automation tool. A `makefile` declares dependencies and build rules:

```makefile
.PHONY: all clean
all: experiment.pdf
experiment.pdf: experiment.tex results/chart.pdf
	latexmk -pdf -interaction=nonstopmode -halt-on-error experiment.tex
results/chart.pdf: generate_chart.py results/results.csv
	python3 generate_chart.py results/results.csv 10 results/chart.pdf
results/results.csv: run_experiment.sh pplease.py pplease_split.py pplease_stats.py recipe.txt
	bash run_experiment.sh recipe.txt 10 42 make_run
clean:
	rm -f experiment.pdf results/chart.pdf
	rm -f results/results.csv results/polite_*.txt results/stats_*.txt
	latexmk -c
```

**Key concepts**:
- **Target**: a file to be built (e.g., `experiment.pdf`)
- **Prerequisite**: a file that must exist before the target can be built
- **Recipe**: the shell commands to build the target from the prerequisites
- **`.PHONY`**: declares a target that doesn't correspond to a file (always run)
- **Dependency chain**: Make figures out the build order from the dependency graph

**Example: typo fix scenario**:
- After `make all`, modify `generate_chart.py` (e.g., fix a typo in the legend)
- `make all` re-runs because `results/chart.pdf` depends on `generate_chart.py`
- But `results/results.csv` does *not* depend on `generate_chart.py`, so it's NOT regenerated
- Final answer: **Only `results/chart.pdf` is recreated**

**Example: changing sample size to 2048**:
- `gen_df_sin.py` would be the source for the dataframe
- If `gen_df_sin.py` is in the dependency chain of `results/results.csv`, the entire chain regenerates
- Answer: **All targets (except clean) are regenerated** — if the dependency is correctly specified
- In real makefiles, you'd need to check the exact dependency specification

### 6. Reproducible Builds (Multiple Choice)

**6a: How many snippets allow bitwise identical builds?**
1. Plain `printf("Hello World")` — yes (no time/file/line macros)
2. `__FILE__` — no (path differs across builds)
3. `__TIME__` — no (time differs across builds)
4. `__LINE__` — depends — if compiled at the same line every time, yes; in practice, the line number is fixed in the source so `__LINE__` is constant across rebuilds of the *same source* on the *same source path* — but it can change if the source is moved or the line number changes

Actually, `__LINE__` is the line number *in the source file at the point of expansion*. As long as the source file is the same and the line is the same, the macro expands to the same value. So:
1. ✓ (no time/path macros)
2. ✗ (__FILE__ includes the full path)
3. ✗ (__TIME__ changes every second)
4. ✓ (line number is fixed in the source)

So 2 of 4 are bitwise reproducible: programs 1 and 4.

**6b: Make re-build targets after generate_chart.py modification**
- `experiment.pdf` depends on `results/chart.pdf`
- `results/chart.pdf` depends on `generate_chart.py`
- Modifying `generate_chart.py` makes `results/chart.pdf` out of date → rebuild
- Then `experiment.pdf` is out of date (because `results/chart.pdf` changed) → rebuild
- `results/results.csv` does NOT depend on `generate_chart.py` → not rebuilt
- Answer: **results/chart.pdf and experiment.pdf** (both are rebuilt)

## Related Lectures
- [[reproducibility-engineering-lecture-5]]
- [[reproducibility-engineering-lecture-6]]
- [[reproducible-builds]]
- [[containerization-for-builds]]
- [[source-date-epoch]]
- [[diffoscope]]
- [[build-environment-isolation]]
- [[reprotest]]
- [[binary-build-reproducibility]] — the umbrella concept: bitwise-identical builds
- [[c-preprocessor]] — the `__FILE__`, `__TIME__`, `__LINE__` non-determinism sources
- [[out-of-source-build]] — the hygiene practice (build/ separate from src/)
- [[make-dependency-tracking]] — Make's mtime-based algorithm
- [[sqlite-architecture]] — the file-based DB
- [[docker-compose]] — the standard for multi-service DB stacks
- [[client-server-db-architecture]] — the contrast to file-based
- [[foreign-tables-postgresql]] — for capturing experiment metadata
