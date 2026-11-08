---
title: "Shortest Path and Diameter"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [paths-walks-and-cycles, graph-fundamentals]
---

## One-line Summary
The shortest path dist(u,v) **is the minimum number of edges between two nodes**; the diameter is the longest shortest path in the entire graph.

## Core Intuition
Distance in a graph is not about physical space — it's about the minimum number of steps (edges) needed to get from one node to another. The diameter captures the "worst case" distance: how far apart are the most distant nodes? This tells us how "big" a network feels from the inside.

## Formal Definition / Statement
- **Path length**: The length of a path v₀, …, vₖ is k (number of edges). In a [[weighted-graphs|weighted graph]]: Σ w(v_{i-1}, vᵢ)
- **Shortest path**: dist(u, v) = min{k : path of length k from u to v}. If no path exists, dist(u, v) = ∞.
- **Diameter**: diam(G) = max_{u,v ∈ V} dist(u, v) — the longest shortest path in the graph

## Key Properties / Complexity
- In [[directed-and-undirected-graphs|undirected graphs]], dist(u,v) = dist(v,u)
- In directed graphs, dist(u,v) ≠ dist(v,u) in general
- If no path connects u and v, dist(u,v) = ∞
- The diameter is determined by the farthest pair of nodes
- Diameter is sensitive to network structure — removing a single bridge edge can dramatically increase it
- [[breadth-first-search|BFS]] computes shortest paths in unweighted graphs; [[dijkstras-algorithm|Dijkstra]] for weighted graphs

## Worked Example
Graph: A-B, B-C, C-D, D-E, A-C

- dist(A, B) = 1 (direct edge)
- dist(A, C) = 1 (direct edge)
- dist(A, D) = 2 (A→C→D)
- dist(A, E) = 3 (A→C→D→E)
- dist(B, E) = 3 (B→C→D→E)
- diam(G) = 3 (the pair A,E or B,E achieves the maximum)

## Common Pitfalls
- Using [[breadth-first-search|BFS]] for shortest paths in [[weighted-graphs|weighted graphs]] — BFS assumes equal edge weights (**BFS cannot be used to find shortest path in weighted graphs because BFS doesnt calculate the weight meanwhile the weight is used in calculation for the path length of weighted graph**)
- Confusing diameter with the number of nodes — diameter measures steps, not size
- Forgetting that disconnected nodes have infinite distance — this makes the diameter infinite unless restricted to the largest [[connectivity-and-components|component]]

## Connections
- [[paths-walks-and-cycles]] — shortest path is a path with minimum length
- [[breadth-first-search]] — BFS computes shortest paths in unweighted graphs
- [[dijkstras-algorithm]] — Dijkstra computes shortest paths in weighted graphs
- [[connectivity-and-components]] — diameter is often computed within the [[connectivity-and-components|giant component]]
- [[directed-and-undirected-graphs]] — directed graphs have asymmetric distances

## Open Questions
- How does the diameter of real-world networks compare to random graphs of the same size?
- What is the relationship between diameter and network resilience?
