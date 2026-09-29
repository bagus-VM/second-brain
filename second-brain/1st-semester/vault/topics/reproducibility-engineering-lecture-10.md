---
title: "Lecture 10: Remote Experiments and Artifact Packaging"
tags: [topic, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-07-10
prerequisites: ["[[reproducibility-engineering-lecture-9]]", "[[reproducible-builds]]", "[[containerization-for-builds]]"]
sources: ["raw/lectures/reproducibility_engineering/Vorlesung/SoSe_2026_RepEng_IC_10___Remote_Experiments.pdf"]
---

## One-line Summary
*When experiments run on remote platforms (not your laptop), you need a structured workflow to ensure every artifact — from build to measured data to paper figures — remains reproducible.*

## Core Intuition
Not every experiment runs on the researcher's laptop. Sometimes you get compute time on a cluster, a cloud VM, or a shared lab machine that doesn't support Docker. The challenge: how do you ensure that building binaries, running experiments, and analyzing measured data are all reproducible when you can't just ship a container?

Lecture 10 addresses this with a structured artifact workflow from the ICDE 2021 tutorial "Nullius in Verba: Reproducibility for Database Systems Research, Revisited" (Mauerer, Scherzinger). The key insight is separating the workflow into distinct artifact types — build artifacts, experiment execution packages, measured data, and analysis scripts — each with clear dependencies and temporal ordering.

## Formal Definition / Statement

### The Remote Experiment Workflow

The workflow has five stages:

1. **Build artifacts** — compile the software (may happen on a different machine than where experiments run)
2. **Experiment execution package** — bundle the compiled binary + configuration + scripts needed to run experiments
3. **Run experiments** — execute on the target platform (cluster, cloud, lab machine)
4. **Measured data** — collect results (CSV files, logs, measurements)
5. **Generate graphs and paper** — analyze measured data, produce figures and tables

### Artifact Dependencies

The dependency graph shows both integration (A → B, meaning B incorporates A) and production (A ⇒ B, meaning A produces B):

```
Source code → Build artifacts → Experiment execution package
                                        ↓
                                  Run experiments
                                        ↓
                                  Measured data → Generate graphs and paper
```

The Docker container sits alongside the build artifacts — when the target platform supports Docker, you package the entire execution environment. When it doesn't, you must manually ensure the build environment is reproducible.

### The SQPolite Case Study

SQPolite (https://github.com/lfd/icde2021_tutorial) demonstrates end-to-end artifact packaging:

1. **Fork** SQLite from upstream (https://github.com/sqlite/sqlite)
2. **Apply patches** that add TPC-H query support
3. **Include dbgen** (TPC-H data generator)
4. **Write doall.sh** that builds, generates data, runs queries, and verifies results
5. **Package reproduction material** — the ICDE 2021 tutorial, slides, and the SQPolite project

The key: `./doall.sh docker` reproduces the paper's results from scratch. The patches document exactly what changed. The fork preserves attribution and commit history.

### The Nullius in Verba Paper

The accompanying article (Mauerer & Scherzinger, ICDE 2021) surveys reproducibility practices in the database systems community. Key findings:

- Many reproduction packages are incomplete or broken
- The badge system (ACM reproducibility badges) incentivizes packaging but doesn't guarantee quality
- Self-contained environments (Docker, VMs) are the most reliable approach
- Long-term reproducibility requires archiving artifacts, not just linking to GitHub

## Key Properties

- **Separation of concerns**: build, execute, analyze are distinct phases with clear interfaces
- **Platform independence**: the workflow works whether or not Docker is available on the target
- **Artifact traceability**: each artifact type has documented inputs and outputs
- **Reproduction verification**: expected outputs are included for comparison
- **Patch-based changes**: modifications to third-party code are documented as diffs
- **End-to-end automation**: doall.sh runs the entire pipeline

## Worked Example

The SQPolite reproduction workflow:

1. Clone the tutorial repo: `git clone https://github.com/lfd/icde2021_tutorial`
2. Enter the SQPolite directory
3. Run: `./doall.sh docker`
4. What happens:
   - Builds SQLite from patched source (inside Docker)
   - Generates TPC-H test data with dbgen
   - Runs all 22 TPC-H queries
   - Compares output to reference results
   - Produces timing measurements
5. Output: query results match the paper's tables, timings are comparable

The entire pipeline is one command. No manual steps. No "install these dependencies first."

## Common Pitfalls

- **Assuming Docker is always available.** Shared clusters and HPC systems often don't support Docker. The workflow must work without it — use Singularity, or bundle build instructions manually.
- **Linking to GitHub instead of archiving.** Repositories get deleted, moved, or renamed. Archive artifacts with the paper (e.g., Zenodo, ACM DL).
- **Incomplete reproduction packages.** Missing data files, broken scripts, undocumented dependencies. The package must be self-contained.
- **Not testing the reproduction package.** Always test on a clean machine before submitting. If you can't reproduce it, nobody can.
- **Confusing the workflow with the tooling.** Docker is a tool, not a methodology. The workflow (build → execute → analyze) is the methodology.

## Connections

- [[artifact-packaging]] — the concept page for packaging research artifacts
- [[reproducible-builds]] — build reproducibility is the foundation
- [[containerization-for-builds]] — Docker as the primary packaging tool
- [[git-for-reproducibility]] — version control preserves artifact history
- [[git-patches-and-diffs]] — patches document changes to third-party code
- [[reproducibility-engineering-lecture-9]] — LLMs introduce new reproducibility challenges
- [[reproducibility-engineering-lecture-5]] — reproducible builds are the foundation
- [[reproducibility-engineering-lecture-6]] — database architectures affect packaging

## Open Questions

- How do you handle experiments that require specific hardware (GPU, FPGA) that's not available on the reproduction platform?
- What is the right level of granularity for artifact packaging? Per experiment? Per paper? Per project?
- How do you version reproduction packages when the paper is revised?
- Should reproduction packages be peer-reviewed? What would that review process look like?
