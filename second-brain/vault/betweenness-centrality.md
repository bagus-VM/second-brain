---
title: "Betweenness Centrality"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Betweenness centrality measures how often a node sits on shortest paths between other nodes — quantifying brokerage and control over information flows.

## Core Intuition
A node with high betweenness is a bottleneck: many shortest paths between other nodes pass through it. This gives it control over information flows and makes it critical for network connectivity.

## Formal Definition / Statement
**Betweenness centrality:**
C_B(v) = Σ_{s≠v≠t} σ_st(v) / σ_st

where:
- σ_st = number of shortest paths from s to t
- σ_st(v) = number of shortest paths from s to t that pass through v

**Normalized form:** divide by (n-1)(n-2)/2 for undirected graphs (number of pairs excluding v).

**Range:** 0 to 1 (normalized). 1 means all shortest paths between other nodes use v.

**Complexity:** O(n(n + m)) with Brandes algorithm for all nodes.

**Difference from closeness:** Closeness asks "How near is v to everyone?" Betweenness asks "How many shortest paths between other nodes depend on v?"

## Key Properties
1. **Brokerage theory**: importance from sitting on paths between others
2. **Global measure**: requires all-pairs shortest paths
3. **Brandes algorithm**: computes all nodes in O(n(n + m))
4. **Edge betweenness**: same idea applied to edges — used in [[girvan-newman-algorithm]] (see [[edge-betweenness]] for the full treatment)
5. **Vulnerability indicator**: high-betweenness nodes are critical for connectivity

## Worked Example
Toy network: A-B, A-C, A-D, D-E (n=5):

**Betweenness of A:**
- Paths between others: B-C, B-D, B-E, C-D, C-E, D-E (6 pairs)
- Paths through A: B-C, B-D, B-E, C-D, C-E (5 of 6)
- C_B(A) = 5/6 ≈ 0.83

**Betweenness of D:**
- Paths through D: A-E, B-E, C-E (3 of 6)
- C_B(D) = 3/6 = 0.50

**Betweenness of E:**
- No paths between others pass through E
- C_B(E) = 0

## Common Pitfalls
1. **Confusing with closeness**: closeness measures proximity; betweenness measures path dependency
2. **Ignoring that betweenness counts paths between OTHER nodes**: paths starting or ending at v are not counted
3. **Assuming high betweenness means high degree**: a node can have high betweenness with low degree (if it's a bottleneck)
4. **Forgetting that betweenness must be recomputed after edge removal**: unlike some centrality measures

## Connections
- [[centrality-measures]] — one of the main centrality measures
- [[closeness-centrality]] — related but measures proximity, not brokerage
- [[girvan-newman-algorithm]] — uses edge betweenness to find communities
- [[edge-betweenness]] — the edge-level analogue of betweenness centrality
- [[structural-holes]] — brokers spanning structural holes have high betweenness
- [[embeddedness]] — embedded nodes have low betweenness
- [[network-science-l04]] — lecture overview

## Open Questions
- How does betweenness perform on directed or weighted graphs?
- Can we approximate betweenness efficiently for very large graphs?
- How does betweenness relate to network robustness and attack tolerance?
