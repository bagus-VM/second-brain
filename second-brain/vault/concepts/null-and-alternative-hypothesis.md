---
title: "Null and Alternative Hypothesis"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [hypothesis-formulation]
---


## One-line Summary
The null hypothesis (H₀) assumes no effect; the alternative hypothesis (H₁) claims an effect exists. Statistical testing evaluates evidence against H₀.

## Core Intuition
In reproducible science, we don't "prove" our method works—we gather evidence *against* the assumption that it doesn't. This asymmetry is fundamental: we can only reject or fail to reject the null hypothesis, never confirm the alternative directly.

## Formal Definition / Statement
- **H₀ (Null Hypothesis):** The default assumption—no difference, no effect, no relationship. Example: "The new system has the same average query latency as the baseline."
- **H₁ (Alternative Hypothesis):** The research claim—there *is* a difference or effect. Example: "The new system has lower average query latency than the baseline."
- A statistical test produces a **p-value**: the probability of observing data as extreme as what we got, *if H₀ were true*.
- If p-value < α (significance level, typically 0.05), we reject H₀.

## Key Properties / Complexity
- H₀ is always the "no effect" claim.
- H₁ can be one-tailed (directional) or two-tailed (any difference).
- Rejecting H₀ does *not* prove H₁; it just means the data is unlikely under H₀.
- Failing to reject H₀ does not prove H₀ is true—absence of evidence ≠ evidence of absence.

## Worked Example
- H₀: "Algorithm A and Algorithm B have the same average runtime."
- H₁: "Algorithm A is faster than Algorithm B on average."
- Run both algorithms multiple times, compute means, run a t-test.
- If p = 0.03 < 0.05, reject H₀ → evidence that A is faster.
- If p = 0.12, fail to reject H₀ → insufficient evidence (but not proof of equality).

## Common Pitfalls
- Confusing "fail to reject H₀" with "H₀ is true."
- One-tailed vs. two-tailed: using a one-tailed test when you should test for *any* difference.
- p-hacking: running many tests until one gives p < 0.05.

## Connections
- [[hypothesis-formulation]] — H₁ must be well-formulated to be testable.
- [[p-values]] — The mechanism for evaluating H₀.
- [[statistical-significance]] — The threshold for rejecting H₀.
- [[confidence-intervals]] — An alternative/complement to hypothesis testing.
- [[reproducibility-crisis]] — Misuse of null hypothesis testing contributes to non-replication.

## Open Questions
- Should we move beyond null hypothesis testing toward estimation (confidence intervals, effect sizes)?
- How should pre-registration change how we formulate H₀ and H₁?
