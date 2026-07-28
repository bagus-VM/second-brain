---
title: "DeepWalk"
tags: [concept, network-science, semester-1, random-walks, graph-embeddings]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[random-walks]]", "[[word2vec-skip-gram]]"]
---

## One-line Summary
DeepWalk learns node embeddings by treating random walks as sentences and applying word2vec's skip-gram objective — nodes that co-occur in walks end up close in embedding space (Perozzi et al. 2014).

## Core Intuition
The key analogy: graph ≈ corpus of text.

| Language (word2vec) | Graph (DeepWalk) |
|---|---|
| Vocabulary | Node set V |
| Corpus | Collection of random walks |
| Sentence | One walk v_1, v_2, ..., v_L |
| Word | Node v_i |
| Context window | Walk window of size c |

If we generate many random walks from each node, we can reuse the entire word2vec machinery to learn node embeddings.

## Formal Definition / Statement
1. From each node v, sample γ random walks of length L (uniform random walks)
2. Slide a window of size c over each walk; emit (v, context) training pairs
3. Train skip-gram to maximise:

L = Σ_i Σ_t Σ_{-c≤j≤c, j≠0} log P(v_{t+j} | v_t)

where P(u|v) = exp(z_u · z_v) / Σ_{u'} exp(z_{u'} · z_v)

Dense softmax over |V| is too expensive → negative sampling approximates with k random non-context nodes per pair.

## Key Properties / Complexity
1. Scalable: SGD-based, no eigendecomposition needed
2. Unsupervised: no labels or features required
3. Implicitly factorises the log of a shifted PPMI matrix from walk co-occurrence (Qiu et al. 2018)
4. Connects to spectral methods: both minimise matrix factorisation objectives — the matrices differ
5. Transductive: new node requires new walks + retraining
6. Feature-free: uses only graph structure

## Worked Example
Graph with nodes v_1 through v_9. Random walk: v_1 → v_2 → v_4 → v_5 → v_7.
Window c = 2 around v_4: context = {v_1, v_2, v_5, v_7}.
Training pairs: (v_4, v_1), (v_4, v_2), (v_4, v_5), (v_4, v_7).
Repeat γ times per node. Skip-gram learns z_v such that co-walked nodes are close.

## Common Pitfalls
- Walk length L and number of walks γ are hyperparameters that matter
- Negative sampling k affects quality — too few = noisy, too many = slow
- Uniform walks blur homophily and structural equivalence — use [[node2vec]] to control
- Transductive: cannot handle new nodes without retraining
- The PPMI connection means DeepWalk is not as "novel" as it seems — it's sampled spectral embedding

## Connections
- [[node-embeddings]] — DeepWalk is a key embedding method
- [[node2vec]] — extends DeepWalk with biased walks
- [[word2vec-skip-gram]] — the NLP technique DeepWalk reuses
- [[adjacency-matrix-factorization]] — DeepWalk implicitly factorises a co-occurrence matrix
- [[laplacian-eigenmaps]] — theoretical connection via matrix factorisation
- [[random-walks]] — the source of "sentences"

## Open Questions
- How sensitive is DeepWalk to walk length and window size?
- Can we do better than uniform walks without the complexity of node2vec?
- How does the implicit PPMI matrix relate to the graph Laplacian?
