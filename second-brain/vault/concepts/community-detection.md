---
title: "Community Detection"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Community detection partitions a graph into groups of nodes that are densely connected internally but sparsely connected to other groups.

## Core Intuition
A community is a subset of nodes with relatively many internal edges and relatively few external edges — a region of the graph where connection density is meaningfully higher than the surrounding network. The challenge is defining "meaningfully higher" precisely enough for an algorithm to optimise.

## Formal Definition / Statement
A **community** is a subset S ⊆ V such that:
- The internal edge density of S is higher than expected under a random null model
- The external edge density (edges leaving S) is lower than expected

The canonical formalization is [[modularity]] Q, which compares observed internal edges to expected edges under degree-preserving random rewiring (the [[configuration-model]]).

**NP-hardness result** (Brandes et al. 2008): Finding the partition that maximizes Q on a general graph is NP-hard. No polynomial-time algorithm for the exact optimum is known.

## Key Properties / Complexity
1. **No unique definition**: different formalizations (modularity, conductance, normalized cut) can yield different communities
2. **Resolution limit**: modularity can miss small communities in large graphs (Fortunato & Barthélemy 2007)
3. **NP-hard optimization**: all practical methods are heuristics
4. **Hierarchical structure**: communities exist at multiple scales — a dendrogram captures this
5. **Validation challenge**: ground-truth communities are often unknown or debatable

## Worked Example
Consider a workplace graph with two dense teams (A and B) connected by a single weak edge (Dia↔Fin). Community detection should recover:
- Team A: {Ana, Ben, Cai, Dia} — densely connected
- Team B: {Eli, Fin, Gia, Hal, Ivo} — densely connected
- The Dia↔Fin edge is the bridge between communities

The algorithm discovers this boundary without being told the team labels — it finds the structural gap.

## Common Pitfalls
1. **Assuming communities are unique**: different methods and parameters yield different partitions
2. **Ignoring resolution limit**: modularity may merge small communities or split large ones
3. **Confusing algorithm output with ground truth**: detected communities are algorithmic artifacts, not necessarily "real" groups
4. **Over-interpreting small graphs**: community structure is more meaningful in large networks

## Connections
- [[modularity]] — the canonical objective function
- [[girvan-newman-algorithm]] — divisive heuristic
- [[louvain-algorithm]] — agglomerative heuristic
- [[leiden-algorithm]] — improved Louvain with refinement
- [[hierarchical-clustering]] — dendrogram output
- [[spectral-partitioning]] — cut-based alternative
- [[conductance]] — alternative community quality measure
- [[normalized-cut]] — balanced partition objective
- [[edge-betweenness]] — metric used by Girvan-Newman to identify inter-community bridges
- [[embedding-based-community-detection]] — modern approach using node embeddings and clustering
- [[graph-partitioning]] — fixed-k balanced partitioning as alternative to community detection
- [[modularity-resolution-limit]] — fundamental limitation of modularity-based methods
- [[product-space-network]] — real-world application of community detection to economic products
- [[network-science-l04]] — lecture overview

## Open Questions
- How do we handle overlapping communities (nodes belonging to multiple groups)?
- What is the right resolution scale for a given network?
- How do we validate community detection without ground truth?
- How do dynamic networks affect community structure?
