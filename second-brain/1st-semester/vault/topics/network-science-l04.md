---
title: "L04 — Communities and Graph Partitioning"
tags: [topic, network-science, semester-1]
course: "Network Science"
lecture: 4
status: current
last_updated: 2026-06-01
prerequisites: ["[[network-science-l03]]"]
---

## One-line Summary
Graph communities are dense subsets with few external links; finding them requires NP-hard optimization (modularity), which is approximated by divisive (Girvan–Newman) and agglomerative (Louvain/Leiden) heuristics.

## Core Intuition
Lecture 03 classified edges (strong vs. weak, bridges vs. embedded). Lecture 04 classifies **nodes** and **groups**. The central question: which nodes are important, and where are the natural boundaries between dense groups? "Importance" is never one thing — degree, closeness, betweenness, and eigenvector centrality capture different theories of influence. "Community" is formalized as modularity Q: observed within-group edges minus expected edges under a random null model. Maximizing Q is NP-hard, so practical methods are polynomial-time heuristics.

## Topics Covered

### Node Roles and Centrality
- [[structural-holes-and-brokerage]] — embeddedness vs. brokerage; Burt's social capital
- [[centrality-measures]] — degree, closeness, harmonic, betweenness, eigenvector, PageRank

### Community Structure
- [[modularity]] — the canonical objective: observed minus expected internal density
- [[community-detection-overview]] — families of algorithms for finding groups

### Algorithms
- [[girvan-newman-algorithm]] — divisive: peel apart high-betweenness edges
- [[louvain-algorithm]] — agglomerative: local moves + super-node aggregation
- [[leiden-algorithm]] — Louvain with refinement before aggregation
- [[hierarchical-clustering]] — dendrograms as algorithm output

### Partitioning Methods
- [[graph-partitioning-cut-spectral]] — min-cut, Kernighan–Lin, spectral partitioning (Laplacian)
- [[graph-partitioning]] — fixed-k balanced partitioning as an alternative to community detection

### Empirical Validation
- [[zacharys-karate-club]] — the canonical benchmark for community detection
- [[product-space-network]] — community detection applied to product capability space

## Key Relations
- L03 → L04: edge classification (weak ties, bridges) enables group classification
- Modularity maximization is NP-hard (Brandes et al. 2008), paralleling MaxSTC from L03
- Girvan–Newman is the algorithmic operationalization of Granovetter's weak-tie theory
- All community detection answers depend on the chosen objective — there is no neutral measurement

## Reading
- Easley & Kleinberg Ch. 3.6, Ch. 9
- Newman (2010) Ch. 7
- Blondel et al. (2008) for Louvain
- Traag et al. (2019) for Leiden

## Exam Notes (28 July 2026)
- Know the formulas for all centrality measures and their O() complexities
- Be able to compute modularity Q by hand for a small graph + partition
- Explain why modularity maximization is NP-hard and what that means in practice
- Compare Girvan–Newman vs. Louvain vs. Leiden (strategy, complexity, strengths)
- Understand spectral partitioning via the Fiedler vector
- Zachary's karate club: what algorithms find, what they miss (resolution limit, binary ground truth)
- Know the [[modularity-resolution-limit]]: why modularity cannot detect communities smaller than √(2m)
- [[edge-betweenness]] is the key metric in Girvan-Newman — recomputed after each edge removal
- [[embedding-based-community-detection]] handles overlapping communities via node2vec + clustering
