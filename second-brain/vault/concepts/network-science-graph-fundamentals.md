---
title: "Graph Fundamentals"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
A graph is a collection of dots (nodes) connected by lines (edges) — the simplest way to describe relationships between things.

## Core Intuition
Graphs exist because reality is full of relationships, and we need a language for them. A social network is people connected by friendships. The internet is routers connected by cables. A molecule is atoms connected by bonds. The power of graph theory is that the *same mathematics* applies to all of these — once you abstract away what the nodes and edges "really" are, you can apply a vast toolkit of structural analysis. The choice of graph model (directed vs. undirected, weighted vs. unweighted, simple vs. multigraph) is itself a modeling decision that determines what questions you can ask.

## Formal Definition / Statement

A **graph** is a pair G = (V, E) where:
- V is a finite set of **vertices** (nodes, points)
- E ⊆ V × V is a set of **edges** (links, arcs)

Variants:
- **Undirected**: edges are unordered pairs {u, v}; adjacency is symmetric
- **Directed** (digraph): edges are ordered pairs (u, v); adjacency is asymmetric
- **Weighted**: each edge carries a real-valued weight w: E → ℝ
- **Simple**: no self-loops, at most one edge per pair
- **Multigraph**: multiple edges between the same pair allowed

The **adjacency matrix** A is an |V| × |V| matrix where A[i][j] = 1 (or w(i,j)) iff edge (i,j) ∈ E. For undirected graphs, A is symmetric.

The **degree** of a node v, denoted deg(v), is the number of edges incident to v. For directed graphs: in-degree (edges coming in) and out-degree (edges going out).

A **path** is a sequence of distinct nodes v₁, v₂, ..., vₖ where each consecutive pair is connected by an edge. A **walk** allows repeated nodes. A **cycle** is a walk that starts and ends at the same node with no other repetitions.

A graph is **connected** if there exists a path between every pair of nodes.

## Key Properties / Complexity

- Handshaking lemma: Σ deg(v) = 2|E| — every edge contributes to exactly two degrees
- Maximum edges in a simple graph: |V|(|V|-1)/2 (undirected) or |V|(|V|-1) (directed)
- Adjacency matrix storage: O(|V|²) space; adjacency list: O(|V| + |E|) space
- Checking connectivity: O(|V| + |E|) via BFS or DFS
- A tree is a connected acyclic graph with exactly |V| - 1 edges
- The complement graph has an edge iff the original does not
- Bipartite graphs have no odd-length cycles (König's theorem)

## Worked Example

Consider a graph of 4 people and their friendships (undirected):
- V = {Alice, Bob, Carol, Dave}
- E = {{Alice, Bob}, {Bob, Carol}, {Carol, Dave}, {Alice, Carol}}

Degrees: Alice=2, Bob=2, Carol=3, Dave=1. Total edges = 4. Check: 2+2+3+1 = 8 = 2×4 ✓

Adjacency matrix:
```
       Alice  Bob  Carol  Dave
Alice    0     1     1     0
Bob      1     0     1     0
Carol    1     1     0     1
Dave     0     0     1     0
```

The graph is connected (every node reachable from every other). There is a path Alice→Bob→Carol→Dave of length 3.

## Common Pitfalls

- Confusing **paths** with **walks**: paths require distinct nodes; walks can repeat
- Assuming symmetry in directed graphs — in-degree ≠ out-degree in general
- Using adjacency matrices for sparse graphs — wastes O(|V|²) space when |E| << |V|²
- Forgetting that "graph" in CS means something different from "graph of a function" in calculus
- Treating multigraph degree counting the same as simple graphs (multi-edges contribute multiple counts)
- Confusing **connected** with **strongly connected** — the latter requires directed paths in both directions

## Connections

- [[edge-types]] — the modeling choices for edges (directed, weighted, signed)
- [[network-intro]] — graphs as the mathematical model for networks
- [[graph-representations]] — adjacency matrix vs. adjacency list trade-offs
- [[neighbourhood-and-degree]] — degree as the most basic node property
- [[connected-component]] — maximal connected subgraphs
- [[paths-walks-and-cycles]] — formal definitions of traversal
- [[network-science-l01]] — first lecture motivation for graph modeling

## Open Questions

- How does the choice of graph model (simple vs. multigraph, weighted vs. unweighted) affect which analyses are valid?
- When is the adjacency matrix preferable to adjacency lists, and vice versa?
- How do graph properties change when we move from static to dynamic (time-evolving) graphs?
