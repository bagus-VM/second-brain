---
title: "Diffusion of Innovations"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Diffusion of innovations studies how new ideas, technologies, and behaviors spread through social networks, often as [[complex-contagion]] processes requiring social reinforcement.

## Core Intuition
Not all innovations spread like diseases. Many require social reinforcement — people need to see multiple peers using a technology before adopting it themselves. This makes innovation diffusion a [[complex-contagion]] process where network structure (especially clustering and bridge width) determines whether adoption cascades globally or stalls locally. The classic S-curve of adoption (slow start, rapid growth, saturation) emerges from threshold dynamics.

## Formal Definition / Statement
**Diffusion of innovations** (Rogers, 1962) describes how innovations spread through social systems. Key adopter categories:
- **Innovators** (2.5%): First to adopt, low threshold
- **Early adopters** (13.5%): Opinion leaders, moderate threshold
- **Early majority** (34%): Adopt after seeing evidence, higher threshold
- **Late majority** (34%): Adopt due to social pressure, high threshold
- **Laggards** (16%): Last to adopt, very high threshold

In network terms, these categories map to different adoption thresholds q in the [[complex-contagion]] model. The S-curve of cumulative adoption emerges from the cascade dynamics of [[threshold-cascades]].

## Key Properties
1. Adoption often requires social reinforcement — multiple adopting neighbors
2. Network clustering accelerates adoption (see [[centola-2010-experiment]])
3. Weak ties spread awareness but may not trigger adoption (see [[weak-tie-paradox-contagion]])
4. The S-curve shape reflects threshold dynamics: slow start while clusters form, rapid growth as cascades link clusters, saturation as remaining nodes have high thresholds
5. Opinion leaders (high-degree, high-centrality nodes) can trigger cascades by adopting early

## Worked Example
A new collaboration tool is introduced in a company. Innovators (tech enthusiasts) adopt immediately. Early adopters adopt after seeing 1-2 colleagues use it. The early majority needs to see 3-4 colleagues using it before switching. In a clustered team structure, once a critical mass in one team adopts, the density of local reinforcement triggers cascade through adjacent teams via wide bridges. In a sparse random structure, adoption stalls because individual bridges cannot provide enough reinforcement.

## Common Pitfalls
- Treating innovation diffusion as simple contagion — awareness spreads simply, but adoption often requires reinforcement
- Assuming the S-curve is universal — the shape depends on network structure and threshold distribution
- Ignoring that adoption can reverse — people abandon innovations, which basic threshold models don't capture

## Connections
- Modeled as [[complex-contagion]] with adoption thresholds
- Cascade dynamics from [[threshold-cascades]]
- Empirical support from [[centola-2010-experiment]]
- The [[weak-tie-paradox-contagion]] explains why awareness ≠ adoption
- Network structure effects relate to [[community-structure]]
- Part of [[network-diffusion]]

## Open Questions
- How do competing innovations interact on the same network?
- What is the role of network adaptation (rewiring) in innovation diffusion?
- How does the threshold distribution across nodes affect cascade outcomes?
