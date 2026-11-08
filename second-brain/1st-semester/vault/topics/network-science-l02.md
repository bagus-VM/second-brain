---
title: "Network Science L02 — Graph Theory"
tags: [topic, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
lecture: "Lecture 02"
---

## Overview
Lecture 02 introduces the formal language of graph theory as the foundation for network science. It covers graph definitions, representations, traversal algorithms, and connectivity — the essential toolkit for modeling and analyzing any network.

## Core Pages

### Foundations
- [[graph-fundamentals]] — G = (V, E), modeling choices, from reality to graph
- [[directed-and-undirected-graphs]] — symmetric vs. asymmetric relationships
- [[weighted-graphs]] — edges carrying numerical values
- [[bipartite-graphs]] — two disjoint node sets, cross-set edges only
- [[sparse-dense-and-random-graphs]] — quantitative graph differences

### Representation
- [[graph-representations]] — edge list, adjacency list, adjacency matrix
- [[neighbourhood-and-degree]] — N(v), deg(v), handshaking lemma

### Paths and Traversal
- [[paths-walks-and-cycles]] — walk → path → cycle hierarchy
- [[shortest-path-and-diameter]] — dist(u,v), diam(G)
- [[eulerian-path-and-circuit]] — Königsberg bridges, degree parity conditions

### Graph Search
- [[breadth-first-search]] — layer-by-layer, FIFO queue, O(|V|+|E|), guarantee shortest paths in unweighted graph
- [[depth-first-search]] — deep-first, LIFO stack, O(|V|+|E|), determines reachability and sorting, but doesn't guarantee shortest path
- [[dijkstras-algorithm]] — weighted shortest paths, priority queue

### Connectivity
- [[connectivity-and-components]] — connected graphs, components, giant component
- [[directed-connectivity]] — strong vs. weak, SCC, Web bow tie

## Key Takeaways
1. Graph theory provides a precise formal language for describing networks
2. The modeling choice (nodes, edges, direction, weights) determines what you can analyze
3. Three representations (edge list, adjacency list, adjacency matrix) trade off between compactness and query speed
4. BFS guarantees shortest paths in unweighted graphs; Dijkstra extends to weighted graphs with non-negative costs
5. Connected components and giant components reveal whether a network is one system or fragmented

## Reading
Chapter 2 of Easley & Kleinberg (2010): *Networks, Crowds, and Markets* — covers graph theory foundations, paths, BFS, and connectivity.
