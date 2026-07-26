---
title: "Smoothing Techniques"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [n-gram-language-models]
---

## One-line Summary
Smoothing techniques redistribute probability mass from seen to unseen n-grams, preventing zero probabilities that would make [[perplexity-and-entropy|cross-entropy]] infinite.

## Core Intuition
A trigram model over a 10,000-token vocabulary has 10¹² possible trigrams — but any real corpus contains far fewer. Most n-grams will never appear in training data, yet assigning them zero probability is catastrophic: any test sentence containing an unseen trigram gets total probability zero. Smoothing "steals" a little probability from frequent events and gives it to unseen ones, ensuring no event is completely impossible.

## Formal Definition / Statement
Given an n-gram model with vocabulary V, the **sparsity problem**:
- A trigram model with |V| = 10⁴ has 10¹² possible parameters
- A typical training corpus has far fewer trigrams
- Unseen n-grams: P = 0 → surprisal = ∞ ([[surprisal-and-code-prediction]])

**Smoothing** = redistributing probability mass:
```
P_smoothed(aᵢ | context) > 0   for all aᵢ ∈ V
```

The lecture mentions several techniques:
- **Add-one (Laplace)**: add 1 to every count → P(aᵢ|aᵢ₋₁) = [count(aᵢ₋₁,aᵢ) + 1] / [count(aᵢ₋₁) + |V|]
- **Good-Turing estimate**: adjust counts based on frequency of frequencies
- **Jelinek-Mercer (interpolation)**: linearly combine unigram, bigram, trigram estimates
- **Katz smoothing (backoff)**: use lower-order n-gram when higher-order count is zero
- **Witten-Bell smoothing**: reserve probability mass proportional to number of unique following tokens
- **Absolute discounting**: subtract a fixed constant from each count
- **Kneser-Ney smoothing**: best known method — uses continuation probabilities instead of raw counts
- **Modified Kneser-Ney**: variant with multiple discount values

## Key Properties / Complexity
- Add-one is simple but too aggressive — it gives too much probability to unseen events
- **Backoff** uses lower-order models when higher-order counts are zero (fall back from trigram to bigram to unigram)
- **Interpolation** blends all orders simultaneously (weighted average)
- Kneser-Ney is generally the best-performing method for natural language
- All smoothing methods reduce [[perplexity-and-entropy|perplexity]] on test data compared to unsmoothed models

## Worked Example
**Add-one (Laplace) smoothing:**

Training corpus (from lecture):
```
<s> I am Sam </s>
<s> Sam I am </s>
<s> I do not like green eggs and ham </s>
```

Unsmoothed bigram probabilities:
```
P(I | <s>) = 2/3    P(Sam | <s>) = 1/3
P(am | I) = 2/3     P(do | I) = 1/3
P(Sam | am) = 1/2   P(</s> | Sam) = 1/2
```

With add-one smoothing (|V| = 9 including <s> and </s>):
```
P(I | <s>) = (2+1)/(3+9) = 3/12 = 0.25
P(Sam | <s>) = (1+1)/(3+9) = 2/12 = 0.17
```

Note: all probabilities decreased (because probability mass was redistributed to unseen bigrams like P(eggs|I) = 0+1/12).

## Common Pitfalls
- Add-one smoothing is almost never used in practice — it distorts distributions too much
- Smoothing doesn't eliminate [[surprisal-and-code-prediction|surprisal]], it just caps it
- The choice of smoothing method significantly affects model quality — Kneser-Ney is preferred for text, but the optimal choice for code may differ
- Smoothing parameters (discount values) often need tuning on held-out data

## Connections
- [[n-gram-language-models]] — smoothing fixes the zero-probability problem in n-gram models
- [[perplexity-and-entropy]] — smoothing reduces perplexity on test data
- [[surprisal-and-code-prediction]] — smoothing prevents infinite surprisal for unseen tokens
- [[code-naturalness-hypothesis]] — smoothed models are used to measure code naturalness

## Open Questions
- Which smoothing method works best for source code (vs natural language)?
- How does the vocabulary size of programming languages affect smoothing choices?
- Can character-level models reduce the sparsity problem for code?
