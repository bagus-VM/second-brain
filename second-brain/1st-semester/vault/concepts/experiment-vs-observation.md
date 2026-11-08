---
title: "Experiment vs Observation"
tags: [concept, network-science, methodology, causal-inference, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[confounding]]", "[[selection-vs-socialization]]"]
---

## One-line Summary
*Experiments let you conclude "X caused Y"; observations only let you conclude "X is associated with Y" — and the gap between those two statements is where most social-science controversy lives.*

## Core Intuition
There are two ways to learn about the world from data. In an **experiment**, the researcher decides who gets the treatment and who doesn't (random assignment). In an **observational study**, the researcher merely watches — nature (or society) has already assigned the treatments, and the researcher has no control over who ended up where.

The difference matters because of **confounding**. In an experiment, random assignment breaks the link between the treatment and any pre-existing differences between groups — so if the treated group ends up different, you know the treatment caused it. In an observational study, the treated and untreated groups may have differed *before* the treatment in ways you can't see. A difference in outcomes could be the treatment, or it could be those pre-existing differences. You can't tell.

This is why network scientists study homophily and peer effects with such caution: you can't randomly assign friends to people (usually). You observe that friends become similar over time and ask — did the friendship *cause* the convergence (socialization), or were they already similar and that's *why* they became friends (selection)? Without an experiment, both stories fit the data.

## Formal Definition / Statement

An **experiment** (randomized controlled trial) assigns treatment $T_i \in \{0,1\}$ to unit $i$ by a known random mechanism, independent of all other variables:

$$T_i \perp\!\!\!\perp (Y_i(0), Y_i(1), X_i)$$

where $Y_i(1), Y_i(0)$ are potential outcomes under treatment/control and $X_i$ are covariates.

An **observational study** assigns treatment by an unknown mechanism that may depend on $X_i$:

$$T_i \not\perp\!\!\!\perp X_i$$

Under random assignment, the average treatment effect is identified: $\text{ATE} = E[Y(1)] - E[Y(0)] = E[Y|T=1] - E[Y|T=0]$.

Under non-random assignment, $E[Y|T=1] - E[Y|T=0] \neq \text{ATE}$ because of selection bias: $E[Y(0)|T=1] \neq E[Y(0)|T=0]$.

## Key Properties / Complexity
- **Randomization = the great equalizer**: experiments balance observed AND unobserved confounders across groups (in expectation).
- **Observational causal inference is possible but requires assumptions**: conditional independence (ignorability given covariates), instrument variables, or natural experiments — none are guaranteed to hold.
- **Network interference**: in social networks, one person's treatment can affect another's outcome (spillover). This violates the Stable Unit Treatment Value Assumption (SUTVA), complicating both experimental and observational designs.
- **Natural experiments**: quasi-experimental designs (instrumental variables, regression discontinuity, difference-in-differences) try to recover experimental-like inference from observational data by exploiting "as-good-as-random" variation.

## Worked Example
**Question:** Do students' grades improve because their friends get good grades (peer effect), or do students with similar ability become friends (selection)?

- **Observational approach:** Measure friendship networks and grades at the end of the semester. Find that friends have similar grades. Conclusion? None — both socialization and selection produce this pattern.
- **Experimental approach:** Randomly assign students to study groups (breaking self-selection). If the groups' grades converge more than random groups would, you have evidence of a causal peer effect.
- **Natural experiment:** Use a dorm-room random assignment (students don't choose their roommates). If roommate GPA affects your GPA, it's a peer effect — because the assignment was random, selection is ruled out. (Sacerdote 2001 did exactly this.)

## Common Pitfalls
- **"Correlation is not causation" is necessary but not sufficient.** The deeper issue is: what would have happened *without* the treatment? Without a counterfactual, you're guessing.
- **Assuming you've measured all confounders.** Even with rich observational data, unmeasured confounders can flip the conclusion. This is why [[confounding]] is a third explanation beyond selection and socialization.
- **Ignoring network interference.** In a social network, SUTVA is routinely violated — your friend's treatment affects your outcome. Standard causal-inference methods assume this away.
- **Overclaiming from natural experiments.** A natural experiment is only as good as its "as-good-as-random" claim. If the supposed instrument is actually correlated with an unmeasured confounder, you're back to square one.

## Connections
- [[confounding]] — the third explanation (beyond selection and socialization) for why observational data misleads
- [[selection-vs-socialization]] — the canonical network-science question that hinges on this distinction
- [[manski-reflection-problem]] — the formal proof that even with perfect observational data, you still can't identify peer effects
- [[homophily]] — the observed-similarity pattern that could be selection or socialization

## Open Questions
- Can network randomized experiments (treating some nodes, measuring spillover on others) identify peer effects under interference? (Partial progress; the interference estimation problem is active research.)
- How reliable are digital trace data (email, social media) as observational proxies for real-world social ties? (Kossinets & Watts used email; the mapping from digital to real ties is noisy.)
