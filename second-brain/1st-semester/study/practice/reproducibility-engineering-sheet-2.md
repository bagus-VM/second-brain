---
title: "Reproducibility Engineering - Exercise Sheet 2"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-02
---

## Topic Map

| Exercise | Key Vault Pages |
|----------|----------------|
| Exercise 1 — Preparation | [[computational-reproducibility-in-ml]] |
| Exercise 2 — Dealing with Randomness | [[levels-of-reproducibility]] · [[computational-reproducibility-in-ml]] |
| Exercise 3 — Reproducibility Package | [[data-provenance]] · [[workflow-reproducibility]] |
| Exercise 4 — Dockerfile Review | [[containerization-for-builds]] · [[reproducibility-standards-bronze-silver-gold]] |

# Exercise Sheet 2 — Dealing with Randomness & Reproducibility Packages

> **Note:** No official solutions available.

Lab Sessions: April 30 / May 8, 2026

## Exercises

### 1. Preparation
Update your local RepEng repository: `git pull`

### 2. Dealing with Randomness

**(2.1) Data Generation — The `pplease` Script:**
Implement `pplease.py` — a Python CLI script that reads text from stdin and randomly inserts ", please" at the end of sentences (50% chance per sentence), writing output to stdout.

Example:
```
cat water.txt | python pplease.py
I am thirsty, please. My glass is empty.
Can you pass me the water?
```

**(2.2) Data Analysis:**
Implement `pplease_stats.py` — a Python CLI script that:
- Accepts input and output file paths as arguments
- Computes min, max, and median character length per sentence for both original and "polite" output
- Prints results as a table

Example:
```
python pplease.py < water.txt > water_polite.txt
./pplease_stats.py water.txt water_polite.txt
```

**(2.3) Repeatability:**
- What modifications are required to ensure the experiment is repeatable?
- **(2.3.1)** Implement the changes and test with `run_experiment.sh` (Linux/Mac) or `run_experiment.ps1` (Windows):
  ```
  ./run_experiment.sh recipe.txt 10
  ```
  All subsequent runs should produce identical results to the first run.

### 3. Reproducibility Package

Build a fully automated reproducibility package by extending the provided Dockerfile skeleton.

Checklist of required items:
- First 1–2 lines document the purpose of the package
- State who owns the copyright
- Specify the license using an SPDX license identifier
- Start from a recent LTS Ubuntu distribution
- Declare maintainer: `LABEL org.opencontainers.image.authors=<author-email>`
- Sort installed packages alphabetically
- No dead code (no commented-out instructions)

Optional: Pin exact versions of installed packages.

**(3.1) Testing your Dockerfile:**
```
docker build -t repeng_lab2 .
docker run --rm repeng_lab2
```
Verify all 10 runs produce identical results.

### 4. Dockerfile Review (Multiple Choice)

Given a Dockerfile with specific issues, evaluate against the checklist:

1. Which line violates required items? → **Line 4** (`FROM ubuntu:latest` — not a pinned LTS version)
2. Which line violates required items? → **Line 6** (maintainer should use `LABEL org.opencontainers.image.authors`, not a comment)
3. Which line should be removed? → **Line 20** (dead code — commented-out `chmod` instruction)
4. After fixing, are there still violations? → **Yes** (packages not sorted alphabetically)
5. Can we guarantee the exact same image long-term? → **No** (unpinned package versions)


---

## Related Resources

### 📖 Reproducibility Engineering - Lecture 2: Levels and Provenance
- Lecture topic: [[reproducibility-engineering-lecture-2]]

**Key concepts covered:**
- [[levels-of-reproducibility]]
- [[provenance-in-reproducibility]]
- [[vistrails]]
- [[workflow-reproducibility]]
- [[reproducibility-standards-bronze-silver-gold]]
- [[computational-reproducibility-in-ml]]
- [[data-provenance]]
