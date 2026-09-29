---
title: "Network Science L05: Social Context and Link Formation"
tags: [topic, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Lecture 05 adds attributes and context to the graph: nodes carry properties, ties have reasons, and social settings (foci) become explicit — shifting the question from "what structure exists?" to "why does it exist?".

## Core Intuition
L03–L04 treated the graph as colorless — every node interchangeable, every edge equivalent. L05 asks: what happens when nodes carry attributes (track, political leaning, weight) and edges carry reasons (shared class, friend introduction, algorithmic recommendation)? The central problem is causal: a cross-sectional snapshot shows a pattern (similar people are connected), but cannot distinguish whether similarity caused the tie (selection), the tie caused similarity (socialization), or a shared environment caused both (contextual correlation). The fix is not a better algorithm — it is richer data (longitudinal, affiliation-based) or a generative model.

## Key Concepts

### Measurement: [[homophily]]
- **[[homophily]]**: tie formation biased toward similarity in node attributes
- **Random-mixing baseline** H_base = Σ p_i² — what same-class rate chance alone predicts
- **Homophily index** r = (H_obs − H_base) / (1 − H_base) — excess above chance, normalized to [−1, 1]
- **Baseline trap**: same H_obs can mean very different things depending on population composition
- **[[echo-chambers]]**: online homophily by political leaning (Cinelli et al. 2021)
- **[[network-autocorrelation]]**: the statistical signature of connected nodes sharing attributes — Moran's I, Geary's C, network regression

### Mechanism: [[selection-vs-socialization]]
- **Selection**: similarity precedes the tie — people choose friends who are already alike
- **Socialization (influence)**: tie precedes similarity — friends become more alike over time
- **Contextual correlation**: shared environment (foci) independently causes both attribute and tie
- Cross-sectional data cannot distinguish the three; longitudinal data helps but cannot fully eliminate confounding
- **Christakis & Fowler (2007)**: obesity "contagion" in Framingham — 57% increased risk if friend becomes obese
- **Nyhan et al. (2023)**: Facebook feed experiment — reducing like-minded exposure did not change attitudes

### Context: [[affiliation-networks]]
- Bipartite graph G = (P ∪ F, E): persons P, foci F, edges only between them
- **Co-occurrence projection**: BB^T (person-person), B^TB (focus-focus)
- Three closure processes:
  - **Triadic closure**: person–person–person → new friendship (shared friend)
  - **Focal closure**: person–focus–person → new friendship (shared context, no shared friend needed)
  - **Membership closure**: person–person–focus → new membership (friend introduces you to a club)
- **Kossinets & Watts (2006)**: university email data — closure curves at scale, saturating shape
- **Wikipedia editing**: membership closure with articles as foci (Crandall et al. 2008)

### Dynamics: [[schelling-segregation-model]]
- Agents on grid/network with threshold τ for same-type neighbor fraction
- Mild local preferences (τ ≈ 1/3) produce sharp global segregation
- Network version: rewiring ties instead of relocating on grid
- Recommendation algorithms act as automated Schelling rewirers

## Connections
- Builds on L03 ([[network-science-l03|Lecture 03]]) — weak ties, bridges, triadic closure
- Builds on L04 ([[network-science-l04|Lecture 04]]) — communities, modularity
- [[homophily]] connects to [[modularity]] — both measure within-group excess over chance
- [[affiliation-networks]] extend the graph model to bipartite settings
- [[selection-vs-socialization]] is the causal question underlying all homophily claims
- [[network-autocorrelation]] is the measurable statistical footprint of homophily, socialization, and contextual correlation
- [[schelling-segregation-model]] connects local rules to global patterns
- [[echo-chambers]] are a modern empirical case of homophily at scale

## Open Questions
- How do we design studies that can truly distinguish selection from socialization?
- Can we quantify the contribution of algorithmic recommendation to observed homophily?
- How do affiliation networks generalize to overlapping, hierarchical foci?
- What is the right threshold τ for Schelling dynamics on real social networks?
- How do echo chambers form and dissolve across different platform architectures?
