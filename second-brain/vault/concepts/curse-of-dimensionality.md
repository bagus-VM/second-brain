---
title: "Curse of Dimensionality"
tags: [concept, multimedia-databases, semester-1, curse-of-dimensionality, indexing, high-dimensions]
course: "Multimedia Databases"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[content-based-retrieval]]", "[[feature-vector]]", "[[hierarchical-navigable-small-world|HNSW]]"]
---

## One-line Summary
The curse of dimensionality is the phenomenon that, as the number of dimensions grows, the volume of the space grows exponentially, so data becomes sparse and many algorithms (nearest-neighbour search, distance-based clustering, density estimation) become ineffective or inefficient.

## Core Intuition
In 1D, a unit interval [0, 1] has length 1. In 2D, a unit square [0, 1]² has area 1. In 3D, a unit cube [0, 1]³ has volume 1. In nD, a unit hypercube [0, 1]ⁿ has volume 1. But the *number of points needed to densely sample* the space grows exponentially with n.

For n = 100, if you want 10 samples per dimension, you need 10¹⁰⁰ samples. You will never have that much data. The result: most of the high-dimensional space is *empty*, and any given query is far from all the data points.

The practical consequences:
- **All points become roughly equidistant from a query**: the concept of "nearest" loses meaning
- **Distance-based indexes (kd-trees) fail**: above ~20 dimensions, kd-trees are no better than linear scan
- **Density estimation fails**: histograms and kernel density estimators need exponentially more data
- **Concentration of distances**: the relative difference between the nearest and farthest neighbour shrinks

## Formal Definition / Statement

The "curse of dimensionality" doesn't have a single formal definition, but several formal results quantify it:

**Volume concentration**: For a unit n-sphere inscribed in a unit n-cube, the ratio of volumes is:
    V(sphere) / V(cube) = (π^(n/2) / (2^(n+1) · Γ(n/2 + 1)))

This ratio goes to 0 as n → ∞. The sphere becomes a vanishingly small fraction of the cube.

**Distance concentration**: For n i.i.d. Gaussian random variables, the expected L2 distance from a fixed point is:
    E[d_min] / E[d_max] → 1 as n → ∞

The ratio of nearest to farthest neighbour approaches 1 — all points become "equally near".

**Sample complexity**: To cover a unit hypercube with samples spaced ε apart in each dimension requires (1/ε)ⁿ samples. For ε = 0.1 and n = 10, that's 10¹⁰ samples.

## Key Properties / Complexity

### Practical consequences
- **Kd-trees are effective for low dimensions** (< 20), but degrade to O(n) (linear scan) for high dimensions
- **Locality-sensitive hashing (LSH)** is one workaround: hash similar points to the same bucket with high probability
- **HNSW (Hierarchical Navigable Small World)** graphs scale to millions of high-dimensional vectors
- **Product quantization** compresses vectors for in-memory search
- **Dimensionality reduction** (PCA, t-SNE, UMAP) can help but loses information

### Why distance loses meaning
For n i.i.d. uniform random points in [0, 1]ⁿ:
- The expected distance from any point to its nearest neighbour grows like O(n^(1/2) · log(n) / n)
- The expected distance to the farthest point grows like O(sqrt(n))
- The ratio (nearest / farthest) approaches 1 as n grows

In high dimensions, the nearest and farthest points are nearly equidistant from the query. The "nearest neighbour" is not meaningfully closer than the "farthest".

### Why high-dimensional indexing is hard
- **Tree-based indexes** (kd-trees, R-trees) partition the space recursively. The partitions are effective when the space is dense, but in high dimensions, the partitions are mostly empty.
- **LSH** hashes similar points to the same bucket, with collision probability related to the distance. Effective but approximate.
- **Graph-based indexes** (HNSW, NSW) build a navigable small-world graph over the points. Effective and scalable.
- **Vector quantization** (PQ, OPQ) compresses vectors so millions can fit in memory.

### Empirical rules of thumb
- For n ≤ 16: kd-trees work well
- For 16 < n ≤ 100: HNSW or LSH
- For 100 < n ≤ 1000: HNSW, IVF-PQ, or ScaNN
- For n > 1000: dimensionality reduction first, then HNSW

These are not hard rules; the right choice depends on the data distribution and the query workload.

## Worked Example

Consider the difference between low and high dimensions for image similarity:
- **Low-dim (n = 10)**: a colour histogram of 10 bins. Kd-tree can find nearest neighbours in O(log n) per query.
- **Medium-dim (n = 100)**: a concatenation of multiple colour, texture, shape features. HNSW finds nearest neighbours in O(log n) per query.
- **High-dim (n = 2048)**: a CNN embedding (ResNet-50). HNSW still works, but each vector takes 8 KB (2048 floats × 4 bytes); 1 million vectors = 8 GB. Need compression (product quantization) or distributed indexes.

For 1 million 2048-dim vectors, the storage cost is 8 GB. HNSW indexes add 2-4x overhead (graph links). So 16-32 GB of RAM for the index. At this scale, you need a server with significant memory, or a distributed index.

## Common Pitfalls
- **Confusing "many features" with "high dimension"**: 1000 features is high-dim; 10 features is low-dim. The label is by feature count, not by data size.
- **Trusting nearest-neighbour results in high dimensions**: the "nearest" is not meaningfully closer than the "farthest". You may be matching noise.
- **Using kd-trees for high-dim data**: they degrade to linear scan, defeating the purpose. Use HNSW or LSH.
- **Forgetting to normalise features**: features with very different scales can dominate the distance, even in low dimensions.
- **Dimensionality reduction loses information**: PCA preserves global structure but loses local detail. t-SNE/UMAP preserve local structure but distort global. Choose carefully.

## Connections
- [[content-based-retrieval]] — the broader topic
- [[feature-vector]] — what grows with dimensionality
- [[hierarchical-navigable-small-world|HNSW]] — modern high-dim indexing
- [[minkowski-distance]] — distances that lose meaning in high dimensions
- [[multimedia-databases-lecture-06]] — the lecture

## Open Questions
- Are there distance functions that are *robust* in high dimensions (don't suffer the curse)?
- Can we design feature vectors that are intrinsically low-dimensional (e.g., using sparse representations)?
- For modern deep learning embeddings, is the curse still a problem, or has it been overcome?
- How do you choose between HNSW, LSH, and product quantization for a given workload?
