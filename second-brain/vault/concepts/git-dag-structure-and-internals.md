---
title: "Git DAG Structure and Internals"
tags: [concept, reproducibility-engineering, semester-1, git, version-control]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Git stores project history as a [[directed-and-undirected-graphs|directed acyclic graph (DAG]] of immutable objects (blobs, trees, commits), each addressed by a SHA-1 hash.

## Core Intuition
Every time you commit, Git snapshots the entire project state. Rather than storing full copies, Git stores four types of objects in `.git/objects/`: **blobs** (file contents), **trees** (directory listings mapping names to blobs), **commits** (metadata + pointer to root tree + parent commit(s)), and **tags** (annotated pointers). These objects form a DAG — each commit points backward to its parent(s), creating a tamper-evident chain. Because objects are content-addressed (identified by their SHA-1 hash), any change anywhere in history produces a different hash at every affected commit.

## Formal Definition / Statement
A Git repository is a content-addressable object store containing four object types:

| Object | Contains |
|--------|----------|
| **blob** | Raw file content (no filename, no permissions) |
| **tree** | List of (mode, name, SHA-1) entries — maps filenames to blobs or sub-trees |
| **commit** | tree SHA-1, parent commit SHA-1(s), author, committer, message |
| **tag** | Pointer to an object with metadata (for annotated tags) |

The commit history forms a DAG: if commit C has parent P, there is a directed edge C → P. The root commit has no parent. A merge commit has two or more parents.

## Key Properties / Complexity
- **Content-addressable**: Objects are identified by the SHA-1 hash of their content. Identical content always produces the same hash.
- **Immutable**: Once written, objects never change. "Editing" a file creates a new blob; amending a commit creates a new commit object.
- **Snapshots, not diffs**: Each commit stores a complete snapshot via its tree, not a delta. (Packfiles compress this for storage.)
- **Tamper-evident**: Changing any byte in any object changes its hash, which breaks the chain of parent pointers in commits.
- **Branches are just pointers**: A branch is a mutable reference (file in `.git/refs/`) pointing to a commit SHA-1. HEAD points to the current branch.

## Worked Example
Consider a repo with one file `hello.c`. After two commits:

```
Commit A (root)
  tree → T1
    hello.c → B1 (content: "#include <stdio.h>...")
  parent: none

Commit B
  tree → T2
    hello.c → B2 (content: "#include <stdio.h>... return 0;")
  parent: Commit A
```

The DAG: `B → A`. B1 ≠ B2 (different content → different SHA-1). T1 ≠ T2 (different blob hashes in listing). The `main` branch label points to B; HEAD points to `main`.

Running `git log` traverses the DAG backward: `B → A`.

## Common Pitfalls
- **Confusing branches with copies**: Branches are just pointers — they share all existing objects until a divergence occurs.
- **Thinking Git stores diffs per commit**: It stores snapshots. Diffs are computed on the fly.
- **Assuming SHA-1 is collision-proof**: SHA-1 has known collision attacks; Git is migrating to SHA-256.
- **Ignoring the DAG when rebasing**: Rebasing rewrites commit objects (new hashes), creating new nodes even though the content is similar.

## Connections
- [[git-branching-and-merging]] — branches exploit the DAG structure
- [[git-rebasing-and-history-rewriting]] — rewrites the DAG by creating new commit objects
- [[git-patches-and-diffs]] — diffs are derived from comparing snapshots in the DAG
- [[git-commit-hygiene]] — how to structure commits along the DAG
- [[directed-and-undirected-graphs]] — DAG is a specific graph type

## Open Questions
- How does Git handle SHA-1 → SHA-256 migration for existing repositories?
- What is the computational cost of verifying the full object chain in a large repository?
