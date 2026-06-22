---
title: "Word2Vec Skip-Gram"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
Skip-gram learns a vector for each word by training a neural network to predict the surrounding words from a target word — and the same trick works for nodes in a graph.

## Core Intuition
The core insight is deceptively simple: a word's meaning is determined by the company it keeps (Firth, 1957). If two words appear in similar contexts, they should have similar vectors. Skip-gram turns this into a machine learning problem: given a target word, predict which words appear nearby in a sliding window. The network learns an embedding vector for each word that makes the prediction work. The magic is that these vectors capture *semantic relationships* — "king - man + woman ≈ queen" falls out of the geometry. The same principle applies to graphs: replace "words in a sentence" with "nodes in a random walk," and you get DeepWalk/node2vec. This is why skip-gram is the bridge between NLP and graph embeddings.

## Formal Definition / Statement

**Skip-gram model** (Mikolov et al., 2013):

Given a corpus of words w₁, w₂, ..., wₜ and a context window of size c:

**Objective**: Maximize the average log probability:
$$\frac{1}{T} \sum_{t=1}^{T} \sum_{-c \leq j \leq c, j \neq 0} \log P(w_{t+j} | w_t)$$

**Softmax probability**:
$$P(w_O | w_I) = \frac{\exp(v'_{w_O} \cdot v_{w_I})}{\sum_{w=1}^{W} \exp(v'_w \cdot v_{w_I})}$$

where v_w ∈ ℝᵈ is the input embedding and v'_w ∈ ℝᵈ is the output embedding of word w.

**Negative sampling** (efficient approximation): Instead of summing over all W words, sample k "negative" words from a noise distribution P_n(w):
$$\log \sigma(v'_{w_O} \cdot v_{w_I}) + \sum_{i=1}^{k} \mathbb{E}_{w_i \sim P_n} [\log \sigma(-v'_{w_i} \cdot v_{w_I})]$$

where σ is the sigmoid function. This reduces O(W) per update to O(k), making training feasible for large vocabularies.

**Noise distribution**: P_n(w) ∝ f(w)^{3/4} where f(w) is the word frequency — the 3/4 power balances frequent and rare words.

## Key Properties / Complexity

- **Training complexity**: O(W · d) per step with full softmax; O(k · d) with negative sampling
- **Typical dimensions**: d = 100–300 for NLP; d = 64–256 for graph embeddings
- **Negative samples**: k = 5–20 typical; more for smaller corpora
- The learned vectors capture analogies as linear offsets in vector space
- Skip-gram learns two matrices: W (input, used as the embedding) and W' (output, usually discarded)
- The model is "shallow" — a single linear projection — yet produces rich representations
- Graph adaptation: replace word sequences with random walk sequences (DeepWalk) or biased walks (node2vec)

## Worked Example

Sentence: "the cat sat on the mat"
Window size c = 2:

Training pairs (target → context):
- the → {cat, sat}
- cat → {the, sat, on}
- sat → {the, cat, on, the}
- on → {cat, sat, the, mat}
- sat → {on, the, mat}
- the → {sat, on, mat}

For the pair (cat, sat) with k=2 negative samples (say "democracy" and "piano"):
- Maximize: log σ(v'_sat · v_cat) + log σ(−v'_democracy · v_cat) + log σ(−v'_piano · v_cat)
- This pushes v_cat close to v_sat and far from v_democracy and v_piano

After training over millions of sentences, words with similar contexts (e.g., "cat" and "dog") end up with similar vectors because they must predict similar context words.

## Common Pitfalls

- Skip-gram and CBOW are different: skip-gram predicts context from target; CBOW predicts target from context
- The "king - man + woman ≈ queen" analogy works because of *linear* offsets — this is an empirical property, not a guaranteed one
- Negative sampling is not just "faster softmax" — it's a different objective that approximates the full softmax
- The 3/4 power on the noise distribution matters: uniform sampling hurts rare words; frequency-proportional sampling hurts common words
- For graph applications (DeepWalk), the "sentences" are random walks — the quality of embeddings depends on the walk strategy
- Skip-gram is transductive: it learns a fixed embedding per token. New tokens require retraining.

## Connections

- [[deepwalk]] — applies skip-gram to random walk sequences on graphs
- [[node2vec]] — extends DeepWalk with biased walks (p, q parameters)
- [[node-embeddings]] — the general framework skip-gram feeds into
- [[hierarchical-navigable-small-world]] — HNSW indexes over vectors produced by skip-gram–based methods
- [[link-prediction-via-embeddings]] — downstream task for graph embeddings
- [[graph-partitioning-cut-spectral]] — alternative embedding approach (algebraic vs. statistical)
- [[network-science-l09]] — lecture connecting NLP embeddings to graph embeddings

## Open Questions

- How do modern transformer-based embeddings (BERT, GPT) compare to skip-gram for graph tasks?
- What is the theoretical relationship between skip-gram and matrix factorization of the PPMI matrix?
- Can we learn *dynamic* embeddings that evolve as the graph changes over time?
