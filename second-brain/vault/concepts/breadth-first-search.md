---
title: "Breadth-First Search"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [graph-fundamentals, graph-representations, paths-walks-and-cycles]
---

## One-line Summary
BFS explores a graph layer by layer using a FIFO queue, guaranteeing shortest paths in unweighted graphs with O(|V|+|E|) complexity.

## Core Intuition
==BFS is like dropping a stone in water: ripples expand outward one layer at a time==. Starting from a source node, BFS first visits all direct neighbors (layer 1), then all their unvisited neighbors (layer 2), and so on. Because it processes nodes in FIFO order, the first time it reaches a node, it has found the shortest path to that node.

## Formal Definition / Statement
**Algorithm: BFS** (Input: Graph G = (V, E), source node s)
1. Initialize a queue Q and add s
2. Mark s as visited
3. While Q is not empty:
   - Extract current node u from the front of Q
   - For each neighbor v of u: if v is not visited, mark v as visited and add v to the back of Q

## Key Properties
- Uses a FIFO (First-In, First-Out) queue
- Discovers nodes strictly layer by layer
- Runs in **O(|V| + |E|)** time — each vertex and edge visited at most once
- Guarantees **shortest paths** in unweighted graphs
- Works identically on [[directed-and-undirected-graphs|directed graphs]] — follows edges in their given direction
- Does **NOT** give shortest paths in [[weighted-graphs|weighted graphs]] — use [[dijkstras-algorithm|Dijkstra]] instead
- Can be used to find [[connectivity-and-components|connected components]]

## Worked Example
BFS on ARPANET starting from UCLA:
- Layer 0: UCLA
- Layer 1: SRI, UCSB, RAND, Stanford
- Layer 2: UTAH, BBN, SDC
- Layer 3: MIT, CASE
- Layer 4: Harvard, Carnegie
- Layer 5: Lincoln

Each layer represents nodes at distance exactly k from UCLA.

Python implementation:
```python
from collections import deque

def bfs(graph, start):
    distances = {start: 0}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in graph.get(current, []):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    return distances
```

## Common Pitfalls
- Using BFS for shortest paths in weighted graphs — BFS treats all edges equally
- Confusing BFS with [[depth-first-search|DFS]] — BFS uses a queue (FIFO), DFS uses a stack (LIFO)
- Assuming BFS builds a tree — a true BFS tree has exactly one parent per node; drawing all shortest-path edges creates a "level graph", not a spanning tree

## Connections
- [[depth-first-search]] — the complementary traversal strategy
- [[dijkstras-algorithm]] — extends BFS logic to weighted graphs
- [[shortest-path-and-diameter]] — BFS computes shortest paths and can determine diameter
- [[connectivity-and-components]] — BFS can find connected components
- [[graph-representations]] — BFS typically uses adjacency lists

## Open Questions
- How does BFS scale to graphs with billions of nodes?
- What is the relationship between BFS layers and the "small-world" property?
