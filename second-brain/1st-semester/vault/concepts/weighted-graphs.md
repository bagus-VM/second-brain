---
title: "Weighted Graphs"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [graph-fundamentals]
---

## One-line Summary
**A weighted graph assigns a numerical value w(e) to each edge, encoding strength, cost, distance, probability, or capacity.**

## Core Intuition
Binary edges (present/absent) are often not enough. A road network needs distances, a communication network needs bandwidth, a social network might need interaction frequency. Weights let edges carry quantitative meaning while preserving the graph topology.

## Formal Definition / Statement
A **weighted graph** G = (V, E, w) is a graph equipped with a weight function w: E → ℝ. The weight w(e) represents a property of edge e such as cost, length, capacity, or probability.

## Key Properties / Complexity
- The same topological structure can mean vastly different things depending on what weights encode
- [[shortest-path-and-diameter|Path length]] in a weighted graph: length = Σ w(v_{i-1}, v_i)
- **[[breadth-first-search|BFS]] does **not** find shortest paths in weighted graphs**
- **[[dijkstras-algorithm|Dijkstra's algorithm]] handles weighted shortest paths** (non-negative additive weights)
- Weights can be combined with [[directed-and-undirected-graphs|direction]] (directed weighted graphs)

## Worked Example
Transport network:
- Nodes: cities
- Edges: roads between cities
- Weights: travel distance in km (or travel time in minutes)
- Shortest path A→B might not be the path with fewest edges, but the one with minimum total weight

## Common Pitfalls
- Using [[breadth-first-search|BFS]] for shortest paths in weighted graphs — BFS assumes all edges have equal cost
- Applying [[dijkstras-algorithm|Dijkstra]] with negative weights — the greedy assumption breaks because a later detour can make an already-settled node cheaper
- Confusing "weight" meaning (cost vs. capacity vs. probability) — the interpretation changes the algorithm choice

## Connections
- [[graph-fundamentals]] — base graph definition
- [[dijkstras-algorithm]] — shortest paths for weighted graphs with non-negative weights
- [[shortest-path-and-diameter]] — weighted path length definition
- [[directed-and-undirected-graphs]] — weights combine with directionality

## Open Questions
- How do we choose between different weight interpretations (distance vs. similarity vs. capacity)?
- What algorithms handle negative edge weights? (Answer: **Bellman-Ford,** covered in later lectures)
