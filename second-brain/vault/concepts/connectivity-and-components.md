---
title: "Connectivity and Components"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [graph-fundamentals, paths-walks-and-cycles, breadth-first-search]
---

## One-line Summary
A graph is connected if every pair of nodes has a path between them; connected components are maximal connected subgraphs, and a giant component dominates many real networks.

## Core Intuition
Connectivity answers the question: "==Is this network still one system, or has it split apart?==" A connected graph means you can get from any node to any other. Connected components partition a disconnected graph into isolated islands. Many real networks have one giant component containing most nodes, plus several small peripheral groups.

## Formal Definition / Statement
- **Connected** (undirected): G is connected if for every pair u, v ∈ V there exists a path from u to v.
- **Connected component**: A subgraph H ⊆ G such that:
  1. H is connected (every pair of vertices in H has a path within H)
  2. H is **maximal** — no vertex outside H has a path to any vertex in H
- **Giant component**: A connected component significantly larger than all others, containing a macroscopic fraction of all vertices.

## Key Properties
- Connected components partition the node set — every node belongs to exactly one component
- A graph with k connected components has no edges between components
- Real-world examples of disconnected components: separate friendship groups, isolated islands in road networks, disconnected subnetworks after link failures
- [[breadth-first-search|BFS]] or [[depth-first-search|DFS]] from an unvisited node finds one full component; repeating finds all
- In [[directed-and-undirected-graphs|directed graphs]], connectivity splits into [[directed-connectivity|strong and weak connectivity]]
- Many real networks have a **giant component** plus small peripheral groups

## Worked Example
Finding connected components with BFS:
```python
def find_components(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            reachable = bfs(graph, node)
            component = set(reachable.keys())
            visited |= component
            components.append(component)
    return components
```

Graph: {A:[B], B:[A,C], C:[B], X:[Y], Y:[X,Z], Z:[Y]}
Result: [{A, B, C}, {X, Y, Z}] — two disconnected components.

## Common Pitfalls
- Confusing "connected" with "has many edges" — a graph can be sparse but connected
- Forgetting that for directed graphs, this finds [[directed-connectivity|weakly connected components]] (WCCs), not strongly connected components (SCCs)
- Assuming a giant component always exists — some networks are fragmented into many small components
- Treating the giant component as "the whole network" — peripheral nodes may be important

## Connections
- [[directed-connectivity]] — strong vs. weak connectivity for directed graphs
- [[breadth-first-search]] — BFS is the standard tool for finding components
- [[depth-first-search]] — DFS also finds components
- [[shortest-path-and-diameter]] — diameter is often computed within the giant component
- [[sparse-dense-and-random-graphs]] — random graph theory predicts when giant components emerge
- [[graph-fundamentals]] — connectivity is a fundamental graph property

## Open Questions
- At what edge density does a giant component emerge in a random graph?
- How does the removal of critical nodes/edges affect connectivity (network resilience)?
