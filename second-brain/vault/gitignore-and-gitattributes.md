---
title: "Gitignore and Gitattributes"
tags: [concept, reproducibility-engineering, semester-1, git, version-control, configuration]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [git-dag-structure-and-internals]
---

## One-line Summary
`.gitignore` tells Git which files to exclude from tracking; `.gitattributes` controls how Git handles line endings, diff drivers, and binary files.

## Core Intuition
Not everything in a project directory should be version-controlled. Build artifacts (`*.o`, `*.pyc`), IDE settings (`.vscode/`), credentials (`.env`), and large data files pollute the repository and break reproducibility. `.gitignore` uses glob patterns to tell Git to ignore matching files. From the lecture: the `LabSession2` repo's `.gitignore` contained `hello` (the compiled binary) and `.*` (dotfiles like `.gitignore` itself — though this pattern is aggressive).

## Formal Definition / Statement
**`.gitignore` format:**
```
# Comment
pattern          # ignore files matching pattern
!pattern         # negate: do NOT ignore this pattern
dir/             # trailing slash = only match directories
```

**Pattern matching:**
- `*` — matches anything except `/`
- `?` — matches any single character
- `[abc]` — character class
- `**/` — matches zero or more directories

**Scope:**
- `.gitignore` (repo root) — project-wide rules
- `.gitignore` in subdirectories — scoped to that directory
- `.git/info/exclude` — local rules (not shared)
- `~/.gitignore_global` — personal global rules

**`.gitattributes` format:**
```
*.txt text=auto
*.bin binary
*.py diff=python
```

## Key Properties
- **Prevents accidental commits**: Ignored files are not staged by `git add .`
- **Does not affect already-tracked files**: Adding a tracked file to `.gitignore` does not untrack it. Use `git rm --cached`.
- **Shareable**: Committed `.gitignore` is shared with all collaborators.
- **Layered**: Multiple `.gitignore` files at different levels combine.

## Worked Example
From the lecture's `LabSession2` `.gitignore`:
```gitignore
hello       # compiled binary
.*          # dotfiles (note: this is aggressive — also ignores .gitignore!)
```

A more typical `.gitignore` for a C project:
```gitignore
# Build artifacts
*.o
*.a
hello

# Editor files
.vscode/
*.swp
*~

# OS files
.DS_Store
Thumbs.db

# Environment
.env
```

## Common Pitfalls
- **`.gitignore` doesn't untrack**: If a file was already committed, adding it to `.gitignore` has no effect until you run `git rm --cached <file>`.
- **Overly broad patterns**: `.*` ignores `.gitignore` itself! Be specific.
- **Committing secrets**: `.env` files with API keys or passwords should NEVER be committed. Add them to `.gitignore` before the first commit.
- **Not having a `.gitignore`**: Without one, `git add .` will include everything, including build artifacts and IDE configs.

## Connections
- [[git-for-reproducibility]] — proper `.gitignore` is essential for clean reproduction packages
- [[git-commit-hygiene]] — ignoring irrelevant files keeps commits focused
- [[git-dag-structure-and-internals]] — ignored files are simply never added to the object store

## Open Questions
- How do large file storage solutions (Git LFS) interact with `.gitignore` and reproducibility?
- Should reproduction packages commit everything (including build artifacts) for absolute reproducibility?
