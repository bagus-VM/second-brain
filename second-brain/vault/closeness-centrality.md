---
title: "Closeness Centrality"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Closeness centrality measures how near a node is to all other nodes on average — quantifying accessibility and short-path reach.

## Core Intuition
A node with high closeness can reach everyone quickly. This makes it ideal for service hubs, emergency-response centers, or information spreaders — anything where minimizing average distance matters.

## Formal Definition / Statement
**Closeness centrality:**
C_C(v) = (n-1) / Σ_{u≠v} d(v,u)

where d(v,u) is the shortest-path distance from v to u.

**Range:** 0 to 1 (normalized). 1 only if v is adjacent to everyone.

**Complexity:** One node: O(n + m) BFS. All nodes: O(n(n + m)).

**Limitation:** fails on disconnected graphs (distance to unreachable nodes is ∞).

**Use:** accessibility studies — which hospital, station, or facility minimizes network distance to a population center.

## Key Properties
1. **Accessibility theory**: importance from short paths to everyone
2. **Global measure**: requires all-pairs shortest paths
3. **Fails on disconnected graphs**: distance to unreachable nodes is ∞
4. **Harmonic centrality** is the robust alternative for disconnected graphs
5. **Useful for hub placement**: minimizes average distance to all nodes

## Worked Example
Toy network: A-B, A-C, A-D, D-E (n=5):

**Closeness of A:**
- Distances: d(A,B)=1, d(A,C)=1, d(A,D)=1, d(A,E)=2
- Sum = 1+1+1+2 = 5
- C_C(A) = 4/5 = 0.80

**Closeness of D:**
- Distances: d(D,A)=1, d(D,B)=2, d(D,C)=2, d(D,E)=1
- Sum = 1+2+2+1 = 6
- C_C(D) = 4/6 ≈ 0.67

**Closeness of E:**
- Distances: d(E,D)=1, d(E,A)=2, d(E,B)=3, d(E,C)=3
- Sum = 1+2+3+3 = 9
- C_C(E) = 4/9 ≈ 0.44

## Common Pitfalls
1. **Fails on disconnected graphs**: use [[harmonic-centrality]] instead
2. **Confusing with betweenness**: closeness measures proximity; betweenness measures path dependency
3. **Assuming high closeness means high degree**: a central node can have low degree but short paths to everyone
4. **Ignoring that closeness is a global measure**: requires all-pairs shortest paths, which is expensive

## Connections
- [[centrality-measures]] — one of the main centrality measures
- [[harmonic-centrality]] — robust alternative for disconnected graphs
- [[betweenness-centrality]] — related but measures brokerage, not proximity
- [[degree-centrality]] — local measure, much cheaper to compute
- [[network-science-l04]] — lecture overview

## Open Questions
- How does closeness perform on directed or weighted graphs?
- Can we approximate closeness efficiently for very large graphs?
- How does closeness relate to information diffusion speed?
