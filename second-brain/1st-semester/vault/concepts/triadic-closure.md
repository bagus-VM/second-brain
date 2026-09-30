---
title: "Triadic Closure"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: ["[[graph-fundamentals]]"]
---

## One-line Summary
If two people share a mutual friend, they are significantly more likely to become connected themselves — open triads tend to close into triangles.

## Core Intuition
Social networks are not random. When person A knows both B and C, there is an inherent opportunity, trust, and social pressure for B and C to meet. Over time, this mechanism causes graphs to accumulate triangles, shrink average distances, and produce increasingly clustered neighborhoods. Triadic closure is a *generative* theory — it predicts how edges appear over time, not just a static pattern.

## Formal Definition / Statement
**Triadic Closure.** **If a node A has edges to two distinct nodes B and C, the probability that an edge (B, C) forms over time is significantly higher than for two random nodes.**

An **open triad** is a triple (A, B, C) where edges A–B and A–C exist but B–C does not. Triadic closure predicts the B–C edge tends to appear.

**Motivations for closure:**
- **Opportunity:** A introduces B and C
- **Trust:** B and C trust each other via A's endorsement
- **Social pressure:** It is awkward for A if B and C don't get along

## Key Properties / Complexity
- Predicts triangle accumulation over time
- Predicts shrinking average path lengths
- Predicts increasingly clustered neighborhoods for high-degree nodes
- Makes long-range ties rarer relative to local ones
- It is probabilistic, not deterministic — a single non-closure does not refute the model

## Worked Example
**Kossinets & Watts (2006)** studied 43,553 students/faculty at a US university via one year of email headers.

- Two people sharing one mutual email contact were **~30× more likely** to begin emailing than two people with no mutual contact
- Effect grew monotonically with number of shared contacts
- This is direct, longitudinal evidence for triadic closure at scale

**Limitation:** Their data was binary (email sent: yes/no). They could not distinguish strong daily collaboration from one-off administrative pings. Closure was visible; tie strength was not.

## Common Pitfalls
- Confusing triadic closure with "friends of friends are always friends" — it's probabilistic, not absolute
- Thinking it's just a static observation — it's a claim about edge *formation over time*
- Assuming the same graph cannot have both open and closed triads — closure is a tendency, not a law
- Forseeing that triadic closure alone cannot distinguish strong from weak ties (need edge labeling for that)

## Connections
- Leads to: [[strong-triadic-closure]] (adding edge labels to the closure model)
- Measured by: [[clustering-coefficient]] (fraction of closed neighbour pairs)
- Measured by: [[neighborhood-overlap]] (shared neighbours of edge endpoints)
- Foundation for: [[weak-ties-hypothesis]] (closure + edge labels → weak-tie theorem)
- Empirical validation: Kossinets & Watts (2006) university email network

## Open Questions
- How does triadic closure interact with homophily (do similar people close triads faster)?
- Does closure rate differ by relationship type (friendship vs. professional vs. family)?
- How do online platforms (recommendation algorithms) accelerate or distort natural closure?
