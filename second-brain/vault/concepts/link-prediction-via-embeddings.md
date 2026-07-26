---
title: "Link Prediction via Embeddings"
tags: [concept, network-science, semester-1, link-prediction, graph-embeddings]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[node-embeddings]]", "[[deepwalk]]", "[[node2vec]]"]
---

## One-line Summary
Link prediction via embeddings scores potential edges by the proximity of node vectors — if z_u and z_v are close in embedding space, the edge (u, v) likely exists or should exist.

## Core Intuition
Once every node has an embedding z_v ∈ R^d, predicting links becomes a simple geometric operation: compute similarity (dot product, cosine, or negative distance) between node pairs. High similarity → likely edge. This transforms a structural graph problem into a vector-space problem.

## Formal Definition / Statement
Given learned embeddings z_v for all v ∈ V:
1. Score each candidate pair (u, v): score(u, v) = z_u^T · z_v (dot product) or cos(z_u, z_v)
2. Rank all non-observed pairs by score
3. Top-k pairs are predicted links

The full retrieval pipeline:
1. Build embeddings z_v ∈ R^d (spectral, DeepWalk, node2vec, or GNN)
2. Build [[hierarchical-navigable-small-world]] index over embeddings
3. Query z_q → top-k nearest z_v in O(log n)
4. Use for link prediction, recommendation, RAG, semantic search

## Key Properties / Complexity
1. Embedding quality determines prediction quality
2. Any embedding method works: spectral, random-walk, or GNN
3. HNSW indexing makes retrieval O(log n) instead of O(n²)
4. Same pipeline powers: product recommendation (Amazon), friend suggestion (LinkedIn), fraud detection (PayPal), RAG for LLMs

## Worked Example
Social network: predict missing friendships.
1. Train node2vec with p=1, q=0.5 (community-oriented)
2. For each user, get z_v ∈ R^128
3. For non-friends (u, v), compute z_u^T · z_v
4. Top scores → friend suggestions

## Common Pitfalls
- Cold-start: new nodes have no embedding (transductive methods need retraining)
- Evaluation: must use temporal split (train on past, test on future), not random split
- Embedding dimension: too small loses information, too large overfits
- Ignoring that link prediction quality depends on the embedding method's notion of similarity

## Connections
- [[node-embeddings]] — the embeddings being used
- [[hierarchical-navigable-small-world]] — the index for fast retrieval (L07)
- [[deepwalk]] and [[node2vec]] — common embedding methods for link prediction
- [[graph-neural-networks]] — state-of-the-art for feature-aware link prediction
- [[adjacency-matrix-factorization]] — theoretical connection

## Open Questions
- How to handle dynamic graphs where links appear/disappear over time?
- Can we predict links in heterogeneous graphs (different node/edge types)?
- What is the relationship between embedding-based and heuristic-based link prediction?
