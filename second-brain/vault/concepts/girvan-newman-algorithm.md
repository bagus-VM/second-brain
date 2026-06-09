---
title: "Girvan-Newman Algorithm"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[modularity]]", "[[centrality-measures]]"]
---

## One-line Summary
Girvan-Newman is a divisive community detection algorithm that iteratively removes the edge with highest betweenness centrality, producing a dendrogram whose best cut maximizes modularity Q.

## Core Intuition
Edges with high edge-betweenness are exactly the bridges and weak ties that span [[structural-holes-and-brokerage|structural holes]] — all cross-community communication must cross them. By repeatedly removing these edges, the algorithm peels the graph apart along its natural community boundaries. GN is the algorithmic operationalization of Granovetter's weak-tie argument.

## Formal Definition / Statement
**Algorithm (Girvan–Newman):**
1. Compute edge betweenness of every edge
2. Remove the edge with highest edge betweenness
3. Recompute edge betweenness on the remaining graph
4. Repeat until no edges remain — record the partition at each step
5. Choose the partition that maximizes [[modularity|modularity Q]]

**Complexity**: O(|V| · |E|²) worst case — edge betweenness is recomputed after each removal.

**Edge betweenness** of edge e:
σ_st(e) = number of shortest s-t paths through e
σ_st = total number of shortest s-t paths
Edge betweenness = Σ_{s≠t} σ_st(e) / σ_st

## Key Properties
- Produces a full hierarchy (dendrogram) — every cut is a valid partition
- No pre-given k needed — choose the cut that maximizes Q
- The algorithm is **didactic** but expensive — not scalable to large graphs
- Directly connects to weak-tie theory: high-betweenness edges are inter-community bridges
- Each step may split one community or peel off a small group

## Worked Example
On a graph with two main clusters connected by a bridge, plus a small triangle weakly attached:
- **Step 0**: the bridge edge has highest betweenness (all inter-cluster paths cross it)
- **Step 1**: removing the bridge reveals two main clusters
- **Step 2**: the next high-betweenness edge links the triangle — removing it isolates the third community
- **Final**: three communities, chosen by maximizing Q across all possible cuts

## Common Pitfalls
- O(|V|·|E|²) makes GN infeasible on large graphs — use [[louvain-algorithm]] or [[leiden-algorithm]] instead
- Edge betweenness must be **recomputed** after each removal (not just decremented)
- The Q-maximizing cut may not match ground-truth labels (see [[zacharys-karate-club]])
- GN can produce many small communities at fine-grained cuts before the Q-optimal one

## Connections
- [[centrality-measures]] — uses edge betweenness, a direct extension of node betweenness
- [[edge-betweenness]] — the edge-level metric that drives every step of the Girvan-Newman algorithm
- [[modularity]] — the criterion for choosing the best dendrogram cut
- [[structural-holes-and-brokerage]] — GN removes edges spanning structural holes
- [[louvain-algorithm]] — the agglomerative alternative, much faster
- [[leiden-algorithm]] — further improvement on Louvain
- [[hierarchical-clustering]] — GN produces a dendrogram as output
- [[network-science-l03]] — weak ties and bridges are exactly what GN targets
- [[granovetter-weak-ties]] — theoretical foundation
- [[community-detection]] — the overarching problem
- [[network-science-l04]] — lecture overview

## Open Questions
- Can approximate edge betweenness (sampling) make GN practical for larger graphs?
- How does GN perform on weighted or directed graphs?
