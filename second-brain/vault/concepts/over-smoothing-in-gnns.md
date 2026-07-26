---
title: "Over-Smoothing in GNNs"
tags: [concept, network-science, semester-1, graph-neural-networks]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[message-passing-framework]]"]
---

## One-line Summary
Over-smoothing is the phenomenon where stacking too many GNN layers causes all node embeddings to collapse to nearly identical vectors, destroying discriminative power.

## Core Intuition
Each GNN layer averages a node's representation with those of its neighbours. After L layers, each node's embedding is an average over its L-hop neighbourhood. For typical graphs, L = 3-5 means every node has seen most of the graph. The embeddings converge to the same vector — the graph-level average.

## Formal Definition / Statement
After L layers of message passing with mean aggregation:
$$h_v^{(L)} \approx \frac{1}{|V|} \sum_{u \in V} h_u^{(0)} \quad \text{for all } v$$

as L → ∞ on connected graphs. All nodes collapse to the same representation, making downstream tasks (classification, clustering) impossible.

This happens already at L = 3-5 for typical benchmarks (citation networks, social networks).

## Key Properties / Complexity
1. **Deeper ≠ better**: 1–3 layers is often optimal
2. Affects all GNN variants that use neighbourhood averaging (GCN, GraphSAGE, GAT)
3. Root cause: repeated averaging smooths out node-specific information
4. Related to random walks: after many steps, a random walk converges to the stationary distribution regardless of the starting node

## Worked Example
Citation network with 10 layers:
- Layer 1: each paper aggregates info from papers it cites (1-hop)
- Layer 3: each paper sees papers 3 hops away — already most of a small connected component
- Layer 10: all papers have essentially the same embedding → classification accuracy drops to random

## Common Pitfalls
- Assuming more layers always helps (the opposite is true for GNNs)
- Confusing over-smoothing with overfitting (over-smoothing is a structural problem, not a data problem)
- Using deep architectures from computer vision (ResNet-style) without adaptation
- Not checking if the graph is small enough that 2-3 layers already cover most nodes

## Remedies
1. Residual connections (JKNet): skip connections preserve earlier representations
2. Edge-weight normalisation: control the averaging strength
3. Explicit node-pair features: add features that distinguish nodes directly
4. Use fewer layers: 1-3 is often enough
5. JumpingKnowledge: concatenate representations from all layers

## Connections
- [[message-passing-framework]] — the framework that produces over-smoothing
- [[graph-neural-networks]] — all GNN variants are affected
- [[node-embeddings]] — over-smoothing is a key GNN limitation
- [[random-walks]] — over-smoothing is analogous to random walk convergence
- [[laplacian-eigenmaps]] — spectral methods don't have this problem (they use fixed eigenvectors)

## Open Questions
- Can we design architectures that avoid over-smoothing entirely?
- What is the optimal depth for a given graph?
- How do graph transformers handle depth without over-smoothing?
