---
title: "Community Detection Overview"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[modularity]]"]
---

## One-line Summary
Community detection finds subsets of nodes with dense internal connections and sparse external connections, using divisive, agglomerative, cut-based, or embedding-based strategies.

## Core Intuition
A community is a subset S ⊆ V with relatively many edges inside S and relatively few edges leaving S. Different formal definitions instantiate this intuition differently. The most influential is [[modularity]], which compares observed internal density against a random null model. Since maximizing modularity is NP-hard (Brandes et al. 2008), all practical methods are polynomial-time heuristics.

## Formal Definition / Statement
**Working definition**: A community is a subset S ⊆ V where the internal edge density is meaningfully higher than the surrounding graph.

Four families of approaches:
1. **Divisive** (top-down): start with whole graph, repeatedly remove inter-community edges → [[girvan-newman-algorithm]]
2. **Agglomerative** (bottom-up): start with each node alone, repeatedly merge pairs that increase [[modularity]] → [[louvain-algorithm]], [[leiden-algorithm]]
3. **Cut-based**: minimize edge cuts or use spectral methods → [[graph-partitioning-cut-spectral]]
4. **Embedding-based**: learn node representations, then cluster (node2vec + k-means, GNNs)

## Key Properties
- Divisive and agglomerative methods produce a **hierarchy** (dendrogram), not a single flat partition
- Where to cut the [[hierarchical-clustering|dendrogram]] is the analyst's modeling choice
- No fixed k is needed for Louvain/Leiden — the number of communities emerges from greedy moves
- Cut-based methods (spectral, min-cut) typically require specifying k in advance
- Embedding-based methods can handle overlapping memberships and node features

## Worked Example
The L04 workplace graph with 9 employees naturally splits into:
- Team A: Ana, Ben, Cai, Dia (dense core + bridge)
- Team B: Fin, Gia, Hal, Ivo, Eli (dense core)
- The Dia–Fin edge is the sole inter-community bridge

Any community detection algorithm should recover roughly this split, with the bridge edge as the boundary.

## Common Pitfalls
- Different algorithms give different answers on the same graph — there is no single "correct" partition
- Modularity's resolution limit can hide small communities
- Community detection is not a neutral measurement — it's an optimization against a chosen objective
- Embedding-based methods need k, walk hyperparameters, or training objectives
- Overlapping/soft membership is real but most classical methods produce hard partitions

## Connections
- [[modularity]] — the canonical objective function
- [[girvan-newman-algorithm]] — the didactic divisive method
- [[louvain-algorithm]] — the standard agglomerative method
- [[leiden-algorithm]] — improved Louvain with refinement
- [[graph-partitioning-cut-spectral]] — cut-based and spectral alternatives
- [[hierarchical-clustering]] — the dendrogram output structure
- [[zacharys-karate-club]] — the empirical benchmark
- [[structural-holes-and-brokerage]] — brokers sit on inter-community edges
- [[centrality-measures]] — betweenness centrality identifies bridge nodes
- [[embedding-based-community-detection]] — embedding + clustering approach for overlapping communities
- [[graph-partitioning]] — fixed-k balanced partitioning vs. community discovery
- [[modularity-resolution-limit]] — why modularity can miss small communities
- [[product-space-network]] — community detection applied to product capability space

## Open Questions
- How to choose the "right" number of communities when no ground truth exists?
- Can we detect overlapping or hierarchical communities in a principled way?
- How do dynamic communities evolve over time?
