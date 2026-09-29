---
title: "Network Autocorrelation"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [homophily, selection-vs-socialization]
---

## One-line Summary
Network autocorrelation is the statistical tendency for connected nodes to share attributes — the observable signature of homophily, social influence, or shared context, but not itself proof of any particular mechanism.

## Core Intuition
When we measure a node attribute (political leaning, weight, smoking status) and find that connected nodes are more similar than chance would predict, we observe network autocorrelation. This is the statistical footprint of the mechanisms studied in L05: selection (similar people connect), socialization (connected people become similar), and contextual correlation (shared environment causes both). The autocorrelation itself is measurable; the mechanism behind it is not — that requires longitudinal data, experimental manipulation, or generative models.

## Formal Definition / Statement
**Network autocorrelation**: the correlation of a node attribute x across edges of the network.

For a node attribute x and adjacency matrix A:
- Compute the correlation between xᵢ and xⱼ for all edges (i,j)
- Compare to the correlation expected under random permutation of x across nodes

**Measures**:
- Moran's I: global autocorrelation statistic
- Geary's C: alternative measure, more sensitive to local patterns
- Network regression: regress x on A·x (neighbour average) to estimate peer effects

**Connection to homophily**:
- High autocorrelation + balanced population → evidence of homophily
- High autocorrelation + skewed population → could be baseline (H_base is already high)
- Autocorrelation alone cannot distinguish selection from socialization

## Key Properties / Complexity
1. **Observable**: autocorrelation can be computed from a single cross-sectional snapshot
2. **Mechanism-agnostic**: the same autocorrelation is consistent with selection, socialization, and context
3. **Baseline-dependent**: must compare to random-mixing expectation (like H_base in [[homophily]])
4. **Scale-sensitive**: global autocorrelation (Moran's I) may miss local patterns
5. **Direction-sensitive**: in directed networks, autocorrelation may differ depending on edge direction

## Worked Example
**Political leaning on Facebook**:
- User i has leaning xᵢ = 0.2 (slightly left-leaning)
- Average leaning of friends: xᴺᵢ = 0.18 (very similar)
- High autocorrelation: friends' leanings are correlated with user's leaning

**Obesity in Framingham** (Christakis & Fowler 2007):
- Person A becomes obese → friend B's probability of becoming obese increases 57%
- High autocorrelation in weight across friendship ties
- But: same method "detects" contagion of height and acne (Cohen-Cole & Fletcher 2008) — confounders may explain the pattern

**Smoking in college dorms**:
- Smokers tend to befriend other smokers
- High autocorrelation in smoking status across dorm ties
- Could be selection (smokers choose smoker friends), socialization (friends influence smoking), or context (dorm floor placement)

## Common Pitfalls
1. **Assuming autocorrelation proves influence**: the same pattern is consistent with selection and context
2. **Ignoring baseline**: skewed populations produce high autocorrelation by chance
3. **Confusing correlation with causation**: autocorrelation is descriptive, not causal
4. **Over-interpreting peer effects**: network regression assumes a specific causal model
5. **Missing confounders**: shared environment can produce autocorrelation without any direct peer influence

## Connections
- [[homophily]] — autocorrelation is the statistical signature of homophily
- [[selection-vs-socialization]] — autocorrelation cannot distinguish the mechanisms
- [[echo-chambers]] — political leaning autocorrelation across interaction networks
- [[affiliation-networks]] — shared foci can produce autocorrelation without preference
- [[network-science-l05]] — lecture overview

## Open Questions
- Can we develop autocorrelation measures that are robust to confounders?
- How do we estimate peer effects when the network itself is endogenous?
- What is the right null model for autocorrelation in different network types?
- How does autocorrelation change over time in longitudinal networks?
