---
title: "Presenting Experiments"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [hypothesis-formulation]
---

# Presenting Experiments

## One-line Summary
A well-structured experiments section separates setup, results, and discussion, enabling readers to understand, evaluate, and reproduce the work.

## Core Intuition
How you present experiments is as important as how you run them. A clear structure helps readers assess validity, understand what was measured, and judge whether the conclusions are supported.

## Formal Definition / Statement
The typical structure of an experiments section in a CS paper:

1. **Setup:** What was measured, on what data, with what baselines and metrics.
   - "We evaluate our method on data collected from five campus cafés and compare it against two baselines."
   - "We measure recommendation quality using click-through rate and normalized discounted cumulative gain."

2. **Results:** What the data show.
   - "Our method reduces the average search time by 23% compared with the popularity-based baseline."
   - "Figure 3 shows that the proposed method remains faster than all baselines as the number of users increases."

3. **Discussion:** Interpretation, limitations, context.
   - "This suggests that personalization is especially useful when users have strong dietary preferences."
   - "The gains are smaller late in the day, possibly because several cafés have fewer items available."

## Key Properties / Complexity
- A figure should be accompanied by an explanation of what it shows and why it matters.
- It is important to state limitations clearly.
- The experiments section should **not** only present positive outcomes.
- Setup should explain datasets, baselines, and evaluation metrics.

## Worked Example
Coffee recommendation system case study:
- **Setup:** Data from 5 campus cafés, compared against 2 baselines (popularity-based, random). Metrics: click-through rate, NDCG.
- **Result:** 23% reduction in average search time. Proposed method remains faster as users scale (Figure 3).
- **Discussion:** Personalization helps most with strong dietary preferences. Smaller gains late in the day due to reduced café availability.

## Common Pitfalls
- Mixing setup, results, and discussion without clear separation.
- Figures without explanation ("see Figure 3" with no context).
- Hiding limitations or only showing positive results.
- Not explaining *why* a metric was chosen.

## Connections
- [[hypothesis-formulation]] — The hypothesis determines what the experiments section should test.
- [[effect-sizes]] — Results should report effect sizes, not just p-values.
- [[confidence-intervals]] — Showing uncertainty in results.
- [[reproducibility-engineering-lecture-3]] — Part of Lecture 3.

## Open Questions
- How much detail is needed in the setup for full reproducibility?
- Should code and data be required for the experiments section to be complete?
- How should negative or inconclusive results be presented?
