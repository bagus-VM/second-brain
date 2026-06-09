---
title: "Message Passing Framework"
tags: [concept, network-science, semester-1, graph-neural-networks]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
The message-passing framework defines how GNNs compute node embeddings: each layer, every node aggregates messages from its neighbours (AGG) and updates its state (UPDATE), extending its receptive field by one hop.

## Core Intuition
A node's representation should depend on its neighbourhood. Each GNN layer lets a node "listen" to its immediate neighbours. After L layers, a node has information from its entire L-hop neighbourhood. The framework is: receive messages → aggregate → update.

## Formal Definition / Statement
At each layer l, every node v updates its representation:

h_v^{(l+1)} = UPDATE(h_v^{(l)}, AGG({h_u^{(l)} : u ∈ N(v)}))

Where:
- AGG is a permutation-invariant function: sum, mean, max, or attention
- UPDATE is usually a learnable linear transform + nonlinearity: σ(W · [h_v, m_v])
- h_v^{(0)} = initial features (node attributes, one-hot IDs, or pretrained embeddings)

The AGG function must be permutation-invariant because node neighbourhoods are sets (no ordering).

## Key Properties
1. One GNN layer = one hop of information propagation
2. Stacking L layers → receptive field of L hops
3. AGG must be permutation-invariant (sum, mean, max, attention)
4. UPDATE combines aggregated messages with the node's own previous state
5. The framework unifies GCN, GraphSAGE, GAT, GIN as specific choices of AGG and UPDATE

## Worked Example
Node v with neighbours N(v) = {a, b, c, d, e}:
- Layer 1: v aggregates 1-hop features from {a, b, c, d, e}
- Layer 2: v's embedding now reflects 2-hop neighbourhood (neighbours of neighbours)
- Layer 3: 3-hop neighbourhood — but beware [[over-smoothing-in-gnns]]

Each layer: AGG pools neighbour states → m_v, then UPDATE combines m_v with h_v to get h_v^{(l+1)}.

## Common Pitfalls
- More layers ≠ better: over-smoothing occurs at L = 3-5
- AGG choice matters: sum is most expressive (GIN), mean is more stable, attention is adaptive
- The receptive field grows exponentially with L — computational cost grows too
- Permutation invariance is required because graphs have no canonical node ordering

## Connections
- [[graph-neural-networks]] — GCN, GraphSAGE, GAT, GIN are instances
- [[over-smoothing-in-gnns]] — the key limitation of stacking layers
- [[node-embeddings]] — message passing produces the third wave of embeddings
- [[deepwalk]] — random walks are a "sampled" version of message passing
- [[graph-laplacian]] — GCN's normalised sum relates to spectral filtering

## Open Questions
- Can we design AGG/UPDATE that avoids over-smoothing entirely?
- How does message passing relate to Weisfeiler-Lehman graph isomorphism?
- What are the expressiveness limits of message passing (cf. GIN)?
