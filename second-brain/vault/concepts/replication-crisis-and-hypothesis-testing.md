---
title: "Replication Crisis and Hypothesis Testing"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [p-values, statistical-significance, effect-sizes]
---

# Replication Crisis and Hypothesis Testing

## One-line Summary
The replication crisis is largely driven by misuse of hypothesis testing: p-hacking, publication bias, and overreliance on p < 0.05 without considering effect sizes or power.

## Core Intuition
Many published findings cannot be replicated. A major cause is how we use (and abuse) null hypothesis testing. When the scientific incentive structure rewards "significant" results, researchers—consciously or not—engage in practices that produce false positives.

## Formal Definition / Statement
The replication crisis refers to the finding that a large proportion of published scientific results, especially in psychology, medicine, and increasingly in CS, fail to replicate when the experiments are repeated.

Key contributing factors related to hypothesis testing:
1. **p-hacking:** Trying multiple analyses until p < 0.05.
2. **Publication bias:** Journals preferentially publish significant results.
3. **HARKing:** Hypothesizing After Results are Known—presenting exploratory findings as confirmatory.
4. **Low statistical power:** Small samples miss real effects and inflate effect sizes of detected effects.
5. **Flexible stopping rules:** Collecting data until p < 0.05, then stopping.

## Key Properties / Complexity
- The "file drawer problem": non-significant results are never published.
- With α = 0.05, even a true null has a 5% chance of being rejected.
- If base rate of true effects is low, most "significant" findings may be false positives (see Positive Predictive Value).
- **PPV = (1 - β) × R / ((1 - β) × R + α)** where R = prior probability the effect is real.

## Worked Example
- 1000 hypotheses are tested. Only 100 are true effects (R = 0.1).
- With α = 0.05, power = 0.8:
  - True positives: 100 × 0.8 = 80
  - False positives: 900 × 0.05 = 45
  - Total "significant" results: 125
  - **PPV = 80/125 = 64%** — 36% of published "significant" results are false positives.
- This is before p-hacking, which makes it worse.

## Common Pitfalls
- Assuming all published p < 0.05 results are true.
- Not considering the base rate of true effects in a field.
- Treating replication failure as fraud (it's usually a systemic problem, not individual misconduct).
- Ignoring that computational experiments have their own replication challenges (random seeds, hardware, software versions).

## Connections
- [[reproducibility-crisis]] — The broader crisis; hypothesis testing is one major contributor.
- [[p-values]] — p-values are necessary but insufficient for good science.
- [[statistical-significance]] — The binary significant/not-significant decision is part of the problem.
- [[effect-sizes]] — Reporting effect sizes would improve the situation.
- [[confidence-intervals]] — CIs are more informative than p-values alone.
- [[hypothesis-formulation]] — Better hypotheses upfront reduce p-hacking.
- [[levels-of-equivalence]] — In CS, "replication" requires defining what level of equivalence counts.

## Open Questions
- Should we pre-register all hypotheses and analyses before running experiments?
- How does the replication crisis manifest differently in CS vs. psychology/medicine?
- What role should registered reports (accept/reject before results) play?
- Is the 5% significance threshold too permissive for a world of massive data and multiple testing?
