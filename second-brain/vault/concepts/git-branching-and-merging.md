---
title: "Git Branching and Merging"
tags: [concept, reproducibility-engineering, semester-1, git, version-control]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [git-dag-structure-and-internals]
---

## One-line Summary
A branch is a lightweight, movable pointer to a commit in the [[git-dag-structure-and-internals|DAG]]; merging combines divergent branches by creating a new commit with multiple parents.

## Core Intuition
In Git, branching is cheap because a branch is just a 41-byte file containing a commit SHA-1. Creating a branch doesn't copy any data — it simply adds a new pointer into the DAG. When you commit on a branch, the pointer advances. Merging two branches finds the common ancestor and applies changes from both sides, producing a merge commit with two (or more) parents that preserves the full history of both branches.

## Formal Definition / Statement
- **Branch**: A named reference (ref) in `.git/refs/heads/<name>` that points to a commit object. Moving HEAD to a branch makes it the "current branch."
- **Fast-forward merge**: If the target branch is an ancestor of the source branch, Git simply moves the target pointer forward — no new commit is created.
- **Three-way merge**: Git finds the merge base (most recent common ancestor), computes diffs from base to each branch tip, and applies both sets of changes. If conflicts exist, the user must resolve them manually. The result is a merge commit with two parents.

## Key Properties
- **Cheap creation**: Creating a branch is O(1) — just write a file.
- **Isolation**: Changes on one branch don't affect others until merged.
- **Non-destructive merging**: Merge commits preserve the complete history of both branches.
- **Merge base matters**: The three-way merge algorithm depends on finding the correct common ancestor; this is why rebasing can cause issues.
- **Fast-forward vs. true merge**: Fast-forward is possible when no divergent commits exist; otherwise Git creates a merge commit.

## Worked Example
```
      C3 ← C4 (feature)
     /
C1 ← C2 ← C5 (main)
```

After `git checkout main && git merge feature`:
```
      C3 ← C4
     /         \
C1 ← C2 ← C5 ← M (main)
```
M is the merge commit with parents C5 and C4.

If main hadn't advanced (no C5), Git would fast-forward:
```
C1 ← C2 ← C3 ← C4 (main, feature)
```

## Common Pitfalls
- **Confusing merge and rebase**: Merge preserves history; rebase rewrites it. Both have legitimate uses.
- **Merge conflicts**: When both branches modify the same lines, Git cannot auto-merge. Manual resolution is required.
- **Recursive merge strategy**: With multiple merge bases, Git creates a temporary merge of the bases, then uses that as the base — this can produce surprising results.

## Connections
- [[git-dag-structure-and-internals]] — branches are pointers in the DAG
- [[git-rebasing-and-history-rewriting]] — alternative to merging for linearizing history
- [[git-commit-hygiene]] — how to structure work across branches
- [[git-for-reproducibility]] — branching strategies for reproduction packages

## Open Questions
- When should you prefer merge commits over rebasing in a collaborative workflow?
- How do merge strategies (octopus, ours, subtree) affect reproducibility?
