---
title: "L09: Node Representations and Graph Embeddings"
tags: [topic, network-science, semester-1, graph-embeddings]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[graph-laplacian]]", "[[random-walks]]", "[[spectral-clustering]]", "[[word2vec-skip-gram]]"]
---

## One-line Summary
L09 shows how to map every node to a vector in R^d preserving graph structure — from spectral eigenmaps through random-walk methods (DeepWalk, node2vec) to graph neural networks — and connects embeddings to the HNSW retrieval pipeline from L07.

## Core Intuition
Graphs are discrete objects; ML needs continuous vectors. The central question: can every node be a point in R^d such that graph similarity becomes geometric closeness? Different methods define "similarity" differently — spectral methods use algebraic structure, random walks use co-occurrence, GNNs use learned message passing with features.

## The Three Waves of Embedding Methods

### Wave 1: Spectral Methods
- [[laplacian-eigenmaps]] — eigenvectors of L = D - A give node coordinates
- Principled, globally optimal, but O(|E|·d) per iteration
- Transductive: new node = recompute everything
- [[spectral-clustering-embeddings]] = k-means on Laplacian eigenmaps

### Wave 2: Random-Walk Methods
- [[deepwalk]] — uniform random walks + word2vec skip-gram
- [[node2vec]] — biased walks with return param p and in-out param q
- Scalable (SGD, no eigendecomposition), still transductive and feature-free
- Implicitly factorise a walk co-occurrence PPMI matrix (Qiu et al. 2018)

### Wave 3: Graph Neural Networks
- [[message-passing-framework]] — AGG + UPDATE per layer
- [[graph-neural-networks]]: GCN, GraphSAGE, GAT, GIN
- Inductive + feature-aware + end-to-end trainable
- [[over-smoothing-in-gnns]] limits depth to ~3-5 layers

## Method Comparison

| Method | Scales to | Inductive | Feature-aware |
|---|---|---|---|
| Laplacian Eigenmaps | ≤ 10^6 nodes | No | No |
| DeepWalk / node2vec | 10^9 edges | No | No |
| GCN / GraphSAGE / GAT | 10^9 edges | Yes | Yes |

## The Retrieval Pipeline (connecting to L07)
1. Build embeddings z_v ∈ R^d
2. Build HNSW index over embeddings
3. Query → top-k nearest neighbours in O(log n)
4. Use for [[link-prediction-via-embeddings]], recommendation, RAG

## Key Concepts
- [[node-embeddings]]
- [[laplacian-eigenmaps]]
- [[deepwalk]]
- [[node2vec]]
- [[graph-neural-networks]]
- [[message-passing-framework]]
- [[over-smoothing-in-gnns]]
- [[spectral-clustering-embeddings]]
- [[link-prediction-via-embeddings]]
- [[adjacency-matrix-factorization]]

## Connections to Other Lectures
- L07 ([[hierarchical-navigable-small-world]]) — embeddings power HNSW retrieval
- L06 ([[signed-networks]]) — signed Laplacian embeds friend/enemy structure
- L08 — process-structure comparison (complementary gap)
- [[spectral-clustering]] from earlier lectures = k-means on eigenmaps

## Open Questions
- How do graph transformers and foundation models (2024-2026) extend message passing?
- What are the theoretical limits of random-walk co-occurrence factorisation?
- How to handle heterogeneous graphs with multiple node/edge types?
