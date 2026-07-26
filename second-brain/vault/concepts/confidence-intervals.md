---
title: "Confidence Intervals"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [statistical-significance]
---

# Confidence Intervals

## One-line Summary
A confidence interval gives a range of plausible values for a parameter, providing more information than a binary significant/not-significant decision.

## Core Intuition
Instead of just asking "is there an effect?" (hypothesis testing), a confidence interval asks "how large could the effect be?" This is more informative for reproducibility: it tells you the precision of your estimate and whether the effect is practically meaningful.

## Formal Definition / Statement
- A **95% confidence interval** [L, U] means: if we repeated the experiment many times, 95% of the computed intervals would contain the true parameter value.
- **Not** "there is a 95% probability the true value is in [L, U]" (a common misinterpretation).
- Computed as: estimate ± (critical value × standard error).
- For a 95% CI with a normal distribution: estimate ± 1.96 × SE.

## Key Properties / Complexity
- Wider intervals → less precision (smaller sample, more variability).
- Narrower intervals → more precision (larger sample, less variability).
- If a 95% CI for a difference does not include 0, the result is significant at α = 0.05.
- CIs show both the magnitude and uncertainty of an effect.

## Worked Example
- Algorithm A averages 95ms, Algorithm B averages 100ms.
- 95% CI for the difference: [2ms, 8ms].
- Interpretation: the true difference is likely between 2ms and 8ms.
- Since 0 is not in the interval, the difference is statistically significant.
- But is 2-8ms practically important? That depends on the application.

## Common Pitfalls
- Misinterpreting "95% confidence" as "95% probability the true value is here."
- Reporting only the point estimate without the interval.
- Using CIs without understanding the underlying assumptions (normality, independence).

## Connections
- [[p-values]] — CI and p-values are mathematically related but CIs are more informative.
- [[effect-sizes]] — CIs quantify the range of plausible effect sizes.
- [[statistical-significance]] — CI that excludes 0 ≡ p < 0.05 (for two-sided tests).
- [[presenting-experiments]] — confidence intervals should be shown in the results section to convey uncertainty.
- [[hypothesis-formulation]] — Well-formulated hypotheses specify what the CI should cover.

## Open Questions
- Should CIs replace p-values as the standard reporting method?
- How should we interpret CIs in Bayesian vs. frequentist frameworks?
