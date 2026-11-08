---
title: "Artifact Packaging for Reproducibility"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 2
status: current
last_updated: 2026-07-10
prerequisites: ["[[reproducible-builds]]", "[[containerization-for-builds]]", "[[git-for-reproducibility]]"]
---

## One-line Summary
*Package your research artifacts so someone else (or future you) can rebuild and verify everything — even without internet access.*

## Core Intuition
A research paper's claims are only as reproducible as the artifacts that produced them. If the code, data, and build instructions are scattered across personal laptops, dead download links, and undocumented toolchains, nobody can reproduce the results. Artifact packaging means bundling everything needed to regenerate the paper's outputs into a self-contained, documented package. The gold standard: run one command, get the same results.

The SQPolite project (from the RepEng course) demonstrates this end-to-end: a fork of SQLite with TPC-H benchmark queries, packaged so that `./doall.sh docker` reproduces the paper's query results from scratch.

## Formal Definition / Statement

An artifact package is a self-contained bundle that includes:

1. **Source code** — the software that produces the results, version-controlled
2. **Data** — input datasets (or scripts to generate/download them)
3. **Build instructions** — how to compile and run (Makefile, Dockerfile, doall.sh)
4. **Expected outputs** — reference results for verification
5. **Documentation** — what the artifact does, how to run it, what to expect

The key principle: **be independent of external services.** GitHub repositories disappear. Download links break. Package managers update. A well-packaged artifact builds on an island without internet.

### Packaging strategies

**Fork + patches:** Fork the upstream project, apply your changes as patches. The fork inherits commit history and preserves attribution. Patches clearly document what changed. Example: SQPolite forks SQLite, applies TPC-H patches.

```bash
# Fork preserves history
git clone https://github.com/lfd/sqlite  # fork
# Apply patches
git apply TPCH-sqlite.diff
```

**Docker containers:** Bundle the entire build environment. The Dockerfile documents every dependency. Docker Compose orchestrates multi-service setups (database + application + benchmark runner).

**End-to-end scripts:** A single `doall.sh` that builds, runs, and verifies. No manual steps. No "install these 5 tools first" instructions buried in a README.

### Long-term reproducibility

External dependencies are the enemy of long-term reproducibility:
- Base system details change (package versions, kernel)
- GitHub repositories disappear or move
- Software is no longer maintained, download links die
- System runtime configuration changes

Goal: build self-contained, complete environments. Be ready to build even when trapped on an island without internet, or 20 years after all repositories have gone.

## Key Properties / Complexity

- **Self-contained**: no external downloads required at build time
- **Documented**: every step is explicit, no tribal knowledge
- **Verifiable**: expected outputs are included for comparison
- **Automated**: one command builds and runs everything
- **Patch-based changes**: modifications to third-party code are clearly documented as diffs
- **Containerized**: Docker guarantees the build environment is reproducible
- **Version-pinned**: every dependency has an exact version (no `latest` tags)

## Worked Example

The SQPolite project packages a TPC-H benchmark on SQLite:

1. **Fork** SQLite from upstream (https://github.com/sqlite/sqlite)
2. **Apply patches** that add TPC-H query support (TPCH-sqlite.diff)
3. **Include dbgen** (TPC-H data generator) as a submodule or vendored copy
4. **Write doall.sh** that:
   - Builds SQLite from the patched source
   - Generates TPC-H test data with dbgen
   - Runs all 22 TPC-H queries
   - Compares output to reference results
5. **Package as Docker** — `./doall.sh docker` runs everything in a container

The key insight: the patches document exactly what changed in SQLite. The fork preserves the full commit history. The doall.sh script automates the entire pipeline. Someone reading the paper can clone the repo, run one command, and verify every result.

## Common Pitfalls

- **Relying on `git clone` at build time.** If GitHub is down or the repo is deleted, the build fails. Vendor critical dependencies or use submodules with pinned commits.
- **Using `latest` tags in Dockerfiles.** A `FROM python:latest` today is different from one next year. Pin to exact versions.
- **Assuming the reader has the same OS.** Docker eliminates this problem. Without Docker, document the exact OS and version.
- **Not including expected outputs.** Without reference results, the reader can build but cannot verify.
- **Manual steps in the build process.** "First install X, then configure Y" is not reproducible. Automate everything.

## Connections

- [[reproducible-builds]] — artifact packaging extends build reproducibility to the full research pipeline
- [[containerization-for-builds]] — Docker is the primary tool for creating self-contained build environments
- [[git-for-reproducibility]] — version control preserves the history of changes to artifacts
- [[git-patches-and-diffs]] — patches document changes to third-party code clearly and portably
- [[ci-cd-for-reproducibility]] — CI/CD can automatically verify that artifact packages still build
- [[workflow-reproducibility]] — the doall.sh script is a reproducible workflow
- [[reproducibility-engineering-lecture-5]] — reproducible builds are the foundation for artifact packaging
- [[reproducibility-engineering-lecture-6]] — database architectures affect how artifacts are packaged
- [[reproducibility-engineering-lecture-10]] — remote experiments and the SQPolite case study

## Open Questions

- What is the practical size limit for artifact packages? When does including the full build environment become impractical?
- How do you handle artifacts that require GPU hardware or large datasets that cannot be vendored?
- Is there a standard format for research artifact packages, or is every conference different?
- How do you version artifact packages when the paper is revised?
