---
title: "Hierarchical Clustering and Dendrograms"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Divisive and agglomerative community detection methods produce dendrograms — tree structures where each horizontal cut yields a different clustering, and the analyst chooses the level.

## Core Intuition
Both [[girvan-newman-algorithm|Girvan–Newman]] (divisive) and [[louvain-algorithm|Louvain]]/[[leiden-algorithm|Leiden]] (agglomerative) produce a **hierarchy** rather than a single flat partition. The dendrogram encodes all possible clusterings at once. The "right" number of communities depends on where you cut — this is a modeling decision, not an algorithm output.

## Formal Definition / Statement
A **dendrogram** is a tree where:
- Leaves are individual nodes
- Internal nodes represent merges (agglomerative) or splits (divisive)
- Each horizontal cut through the tree yields a flat partition
- The default rule for choosing the cut: pick the one that maximizes [[modularity]] Q

**Agglomerative**: start with n singleton clusters, repeatedly merge the closest pair.
**Divisive**: start with one cluster, repeatedly split or remove inter-cluster edges.

## Key Properties
- Every horizontal cut is a valid clustering
- The "right" cut is the analyst's choice — often guided by Q or domain knowledge
- Different cuts reveal structure at different scales (nested communities)
- The dendrogram is the same regardless of whether you use divisive or agglomerative strategies (on the same graph) — though the order of merges/splits may differ

## Worked Example
A dendrogram with nodes A through G:
- Cut at distance 0 → 7 clusters (each node alone)
- Cut at distance d1 → 4 clusters (e.g., {A,B}, {C,D}, {E,F}, {G})
- Cut at distance d2 → 2 clusters (e.g., {A,B,C,D} and {E,F,G})
- Cut at max distance → 1 cluster (whole graph)

Each level reveals different community structure. The Q-maximizing cut is typically the default choice.

## Common Pitfalls
- The dendrogram doesn't tell you which cut is "right" — it shows all options
- Different algorithms produce different dendrograms on the same graph
- Cutting too high merges distinct communities; cutting too low fragments coherent ones
- The dendrogram assumes a hierarchical structure — some networks have flat community structure

## Connections
- [[girvan-newman-algorithm]] — produces a dendrogram by iteratively removing edges
- [[louvain-algorithm]] — produces multi-level aggregation (implicit dendrogram)
- [[leiden-algorithm]] — same multi-level structure with refinement
- [[modularity]] — the default criterion for choosing the dendrogram cut
- [[community-detection-overview]] — the hierarchy vs. flat partition distinction
- [[community-detection]] — the overarching problem
- [[network-science-l04]] — lecture overview

## Open Questions
- How to detect when a network's community structure is genuinely hierarchical vs. flat?
- Can we use statistical tests to determine the "significant" cut level?
