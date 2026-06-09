---
title: "Reproducibility Crisis"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
A widespread failure across sciences where published results cannot be independently reproduced, threatening the credibility of research.

## Core Intuition
If science is supposed to be self-correcting—anyone can verify anyone else's findings—then what happens when most published results can't be verified? The reproducibility crisis is exactly this: a growing body of evidence that a disturbingly large fraction of published research findings are false, inflated, or simply unrepeatable.

## Formal Definition / Statement
A 2016 Nature survey of **1,576 researchers** found:
- **52%** said there is a **significant** reproducibility crisis
- **38%** said there is a **slight** crisis
- Only **3%** said there is **no crisis** at all

This means ~90% of surveyed researchers acknowledge some level of crisis. The crisis manifests across disciplines—psychology, medicine, biology, computer science, and others.

## Key Properties
- **Not new**: Concerns about reproducibility have existed for decades, but large-scale studies have quantified the problem
- **Multidisciplinary**: It's not limited to one field; it's a systemic issue
- **Multiple causes**: p-hacking, publication bias, insufficient documentation, opaque code, underpowered studies
- **Consequences**: Wasted resources, failed drug trials, erosion of public trust in science
- **Driving reform**: Open science, pre-registration, registered reports, artifact sharing

## Worked Example
Common scenarios that contribute to the crisis:
1. A researcher runs 20 experiments but only publishes the 1 with a significant result (publication bias)
2. A computational paper reports results but doesn't share the code or random seeds
3. A psychology study with 20 participants finds an effect that disappears with 200 (underpowered study)
4. A medical trial's p-value of 0.049 disappears when the analysis is corrected for multiple comparisons

## Common Pitfalls
- **"Crisis" doesn't mean all science is wrong**: It means the current system allows too many unverified claims through
- **Reproducibility failure ≠ fraud**: Most cases involve methodological issues, not deliberate misconduct
- **Overcorrecting**: Demanding perfect reproducibility for every study type (e.g., field ecology) may be unrealistic
- **Confusing statistical significance with truth**: A p < 0.05 result is not necessarily reproducible

## Connections
- [[repeat-reproduce-replicate]] — The definitions that clarify what we mean by "reproducible"
- [[artifact-availability]] — Sharing artifacts is a direct mitigation strategy
- [[research-artifacts]] — The materials that need to be preserved and shared
- [[types-of-reproducibility]] — Different dimensions of the crisis (computational, empirical, statistical)

## Open Questions
- Has the crisis improved since 2016, or gotten worse with increasing complexity of research (e.g., deep learning)?
- What role do conferences and journals play in incentivizing or discouraging reproducibility?
- Should reproducibility be a requirement for publication, or an aspirational goal?
