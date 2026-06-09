---
title: "Online Link Formation"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [affiliation-networks, homophily]
---

## One-line Summary
Online data with timestamps turns link formation into a measurable process — empirical closure curves show that the first shared contact matters most, and additional contacts are redundant rather than independent.

## Core Intuition
The problem with cross-sectional snapshots is that they freeze the network in time. Online platforms generate timestamped data — emails, edits, messages — that lets us observe what existed at time t, then ask which new ties form at t+1. This makes link formation forward-looking and measurable. The key empirical finding: closure curves (probability of new tie vs number of shared contacts) follow a saturating shape. One shared friend or one shared class is already highly informative; additional shared contacts add less than an independence model predicts. The reason: shared contacts are correlated (typically embedded in the same group), so they provide less independent opportunity than assumed.

## Formal Definition / Statement
**Independent-opportunity baseline**:
Assume each mutual friend independently creates an opportunity for a new tie with probability q.

P(new tie | k shared friends) = 1 − (1 − q)^k

**Empirical closure curve** (Kossinets & Watts, 2006):
- At each time step, take every pair (u,v) that has not yet emailed
- Count k: how many mutual email contacts they already share
- Ask whether (u,v) exchanges email in the next interval
- Output: P(new tie) vs k

**Three closure types measured**:
| Type | Shared element | What forms |
|------|---------------|------------|
| Triadic | Mutual friends | New friendship |
| Focal | Shared classes/foci | New friendship |
| Membership | Friends in a focus | New membership |

**Key result**: All three show saturating curves — first shared contact matters most, diminishing returns thereafter.

## Key Properties
1. **Timestamped data enables forward-looking analysis**: observe what exists at t, measure what forms at t+1
2. **Saturating curves**: first shared contact is highly informative, additional contacts add less
3. **Redundancy**: shared contacts are correlated (embedded in same group), not independent
4. **Focal closure needs no shared friend**: strangers in the same context form ties through exposure alone
5. **Membership closure is the reverse direction**: friends pull you into contexts they inhabit

## Worked Example
**Kossinets & Watts (2006)**: Large U.S. research university, ~43,000 people, ~14M email messages, ~1 year.

**Triadic closure curve**:
- k=0 shared friends: P(new tie) ≈ very low (baseline)
- k=1: sharply higher
- k=2: higher still
- k=5–8: roughly follows independent-friend baseline
- k=9+: rises steeply again, but with fewer observations (noisier)

**Focal closure curve**:
- k=0 shared classes: P(new tie) = baseline
- k=1: already informative
- k>1: observed curve stays *below* independent-focus baseline — additional classes are redundant

**Wikipedia editing** (Crandall et al. 2008):
- Editors are persons, articles are foci
- P(editing article) rises with k = number of communication partners who already edited that article
- Same saturating shape — friends already active in a focus make joining more likely, with diminishing returns

**Quick check** (coworker Facebook study):
- k=0: 1%, k=1: 20%, k=2: 30%, k=3+: 33%
- Independent model with q=0.20 predicts k=2: 1−(1−0.2)² = 0.36, but observed 0.30
- Mismatch: shared friends are correlated, providing less independent opportunity

## Common Pitfalls
1. **Treating shared contacts as independent**: they're typically embedded in the same group
2. **Reading baseline curves as confidence intervals**: they're toy-model comparisons, not fitted values
3. **Ignoring redundancy at high k**: pairs with many mutual friends are rare, so curves are noisier
4. **Confusing focal closure with triadic**: focal closure creates ties among strangers through shared context
5. **Over-interpreting single platforms**: closure dynamics may differ across architectures

## Connections
- [[affiliation-networks]] — the bipartite framework underlying focal and membership closure
- [[homophily]] — closure processes can produce homophily-like patterns without preference
- [[selection-vs-socialization]] — timestamped data helps distinguish mechanisms
- [[echo-chambers]] — platform architecture shapes closure dynamics
- [[schelling-segregation-model]] — closure curves feed into Schelling-style dynamics
- [[network-science-l03]] — triadic closure from Lecture 03
- [[network-science-l05]] — lecture overview

## Open Questions
- How do closure dynamics differ across platform architectures?
- Can we predict which new ties will form from closure patterns alone?
- How do recommendation algorithms interact with natural closure processes?
- What is the right model for redundancy among shared contacts?
