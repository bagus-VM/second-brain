---
title: "Perplexity and Entropy"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [n-gram-language-models]
---

## One-line Summary
Perplexity and cross-entropy are metrics for evaluating language models — perplexity measures how "confused" a model is, while cross-entropy measures how surprised a model is by a document.

## Core Intuition
Imagine you're predicting the next word in a sentence. If you're always confident and correct, your model is good. If you're constantly surprised, it's bad. Perplexity quantifies this: it's the effective number of choices the model is uncertain among at each step. A perplexity of 10 means "at each position, the model is as confused as if choosing uniformly among 10 options."

## Formal Definition / Statement
**Perplexity** (PP) of a language model on a test set W = w₁w₂…wₙ:

```
PP(W) = P(w₁w₂…wₙ)^(-1/N)
       = 1 / [∏ᵢ P(wᵢ|wᵢ₋₁)]^(1/N)
```

Interpretation: **weighted average branching factor** — the number of possible next tokens at each position.

**Cross-entropy** (H) — the log-transformed version:

```
H(s) = -(1/N) × log₂ P(a₁…aₙ)
```

Cross-entropy measures **how surprised** a model is by a document (in bits).

**Relationship**: PP = 2^H — perplexity is 2 raised to the cross-entropy power.

## Key Properties
- **Lower is better** for both metrics — a good model is less surprised
- Perplexity = 1 means perfect prediction (zero surprise)
- Perplexity = |V| (vocabulary size) means uniform random guessing
- Cross-entropy has a theoretical minimum equal to the true entropy of the source
- These metrics enable comparison across different models and domains (e.g., English vs Java code — key to [[code-naturalness-hypothesis]])

## Worked Example
**Example 1: Uniform digit language**
Each of 10 digits occurs with equal probability P = 1/10:
```
PP(W) = (1/10)^(-1) = 10
```
The model is as confused as choosing among 10 equally likely options.

**Example 2: Skewed digit distribution**
Training set: 0 occurs 91 times, each other digit once (total 100).
Test set: `0 0 0 0 0 3 0 0 0 0`
```
PP(W) = [(91/100)⁹ × (9/100)]^(1/10)
      = [0.389 × 0.09]^(0.1)
      = 1.73
```
Much lower than 10 because the model correctly expects 0 most of the time.

**Example 3: Code vs English**
The lecture showed that source code typically achieves lower cross-entropy than English text, confirming that code is more predictable — the foundation of [[code-naturalness-hypothesis]].

## Common Pitfalls
- Perplexity is **not** a probability — it's the inverse geometric mean of probabilities
- Lower perplexity doesn't always mean better model — it might just overfit the training data
- Cross-entropy depends on the test set — comparing across different test sets requires care
- Don't confuse perplexity with accuracy: a model can have low perplexity but still make wrong predictions

## Connections
- [[n-gram-language-models]] — the model whose quality perplexity measures
- [[code-naturalness-hypothesis]] — uses cross-entropy to compare code and natural language
- [[surprisal-and-code-prediction]] — individual token surprise = -log₂ P(token), cross-entropy is the average surprisal
- [[smoothing-techniques]] — smoothing affects perplexity (reduces it by eliminating zero probabilities)

## Open Questions
- What's the relationship between perplexity and practical code completion accuracy?
- How does perplexity vary across different programming languages?
- Can perplexity be used as a code quality metric?
