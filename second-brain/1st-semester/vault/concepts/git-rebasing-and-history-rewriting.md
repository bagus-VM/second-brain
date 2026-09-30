---
title: "Git Rebasing and History Rewriting"
tags: [concept, reproducibility-engineering, semester-1, git, version-control]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [git-dag-structure-and-internals, git-branching-and-merging]
---

## One-line Summary
Rebasing replays commits onto a new base to create a linear history; interactive rebase lets you squash, reorder, edit, or drop commits to clean up messy development history.

## Core Intuition
During development, you often accumulate messy commits: "WIP", "fix typo", "oops forgot a file". Interactive rebase (`git rebase -i`) lets you rewrite this history before sharing it. It replays your commits one by one on top of a new base, giving you the chance to squash (combine), reorder, reword, or drop commits. The result is a clean, linear history that tells a coherent story — the history you *wish* you had written, not the one you actually wrote.

## Formal Definition / Statement
- **Rebase**: Given a branch diverging from a common ancestor C, rebasing onto branch B replays each commit (C+1, C+2, ..., tip) as new commits on top of B. Original commits are abandoned; new commits have different SHA-1s.
- **Interactive rebase** (`git rebase -i <base>`): Opens an editor listing commits with actions:
  - `pick` — keep commit as-is
  - `reword` — keep changes, edit message
  - `edit` — pause to amend
  - `squash` — meld into previous commit
  - `fixup` — like squash, discard this commit's message
  - `drop` — remove commit entirely
  - Reorder lines to change commit order
- **`--autosquash`**: Automatically arranges `fixup!` and `squash!` prefixed commits next to their targets.

## Key Properties / Complexity
- **Rewrites history**: All replayed commits get new SHA-1s. Never rebase commits that others have already pulled.
- **Linearizes history**: Removes merge commits, creating a straight line.
- **Atomic presentation**: Development noise (fixes, WIPs) can be consolidated into meaningful commits.
- **`--autosquash` for workflow**: Create fixup commits during development (`git commit --fixup=<hash>`), then squash them all in one interactive rebase.

## Worked Example
Starting history (messed up):
```
A ← B ← C ← D ← E
  "init" "add code" "fix typo" "fix build" "WIP"
```

Run `git rebase -i A`:
```
pick B "add code"
squash C "fix typo"       ← meld into B
squash D "fix build"       ← meld into B
pick E "WIP" → reword E   ← clean up message
```

Result:
```
A ← B' "Add code with proper build and tests"
```

From the lecture: The `LabSession2` repository had fixup commits after initial work. Using `git rebase -i` with `--autosquash`, fixup commits like "fixup: Actually improve code quality" and "fixup: Ensure that build system sets highest standards" can be folded into their target commits to present a clean history.

## Common Pitfalls
- **Rebasing published commits**: If others have based work on your commits, rebasing forces them to deal with divergent histories. Golden rule: don't rebase shared commits.
- **Losing work**: Dropped commits vanish from the branch (but remain in the reflog for ~90 days).
- **Merge commit rebase complexity**: `git rebase` skips merge commits by default; use `--rebase-merges` to preserve branch structure.

## Connections
- [[git-dag-structure-and-internals]] — rebase creates new commit objects (new SHA-1s)
- [[git-branching-and-merging]] — alternative to merge for combining branches
- [[git-commit-hygiene]] — interactive rebase is the tool for enforcing commit hygiene
- [[git-patches-and-diffs]] — each replayed commit produces a new diff

## Open Questions
- How does rebasing affect signed commits (GPG signatures become invalid)?
- When is it better to preserve messy history vs. rewriting it for clarity?
