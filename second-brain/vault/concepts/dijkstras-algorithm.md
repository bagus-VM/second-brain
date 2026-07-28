---
title: "Dijkstra's Algorithm"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [breadth-first-search, weighted-graphs, shortest-path-and-diameter]
---

## One-line Summary
Dijkstra's algorithm finds shortest paths in weighted graphs with non-negative edge costs using a priority queue, **always expanding the currently cheapest unvisited node.**

## Core Intuition
[[breadth-first-search|BFS]] explores layer by layer because all edges cost the same. But when edges have different weights, we need to be smarter: always process the node with the smallest accumulated distance first. This greedy strategy works because with non-negative weights, once a node is settled, no cheaper path to it can appear later.

## Formal Definition / Statement
**Algorithm: Dijkstra** (Input: Graph G = (V, E), source s, additive weights w ≥ 0)
1. Set distance to s as 0 and all others as ∞
2. Initialize a priority queue PQ with all nodes
3. While PQ is not empty:
   - Extract node u with the minimum distance
   - For each neighbour v of u:
     - If path through u is shorter: update v's distance

**Complexity**: O((|V| + |E|) log |V|) with a min-heap priority queue.

## Key Properties / Complexity
- Uses a **priority queue (min-heap)** instead of a simple queue
- Always expands the cheapest unvisited node — greedy strategy
- Guarantees shortest paths when all edge weights are **non-negative**
- **Breaks with negative weights**: a later detour can make an already-settled node cheaper
- Extends [[breadth-first-search|BFS]] logic to [[weighted-graphs|weighted networks]]
- Priority queue: instead of FIFO, the node with the shortest accumulated distance is extracted next

## Worked Example
Graph: S→A(2), S→C(5), A→B(3), C→B(-10)

With Dijkstra (treating as non-negative):
1. Settle S (d=0), update A(d=2), C(d=5)
2. Settle A (d=2), update B(d=5)
3. Settle B (d=5) — WRONG! Path S→C→B has cost 5+(-10) = -5

This shows why negative weights break Dijkstra: B was settled with d=5, but the true shortest path has cost -5.

Correct approach for negative weights: Bellman-Ford algorithm (covered in later lectures).

## Common Pitfalls
- Applying Dijkstra with negative edge weights — the greedy assumption breaks
- Confusing Dijkstra with [[breadth-first-search|BFS]] — BFS is for unweighted graphs, Dijkstra for weighted
- Forgetting that Dijkstra requires **additive** weights — the cost of a path is the sum of edge weights
- Using Dijkstra when you only need unweighted shortest paths — BFS is simpler and faster

## Connections
- [[breadth-first-search]] — Dijkstra generalizes BFS to weighted graphs
- [[weighted-graphs]] — Dijkstra operates on weighted graphs
- [[shortest-path-and-diameter]] — Dijkstra computes shortest path distances
- [[directed-and-undirected-graphs]] — Dijkstra works on both directed and undirected weighted graphs

## Open Questions
- What algorithm handles negative edge weights? (Bellman-Ford, covered later)
- How does Dijkstra relate to A* search with heuristics?
- What are the practical optimizations for Dijkstra on very large graphs?
