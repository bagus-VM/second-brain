---
title: "latexmk"
tags: [concept, reproducibility-engineering, build-tools, latex, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[make-and-build-systems]]", "[[make-dependency-tracking]]"]
---

## One-line Summary
*A Perl script that compiles your LaTeX document the correct number of times, runs bibtex when needed, and tracks dependencies automatically — so you never have to guess "did I run it enough?"*

## Core Intuition
Compiling a LaTeX document is not a single step. You run `pdflatex` once to get the labels; then `bibtex` to process the bibliography; then `pdflatex` again to resolve the citation labels; then `pdflatex` a third time to resolve cross-references. If you change a `\cite`, you repeat the cycle. If you change a `\label`, you run at least twice.

Doing this manually is error-prone. `latexmk` automates it: it runs the necessary commands, checks whether the output has stabilized (no more "Rerun to get cross-references right" warnings), and stops when the document is fully compiled. Crucially, it tracks dependencies by parsing the `.fls` (file list) output from `pdflatex -recorder`, so if you `\input` a file or `\includegraphics` a figure, `latexmk` knows about it — and knows to recompile when those change.

This is why it appears in the Reproducibility Engineering course alongside Make: `latexmk` is the LaTeX-specific equivalent of Make's dependency tracking, but it's automatic — you don't write the dependency rules yourself.

## Formal Definition / Statement
`latexmk` is a Perl script (by John Collins, distributed with TeX Live) that manages the compilation cycle of LaTeX documents. Given a `.tex` source, it:

1. Runs the primary engine (`pdflatex`, `lualatex`, `xelatex`, or `latex`+`dvips`) repeatedly until the output stabilizes.
2. Runs auxiliary programs (`bibtex`, `biber`, `makeindex`, `makeglossaries`) when their inputs have changed.
3. Tracks dependencies via the `-recorder` mechanism (`.fls` files listing all files read/written).
4. On subsequent runs, only recompiles if a source or dependency has changed (mtime-based, like Make).

## Key Properties / Complexity
- **Automatic dependency discovery**: uses `.fls` files from `pdflatex -recorder`, which list every file opened for reading or writing. No manual dependency rules needed.
- **Idempotent**: running `latexmk` on an already-compiled, up-to-date document does nothing (like `make` with nothing to do).
- **Continuous mode**: `latexmk -pvc` watches for file changes and recompiles automatically, then refreshes the PDF viewer.
- **Reproducibility caveat**: like Make, `latexmk` is mtime-based. After a `git checkout`, mtimes may not reflect content changes. For reproducible builds, use `SOURCE_DATE_EPOCH` or force a full recompile.
- **Integration with Make**: can be called from a Makefile as the recipe for a PDF target: `latexmk -pdf -interaction=nonstopmode -halt-on-error document.tex`.

## Worked Example
The lecture's Makefile example (Reproducibility Engineering, L05/L06):

```makefile
experiment.pdf: experiment.tex results/chart.pdf
    latexmk -pdf -interaction=nonstopmode -halt-on-error experiment.tex

results/chart.pdf: generate_chart.py results/results.csv
    python3 generate_chart.py results/results.csv 10 results/chart.pdf
```

If you modify only `generate_chart.py`:
- `make` sees `chart.pdf` is out of date (its prerequisite `generate_chart.py` changed).
- `make` regenerates the chart, then runs `latexmk` because `experiment.pdf`'s prerequisite `chart.pdf` changed.
- `latexmk` runs `pdflatex` once (the `.tex` didn't change, but an included figure did). If the figure's dimensions changed and labels shifted, it runs again until stable.
- The expensive experiment (generating `results.csv`) is NOT rerun — it's upstream of the change.

## Common Pitfalls
- **Forgetting `-interaction=nonstopmode`**: without it, `latexmk` will pause on errors and wait for user input — which hangs in automated/CI builds. Always use `-interaction=nonstopmode -halt-on-error` in scripts.
- **Stale `.fls` files**: if you delete a `\input` but the `.fls` still lists it, `latexmk` may warn about a missing dependency. Fix: clean auxiliary files (`latexmk -c`) and recompile.
- **mtime skew after git checkout**: same issue as Make. If git doesn't update mtimes, `latexmk` may think nothing changed. Fix: `latexmk -gg` (force full recompile) or touch the `.tex` file.
- **Confusing `latexmk -pdf` (pdflatex) with `latexmk -pdfxe` (xelatex)**: the `-pdf` flag specifically means pdflatex. For XeLaTeX, use `-pdfxe`. Using the wrong engine produces errors with non-ASCII or custom-font documents.

## Connections
- [[make-and-build-systems]] — Make provides the outer dependency graph; latexmk handles the LaTeX-specific inner cycle
- [[make-dependency-tracking]] — the lecture's Makefile example that uses latexmk as the PDF build recipe
- [[reproducible-builds]] — latexmk is mtime-based, so for bit-for-bit reproducibility, pair with [[source-date-epoch]]
- [[deterministic-builds]] — latexmk's output is deterministic given the same inputs (no embedded timestamps in modern TeX engines with SOURCE_DATE_EPOCH)

## Open Questions
- Can latexmk's `.fls`-based dependency tracking be combined with content-based hashing (like Bazel) for fully reproducible, mtime-independent builds?
- How does latexmk interact with the `minted` package (which requires `--shell-escape` and external Python calls)? The dependency chain extends outside TeX.
