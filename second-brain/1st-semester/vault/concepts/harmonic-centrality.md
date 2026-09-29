---
title: "Harmonic Centrality"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Harmonic centrality is the disconnected-graph extension of [[closeness-centrality]] — unreachable nodes contribute 0 instead of making the distance sum infinite.

## Core Intuition
Closeness centrality fails on disconnected graphs because the distance to unreachable nodes is ∞. Harmonic centrality fixes this by using reciprocal distances: 1/d(v,u) instead of d(v,u). Unreachable nodes (d = ∞) contribute 0, not ∞.

## Formal Definition / Statement
**Harmonic centrality:**
H(v) = Σ_{u≠v} 1/d(v,u)

with 1/∞ = 0 (unreachable nodes contribute nothing).

**Range:** 0 to n-1 (raw). n-1 means direct access to everyone.

**Harmonic mean distance:**
HMD(v) = (n-1) / H(v)

**Complexity:** One node: O(n + m) BFS. All nodes: O(n(n + m)).

**Interpretation:** many reachable nodes through short paths.

## Key Properties / Complexity
1. **Handles disconnected graphs**: unreachable nodes contribute 0, not ∞
2. **Robust alternative to closeness**: works on any graph
3. **Same complexity as closeness**: O(n(n + m)) for all nodes
4. **Higher is better**: more reachable nodes through shorter paths
5. **Connects to harmonic mean**: HMD is the harmonic mean distance

## Worked Example
Toy network: A-B, A-C, A-D, D-E (n=5):

**Harmonic centrality of A:**
- Distances: d(A,B)=1, d(A,C)=1, d(A,D)=1, d(A,E)=2
- H(A) = 1/1 + 1/1 + 1/1 + 1/2 = 3.50
- HMD(A) = 4/3.50 ≈ 1.14

**Harmonic centrality of D:**
- Distances: d(D,A)=1, d(D,B)=2, d(D,C)=2, d(D,E)=1
- H(D) = 1/1 + 1/2 + 1/2 + 1/1 = 3.00
- HMD(D) = 4/3.00 ≈ 1.33

**Harmonic centrality of E:**
- Distances: d(E,D)=1, d(E,A)=2, d(E,B)=3, d(E,C)=3
- H(E) = 1/1 + 1/2 + 1/3 + 1/3 ≈ 2.17
- HMD(E) = 4/2.17 ≈ 1.85

## Common Pitfalls
1. **Confusing with closeness**: closeness uses 1/sum(distance); harmonic uses sum(1/distance)
2. **Ignoring that harmonic handles disconnected graphs**: this is its main advantage
3. **Assuming harmonic and closeness always agree**: they can rank nodes differently
4. **Forgetting the normalization**: raw harmonic centrality ranges from 0 to n-1

## Connections
- [[closeness-centrality]] — the measure harmonic centrality improves
- [[centrality-measures]] — one of the main centrality measures
- [[betweenness-centrality]] — related but measures brokerage, not reachability
- [[network-science-l04]] — lecture overview

## Open Questions
- How does harmonic centrality perform on directed or weighted graphs?
- Can we approximate harmonic centrality efficiently for very large graphs?
- How does harmonic centrality relate to information diffusion speed?
