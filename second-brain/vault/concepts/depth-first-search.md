---
title: "Depth-First Search"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [graph-fundamentals, graph-representations, paths-walks-and-cycles]
---

## One-line Summary
DFS explores a graph by going as deep as possible along each branch before backtracking, using a LIFO stack with O(|V|+|E|) complexity.

## Core Intuition
DFS is like exploring a maze: **pick a path and keep going until you hit a dead end, then backtrack to the last junction with unexplored exits**. This "deep first, wide later" strategy is useful for structural exploration — finding cycles, determining reachability, and topological sorting — **but it does NOT guarantee shortest paths.**

## Formal Definition / Statement
**Algorithm: DFS** (Input: Graph G = (V, E), source node s)
1. Initialize a stack S and add s
2. While S is not empty:
   - Pop current node u from the top of S
   - If u is not visited:
     - Mark u as visited
     - Push all neighbours of u onto the stack S

## Key Properties / Complexity
- Uses a LIFO (Last-In, First-Out) stack (or recursion)
- Explores deep before wide — can wander far across the network
- Runs in **O(|V| + |E|)** time
- **Does NOT guarantee shortest paths** — finds any path, not the shortest
- Standard for finding **cycles**, **reachability**, and **topological sorting**
- Can be used to find [[connectivity-and-components|connected components]]
- Discovery order depends on the order neighbours are processed

## Worked Example
DFS on ARPANET starting from UCLA:
- Discovery order (assuming adjacency-list order): UCLA(0), SRI(1), UCSB(2), Stanford(3), UTAH(4), SDC(5), RAND(6), BBN(7), MIT(8), Lincoln(9), CASE(10), Harvard(11), Carnegie(12)
- Notice how DFS wanders far (to Utah and Illinois) before exploring nodes close to the start

Python implementation:
```python
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph.get(start, []):
        if node not in path:
            result = find_path(graph, node, end, path)
            if result is not None:
                return result
    return None
```

## Common Pitfalls
- Using DFS to find shortest paths — DFS finds any path, not necessarily the shortest
- Confusing DFS with [[breadth-first-search|BFS]] — DFS uses a stack (LIFO), BFS uses a queue (FIFO)
- Forgetting that DFS's path depends on neighbour processing order — different orderings can yield different paths

## Connections
- [[breadth-first-search]] — the complementary traversal strategy (BFS vs DFS comparison table)
- [[paths-walks-and-cycles]] — DFS finds paths and can detect cycles
- [[connectivity-and-components]] — DFS can find connected components
- [[graph-representations]] — DFS typically uses adjacency lists

## Open Questions
- When should DFS be preferred over BFS in practice?
- How does DFS relate to recursive graph algorithms and dynamic programming on graphs?
