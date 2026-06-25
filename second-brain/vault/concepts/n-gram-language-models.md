---
title: "N-Gram Language Models"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [tokenization-and-token-types]
---

## One-line Summary
N-gram language models estimate the probability of a token sequence by conditioning each token on the previous n-1 tokens — the statistical foundation for measuring [[code-naturalness-hypothesis]].

## Core Intuition
Language is predictable. After the word "I", you're more likely to see "want" than "xylophone". N-gram models capture this by counting how often each token follows its preceding context. For code: after `int`, you're likely to see a variable name; after `if`, you expect `(`. These regularities are the basis of the [[code-naturalness-hypothesis]].

## Formal Definition / Statement
A **language model** assigns a probability to any token sequence s = a₁a₂…aₙ:

**Chain rule decomposition:**
```
p(s) = p(a₁) × p(a₂|a₁) × p(a₃|a₁a₂) × … × p(aₙ|a₁…aₙ₋₁)
```

**Markov assumption** (n-gram approximation): each token depends only on the previous n-1 tokens:
```
p(aᵢ | a₁…aᵢ₋₁) ≈ p(aᵢ | aᵢ₋ₙ₊₁ … aᵢ₋₁)
```

Special cases:
| n | Name | Formula |
|---|------|---------|
| 1 | **Unigram** | P(a₁…aₙ) ≈ ∏ P(aᵢ) |
| 2 | **Bigram** | P(a₁…aₙ) ≈ ∏ P(aᵢ\|aᵢ₋₁) |
| 3 | **Trigram** | P(a₁…aₙ) ≈ ∏ P(aᵢ\|aᵢ₋₂aᵢ₋₁) |

**Maximum Likelihood Estimation (MLE):**
```
P(aᵢ | aᵢ₋₁) = count(aᵢ₋₁, aᵢ) / count(aᵢ₋₁)
```

Generalized:
```
P(a₄ | a₁a₂a₃) = count(a₁a₂a₃a₄) / count(a₁a₂a₃*)
```
where `*` represents any token.

## Key Properties
- N-gram models are **local**: only the last n-1 tokens matter (Markov property)
- Larger n → more context → better predictions, but **exponential data sparsity**
- A trigram model over a vocabulary of 10⁴ tokens has 10¹² possible parameters — far more than any training corpus
- Probabilities are estimated by **frequency counting** on a training corpus
- **Sparsity problem**: unseen n-grams get probability 0 → infinitely surprising

## Worked Example
From the lecture (Berkeley Restaurant Project corpus):

To estimate P("I want chinese food"):
```
P(<s>I want chinese food</s>) =
    P(I | <s>) ×
    P(want | I) ×
    P(chinese | want) ×
    P(food | chinese) ×
    P(</s> | food)
= .25 × .33 × .0065 × .52 × .68
= .00019
```

Each factor is computed from corpus counts, e.g.:
```
P(want | I) = count("I want") / count("I *") = ...
```

**Unigram generation** (n=1) produces random word salad:
`"fth, an, of, futures, the, an, incorporated, a, a, the..."`

**Bigram generation** (n=2) is more coherent but still nonsensical:
`"this, would, be, a, record, november"`

Higher n produces increasingly realistic text — this is the core idea behind measuring [[code-naturalness-hypothesis]].

## Common Pitfalls
- **Zero probabilities**: any unseen n-gram makes the entire product zero → requires [[smoothing-techniques]]
- **Domain dependence**: a model trained on English text is useless for Java code (and vice versa)
- Log probabilities are preferred over raw products to avoid numerical underflow:
  `p₁ × p₂ × p₃ = exp(log(p₁) + log(p₂) + log(p₃))`

## Connections
- [[code-naturalness-hypothesis]] — applies n-gram models to source code tokens
- [[perplexity-and-entropy]] — metrics to evaluate n-gram model quality
- [[smoothing-techniques]] — solutions for the zero-probability problem
- [[tokenization-and-token-types]] — tokens are the "words" in code n-gram models
- [[surprisal-and-code-prediction]] — surprisal is derived directly from n-gram probabilities

## Open Questions
- What n works best for source code? (Hindle et al. used n=6 for code vs n=3-4 for English)
- How does the vocabulary size of code compare to natural language?
- Can n-gram models capture long-range dependencies in code (e.g., matching braces)?
