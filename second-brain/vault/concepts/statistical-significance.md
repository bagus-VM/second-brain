---
title: "Statistical Significance"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [p-values]
---

# Statistical Significance

## One-line Summary
A result is statistically significant when the p-value falls below a pre-defined significance level α, indicating the data is unlikely under the null hypothesis.

## Core Intuition
"Significant" in statistics means "unlikely to have occurred by chance alone"—*not* "important" or "large." This common confusion is one of the biggest sources of misinterpretation in science.

## Formal Definition / Statement
- **Significance level α:** A threshold chosen before the experiment (typically 0.05).
- A result is **statistically significant** if **p ≤ α**.
- This means: if H₀ were true, there's at most an α probability of observing data this extreme.
- **Type I error (false positive):** Rejecting H₀ when it is true. Probability = α.
- **Type II error (false negative):** Failing to reject H₀ when it is false. Probability = β.
- **Power = 1 - β:** Probability of correctly rejecting a false H₀.

## Key Properties / Complexity
- α is chosen *before* the experiment, not after seeing the data.
- Common values: α = 0.05 (5%), α = 0.01 (1%), α = 0.001 (0.1%).
- Multiple testing: if you run 20 tests at α = 0.05, you expect ~1 false positive by chance.
- Bonferroni correction: divide α by the number of tests.

## Worked Example
- You test 5 different configurations of a system against a baseline.
- At α = 0.05, you expect 0.25 false positives (5 × 0.05).
- If you find 1 configuration with p = 0.04, is it a true effect or a false positive?
- Using Bonferroni: adjusted α = 0.05 / 5 = 0.01. Since 0.04 > 0.01, the result is *not* significant after correction.

## Common Pitfalls
- **Confusing significance with importance.** A tiny effect can be "significant" with enough data.
- **Not pre-registering α.** Choosing α after seeing the data is p-hacking.
- **Ignoring power.** A study with low power (small sample) can miss real effects.
- **Multiple comparisons without correction.** Running many tests inflates false positive rate.

## Connections
- [[p-values]] — The mechanism for determining significance.
- [[effect-sizes]] — Significance says "is there an effect?"; effect size says "how big?"
- [[confidence-intervals]] — Often more informative than a binary significant/not-significant.
- [[reproducibility-crisis]] — Overemphasis on p < 0.05 drives publication bias and non-replication.

## Open Questions
- Should we move to a lower threshold (e.g., α = 0.005)?
- How should significance be interpreted in exploratory vs. confirmatory research?
- Is "statistical significance" a useful concept at all, or should we abandon it?
