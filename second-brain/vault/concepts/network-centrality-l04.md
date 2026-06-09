---
title: "Network Centrality Measures"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*Quantitative measures that identify the most important or influential nodes in a network based on different definitions of 'importance.'*

## Core Intuition
In a network, not all nodes are equal. Some are hubs connecting many others; some bridge distant groups; some are close to everyone. But 'important' means different things in different contexts — a celebrity with millions of followers is important for information spread, a border router is important for network connectivity, and a protein hub is important for cellular function. Centrality measures formalize these different notions of importance.

## Formal Definition / Statement
Centrality measures quantify the importance of nodes in a network. Major measures include:

1. **Degree Centrality**: C_D(v) = deg(v) / (n-1)
   - Fraction of nodes a node is connected to
   - Simple, local measure. Good for identifying hubs.

2. **Betweenness Centrality**: C_B(v) = Σ_{s≠v≠t} σ_st(v) / σ_st
   - Fraction of shortest paths through a node
   - Identifies bridges and bottlenecks
   - Computationally expensive: O(nm) for unweighted, O(nm + n² log n) for weighted

3. **Closeness Centrality**: C_C(v) = (n-1) / Σ_{u≠v} d(v,u)
   - Inverse of average shortest path distance to all other nodes
   - Identifies nodes that can quickly reach the entire network

4. **Eigenvector Centrality**: C_E(v) = (1/λ) Σ_{u∈N(v)} C_E(u)
   - A node is important if connected to other important nodes
   - Recursive definition solved by the principal eigenvector of the adjacency matrix

5. **PageRank**: PR(v) = (1-d)/n + d Σ_{u∈B(v)} PR(u)/|N(u)|
   - Modified eigenvector centrality with damping factor d (typically 0.85)
   - Handles dangling nodes, models random walk with teleportation

6. **Katz Centrality**: C_K(v) = Σ_{k=1}^∞ Σ_{j=1}^n α^k (A^k)_{jv}
   - Counts all paths (not just shortest), weighted by path length with decay α

7. **HITS (Hubs and Authorities)**: Two scores per node — hub score (links to good authorities) and authority score (linked from good hubs)

## Key Properties / Complexity
- Different centrality measures can rank nodes very differently
- Degree centrality is O(n); betweenness is O(nm) — orders of magnitude difference
- Centrality is relative to the network; comparing across networks is meaningless
- Centralization (Freeman) measures how unequal centrality distribution is in the whole network
- Dynamic centrality tracks how importance changes over time
- In directed networks, in-degree and out-degree centrality capture different roles

## Worked Example
Finding key nodes in a terrorist communication network:
1. **Degree centrality**: Node A has the most connections (15) — likely the organizer
2. **Betweenness centrality**: Node B has few connections but bridges two cells — the courier
3. **Closeness centrality**: Node C can reach everyone in fewest steps — the information hub
4. **Eigenvector centrality**: Node D is connected to other highly connected nodes — the leader's lieutenant
5. **Comparison**: Removing Node A (highest degree) fragments the network less than removing Node B (highest betweenness)
6. **Insight**: Betweenness centrality identifies the most critical vulnerability points in this network

## Common Pitfalls
- **No universal 'best' centrality**: The right measure depends on the question being asked
- **Computational cost**: Betweenness centrality on a million-node graph takes hours
- **Normalization**: Centrality values are only meaningful relative to the same network
- **Dynamic networks**: Static centrality on a temporal network can be misleading
- **Correlation**: High-degree nodes often have high betweenness, but not always (tree structures break this)

## Connections
- [[betweenness-centrality]] — Detailed treatment of betweenness centrality
- [[closeness-centrality]] — Detailed treatment of closeness centrality
- [[pagerank-algorithm]] — PageRank as a centrality measure for directed networks
- [[network-community-structure-l06]] — Central nodes often define community boundaries
- [[small-world-networks]] — Small-world networks have specific centrality distributions
- [[scale-free-networks]] — Hubs in scale-free networks have extreme centrality values

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
