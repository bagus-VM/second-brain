---
title: "Confounding"
tags: [concept, network-science, semester-1, confounding, causality, selection, social-influence]
course: "Network Science"
source_count: 2
status: current
last_updated: 2026-06-14
prerequisites: ["[[homophily]]", "[[selection-vs-socialization]]"]
---

## One-line Summary
Confounding is the situation where an observed correlation between two variables (e.g., similarity and friendship) is explained by a *third* variable that drives both — the classic "correlation is not causation" problem, central to distinguishing homophily-driven tie formation from influence-driven change.

## Core Intuition
You observe: friends are similar (homophily). Two possible causal stories:
- **Selection**: similar people choose to become friends (similarity → tie).
- **Socialisation (influence)**: friends become similar after the tie forms (tie → similarity).

But there's a third story:
- **Confounding**: a third variable (e.g., shared workplace, shared dorm, shared demographic) causes both similarity and tie formation. Neither selection nor socialisation is at work.

Example: colleagues at a tech startup both use Python, and they're friends. The naive reading: "Python users befriend Python users" (homophily). The correct reading: "They're at the same workplace" → same programming language + proximity → friendship. The workplace is the confounder.

This is a fundamental identification problem in observational network data. Cross-sectional observation cannot distinguish the three. Only longitudinal data, exogenous shocks, or experimental designs can.

## Formal Definition / Statement

Let A = "node u has attribute X", B = "nodes u and w are friends", C = "nodes u and w share environment Y".

- **Selection**: P(B | A=true, C=false) > P(B | A=false, C=false) — friendship is more likely when u has X, holding environment constant.
- **Socialisation**: P(A_next | B=true, C=false) > P(A_next | B=false, C=false) — u adopts X *after* befriending w, holding environment constant.
- **Confounding**: P(B | C=true) > P(B | C=false) and P(A | C=true) > P(A | C=false) — the shared environment causes both, and A and B are correlated only through C.

In the structural-causal-model view: A and B have a common cause C. P(A, B) = Σ_c P(A|c) P(B|c) P(c) ≠ P(A) P(B) in general, even when A and B are independent given C (i.e., no direct causal link).

### Pearl's back-door criterion
To identify the *causal effect* of A on B (selection vs. socialisation), block all back-door paths from A to B through confounders. A back-door path is a non-causal path that starts with an arrow into A. Conditioning on C (the confounder) blocks the back-door.

In practice: measure C, condition on it (stratify or regress), and the residual A–B correlation is the *direct* causal effect.

## Key Properties

### Why it's hard
- **Unobserved confounders**: in a real network, the true confounder set is rarely fully known. Proximity, shared history, shared genetics, shared unmeasured preferences — all are potential confounders.
- **Time-varying confounding**: u and w meet, then start attending the same course. The friendship is observed *after* the shared course, but the course was caused by an unobserved preference. Mediational confounding.
- **Network-induced confounding**: u's friends' friends' outcomes are correlated with u's outcome through contagion-like paths. Standard regression assumptions break down (SUTVA, independence).
- **Reflection problem** (Manski 1993): in a linear-in-means model with group effects, the social-effect coefficient is not identified without strong assumptions.

### Strategies to identify the mechanism
1. **Longitudinal data with timing**: measure attributes at t, t+1, t+2. Look at attribute change *after* tie formation (socialisation) vs. tie formation *after* attribute adoption (selection).
2. **Instrumental variables**: find a variable that affects the *cause* but not the *outcome* except through the cause. E.g., random assignment of dorm rooms → friendship networks (Sacerdote 2001).
3. **Natural experiments / shocks**: a policy change, a platform re-design, a relocation. Treat the shock as exogenous.
4. **Randomised encouragement designs**: randomise *encouragement* to form ties, not the ties themselves. Sidesteps the ethics of forced allocation.
5. **Conditional / partial identification**: bound the causal effect under plausible assumptions, even when point identification is impossible.

## Worked Example

The lecture's scenarios:
1. Two students both like jazz, become friends, and a year later both discover classical music. **→ Socialisation.** Confirmation requires longitudinal preference data (jazz at t, classical at t+1, after the tie forms at t+0.5).
2. Two colleagues at a tech startup both use Python; their friendship forms day 1. **→ Confounding.** Both use Python because of the workplace. Compare pre-hire language use (before the workplace) to identify whether the language drove the friendship or the workplace drove both.
3. Students in the same dorm become friends and all prefer the same pizza place. **→ Mostly socialisation, with confounding.** Proximity (dorm) is the confounder; shared experiences create the preference. Compare same-floor vs. cross-floor pairs to partially isolate proximity.
4. A smoker quits after befriending non-smokers. **→ Socialisation** (peer influence), but **selection is plausible** — the smoker may have already wanted to quit and selected non-smoker friends. Random assignment of smokers to friend groups would identify, but raises ethics.

The unifying point: every scenario requires a *strategy* beyond cross-sectional observation. None of them can be settled by a single correlation.

## Common Pitfalls
- **"The data shows selection, not socialisation"**: the data shows a correlation. Naming the mechanism requires theory + design.
- **Conditioning on a collider**: if you condition on a variable caused by *both* A and B, you induce a spurious correlation. Common in network studies where you condition on "present in the sample".
- **Ignoring network effects**: u's outcome may depend on w's friends' outcomes (generalised contagion). Standard regression is biased; you need SNA-aware models (e.g., stochastic actor models, SNMM).
- **Treating the reflection problem as solved by fixed effects**: it isn't. Adding group fixed effects removes the between-group variation but leaves within-group confounding intact.
- **Forgetting the ethics of randomised design**: random assignment of friends is generally not permissible. Randomised *encouragement* designs are the standard alternative.

## Connections
- [[homophily]] — the observed correlation
- [[selection-vs-socialization]] — the two mechanisms being disentangled
- [[triadic-closure]] — a network process that interacts with both
- [[experiment-vs-observation]] — methodological framing
- [[manski-reflection-problem]] — the formal identification obstacle

## Open Questions
- For high-dimensional network data, can machine-learning methods (causal forests, double-ML) identify the mechanism under weaker assumptions? (Partial results; the network interference problem remains hard.)
- How do you bound the causal effect when the confounder is unmeasured? (Sensitivity analysis, e.g., Cinelli & Hazlett 2020; partial identification bounds.)
- Can synthetic controls or instrumental variables be constructed for *naturally occurring* tie formation? (Hard — the instruments must be plausibly exogenous, and most natural candidates are not.)
