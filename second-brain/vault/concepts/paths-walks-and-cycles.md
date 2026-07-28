---
title: "Paths, Walks, and Cycles"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [graph-fundamentals, directed-and-undirected-graphs]
---

## One-line Summary
A walk is any sequence of connected vertices (repeats allowed); a path requires all vertices distinct; a cycle is a closed walk returning to the start.

## Core Intuition
These three concepts form a hierarchy of strictness. **Walks are the most permissive (you can revisit nodes and edges)**, **paths are stricter (no revisiting)**, and **cycles are paths that loop back**. This hierarchy matters because different algorithms and properties rely on different levels: **reachability needs walks**, **shortest distances need paths**, and **cycle detection needs cycles**.

## Formal Definition / Statement
- **Walk** of length k: a sequence v₀, v₁, …, vₖ where (v_{i-1}, vᵢ) ∈ E for all i. Vertices and edges may be repeated.
- **Path** (simple path): a walk where all vertices are distinct — vᵢ ≠ vⱼ for i ≠ j.
- **Cycle**: a walk v₀, v₁, …, vₖ with v₀ = vₖ and all intermediate vertices distinct.

In [[directed-and-undirected-graphs|undirected graphs]], an edge can be traversed in either direction. In directed graphs, each step must follow the edge direction.

## Key Properties / Complexity
- Every path is a walk, but not every walk is a path
- Every cycle contains a path (the cycle minus the repeated endpoint)
- Path length = number of edges traversed
- In [[weighted-graphs|weighted graphs]], path length = Σ w(v_{i-1}, vᵢ)
- Cycles are fundamental for detecting feedback loops, deadlock, and circular dependencies

## Worked Example
Graph: A-B, B-C, C-D, D-A, A-C

- **Walk**: A → B → C → B → D (B is visited twice — valid walk!)
- **Path**: A → B → C → D (each vertex appears exactly once)
- **Cycle**: A → B → C → A (returns to start, no repeated intermediate vertex)

## Common Pitfalls
- Confusing "path" with "walk" — many theorems require simple paths (no repeated vertices), not just any walk
- Forgetting that in directed graphs, you can only follow edge direction
- Assuming a cycle must visit every node — a cycle can involve just a subset of vertices

## Connections
- [[graph-fundamentals]] — paths are built on the basic graph structure
- [[directed-and-undirected-graphs]] — direction affects which walks/paths are valid
- [[weighted-graphs]] — weighted path length
- [[shortest-path-and-diameter]] — shortest path is the minimum-length path
- [[eulerian-path-and-circuit]] — paths/cycles that traverse every edge
- [[depth-first-search]] — DFS is the standard tool for cycle detection

## Open Questions
- How many distinct paths exist between two nodes in a large graph?
- What is the relationship between cycles and network robustness?
