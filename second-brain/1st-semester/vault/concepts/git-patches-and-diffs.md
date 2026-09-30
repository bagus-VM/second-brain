---
title: "Git Patches and Diffs"
tags: [concept, reproducibility-engineering, semester-1, git, version-control]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [git-dag-structure-and-internals]
---

## One-line Summary
A patch (diff) is a structured text representation of changes between two snapshots, consisting of metadata headers and hunk-based change descriptions.

## Core Intuition
When you run `git log -p` or `git diff`, Git computes the difference between two snapshots and formats it as a human-readable (and machine-parseable) patch. The unified diff format shows context lines around each change, with `-` for removals and `+` for additions. This is the fundamental unit of code review, code sharing, and — critically for reproducibility — documenting exactly what changed between versions.

## Formal Definition / Statement
A patch in unified diff format consists of:

```
diff --git a/<path> b/<path>      # Git header (a=source, b=target)
index <blob-hash-a>..<blob-hash-b> <mode>  # blob references and file mode
--- a/<path>                        # source file
+++ b/<path>                        # target file
@@ -<start>,<count> +<start>,<count> @@  # hunk header
 context line                       # unchanged
-removed line                       # deletion
+added line                         # addition
```

**Metadata block** (for commits):
- `commit:` — full SHA-1 hash
- `Author:` — name and email
- `Date:` — timestamp
- Commit message body
- Trailers (`Signed-off-by:`, etc.)

## Key Properties / Complexity
- **Self-contained**: A patch contains enough information to apply the change to the correct file at the correct location.
- **Context-dependent**: Surrounding context lines (default 3) help locate where to apply changes, even if line numbers shift.
- **Composable**: Multiple hunks can represent changes across a file; multiple file diffs can be in one patch.
- **Portable**: Patches can be emailed, stored as files, and applied with `git apply` or `patch`.

## Worked Example
From the lecture, `git log -p` shows:

```diff
commit 32367d76530da8fe77922aa905931ccf1fbd7524
Author: Rosemary Berry <headchef@80s-diner.com>
Date:   Wed Mar 17 10:28:12 2021 -0400

add punch

diff --git a/saucy.md b/saucy.md
index 20b7e5a..8d49c34 100644
--- a/saucy.md
+++ b/saucy.md
@@ -6,8 +6,8 @@
 2 cups - Chopped cilantro
 1/4 cup - Olive oil
 1/4 cup - Lime juice
-1 pinch - Salt
-1 - Jalapeno, deseeded
+2 pinches - Salt
+2 - Jalapenos, deseeded
 ## Instructions
-Add all ingredients to a blender. Mix until smooth.
+Add all ingredients to a blender. Mix until desired consistency.
```

Reading this patch: the commit "add punch" changed salt from 1 pinch to 2 pinches, doubled the jalapenos, and adjusted the blending instruction. Each `-`/`+` pair shows the before/after.

## Common Pitfalls
- **Applying patches out of order**: Context may not match if the file has changed since the patch was generated.
- **Binary files**: Patches cannot represent binary content meaningfully; Git uses `Binary files differ` stubs.
- **Line ending issues**: CRLF vs LF mismatches can cause patch application failures.

## Connections
- [[git-dag-structure-and-internals]] — patches are derived from comparing snapshots in the DAG
- [[git-commit-hygiene]] — clean commits produce clean, reviewable patches
- [[developer-certificate-of-origin]] — metadata in commit patches includes trailers
- [[git-for-reproducibility]] — patches can be shared as reproduction artifacts

## Open Questions
- How do `git format-patch` and `git send-email` workflows compare to pull requests for code review?
- What are the limitations of patch-based workflows for large-scale changes?
