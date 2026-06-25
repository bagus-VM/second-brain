---
title: "Homophily"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Homophily is the tendency for ties to form between similar nodes — but measuring it requires comparing the observed within-group edge rate to a random-mixing baseline, not just eyeballing the pattern.

## Core Intuition
Seeing that most friendships are within-group is not enough to claim homophily. If 90% of a population is in group A, then 82% of random pairs already match by chance. The real question is: how much does the observed within-group rate exceed what chance alone predicts? The homophily index r quantifies this excess on a 0–1 scale (or negative for heterophily). Never interpret "X% of ties are within-group" without asking: compared to what baseline?

## Formal Definition / Statement
For a categorical attribute with class shares p₁, …, p_k:

**Random-mixing baseline** (diagonal of the probability square):
H_base = Σᵢ pᵢ²

**Observed homophily**: fraction of actual ties connecting same-class nodes = H_obs

**Homophily index** (normalized excess):
r = (H_obs − H_base) / (1 − H_base)

- r = 0: random mixing
- r = 1: perfect segregation
- r < 0: heterophily (preference for different attributes)

## Key Properties
1. **Baseline depends only on population shares** — not on the network
2. **r normalizes to [−1, 1]** — comparable across different populations
3. **Same H_obs, different r**: 85% within-group means r = 0.70 (50/50 split) but r = 0.17 (90/10 split)
4. **Baseline trap**: skewed populations inflate H_base, making observed rates misleading
5. **McPherson et al. 2001**: distinguish baseline homophily (from opportunity structure) from inbreeding homophily (genuine preference)

## Worked Example
Classroom: 12 students, 6 STEM (blue) + 6 Arts (orange), balanced.

- H_base = 0.5² + 0.5² = 0.50
- 17 of 19 edges are within-track: H_obs = 17/19 ≈ 0.89
- r = (0.89 − 0.50) / (1 − 0.50) = 0.78

r = 0.78 is strong — 78% of the way from chance to perfect segregation. But it tells us nothing about *why*: selection, socialization, or shared context could all produce this pattern.

**Quick check** (60/40 split, 78% within-track):
- H_base = 0.6² + 0.4² = 0.52
- r = (0.78 − 0.52) / (1 − 0.52) = 0.54 — moderate-to-strong

## Common Pitfalls
1. **Reporting H_obs without H_base**: "85% within-group" means nothing without knowing the population split
2. **Confusing homophily with mechanism**: r measures excess similarity, not whether it's selection or influence
3. **Ignoring opportunity structure**: age-graded classes produce same-age friendships without any preference
4. **Assuming homophily is universal**: different platform architectures produce dramatically different intensities (see [[echo-chambers]])

## Connections
- [[selection-vs-socialization]] — homophily = selection + socialization + context
- [[affiliation-networks]] — shared foci can produce homophily-like patterns without preference
- [[network-autocorrelation]] — the statistical measure of attribute similarity across network ties
- [[echo-chambers]] — empirical case of homophily by political leaning online
- [[schelling-segregation-model]] — how mild homophily preferences scale to global segregation
- [[modularity]] — both measure within-group excess over a random baseline
- [[network-science-l05]] — lecture overview

## Open Questions
- How do we measure homophily when attributes are continuous, not categorical?
- Can we decompose observed homophily into selection, socialization, and context contributions?
- How does algorithmic recommendation change the effective homophily of a network?
- What is the right baseline for homophily in directed or weighted networks?
