---
title: "Kossinets & Watts (2006) — Empirical Analysis of an Evolving Social Network"
tags: [concept, network-science, papers, empirical, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[homophily]]", "[[triadic-closure]]", "[[selection-vs-socialization]]"]
---

## One-line Summary
*A year of university email records showing that social networks evolve through a mix of homophily (birds of a feather flock together) and triadic/focal closure (friends of friends become friends) — and that you can't separate the two without longitudinal data.*

## Core Intuition
Most network science studies a snapshot: here's the network today, here are its properties. Kossinets and Watts did something more valuable — they watched a network *grow* over time. They had access to one academic year of email logs at a large university (≈43,000 students/staff, ≈14 million emails). By constructing the communication network at regular intervals and tracking which new ties formed, they could ask: *why* do two people who weren't connected become connected?

They decomposed tie formation into three mechanisms:
1. **Triadic closure**: you befriend your friends' friends (shared contacts introduce you).
2. **Focal closure**: you befriend people who share your "foci" — classes, dorms, departments (shared context brings you together).
3. **Membership closure**: you join the foci (classes, groups) that your friends are in (social influence pulls you into shared contexts).

The key insight: homophily (similarity → friendship) and these closure mechanisms are entangled. People who share classes are similar *and* in the same context. Without longitudinal data, you can't tell whether the shared class caused the friendship or the shared characteristics did. Kossinets & Watts could, because they saw the temporal order.

## Formal Definition / Statement

**Kossinets, G., & Watts, D. J. (2006).** "Empirical Analysis of an Evolving Social Network." *Science*, 311(5757), 88–90.

Given an evolving network $G_t = (V, E_t)$ observed at discrete time steps, a new tie $(i, j) \in E_{t+1} \setminus E_t$ is attributed to:

- **Triadic closure** if $i$ and $j$ share a common neighbor at time $t$: $\exists k: (i,k), (j,k) \in E_t$
- **Focal closure** if $i$ and $j$ share a focus (class, dorm, department) at time $t$ but no common neighbor
- **Membership closure** if $i$ joins a focus that $j$ already belongs to between $t$ and $t+1$

The study measures the **conditional probability** of tie formation given each mechanism, controlling for the others.

## Key Properties / Complexity
- **Data**: email exchange at one university, one academic year. A tie = at least one email sent in the observation window. Directed (sent vs received) but analyzed as undirected for friendship inference.
- **Scale**: ~43,000 nodes, ~600,000 edges over the year. Large enough for statistical power, small enough to compute triadic/focal overlaps.
- **Main findings**:
  - Homophily (shared attributes) and triadic/focal closure are **both** significant and **interact**: shared foci amplify triadic closure, and vice versa.
  - The probability of tie formation increases sharply with the number of shared foci and shared neighbors.
  - Network evolves through a combination of selection (homophily drives who meets whom) and opportunity (shared context creates the chance to meet).
- **Limitation**: email is a proxy for social ties — not all emails are friendships, not all friendships produce emails. The mapping is noisy.

## Worked Example
At time $t$, students Alice and Bob are not connected. Alice is in Course X and friends with Carol. Bob is in Course X and friends with Carol.

At time $t+1$, Alice and Bob become connected. Why?

- **Triadic closure**: they share Carol as a common friend → probability of tie formation increases.
- **Focal closure**: they share Course X → probability increases.
- **Both**: the effects compound — having both a shared friend AND a shared class more than doubles the tie-formation probability compared to either alone.

This is the paper's central empirical finding: the mechanisms are not independent alternatives; they **reinforce** each other.

## Common Pitfalls
- **Treating this as proof of causation.** Even with longitudinal data, Kossinets & Watts measure conditional probabilities, not causal effects. The [[manski-reflection-problem]] applies — unmeasured confounders could drive both the shared context and the tie formation.
- **Generalizing from one university's email network.** Email behavior at one institution in the 2000s is not universal. Cultural, technological, and institutional context matters.
- **Ignoring the temporal window.** The study uses one academic year. Tie formation mechanisms may differ over longer timescales or in different lifecycle stages of a network.
- **Exams:** A question may ask "what are the three closure mechanisms in Kossinets & Watts?" — answer: triadic, focal, membership. Or "why is longitudinal data necessary?" — answer: to separate selection from socialization, you need the temporal order of events.

## Connections
- [[triadic-focal-membership-closure]] — the dedicated page decomposing the three mechanisms
- [[homophily]] — the similarity-driven force that interacts with closure mechanisms
- [[selection-vs-socialization]] — the causal-inference framing this study contributes to
- [[experiment-vs-observation]] — this study is observational; the temporal ordering helps but doesn't fully solve identification
- [[triadic-closure]] — the specific mechanism (shared contacts → new tie) that this study validates empirically

## Open Questions
- How do these closure mechanisms operate in online social networks (Facebook, Twitter) where foci are less clearly defined?
- Does the reinforcement effect (triadic + focal > sum of parts) hold in networks with weaker institutional structure?
- Can the decomposition be extended to multiplex networks (multiple types of ties simultaneously)?
