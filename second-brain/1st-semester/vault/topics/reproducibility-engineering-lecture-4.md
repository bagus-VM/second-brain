---
title: "Reproducibility Engineering — Lecture 4: Git"
tags: [topic, reproducibility-engineering, semester-1, git, version-control]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Lecture 4 covers Git as the fundamental tool for version control and reproducibility: its internal data model, workflow practices, and how to use it to build trustworthy reproduction packages.

## Core Intuition
Git is not just a "save button" for code — it is a content-addressable object store that forms a tamper-evident [[git-dag-structure-and-internals|directed acyclic graph]]. Understanding Git internals (blobs, trees, commits) is essential for using it effectively for reproducibility. The lecture emphasizes that how you structure your git history (commit hygiene, rebasing) and how you document responsibility ([[developer-certificate-of-origin|DCO]]) directly impacts whether your research is verifiable and reproducible.

## Topics Covered

### Git Internals
- [[git-dag-structure-and-internals]] — The four object types (blob, tree, commit, tag), content-addressable storage, SHA-1 hashing, and the DAG structure that makes Git tamper-evident.

### Workflow Practices
- [[git-branching-and-merging]] — Branches as lightweight pointers; fast-forward vs. three-way merges; merge strategies.
- [[git-rebasing-and-history-rewriting]] — Interactive rebase for cleaning up history; squashing fixup commits; rewriting the DAG.
- [[git-commit-hygiene]] — Atomic commits, imperative subject lines, trailer blocks; Norm's cautionary tale of bad commit practices.
- [[gitignore-and-gitattributes]] — Controlling what gets tracked; preventing accidental commits of build artifacts and secrets.

### Documentation and Sharing
- [[git-patches-and-diffs]] — Unified diff format; how patches encode changes; the structure of `git log -p` output.
- [[developer-certificate-of-origin]] — `Signed-off-by` trailers; the trail of responsibility from author through reviewer to tester.

### Reproducibility
- [[git-for-reproducibility]] — Three strategies for incorporating upstream code (snapshot, clone+patches, fork); pinning versions; building reproduction packages with full provenance.

## Connections to Other Lectures
- [[reproducibility-engineering-lecture-1]] — Foundational concepts that Git-based reproducibility builds upon
- [[reproducibility-engineering-lecture-2]] — Broader reproducibility framework
- [[reproducibility-engineering-lecture-3]] — Prior lecture topics
- [[data-provenance]] — Code provenance via Git is one dimension of full provenance tracking
- [[computational-reproducibility-in-ml]] — ML reproducibility often requires git + containers + dependency pinning

## Key Takeaways for the Exam
1. Git stores **snapshots** (not diffs) as objects in a DAG; branches are just pointers.
2. **Commit hygiene**: atomic commits, good messages, trailer blocks (Signed-off-by, Reviewed-by).
3. **Interactive rebase** (`git rebase -i`) cleans up messy development history before sharing.
4. **DCO** (`git commit -s`) certifies contribution rights — lightweight alternative to CLAs.
5. Three strategies for reproduction packages: snapshot, clone+patches, fork — each with tradeoffs.
6. `.gitignore` is essential for keeping repositories clean; it does NOT untrack already-committed files.
7. Patches are structured diffs with metadata — portable, reviewable, and self-documenting.

## Open Questions
- How do modern platforms (GitHub, GitLab) change the patch/email workflow?
- What is the role of containerization alongside Git for full reproducibility?
- How does Git interact with data versioning tools (DVC, Git LFS)?
