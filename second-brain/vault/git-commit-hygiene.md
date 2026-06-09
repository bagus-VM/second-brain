---
title: "Git Commit Hygiene"
tags: [concept, reproducibility-engineering, semester-1, git, version-control]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [git-dag-structure-and-internals]
---

## One-line Summary
Commit hygiene means writing atomic, well-messaged commits that each represent a single logical change, making history readable and bisectable.

## Core Intuition
From the lecture: Norm committed incomplete, broken code ("wip: halfway done, then fixed a bug") because he treated commits as save points rather than logical units. His project manager was not amused. The lesson: each commit should compile, pass tests, and represent one coherent idea. Commit messages should explain *why* the change was made, not just *what* changed.

## Formal Definition / Statement
Good commit hygiene follows conventions:

**Commit structure:**
1. Subject line: imperative mood, ≤50 chars, no period
2. Blank line
3. Body: wrapped at 72 chars, explains *what* and *why*

**Atomicity:**
- Each commit does one thing
- Each commit leaves the repository in a working state (compiles, tests pass)
- Separate concerns: bug fix vs. feature vs. refactor

**The trailer block** (at the end of the message):
- `Signed-off-by:` — [[developer-certificate-of-origin|DCO]]
- `Reviewed-by:` — code review attribution
- `Tested-by:` — testing attribution
- `Co-authored-by:` — multi-author attribution

## Key Properties
- **Bisectable**: Atomic commits enable `git bisect` to find the exact commit that introduced a bug.
- **Revertible**: A single logical change can be reverted cleanly.
- **Readable**: Good messages make `git log --oneline` a useful overview.
- **Traceable**: Trailers link commits to reviews, tests, and responsibility chains.

## Worked Example
Bad (Norm's approach):
```
wip: halfway done with the feature
fix the bug I just introduced
```

Good:
```
Implement user authentication with JWT tokens

Add login endpoint and token validation middleware.
Separate auth logic from route handlers for testability.

Signed-off-by: Norm <norm@company.com>
Reviewed-by: Manager <manager@company.com>
```

From the lecture exercise: The `LabSession2` repo had development noise that needed cleanup:
```
"Kick-Off a new project..."     ← good: project setup
"Add code proper"               ← good: core implementation
"Add build infrastructure"      ← good: build system
"fixup: Actually improve code quality"    ← should be squashed
"fixup: Ensure that build system..."      ← should be squashed
```

After interactive rebase: 3 clean commits instead of 5 messy ones.

## Common Pitfalls
- **"WIP" commits in main**: Never push work-in-progress to shared branches.
- **Mega commits**: Combining unrelated changes makes review and bisection impossible.
- **Vague messages**: "fixed stuff" or "updates" provide no useful information.
- **Missing trailers**: In academic/oss contexts, missing `Signed-off-by` violates contribution norms.

## Connections
- [[git-rebasing-and-history-rewriting]] — interactive rebase is the primary tool for enforcing commit hygiene
- [[git-dag-structure-and-internals]] — commits are nodes in the DAG
- [[developer-certificate-of-origin]] — the `Signed-off-by` trailer
- [[git-patches-and-diffs]] — each commit is a self-contained diff
- [[git-for-reproducibility]] — clean history aids reproduction

## Open Questions
- How do different projects enforce commit message conventions (commitlint, CI checks)?
- Should fixup/squash commits be used in feature branches before merging?
