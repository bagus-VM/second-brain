---
title: "Community Detection"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-07-27
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

## Algorithm Comparison

Four widely-taught community detection algorithms, compared along the dimensions that matter for choosing one in practice.

| Dimension | [[girvan-newman-algorithm\|Girvan–Newman]] | Greedy Modularity Maximisation | [[louvain-algorithm\|Louvain]] | [[leiden-algorithm\|Leiden]] |
|---|---|---|---|---|
| **Approach** | Divisive: remove highest-betweenness edges one by one | Agglomerative: merge community pairs greedily by ΔQ | Agglomerative: local node moves + community aggregation | Agglomerative: local moves + refinement + aggregation |
| **Objective** | Maximise Q at best dendrogram cut | Maximise Q greedily | Maximise Q greedily | Maximise Q (or CPM) with connectedness guarantee |
| **Complexity** | O(\|V\|·\|E\|²) — recompute betweenness each removal | O(\|E\|·\|V\|) typical for efficient implementations | Near-linear in \|E\| empirically | Near-linear, small overhead over Louvain |
| **Scalability** | Small graphs only (hundreds of nodes) | Moderate (thousands of nodes) | Millions of nodes/edges | Millions of nodes/edges |
| **Hierarchy** | Full dendrogram — every cut is a partition | Dendrogram of merges | Implicit multi-level hierarchy | Implicit multi-level hierarchy |
| **Determinism** | Deterministic (ties aside) | Deterministic (ties aside) | Non-deterministic — depends on node visit order | Non-deterministic — depends on node visit order |
| **k given?** | No — choose best cut by Q | No — merges until merge stops improving Q | No — emerges from greedy moves | No — emerges from greedy moves + refinement |
| **Community quality** | High quality on small graphs | Good, but greedy merges can lock in early mistakes | Can produce internally disconnected communities | Guarantees connectedness via refinement |
| **Resolution limit** | Inherited from Q (dendrogram cut) | Yes — merges small communities | Yes — merges small communities | Yes, but refinement mitigates some cases |
| **Best for** | Teaching, small networks, theoretical clarity | Medium graphs where a simple merge suffices | Large networks, standard research default | Large networks needing reliable, connected communities |

Girvan–Newman is the reference algorithm textbooks teach first because the edge-betweenness mechanic is easy to explain and the dendrogram makes every intermediate partition visible. Greedy modularity maximisation (Clauset, Newman, Moore 2004) is the middle ground: faster than GN, slower than Louvain, and it can lock in bad early merges without any repair step. Louvain is the practical default for large graphs. Leiden is what you reach for when you need Louvain's speed but cannot tolerate disconnected communities.

All four are heuristics — Q maximisation is NP-hard (Brandes et al. 2008), so none can promise the global optimum.

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
