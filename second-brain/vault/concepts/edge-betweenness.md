---
title: "Edge Betweenness"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Edge betweenness measures how often an edge lies on shortest paths between all pairs of nodes — the edge-level analogue of [[betweenness-centrality]].

## Core Intuition
Edges with high edge betweenness are exactly the local bridges and weak ties — they carry many shortest paths because all cross-community communication must cross them. This is why the [[girvan-newman-algorithm]] removes high-betweenness edges to find communities.

## Formal Definition / Statement
**Edge betweenness:**
C_B(e) = Σ_{s≠t} σ_st(e) / σ_st

where:
- σ_st = number of shortest paths from s to t
- σ_st(e) = number of shortest paths from s to t that pass through edge e

**Normalized form:** divide by (n-1)(n-2)/2 for undirected graphs.

**Range:** 0 to (n-1)(n-2)/2 (raw). 0 to 1 (normalized).

**Complexity:** O(nm) with Brandes algorithm for all edges.

**Use in [[girvan-newman-algorithm]]:** iteratively remove the edge with highest edge betweenness to find communities.

## Key Properties / Complexity
1. **Edge-level measure**: quantifies how much an edge is a bridge
2. **Connects to weak ties**: high-betweenness edges are local bridges
3. **Foundation of Girvan-Newman**: the algorithm removes high-betweenness edges
4. **Expensive**: O(nm) for all edges
5. **Dynamic**: edge betweenness changes after each edge removal

## Worked Example
Graph with two dense clusters connected by a bridge edge:

**Bridge edge:** every shortest path between the clusters crosses it → high edge betweenness
**Internal edges:** only carry paths within their cluster → low edge betweenness

**Girvan-Newman:** removes the bridge edge first (highest betweenness), revealing the two communities.

## Common Pitfalls
1. **Confusing with node betweenness**: edge betweenness is for edges; node betweenness is for nodes
2. **Ignoring that edge betweenness must be recomputed after each removal**: unlike some centrality measures
3. **Assuming high edge betweenness means the edge is unimportant**: it's structurally important for connecting communities
4. **Forgetting that edge betweenness is expensive**: O(nm) for all edges

## Connections
- [[betweenness-centrality]] — the node-level analogue
- [[girvan-newman-algorithm]] — uses edge betweenness to find communities
- [[granovetter-weak-ties]] — high-betweenness edges are weak ties
- [[community-detection]] — the overarching problem
- [[network-science-l04]] — lecture overview

## Open Questions
- Can we approximate edge betweenness efficiently for very large graphs?
- How does edge betweenness perform on directed or weighted graphs?
- How does edge betweenness relate to network robustness?
