---
title: "Graph Representations"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [graph-fundamentals]
---

## One-line Summary
Graphs can be stored as edge lists, adjacency lists, or adjacency matrices — each encoding the same structure but supporting different operations and scales.

## Core Intuition
The same graph can be written down in multiple ways. An edge list is compact and easy to exchange. An adjacency list stores neighbors directly, making traversal fast. An adjacency matrix enables constant-time edge lookup and algebraic operations. The choice depends on what operations you need and how [[sparse-dense-and-random-graphs|sparse]] the graph is.

## Formal Definition / Statement
For a graph G = (V, E):
- **Edge list**: A list of all edges, e.g., [(u₁,v₁), (u₁,v₂), ...]
- **Adjacency list**: For each node, a list of its neighbors, e.g., {u₁: [v₁, v₂], u₂: [v₂], ...}
- **Adjacency matrix**: An |V|×|V| matrix A where A[i][j] = 1 if (i,j) ∈ E, else 0

## ==Key Properties==

| Representation   | Strength                                                                                                                        | Limitation                                  | Best use cases                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------ |
| Edge list        | Lean, simple, good for import/export                                                                                            | Slow to test whether a specific edge exists | Kruskal's MST, I/O, Streaming  |
| Adjacency list   | Best default for [[breadth-first-search|BFS]]/[[depth-first-search|DFS]] on [[sparse-dense-and-random-graphs|sparse]] graphs | Less convenient for matrix-based methods    | BFS/DFS, Sparse Graphs         |
| Adjacency matrix | Fast edge lookup (O(1)), linear algebra friendly                                                                                | Uses O(\|V\|²) space even for sparse graphs | Dense Graphs, Matrix Ops, GNNs |
![[Pasted image 20260623144601.png]]![[Pasted image 20260623144321.png|383]]![[Pasted image 20260623144712.png]]
- For undirected graphs, the adjacency matrix is symmetric: A[i][j] = A[j][i]
- For directed graphs, the adjacency matrix is generally not symmetric
- Edge lists are natural for tabular data and import/export
- Adjacency lists are the default choice for most graph traversal algorithms

## Worked Example
ARPANET (1970) adjacency list:
```
SRI:    [UCSB, UCLA, Stanford, UTAH]
UCSB:   [SRI, UCLA]
UCLA:   [SRI, UCSB, RAND, Stanford]
RAND:   [UCLA, BBN, SDC]
SDC:    [RAND, UTAH]
Stanford: [SRI, UCLA]
Utah:   [SRI, SDC, MIT]
...
```
This compact representation makes neighbor lookup O(1) per node — ideal for [[breadth-first-search|BFS]] traversal.

## Common Pitfalls
- Using an adjacency matrix for a sparse graph with millions of nodes — it wastes O(|V|²) space
- Using an edge list when you need frequent neighbor lookups — each lookup requires scanning the entire list
- Forgetting that undirected edges must be stored symmetrically in an adjacency list (both u→v and v→u)

## Connections
- [[graph-fundamentals]] — representations encode the same G = (V, E)
- [[sparse-dense-and-random-graphs]] — density determines which representation is efficient
- [[breadth-first-search]] — BFS typically uses adjacency lists
- [[depth-first-search]] — DFS typically uses adjacency lists
- [[neighbourhood-and-degree]] — adjacency list directly stores N(v)

## Open Questions
- How do modern graph databases choose between these representations?
- What hybrid representations exist for very large-scale graphs (e.g., compressed sparse row)?
