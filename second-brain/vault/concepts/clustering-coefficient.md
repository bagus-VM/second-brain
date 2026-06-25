---
title: "Clustering Coefficient"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
The clustering coefficient measures how many of a node's neighbors are also connected to each other — quantifying [[embeddedness]] and local density.

## Core Intuition
A node with high clustering coefficient sits inside a tightly connected neighborhood — its neighbors are also neighbors of each other. This captures the "friends of my friends are my friends" effect.

## Formal Definition / Statement
**Local clustering coefficient:**
C(v) = 2 × (number of edges among v's neighbors) / (deg(v) × (deg(v) - 1))

**Range:** 0 to 1.
- C(v) = 0: none of v's neighbors are connected
- C(v) = 1: all of v's neighbors are connected to each other

**Global clustering coefficient:**
C_global = 3 × (number of triangles) / (number of connected triples)

**Complexity:** O(deg(v)²) per node; O(Σ deg(v)²) for all nodes.

**Use:** measures [[embeddedness]] — high clustering means the node is embedded in a dense neighborhood.

## Key Properties
1. **Local measure**: only considers a node's immediate neighborhood
2. **Measures embeddedness**: high clustering means the node is embedded
3. **Range 0 to 1**: easy to interpret
4. **Expensive for high-degree nodes**: O(deg(v)²) per node
5. **Connects to community detection**: embedded nodes are community cores

## Worked Example
Workplace graph — Team A (Ana, Ben, Cai, Dia):

**Clustering coefficient of Ana:**
- Neighbors: Ben, Cai, Dia
- Edges among neighbors: Ben-Cai, Ben-Dia, Cai-Dia (3 edges)
- Possible edges: 3 × 2 / 2 = 3
- C(Ana) = 2 × 3 / (3 × 2) = 1.0

**Clustering coefficient of Dia:**
- Neighbors: Ana, Ben, Cai, Fin
- Edges among neighbors: Ana-Ben, Ana-Cai, Ben-Cai (3 edges)
- Possible edges: 4 × 3 / 2 = 6
- C(Dia) = 2 × 3 / (4 × 3) = 0.5

**Interpretation:** Ana is fully embedded (all neighbors connected); Dia is partially embedded (some neighbors connected, but Fin is isolated from the others).

## Common Pitfalls
1. **Confusing with degree**: degree counts neighbors; clustering measures inter-neighbor connections
2. **Ignoring that clustering is a local measure**: it doesn't capture global structure
3. **Assuming high clustering means high importance**: embedded nodes may have low betweenness
4. **Forgetting the computational cost**: O(deg(v)²) can be expensive for high-degree nodes

## Connections
- [[embeddedness]] — high clustering means embedded
- [[structural-holes]] — low clustering means brokerage
- [[centrality-measures]] — clustering is related to embeddedness, not centrality
- [[community-detection]] — embedded nodes are community cores
- [[network-science-l04]] — lecture overview

## Open Questions
- How does clustering coefficient perform on directed or weighted graphs?
- Can we approximate clustering coefficient efficiently for very large graphs?
- How does clustering coefficient relate to network robustness?
