---
title: "Reproducibility Engineering - Sheet 2 Flashcards"
tags:
  - flashcards
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-06-02
---

# Flashcards — Exercise Sheet 2

## Flashcards

> [!question]- How can you make a nondeterministic Python experiment repeatable?
> [!answer]- By setting a fixed random seed (e.g., `random.seed(42)`) before any random operations. This ensures the random number generator produces the same sequence every time.

> [!question]- What is a reproducibility package and what should it include?
> [!answer]- A self-contained package (typically a Docker container) that allows a third party to reproduce an experiment with a single command. It includes: a Dockerfile with metadata (purpose, copyright, SPDX license, maintainer), all input data, all scripts, and a CMD that runs the experiment.

> [!question]- Why should you avoid `FROM ubuntu:latest` in a Dockerfile?
> [!answer]- Because `latest` is a floating tag that changes over time. When Ubuntu releases a new version, rebuilding pulls a different base image, potentially breaking dependencies. Use a pinned version like `FROM ubuntu:24.04` instead.

> [!question]- What is the SPDX license identifier and why is it used in Dockerfiles?
> [!answer]- SPDX (Software Package Data Exchange) provides concise, standardized license identifiers (e.g., MIT, Apache-2.0). Using them in Dockerfiles clearly documents the legal terms under which the code is shared, aiding reproducibility and compliance.

> [!question]- Why should installed apt packages be sorted alphabetically in a Dockerfile?
> [!answer]- Alphabetical sorting improves readability and makes it easy to check whether a package is already listed, preventing accidental duplicates. It's a best-practice convention for maintainable Dockerfiles.


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
