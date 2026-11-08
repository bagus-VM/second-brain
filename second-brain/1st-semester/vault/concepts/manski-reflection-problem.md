---
title: "Manski Reflection Problem"
tags: [concept, network-science, causal-inference, econometrics, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[confounding]]", "[[selection-vs-socialization]]", "[[experiment-vs-observation]]"]
---

## One-line Summary
*If your outcome depends on your peers' outcomes, and their outcomes depend on yours, you can't tell who is influencing whom — it's like seeing your reflection and wondering who's moving.*

## Core Intuition
Charles Manski (1993) posed a brutal question for social-effects research: suppose you want to know whether students' grades are affected by their classmates' grades (an endogenous peer effect). You observe that students in high-achieving classes tend to achieve more. But this could be three completely different things:

1. **Endogenous effect**: your classmates' grades *cause* your grades (you learn from them, or compete with them).
2. **Exogenous (contextual) effect**: your classmates' *background* (parental income, prior preparation) causes your grades — and their background also caused their grades, creating a spurious correlation.
3. **Correlated effect**: you and your classmates share the same teacher, school, or neighbourhood — the shared environment causes everyone's grades to be similar.

Manski showed that with standard observational data (one snapshot, no experiment), these three effects are **linearly dependent** — you cannot separate them. The "reflection" metaphor: if person A's outcome depends on person B's, and B's depends on A's, the regression sees one blurred shadow and can't tell which way the light is coming from.

## Formal Definition / Statement

The **linear-in-means** model for individual $i$ in group $g(i)$:

$$y_i = \alpha + \beta \cdot \bar{y}_{g(i)} + \gamma \cdot \bar{x}_{g(i)} + \delta \cdot x_i + \epsilon_i$$

where:
- $\bar{y}_{g(i)}$ = mean outcome of $i$'s group → **endogenous effect** ($\beta$)
- $\bar{x}_{g(i)}$ = mean characteristics of $i$'s group → **exogenous/contextual effect** ($\gamma$)
- $x_i$ = $i$'s own characteristics → **direct effect** ($\delta$)

**The reflection problem:** The group mean outcome satisfies $\bar{y}_{g(i)} = \alpha + \beta \cdot \bar{y}_{g(i)} + \gamma \cdot \bar{x}_{g(i)} + \delta \cdot \bar{x}_{g(i)} + \bar{\epsilon}_{g(i)}$, which gives $\bar{y}_{g(i)} = \frac{\alpha + (\gamma+\delta)\bar{x}_{g(i)} + \bar{\epsilon}_{g(i)}}{1 - \beta}$ (for $\beta \neq 1$).

Substituting back: $y_i = \frac{\alpha}{1-\beta} + \frac{\gamma + \delta\beta}{1-\beta} \cdot \bar{x}_{g(i)} + \delta \cdot x_i + \text{noise}$.

The data identifies $\frac{\alpha}{1-\beta}$, $\frac{\gamma + \delta\beta}{1-\beta}$, and $\delta$ — but **not** $\beta$ and $\gamma$ separately. Any combination of $\beta$ and $\gamma$ that produces the same reduced-form coefficients fits the data identically. The endogenous and contextual effects are **not separately identified**.

## Key Properties / Complexity
- **Not a data problem — an identification problem.** More data does not help. You need either an instrument, a natural experiment, or a structural restriction.
- **Solutions that break the reflection:**
  - **Instrumental variables**: find a variable that affects peers' outcomes but not yours directly (rare in practice).
  - **Partial identification**: Manski himself advocates bounding rather than point-estimating the effects.
  - **Network structure**: if peers are not all in the same symmetric group (e.g., each person has a different friend set), the reflection problem can be partially broken (Bramoullé, Djebbari, and Fortin 2009).
  - **Temporal variation**: if you observe the network over time and can assume peer effects are lagged, you can separate cause from effect.
- **SUTVA violation amplifies the problem**: in networks, one person's treatment spills over to neighbours, creating an even harder identification problem.

## Worked Example
You observe a classroom where students with high-achieving friends get higher grades. The regression of $y_i$ on $\bar{y}_{peers}$ gives a coefficient of 0.5. You conclude: "peer achievement raises your achievement by 0.5."

But the reflection problem says: that 0.5 could be:
- $\beta = 0.5, \gamma = 0$ (pure endogenous effect — friends' grades cause yours)
- $\beta = 0, \gamma = 0.5$ (pure contextual effect — friends' background causes both)
- $\beta = 0.25, \gamma = 0.375$ (a mix)

All three produce the identical regression output. Without additional structure, you cannot distinguish them. This is why a single cross-sectional regression of grades on peer grades is **uninterpretable** for causal claims.

## Common Pitfalls
- **Reporting $\beta$ from a linear-in-means regression as "the peer effect."** It's not identified — the number is a meaningless blend of $\beta$ and $\gamma$.
- **Assuming group-level variation solves it.** If groups are defined by shared context (same classroom = same teacher), the correlated effect is confounded with everything else.
- **Confusing the reflection problem with selection.** Selection is about *who becomes friends with whom*; the reflection problem is about *what happens after*, even if you've perfectly measured the network. They're different obstacles.
- **Exams love this:** A question will present an observational peer-effects study and ask "what can you conclude?" The answer is: "only an association, not a causal effect — the reflection problem prevents identification of endogenous vs contextual effects."

## Connections
- [[confounding]] — the reflection problem is the formal version of why confounding blocks causal inference in social settings
- [[experiment-vs-observation]] — experiments (random assignment) break the reflection; observations cannot
- [[selection-vs-socialization]] — the reflection problem is why you can't settle this debate with observational data alone
- [[homophily]] — selection-driven homophily creates the network structure that makes the reflection problem bite

## Open Questions
- Can network-based identification (Bramoullé et al. 2009) reliably separate endogenous from contextual effects in real-world networks with measurement error?
- How does the reflection problem interact with [[triadic-focal-membership-closure]] when the network itself is evolving simultaneously with the outcomes?
