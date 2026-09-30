---
title: "Git for Reproducibility"
tags: [concept, reproducibility-engineering, semester-1, git, version-control, reproducibility]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [git-dag-structure-and-internals, git-commit-hygiene]
---

## One-line Summary
Git provides exact version tracking, provenance documentation, and change history — all essential for building reproduction packages that allow others to verify and replicate research.

## Core Intuition
Reproducibility requires knowing exactly what code was used to produce a result. Git provides this through immutable snapshots (commits), a tamper-evident history chain (the DAG), and attribution metadata (author, committer, trailers). The lecture poses a key question: when building a reproduction package based on an open-source project, what approach should you take?

## Formal Definition / Statement
Three strategies for incorporating upstream code into a reproduction package:

| Strategy | Pros | Cons |
|----------|------|------|
| **Snapshot** (latest code + your changes) | Simple, self-contained | Loses upstream history, hard to merge updates, no provenance |
| **Clone + patches** (clone repo, add changes as patch stack) | Preserves upstream history, patches are reviewable, clear separation | Requires git knowledge, patches may not apply to newer upstream |
| **Fork** (GitHub fork, independent development) | Full history, GitHub integration, PRs back upstream | Maintains fork sync, dependency on hosting platform |

The lecture emphasizes that for research reproducibility, the choice affects how reviewers and future researchers can understand, verify, and build upon the work.

## Key Properties / Complexity
- **Exact versioning**: A commit SHA-1 uniquely identifies the exact state of every file.
- **Provenance**: `git log` documents who changed what, when, and why.
- **Tamper-evident**: Any modification to history changes hashes, making tampering detectable.
- **Shareability**: Repositories can be archived (e.g., Zenodo), forked, and cited.
- **Reversibility**: `git bisect` can find exactly which change introduced a bug.

## Worked Example
Scenario: You use an open-source library for your research and modify it.

**Approach 1 — Snapshot:**
```bash
cp -r library/ my-reproduction-package/library/
# Add your changes, lose all history
```
Reviewer sees: "modified library code" — no context.

**Approach 2 — Clone + patches:**
```bash
git clone https://github.com/org/library.git
cd library
git checkout v2.3.0  # pin to exact version
# Apply your changes as a patch series
git format-patch HEAD..my-changes -o patches/
```
Reviewer sees: upstream at v2.3.0 + exactly N patches with clear descriptions.

**Approach 3 — Fork:**
```bash
# Fork on GitHub, clone your fork
git clone https://github.com/yourname/library.git
# Make commits, push to your fork
# Cite: "Forked from org/library at commit abc123"
```
Reviewer sees: full history, your changes as commits, link to upstream.

## Common Pitfalls
- **Not pinning versions**: Using "latest" is non-reproducible; pin to a commit, tag, or release.
- **Losing upstream context**: Snapshots lose the "why" of upstream decisions.
- **Fork divergence**: Forgetting to sync with upstream makes merging difficult later.
- **No .gitignore**: Accidentally committing build artifacts, credentials, or large data files.

## Connections
- [[git-dag-structure-and-internals]] — the foundation of exact versioning
- [[git-commit-hygiene]] — clean history aids review of reproduction packages
- [[developer-certificate-of-origin]] — provenance and attribution for contributed code
- [[gitignore-and-gitattributes]] — controlling what gets tracked
- [[computational-reproducibility-in-ml]] — ML-specific reproducibility challenges
- [[data-provenance]] — code provenance is one part of full provenance tracking

## Open Questions
- Should reproduction packages be archived as git repositories (e.g., via Zenodo + GitHub integration)?
- How do containerized environments (Docker) interact with git-based reproducibility?
- What role do lock files and dependency pinning play alongside git-based reproducibility?
