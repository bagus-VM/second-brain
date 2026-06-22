---
title: "Node Embeddings"
tags: [concept, network-science, semester-1, graph-embeddings]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[graph-laplacian]]"]
---

## One-line Summary
Node embeddings map each node v ∈ V to a vector z_v ∈ R^d such that graph-theoretic similarity between nodes is preserved as geometric closeness in the embedding space.

## Core Intuition
Graphs are discrete combinatorial objects — edges, triangles, communities, shortest paths. Classical ML operates on continuous vectors. Node embeddings bridge this gap: turn the graph into a set of points in R^d so we can apply clustering, classification, retrieval, and generative models.

## Formal Definition / Statement
Given a graph G = (V, E), learn a mapping z: V → R^d where d ≪ |V|, such that for nodes u, v:
- If u and v are "similar" in G (same community, similar role, co-visited by walks), then ||z_u - z_v|| is small
- If u and v are dissimilar, then ||z_u - z_v|| is large

Different methods define "similarity" differently:
- [[laplacian-eigenmaps]]: spectral (algebraic) similarity
- [[deepwalk]]: random-walk co-occurrence
- [[node2vec]]: biased walk co-occurrence (community vs. role)
- [[graph-neural-networks]]: learned similarity via message passing

## Key Properties
1. Dimensionality reduction: d ≪ |V| — compresses graph to a dense representation
2. Enables downstream ML: any vector-space algorithm applies to embeddings
3. Three generations: spectral → random-walk → GNN (each adds capabilities)
4. Trade-off: transductive (spectral, DeepWalk) vs. inductive (GNNs)
5. Feature-free (spectral, walks) vs. feature-aware (GNNs)

## Worked Example
A graph with two weakly connected clusters. [[laplacian-eigenmaps]] using the 2nd and 3rd eigenvectors of L = D - A maps nodes to R^2 where the clusters separate linearly. k-means on these embeddings recovers the communities — this is [[spectral-clustering-embeddings]].

## Common Pitfalls
- Confusing "embedding" with "feature": embeddings are learned, features are given
- Assuming all embeddings are inductive: spectral and walk-based methods need retraining for new nodes
- Ignoring the embedding dimension d: too small loses structure, too large wastes computation
- Forgetting that different methods capture different notions of similarity

## Connections
- [[laplacian-eigenmaps]] — spectral foundation
- [[deepwalk]] and [[node2vec]] — random-walk approaches
- [[graph-neural-networks]] — learned, inductive embeddings
- [[adjacency-matrix-factorization]] — unifying perspective
- [[link-prediction-via-embeddings]] — primary downstream task
- [[hierarchical-navigable-small-world]] — embeddings power HNSW retrieval (L07)
- [[graph-partitioning-cut-spectral]] — clustering on embeddings

## Open Questions
- What is the optimal embedding dimension d for a given graph?
- How to evaluate embedding quality without a downstream task?
- Can we unify spectral, walk-based, and GNN embeddings theoretically?
