---
title: "P-Values"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [null-and-alternative-hypothesis]
---

# P-Values

## One-line Summary
A p-value is the probability of observing data as extreme as the result, assuming the null hypothesis is true.

## Core Intuition
The p-value measures *surprise*: if H₀ is true, how likely is it that we'd see data this extreme? A small p-value means the data is unlikely under H₀, giving us reason to doubt H₀.

## Formal Definition / Statement
- **p-value = P(data ≥ observed | H₀ is true)**
- It is *not* the probability that H₀ is true.
- It is *not* the probability that the result is due to chance.
- It *is* the probability of getting a result at least as extreme as observed, if there were truly no effect.
- Common threshold: **α = 0.05** (5%). If p < α, the result is "statistically significant."

## Key Properties / Complexity
- p-values are continuous from 0 to 1.
- Smaller p → stronger evidence against H₀.
- p = 0.05 means a 5% chance of seeing this data *if H₀ is true*.
- p-values depend on sample size: with enough data, even trivial effects become "significant."

## Worked Example
- You test two algorithms. Algorithm A: mean = 95ms, Algorithm B: mean = 100ms.
- t-test gives p = 0.03.
- Interpretation: If there were truly no difference, there's a 3% chance of observing a difference this large.
- Since 0.03 < 0.05, you reject H₀ and conclude the difference is statistically significant.
- But is it *practically* significant? A 5ms difference may not matter. → See [[effect-sizes]].

## Common Pitfalls
- **p ≠ P(H₀ is true):** A p-value of 0.05 does *not* mean there's a 5% chance H₀ is true.
- **p-hacking:** Running many tests, subsetting data, or trying different metrics until p < 0.05.
- **Publication bias:** Only publishing p < 0.05 results inflates the literature with false positives.
- **Confusing significance with importance:** p < 0.05 does not mean the effect is large or meaningful.

## Connections
- [[null-and-alternative-hypothesis]] — p-values evaluate evidence against H₀.
- [[statistical-significance]] — The threshold α determines when p is "significant."
- [[confidence-intervals]] — Provide more information than a binary significant/not-significant decision.
- [[effect-sizes]] — Complement p-values by quantifying *how large* the effect is.
- [[reproducibility-crisis]] — Overreliance on p-values is a major contributor.

## Open Questions
- Should we abandon p-values in favour of Bayesian methods?
- How should we adjust p-values for multiple comparisons?
- Is the 0.05 threshold arbitrary? Should it be 0.005 (as some propose)?
