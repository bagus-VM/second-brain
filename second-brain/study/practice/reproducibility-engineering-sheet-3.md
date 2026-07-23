---
title: "Reproducibility Engineering - Exercise Sheet 3"
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
| Exercises 1–3 — Experiment Dispatching & Binary Container | [[containerization-for-builds]] · [[computational-reproducibility-in-ml]] |
| Exercise 4 — Dependency Management | [[containerization-for-builds]] · [[hypothesis-formulation]] |

# Exercise Sheet 3 — Experiment Dispatching & Binary Containers

> **Note:** No official solutions available.

Lab Sessions: May 7/15, 2026

## Exercises

### 1. Preparation
Update your local RepEng repository: `git pull`

### 2. Experiment Dispatching

**(2.1) Extending `run_experiment.sh`:**

Modify the existing script to support:

**(a) Random seed argument:** Add a third positional argument for the random seed. Pass it to `pplease.py` for deterministic output.
```
./run_experiment.sh recipe.txt 10 42 exp1
```

**(b) Result directory and label:** Add a fourth positional argument for an experiment label. Store results in `results/` with parameters encoded in the subdirectory name, e.g., `results/recipe_runs_10_seed_42_exp1/`.

**(c) Output files per run:** Each run creates one output file (e.g., `polite_1.txt`) in the experiment result directory. Statistics output also goes to the results directory.

**(d) CSV file with generated strings:** Store results in `results.csv` with columns `run`, `original`, `polite`. One row per run per sentence.

**(e) Usage block:** Adapt the usage block (Lines 10–13) to check the new command-line syntax and print correct usage on failure.

**(2.2) Adapting the Analysis:**
Modify `pplease_stats.py` to read the generated CSV file instead of individual text files.
```
python3 pplease_stats.py results.csv 1
```
Select rows for the specified run and compute min, max, median for `original` and `polite` columns.

**(2.3) Adapting the Dockerfile:**
Update the Dockerfile from Sheet 2 to run the full experiment workflow with: `recipe.txt`, 10 runs, seed 42, label `docker`.

**(2.4) Creating a `doAll.sh` Script:**
Create `doAll.sh` that runs the complete experiment with fixed parameters: 100 runs, seed 42, label `doAll`, input file `recipe.txt`.

### 3. Binary Container

- Build image: `docker build -t lab3_<matr_nr> .`
- Export: `docker save -o lab3_<matr_nr>.tar lab3_<matr_nr>`
- Exchange tar file with a fellow student
- Load: `docker load -i lab3_<other_matr_nr>.tar`
- Run: `docker run --rm lab3_<other_matr_nr>`
- Compare outputs and provide feedback

### 4. Dependency Management (Multiple Choice)

Given a Dockerfile pinning Ubuntu packages and a Python script `experiment.py` that fetches time from an external API:

**(a)** If Ubuntu has a new release, reproduction may fail in:
- **Neither the binary nor the source container** (binary is frozen; source uses pinned versions via `FROM ubuntu:latest` but installed packages are version-pinned — actually, `FROM ubuntu:latest` would pull a new release, so: **only the source container**)

**(b)** If a new Python version is released, reproduction may fail in:
- **Neither the binary nor the source container** (packages are version-pinned in the Dockerfile; binary is frozen)

**(c)** If the external time service is offline, reproduction may fail in:
- **Both the binary and the source container** (the script makes a network call at runtime regardless of container type)


---

## Related Resources

### 📖 Reproducibility Engineering – Lecture 3: Hypotheses
- Lecture topic: [[reproducibility-engineering-lecture-3]]

**Key concepts covered:**
- [[hypothesis-formulation]]
- [[presenting-experiments]]
- [[levels-of-equivalence]]
- [[reproducibility-crisis]]
- [[repeat-reproduce-replicate]]
- [[computational-reproducibility-in-ml]]
- [[research-artifacts]]
