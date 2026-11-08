---
title: "Embedding-Based Community Detection"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Embedding-based community detection uses node embeddings (from random walks or neural networks) to detect communities — handling overlapping memberships and node features.

## Core Intuition
Instead of optimising a quality function directly on the graph, embedding-based methods first represent each node as a vector (embedding), then cluster the vectors. This can capture overlapping communities (nodes belonging to multiple groups) and incorporate node features.

## Formal Definition / Statement
**Approach:**
1. Generate node embeddings using random walks (node2vec) or neural message passing (GNNs)
2. Cluster the embeddings using k-means or other clustering methods
3. Assign each node to one or more communities

**Methods:**
- **node2vec + clustering**: random-walk embeddings + k-means
- **GNN-based**: neural message passing + clustering or classification

**Advantages:**
- Handles overlapping communities (soft membership)
- Can incorporate node features
- Scales to large graphs

**Disadvantages:**
- Needs k (number of communities) in advance
- Hyperparameters for walks and training
- Less interpretable than modularity-based methods

## Key Properties / Complexity
1. **Overlapping communities**: nodes can belong to multiple groups
2. **Node features**: can incorporate attributes beyond graph structure
3. **Scalable**: random walks and neural networks scale to large graphs
4. **Hyperparameter-sensitive**: walk length, number of walks, embedding dimension, etc.
5. **Less interpretable**: embeddings are high-dimensional vectors, not intuitive structures

## Worked Example
Graph with overlapping communities (nodes A and B belong to both communities):

**Traditional methods:** assign each node to exactly one community
**Embedding-based:** A and B have embeddings that place them between the two community clusters → soft membership

**Result:** A and B are detected as belonging to both communities.

## Common Pitfalls
1. **Confusing embedding-based with traditional methods**: traditional methods assign each node to one community; embedding-based can assign to multiple
2. **Ignoring that embedding-based needs k**: must specify the number of communities in advance
3. **Over-interpreting embeddings**: high-dimensional vectors are not intuitive
4. **Forgetting that embedding-based is hyperparameter-sensitive**: different settings yield different results

## Connections
- [[community-detection]] — the overarching problem
- [[louvain-algorithm]] — traditional method (no overlapping)
- [[leiden-algorithm]] — traditional method (no overlapping)
- [[modularity]] — traditional objective (no overlapping)
- [[node2vec]] — generates the random-walk embeddings used in the embedding + clustering pipeline
- [[graph-neural-networks]] — neural message passing alternative for learning node embeddings
- [[network-science-l04]] — lecture overview

## Open Questions
- How do embedding-based methods compare to traditional methods on specific networks?
- Can we design embeddings that are more interpretable?
- How do we choose the right number of communities for embedding-based methods?
