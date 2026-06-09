---
title: "Graph Partitioning"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Graph partitioning divides a graph into a fixed number of balanced clusters — unlike community detection, it requires specifying k in advance and optimizes for balanced cut size.

## Core Intuition
Graph partitioning asks: given a graph and a number k, how do we split it into k balanced clusters that minimize the total cut size? This is different from community detection, which discovers the number of communities automatically.

## Formal Definition / Statement
**Graph partitioning:**
Given a graph G = (V, E) and a number k, find a partition of V into k sets V₁, ..., V_k that minimizes the total cut size while maintaining balanced cluster sizes.

**Methods:**
- [[min-cut-max-flow]]: exact for k=2, but minimizes raw cut size
- [[kernighan-lin-algorithm]]: local search for balanced partition
- [[spectral-partitioning]]: uses Laplacian eigenvectors

**Difference from community detection:**
- Partitioning: fixed k, balanced clusters, minimize cut size
- Community detection: discover k, optimize [[modularity]] or [[conductance]]

## Key Properties
1. **Fixed k**: must specify the number of clusters in advance
2. **Balanced clusters**: optimizes for equal-sized partitions
3. **Cut-based objective**: minimizes edges between clusters
4. **Polynomial time**: efficient algorithms exist for small k
5. **Applications**: VLSI design, parallel computing, image segmentation

## Worked Example
Graph with 6 nodes, k=2:

**Initial partition:** {A,B,C} vs. {D,E,F}, cut size = 5
**Kernighan-Lin:** iteratively swap nodes to decrease cut size
**Final partition:** {A,D,E} vs. {B,C,F}, cut size = 3

**Result:** balanced partition with minimized cut size.

## Common Pitfalls
1. **Confusing with community detection**: partitioning requires fixed k; community detection discovers k
2. **Ignoring that partitioning optimizes cut size, not modularity**: different objectives yield different results
3. **Assuming partitioning finds meaningful communities**: balanced clusters may not align with community structure
4. **Forgetting that partitioning requires balanced clusters**: community detection allows unbalanced communities

## Connections
- [[community-detection]] — the overarching problem (different objective)
- [[min-cut-max-flow]] — exact for k=2
- [[kernighan-lin-algorithm]] — local search for balanced partition
- [[spectral-partitioning]] — uses Laplacian eigenvectors
- [[normalized-cut]] — normalized partition objective
- [[conductance]] — related community quality measure
- [[network-science-l04]] — lecture overview

## Open Questions
- How does partitioning compare to community detection on real-world networks?
- Can we extend partitioning to overlapping communities?
- How does partitioning perform on graphs with community structure?
