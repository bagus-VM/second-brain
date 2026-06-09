---
title: "Graph Neural Networks"
tags: [concept, network-science, semester-1, graph-neural-networks, deep-learning]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[message-passing-framework]]", "[[deepwalk]]"]
---

## One-line Summary
Graph Neural Networks learn node embeddings through repeated message passing — each layer extends the receptive field by one hop — making them inductive, feature-aware, and end-to-end trainable.

## Core Intuition
Unlike spectral methods or random-walk embeddings, GNNs can use node features (text, images, tabular data) and learn task-specific representations. Each GNN layer lets a node aggregate information from its immediate neighbours; stacking L layers gives each node a view of its L-hop neighbourhood.

## Formal Definition / Statement
See [[message-passing-framework]] for the general formulation. Four key variants:

### GCN (Kipf & Welling 2017)
- AGG = normalised sum: Ã = D̃^{-1/2}(A + I)D̃^{-1/2}
- h_v^{(l+1)} = σ(Ã H^{(l)} W^{(l)})
- Simple, fast, widely used baseline

### GraphSAGE (Hamilton et al. 2017)
- AGG on a sampled subset of neighbours
- Scales to very large graphs
- Inductive by design: can generalise to unseen nodes

### GAT (Veličković et al. 2018)
- AGG weighted by learned attention α_{uv}
- Different neighbours contribute differently

### GIN (Xu et al. 2019)
- AGG = sum; UPDATE = MLP
- Provably as powerful as the Weisfeiler-Lehman graph isomorphism test

## Key Properties
1. Inductive: new nodes can be embedded without retraining (features → embedding)
2. Feature-aware: initial h_v^{(0)} can be node attributes, one-hot IDs, or pretrained embeddings
3. End-to-end trainable: embeddings optimised for the downstream task
4. Receptive field = L hops after L layers
5. Over-smoothing: too many layers collapse all embeddings to the same vector

## Worked Example
2-layer GCN on a citation network to predict paper topics:
- Receptive field: 2-hop neighbourhood (papers cited by papers you cite)
- Stacking 10 layers: each paper sees ~10-hop neighbourhood → all see the entire graph → embeddings collapse (over-smoothing)
- Adding a new paper tomorrow: can predict topic without retraining (inductive)

## Common Pitfalls
- [[over-smoothing-in-gnns]]: L = 3-5 layers is typically the limit
- GNNs are not universally better: on graphs without features, DeepWalk/node2vec can be competitive
- Message passing is permutation-invariant by design — this is a feature, not a bug
- Choosing the right variant: GCN for simplicity, GraphSAGE for scale, GAT for heterogeneous importance, GIN for expressiveness

## Connections
- [[message-passing-framework]] — the general GNN formulation
- [[over-smoothing-in-gnns]] — the key limitation
- [[node-embeddings]] — third wave of embedding methods
- [[deepwalk]] and [[node2vec]] — predecessors (feature-free, transductive)
- [[link-prediction-via-embeddings]] — GNN embeddings are state-of-the-art for link prediction
- [[embedding-based-community-detection]] — GNN embeddings can be clustered for community detection with node features
- [[graph-laplacian]] — GCN's normalised sum is related to spectral filtering

## Open Questions
- How to go deeper without over-smoothing (residual connections, edge normalisation)?
- Graph transformers: do they replace message passing entirely?
- How to handle heterogeneous graphs with multiple node/edge types?
