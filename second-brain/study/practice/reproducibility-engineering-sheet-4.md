---
title: "Reproducibility Engineering - Exercise Sheet 4"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-02
---

# Exercise Sheet 4 — Structural Equivalence, LaTeX & Automated Reporting

> **Note:** No official solutions available.

Lab Sessions: May 21/22, 2026

## Exercises

### 1. Preparation
Update your local RepEng repository: `git pull`

### 2. Structural Equivalence

**(2.1) Docker Environment:**
Build the Xidel image and start a temporary container:
```
cd LabSession4/2_structural_equivalence/
docker build -t xidel-env .
docker run --rm -it xidel-env
```

**(2.2) Experiment Data:**
Analyze `experiments.xml` with experiments A–E containing structural variations:
- A: has `unit` attribute on `<time>`
- B, C: single `<time>`, no attribute
- D: two `<time>` elements
- E: `<time>` with whitespace padding

**(2.3) Tooling — Xidel:**
```
xidel experiments.xml -se "<XPath expression>"
```

**(2.4) Comparing Equality Notions:**

1. **Value Comparison (`eq`):** `//exp[@id='A']/time eq //exp[@id='E']/time` — Compares exact text of single nodes. Discuss whether "42" equals " 42 ".
2. **Structural Comparison (`deep-equal()`):**
   - `deep-equal(//exp[@id='A']/time, //exp[@id='B']/time)` — Checks identical structure including attributes.
   - `deep-equal(//exp[@id='A']/time, //exp[@id='E']/time)` — Checks if whitespace affects equality.
3. **Node Comparison (`is`):** `//exp[@id='B']/time is //exp[@id='C']/time` — Checks if two expressions point to the same physical node in the tree.
4. **General Comparison (`=`):** `//exp[@id='B']/time = //exp[@id='D']/time` — Sequence comparison; true if any values match.

Find and discuss practical scenarios for each equality notion.

### 3. LaTeX in Docker: Freezing Dependencies

**(3.1) TeX Live Installation:**
Create a Dockerfile (Ubuntu 24.04) installing `texlive-latex-base`, `texlive-latex-extra`, `texlive-fonts-recommended`. Compile the skeleton:
```
pdflatex experiment.tex
pdflatex experiment.tex  # Run twice for references
```

**(3.2) TinyTeX Installation:**
Create a second Dockerfile with TinyTeX:
- Install `ca-certificates`, `perl`, `wget`, `xz-utils`
- Download and install TinyTeX
- Add to PATH: `ENV PATH="/root/.TinyTeX/bin/x86_64-linux:${PATH}"`
- Freeze packages: `RUN tlmgr install amsmath graphicx hyperref`
- Compile the same skeleton

**(3.3) Size Comparison:**
Fill in the table comparing Ubuntu 24.04, TeX Live Base, and TinyTeX image sizes using `docker images`.

### 4. Automated Reporting

**(4.1) Documenting Experiments:**
Fill in the LaTeX skeleton `experiment.tex` covering:
- Hypothesis/Research Question
- Experiment Setup (implementation, environment, input data, measurements)
- Results (dynamically generated chart, textual description)
- Discussion

Get peer feedback, revise, then get tutor feedback.

**(4.2) Reproduction Package Integration:**
1. Merge TinyTeX installation into the Dockerfile from Sheet 3
2. Update `experiment.tex` to load chart from a fixed path (e.g., `results/chart.pdf`)
3. Update `run_experiment.sh` to sequentially:
   - Execute pplease experiments
   - Generate chart and save to expected path
   - Compile paper: `pdflatex -interaction=nonstopmode -halt-on-error experiment.tex`

**(4.2.1) Evaluating Repeatability:**
Run the package twice, compute MD5 hashes of both PDFs. Are they identical? Discuss why PDFs may differ bitwise even with identical experimental data, and whether the result is repeatable.

### 5. XPath and Docker Images (Multiple Choice)

**(a)** Given XML with exp 1 (single `<time>42</time>`) and exp 2 (two `<time>` elements), which XPath evaluates to true?
- `//exp[@id='1']/time = //exp[@id='2']/time` (general comparison matches any value in sequences)

**(b)** Given XML with exp 1 and exp 2 both having single `<time>42</time>`, which XPath evaluates to false?
- `//exp[@id='1'] is //exp[@id='2']` (different physical nodes despite identical content)

**(c)** How many Dockerfile snippets ensure long-term stability?
- **1** (only snippet A with pinned Ubuntu version AND pinned package version, no pip)


---

## Related Resources

### 📖 Reproducibility Engineering — Lecture 4: Git
- Lecture topic: [[reproducibility-engineering-lecture-4]]

**Key concepts covered:**
- [[git-dag-structure-and-internals]]
- [[developer-certificate-of-origin]]
- [[git-branching-and-merging]]
- [[git-rebasing-and-history-rewriting]]
- [[git-commit-hygiene]]
- [[gitignore-and-gitattributes]]
- [[git-patches-and-diffs]]
- [[git-for-reproducibility]]
- [[data-provenance]]
- [[computational-reproducibility-in-ml]]
