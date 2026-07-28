---
title: "Effect Sizes"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [confidence-intervals]
---


## One-line Summary
An effect size quantifies the magnitude of a difference or relationship, complementing p-values which only indicate whether an effect exists.

## Core Intuition
Statistical significance tells you *if* there's an effect; effect size tells you *how big* it is. A result can be statistically significant (p < 0.05) but have a trivially small effect size—meaning it's real but practically unimportant. Conversely, a large effect might not reach significance due to small sample size.

## Formal Definition / Statement
- **Cohen's d:** (mean₁ - mean₂) / pooled standard deviation. Common thresholds: 0.2 (small), 0.5 (medium), 0.8 (large).
- **Pearson's r:** Correlation coefficient. |r| < 0.1 (small), 0.1-0.3 (medium), > 0.3 (large).
- **R²:** Proportion of variance explained. 0.01 (small), 0.09 (medium), 0.25 (large).
- **Relative improvement:** (new - baseline) / baseline × 100%. E.g., "23% reduction in latency."

## Key Properties / Complexity
- Effect sizes are independent of sample size (unlike p-values).
- They enable comparison across studies with different sample sizes.
- They are essential for meta-analysis and power analysis.
- Always report effect sizes alongside p-values.

## Worked Example
- Algorithm A: mean = 95ms, SD = 10ms. Algorithm B: mean = 100ms, SD = 12ms.
- Cohen's d = (100 - 95) / 11 ≈ 0.45 → medium effect.
- Relative improvement: (100 - 95) / 100 = 5% reduction.
- With n = 1000, this 5% difference gives p < 0.001 (highly significant).
- With n = 10, this same 5% difference might give p = 0.4 (not significant).
- The effect size is the same; only the certainty changes.

## Common Pitfalls
- Reporting only p-values without effect sizes.
- Confusing "statistically significant" with "large effect."
- Using relative improvement without absolute values (23% of what?).
- Not standardizing effect sizes, making cross-study comparison impossible.

## Connections
- [[p-values]] — p-values indicate significance; effect sizes indicate magnitude.
- [[confidence-intervals]] — CIs show the plausible range of effect sizes.
- [[statistical-significance]] — Significance + effect size together give a complete picture.
- [[presenting-experiments]] — effect sizes should be reported in the results section of experiments.
- [[replication-crisis-and-hypothesis-testing]] — Overemphasis on significance over effect size fuels the crisis.

## Open Questions
- What thresholds are appropriate for computer science (Cohen's d was designed for psychology)?
- Should journals require effect size reporting?
- How do we compute effect sizes for non-standard metrics (e.g., F1 score, throughput)?
