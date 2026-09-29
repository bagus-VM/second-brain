---
title: "Hierarchical Navigable Small World (HNSW)"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[small-world-property]]", "[[kleinberg-decentralized-search]]"]
---
## One-line Summary
HNSW is a graph structure that lets you find the nearest neighbours of a point in a huge dataset by "zooming in" through layers — like a skip list, but for high-dimensional similarity search.

## Core Intuition
Imagine you want to find the closest restaurant to your house in a city. A skip list analogy: at the top layer you see only highways (long-range connections between distant landmarks), so you quickly get to the right neighbourhood. At the middle layer you see major roads. At the bottom layer you see every street. HNSW does exactly this for vectors in high-dimensional space. Each node exists on multiple layers. The top layers have few nodes with long-range links (small-world shortcuts); the bottom layer has all nodes with mostly local links. A greedy search starting from the top layer descends through layers, getting progressively closer to the true nearest neighbour. The result: O(log n) search time instead of O(n).

## Formal Definition / Statement

An HNSW index is a layered graph H = (L₀, L₁, ..., Lₘₐₓ) where:

- **Layer 0** contains all elements. Each layer Lᵢ ⊇ Lᵢ₊₁ (higher layers are subsets).
- Each element is assigned to a maximum layer drawn from an exponential distribution: P(max_layer = i) ∝ e^{-i/M} where M is a parameter.
- Within each layer, edges connect each node to its approximate nearest neighbours (using the NSW — Navigable Small World — graph construction).
- **Search algorithm** (k-NN query for point q):
  1. Start at the top layer at an entry point ep
  2. At each layer, greedily navigate to the nearest neighbour of q
  3. When no closer node is found, drop to the next layer and continue
  4. At layer 0, return the k nearest neighbours found

**NSW construction** (base layer): Insert nodes one by one. For each new node, find its M nearest neighbours among already-inserted nodes and add bidirectional edges. The insertion order creates long-range "shortcuts" between early-inserted nodes.

**Parameters**:
- M: number of connections per node (higher = better recall, more memory)
- efConstruction: beam width during construction (higher = better graph quality, slower build)
- efSearch: beam width during search (higher = better recall, slower query)

## Key Properties / Complexity

- **Search time**: O(log n) average case for approximate nearest neighbour search
- **Build time**: O(n · log n) with the incremental insertion scheme
- **Space**: O(n · M) for storing the graph (each node has ~2M connections across layers)
- **Recall**: tunable via efSearch parameter; can approach 1.0 with enough beam width
- The multi-layer structure is isomorphic to a skip list — the analogy is exact
- Kleinberg's (2000) navigability theorem guarantees that greedy routing works when long-range links follow the right distribution (r = d in grid; empirically works in high-D with HNSW)
- The graph is "navigable" even in high-dimensional spaces where tree-based methods (KD-trees) fail

## Worked Example

Index 1000 vectors in ℝ¹²⁸ with M=16:

1. **Layer assignment**: ~500 nodes in L₀ only, ~250 in L₀+L₁, ~125 in L₀+L₁+L₂, etc.
2. **Insertion**: Insert node 1 → it's alone. Insert node 2 → connect to node 1. Insert node 3 → connect to nearest of {1,2}. ... By node 500, the base layer has rich local connectivity plus long-range shortcuts from early insertions.
3. **Query**: Given query vector q, start at the top layer (say L₃) at the single entry point. Greedy search finds the nearest node in L₃. Descend to L₂, continue greedy from that position. Descend to L₁, then L₀. At L₀, use beam search (width efSearch) to find the true k nearest neighbours.
4. **Result**: ~log₂(1000) ≈ 10 layer transitions, each with local neighbourhood examination. Total comparisons: ~100-500 instead of 1000.

## Common Pitfalls

- Confusing HNSW with exact nearest neighbour search — it's *approximate*. Recall < 1.0 is expected.
- Setting M too low sacrifices recall; setting it too high wastes memory (diminishing returns past ~32-64)
- The graph is *not* a tree — it's a layered graph with cycles. The skip list analogy is structural, not exact.
- Build order matters: inserting similar items together can create poor long-range shortcuts
- HNSW doesn't work well with very high intrinsic dimensionality (curse of dimensionality still applies)
- The algorithm is patented (US patent by Malkov et al.) — check licensing for commercial use

## Connections

- [[kleinberg-decentralized-search]] — the theoretical foundation: navigability requires specific long-range link distributions
- [[small-world-property]] — HNSW exploits the small-world property (logarithmic distances)
- [[watts-strogatz-model]] — the "few random shortcuts collapse distance" principle
- [[scale-free-networks]] — HNSW's hub structure resembles heavy-tailed degree distributions
- [[node-embeddings]] — HNSW indexes are built over embedding vectors from DeepWalk, node2vec, or GNNs
- [[link-prediction-via-embeddings]] — HNSW enables fast retrieval in the embedding → prediction pipeline
- [[network-science-l07]] — lecture introducing HNSW as Kleinberg's principle in practice
- [[network-science-l09]] — lecture connecting embeddings to HNSW retrieval

## Open Questions

- How does HNSW perform as intrinsic dimensionality increases beyond ~100?
- Can we dynamically update HNSW graphs without rebuilding (for streaming data)?
- How do graph transformers compare to HNSW for retrieval-augmented generation (RAG)?
