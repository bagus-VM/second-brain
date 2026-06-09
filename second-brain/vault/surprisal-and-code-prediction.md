---
title: "Surprisal and Code Prediction"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [n-gram-language-models, perplexity-and-entropy]
---

## One-line Summary
Surprisal (information content) measures how unexpected a specific token is given its context — high surprisal at a code location may indicate novelty, complexity, or potential bugs.

## Core Intuition
If you see `if (` in Java, the next token is very predictable — likely an identifier or a negation `!`. If the model assigns high probability to the actual token, the surprisal is low. But if the token is unusual for the context, surprisal is high. This is related to [[perplexity-and-entropy]] but at the individual token level: while perplexity averages surprise across a whole document, surprisal pinpoints exactly *where* the model is surprised.

## Formal Definition / Statement
The **surprisal** (or information content) of a token aᵢ given context:

```
surprisal(aᵢ) = -log₂ P(aᵢ | aᵢ₋ₙ₊₁ … aᵢ₋₁)
```

Properties:
- surprisal ∈ [0, ∞) — always non-negative
- High probability → low surprisal (expected, "boring")
- Low probability → high surprisal (unexpected, "surprising")
- surprisal = 0 iff P = 1 (certain event)
- surprisal = ∞ iff P = 0 (impossible event — the sparsity problem, see [[smoothing-techniques]])

**Relationship to cross-entropy:**
```
H = (1/N) × Σᵢ surprisal(aᵢ)
```
Cross-entropy is the **average surprisal** across the document.

## Key Properties
- Surprisal is the building block of [[perplexity-and-entropy]]: perplexity = 2^(average surprisal)
- In NLP, surprisal correlates with reading time (higher surprisal = slower reading)
- In code, high surprisal locations may correspond to:
  - Complex logic (unusual patterns)
  - Bug-prone code (unexpected constructs)
  - Learning opportunities (novel idioms)
- Surprisal is **context-dependent**: the same token can have different surprisal in different contexts

## Worked Example
Given a bigram model trained on Java code, consider two contexts for the token `return`:

**Context 1:** `} } return`
- High probability (common pattern: end of nested blocks → return)
- Low surprisal

**Context 2:** `for (int i = 0; return`
- Very low probability (grammatically unusual)
- High surprisal → likely a bug or unusual construct

The surprisal difference quantifies how "natural" each code location is, directly connecting to [[code-naturalness-hypothesis]].

## Common Pitfalls
- Surprisal depends entirely on the model — a poor model gives misleading surprisal values
- High surprisal ≠ bug — it could be intentional unusual code
- Zero-probability tokens (unseen n-grams) have infinite surprisal — [[smoothing-techniques]] are essential
- Surprisal is not additive across token types — comparing surprisal of keywords vs identifiers requires normalization

## Connections
- [[perplexity-and-entropy]] — perplexity = 2^(average surprisal); cross-entropy = average surprisal
- [[n-gram-language-models]] — provides the probabilities from which surprisal is computed
- [[code-naturalness-hypothesis]] — low average surprisal = high naturalness
- [[buggy-code-naturalness]] — surprisal differences between buggy and non-buggy code
- [[smoothing-techniques]] — prevents infinite surprisal for unseen tokens

## Open Questions
- Can surprisal be used as a real-time bug detection signal?
- How does surprisal at the token level relate to surprisal at the AST level?
- Do code review comments correlate with high-surprisal locations?
