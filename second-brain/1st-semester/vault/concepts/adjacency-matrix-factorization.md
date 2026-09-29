---
title: "Adjacency Matrix Factorization"
tags: [concept, network-science, semester-1, matrix-factorization, graph-embeddings]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[laplacian-eigenmaps]]", "[[deepwalk]]"]
---

## One-line Summary
A unifying view: spectral embeddings, DeepWalk, and node2vec all implicitly factorise a matrix derived from the graph — they differ only in which matrix they factorise.

## Core Intuition
Matrix factorisation is the common ancestor of all embedding methods. Given a graph-derived matrix M (adjacency, Laplacian, PPMI), find low-rank factors Z, Z^T such that Z Z^T ≈ M. The rows of Z are the node embeddings.

## Formal Definition / Statement
Different methods factorise different matrices:

| Method | Matrix M | Factorisation |
|---|---|---|
| Laplacian Eigenmaps | L = D - A | min tr(Z^T L Z) s.t. Z^T D Z = I |
| DeepWalk (long walks) | log(PPMI from walk co-occurrence) | Z Z^T ≈ log(PPMI) (Qiu et al. 2018) |
| Node2vec | log(PPMI from biased walks) | Z Z^T ≈ log(PPMI_biased) |

Qiu et al. (2018) proved that DeepWalk with long walks is implicitly factorising the log of a shifted Positive Pointwise Mutual Information (PPMI) matrix built from the random-walk co-occurrence matrix.

## Key Properties / Complexity
1. Connects spectral and random-walk methods on the same theoretical spectrum
2. Spectral: factorises the Laplacian (algebraic, global)
3. DeepWalk: factorises walk PPMI (sampled, local)
4. Both minimise a matrix factorisation objective — the matrices differ
5. The PPMI matrix captures local neighbourhood statistics; the Laplacian captures global structure

## Worked Example
Adjacency matrix A of a small graph. Spectral embedding: eigendecompose L = D - A, take bottom d eigenvectors. DeepWalk: generate walks, compute co-occurrence counts, form PPMI matrix, factorise. Both produce embeddings in R^d, but the spectral version uses exact global structure while DeepWalk approximates via sampling.

## Common Pitfalls
- This is a theoretical unification, not a practical algorithm
- The PPMI matrix is |V|×|V| and dense — we never explicitly form it
- DeepWalk approximates the factorisation via SGD on walk samples
- The "shifted" PPMI matters: without the shift, the factorisation is different

## Connections
- [[laplacian-eigenmaps]] — factorises the Laplacian
- [[deepwalk]] — factorises the walk PPMI matrix
- [[node2vec]] — factorises the biased-walk PPMI matrix
- [[node-embeddings]] — the unifying theoretical framework
- [[graph-partitioning-cut-spectral]] — eigendecomposition as factorisation

## Open Questions
- Can we design better matrices to factorise for specific tasks?
- How does the choice of walk distribution affect the implicit matrix?
- Is there a matrix factorisation view of GNNs?
