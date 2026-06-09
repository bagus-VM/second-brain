---
title: "Normalized Cut"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Normalized cut balances the size of a cut against the total degree (volume) of the clusters it separates — preventing the trivial solution of cutting off a single node.

## Core Intuition
A raw min-cut can be trivially small by isolating a single node. Normalized cut fixes this by dividing the cut size by the total degree of each cluster, ensuring the partition is balanced.

## Formal Definition / Statement
For a partition of V into two sets A and B:

**Normalized cut:**
Ncut(A, B) = cut(A, B) / vol(A) + cut(A, B) / vol(B)

where:
- cut(A, B) = number of edges between A and B
- vol(A) = Σ_{i ∈ A} k_i (total degree of nodes in A)
- vol(B) = Σ_{i ∈ B} k_i (total degree of nodes in B)

**Normalized association:**
Nassoc(A, B) = assoc(A, A) / vol(A) + assoc(B, B) / vol(B)

where assoc(A, A) = number of internal edges in A.

**Relationship:** Ncut(A, B) = 2 - Nassoc(A, B)

**Approximation:** the normalized cut can be approximately minimized using the Fiedler vector of the normalized Laplacian L_norm = D^(-1/2) L D^(-1/2).

## Key Properties
1. **Balanced partitions**: prevents trivial solutions (cutting off a single node)
2. **Normalized by volume**: accounts for cluster size, not just cut size
3. **NP-hard to minimize exactly**: spectral methods provide approximations
4. **Connects to spectral partitioning**: the Fiedler vector of the normalized Laplacian approximates the optimal normalized cut
5. **Used in image segmentation**: originally developed for computer vision

## Worked Example
Graph with two clusters of different sizes:

**Raw min-cut:** might cut off a single peripheral node (trivial)
**Normalized cut:** divides cut size by cluster volumes — a cut between two large clusters is penalized less than a cut isolating a single node

Example: if cut(A, B) = 5, vol(A) = 50, vol(B) = 100:
Ncut = 5/50 + 5/100 = 0.1 + 0.05 = 0.15

## Common Pitfalls
1. **Confusing normalized cut with raw cut**: raw cut favors small clusters; normalized cut balances
2. **Assuming normalized cut is easy to minimize**: it's NP-hard; spectral methods are approximations
3. **Ignoring that normalized cut needs k**: for k > 2, must specify the number of clusters
4. **Confusing normalized cut with [[conductance]]**: they are related but distinct measures

## Connections
- [[spectral-partitioning]] — spectral methods approximate normalized cut
- [[graph-laplacian]] — the normalized Laplacian is used for the approximation
- [[conductance]] — related but distinct community quality measure
- [[modularity]] — alternative community quality objective
- [[community-detection]] — the overarching problem
- [[network-science-l04]] — lecture overview

## Open Questions
- How does normalized cut compare to modularity on real-world networks?
- Can we extend normalized cut to overlapping communities?
- How do we choose between normalized cut and conductance?
