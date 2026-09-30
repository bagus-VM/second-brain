---
title: "Modularity"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[network-science-l02]]", "[[network-science-l03]]"]
---

## One-line Summary
Modularity Q measures how much a partition's internal edge density exceeds what a degree-preserving random rewiring would produce — the canonical objective for community detection.

## Core Intuition
A "good" community has many internal edges and few external ones. But "many" and "few" compared to what? Modularity compares to the **configuration model** — a random graph that preserves each node's degree but randomizes connections. If a partition has more within-community edges than this random baseline, Q is positive; if it has fewer, Q is negative. The partition with the highest Q is the best community structure.

## Formal Definition / Statement

**Pairwise form:**
$$Q = \frac{1}{2m} \sum_{i,j} \left( A_{ij} - \frac{k_i k_j}{2m} \right) \delta(c_i, c_j)$$

where A is the adjacency matrix, m is the total number of edges, k_i is node degree, and δ(c_i, c_j) = 1 iff nodes i and j are in the same community.

**Grouped form:**
$$Q = \sum_c \left( \frac{l_c}{m} - \left(\frac{d_c}{2m}\right)^2 \right)$$

where l_c = number of internal edges in community c, d_c = sum of degrees in community c.

- **Range**: Q ∈ [-0.5, 1] in practice; Q = 0 means no better than random
- **NP-hard**: finding the partition that maximizes Q is NP-hard (Brandes et al., 2008)

## Key Properties / Complexity
- Q compares observed internal density to a degree-preserving null model (configuration model)
- Q > 0 means more within-community edges than expected by chance
- Maximizing Q exactly is NP-hard — all practical methods are heuristics
- **Resolution limit**: Q may fail to detect small communities in large graphs (Fortunato & Barthélemy 2007)
- Multiple near-optimal partitions can exist — the global maximum may not be unique

## Worked Example
Graph with 6 nodes split into two communities {A,B,C} and {D,E,F}:
- m = 7 total edges
- Each community has l_c = 3 internal edges, d_c = 2+2+3 = 7 total degree

$$Q = 2\left(\frac{3}{7} - \left(\frac{7}{14}\right)^2\right) = 2(0.429 - 0.25) \approx 0.36$$

Q is positive → the partition has more within-community edges than expected under random rewiring.

The bridge edge is the only between-community edge. The configuration model null expects k_i·k_j/(2m) edges between each pair — modularity checks whether the actual partition beats this expectation.

## Common Pitfalls
- Forgetting that Q depends on the **entire partition**, not just one community in isolation
- The resolution limit: modularity can merge small communities into larger ones when the graph is large
- Q = 0 doesn't mean "no communities" — it means "no better than random" for that specific partition
- The NP-hard result means Louvain/GN are heuristics that find good-but-not-guaranteed-optimal partitions
- Multiple near-optimal partitions exist — different algorithms may find different ones

## Connections
- [[community-detection-overview]] — modularity is the objective all these methods optimise
- [[girvan-newman-algorithm]] — GN chooses the dendrogram cut that maximizes Q
- [[louvain-algorithm]] — Louvain greedily improves Q via local moves + aggregation
- [[leiden-algorithm]] — Leiden refines Louvain to avoid broken communities
- [[zacharys-karate-club]] — the exact max-Q partition has 4 communities, not 2 (resolution limit)
- [[modularity-resolution-limit]] — the fundamental limitation of modularity for small communities
- [[product-space-network]] — modularity used to detect capability clusters in the product space
- [[network-science-l03]] — the configuration model null mirrors the degree-preserving rewiring from L03
- [[conductance]] — alternative community quality measure
- [[normalized-cut]] — alternative partition objective
- [[network-science-l04]] — lecture overview

## Open Questions
- Can resolution-limit-aware objectives replace standard modularity?
- How robust is Q to noise in the edge data?
- What is the distribution of Q values across all possible partitions?
