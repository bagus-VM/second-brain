---
title: "Network Community Structure"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*The detection and analysis of densely connected groups of nodes within networks, revealing mesoscale structure.*

## Core Intuition
Real networks aren't random — they have clusters. People form friend groups, proteins cluster in functional modules, web pages group by topic. Community detection finds these natural groupings by optimizing for dense intra-community connections and sparse inter-community connections. It's the network equivalent of unsupervised clustering in machine learning.

## Formal Definition / Statement
A community (or module) in a network is a subset of nodes that are densely connected internally but sparsely connected to the rest of the network.

**Formal approaches:**

1. **Modularity optimization (Newman-Girvan)**: Q = (1/2m) Σ_ij [A_ij - k_i*k_j/(2m)] δ(c_i, c_j)
   - Compares actual edge density to expected under a random null model
   - Q ∈ [-0.5, 1]; Q > 0.3 indicates significant community structure
   - Optimization: greedy agglomeration, Louvain algorithm, spectral methods

2. **Spectral partitioning**: Use eigenvectors of the graph Laplacian to find natural cuts
   - Fiedler vector (second smallest eigenvector) gives optimal bipartition
   - Recursive bisection or k-way partitioning

3. **Stochastic Block Models (SBM)**: Probabilistic model where nodes belong to blocks, edge probability depends on block membership

4. **Label propagation**: Each node adopts the majority label of its neighbors; converges to communities

5. **Louvain algorithm**: Greedy modularity optimization with hierarchical aggregation. O(n log n) complexity.

**Overlapping communities**: Nodes can belong to multiple communities (e.g., a person in both work and hobby groups). Methods: clique percolation (CFinder), mixed-membership models.

## Key Properties / Complexity
- Modularity Q is the most widely used quality function but has a resolution limit (misses small communities in large networks)
- Louvain algorithm is the most popular for large networks: near-linear time, good quality
- Leiden algorithm improves on Louvain by guaranteeing well-connected communities
- Community detection is NP-hard in general; all methods are heuristics
- Ground truth communities are often unknown; evaluation uses NMI, ARI, or conductance
- Hierarchical community structure exists in many real networks

## Worked Example
Detecting communities in a social network of 10,000 users:
1. Build the friendship graph: nodes = users, edges = mutual friendships
2. Apply Louvain algorithm:
   - Phase 1: Each node starts as its own community. Iteratively move node to neighbor's community if modularity increases.
   - Phase 2: Aggregate communities into super-nodes, repeat.
3. Result: 15 communities detected, sizes ranging from 50 to 2,000 nodes
4. Interpretation: Community 3 (500 users) are university students; Community 7 (1,200 users) are gamers
5. Validation: Check conductance (ratio of inter/intra edges) — low conductance = good communities
6. Application: Targeted advertising, content recommendation, misinformation containment

## Common Pitfalls
- **Resolution limit**: Modularity optimization may merge small communities that should be separate
- **Degeneracy**: Many network partitions have similar modularity scores; the landscape is flat
- **No ground truth**: Unlike supervised learning, there's no definitive 'correct' community structure
- **Dynamic networks**: Communities evolve over time; static detection misses temporal patterns
- **Resolution parameter**: Some methods require specifying the number of communities a priori

## Connections
- [[spectral-clustering]] — Spectral methods use Laplacian eigenvectors for community detection
- [[modularity]] — Modularity Q is the primary quality function for community structure
- [[hierarchical-navigable-small-world]] — HNSW graphs exhibit community-like clustering
- [[betweenness-centrality]] — Edge betweenness can identify community boundaries
- [[signed-networks]] — Community detection in signed networks uses balance theory
- [[network-centrality-l04]] — Central nodes often sit at community boundaries

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
