---
title: "Granovetter's Weak Ties"
tags: [concept, network-science, semester-1]
course: "Network Science"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

## One-line Summary
Granovetter's weak-tie hypothesis states that weak ties (acquaintances, not close friends) are more important for information diffusion and community bridging than strong ties.

## Core Intuition
Strong ties connect people within the same community (high [[clustering-coefficient]], [[embeddedness]]). Weak ties span communities — they are the bridges that carry novel information from one group to another. This is why acquaintances (weak ties) are often more valuable for job hunting, information spread, and community detection than close friends (strong ties).

## Formal Definition / Statement
**Weak-tie hypothesis** (Granovetter, 1973):
- Weak ties (acquaintances) bridge different communities
- Strong ties (close friends) are embedded within communities
- Information, innovation, and opportunities flow through weak ties

**Connection to network science:**
- Weak ties are local bridges — edges whose removal would disconnect communities
- [[betweenness-centrality]] quantifies how much an edge is a bridge
- [[girvan-newman-algorithm]] is the algorithmic version: remove high-betweenness edges (weak ties) to find communities

## Key Properties / Complexity
1. **Bridging function**: weak ties connect otherwise separated groups
2. **Information advantage**: novel information comes from outside one's community
3. **Community detection**: weak ties are the boundaries between communities
4. **Counter-intuitive**: weak ties are more valuable than strong ties for information spread
5. **Empirically supported**: job-finding studies confirm the weak-tie hypothesis

## Worked Example
Workplace graph — Team A (Ana, Ben, Cai, Dia) and Team B (Eli, Fin, Gia, Hal, Ivo):

**Strong ties:** edges within Team A and within Team B (thick edges)
**Weak tie:** the Dia↔Fin edge (thin edge) — the only connection between teams

**Weak-tie hypothesis:** the Dia↔Fin edge is the most valuable for information spread between teams. If Ana wants to learn about Team B's activities, her best source is Dia (who has the weak tie to Fin), not Ben or Cai (who have strong ties within Team A).

## Common Pitfalls
1. **Confusing weak ties with unimportant ties**: weak ties are structurally important for bridging
2. **Ignoring that strong ties matter for local cohesion**: strong ties build trust and redundancy
3. **Assuming all weak ties are bridges**: some weak ties connect nodes within the same community
4. **Over-generalizing**: the weak-tie hypothesis applies to information diffusion, not all network effects

## Connections
- [[betweenness-centrality]] — quantifies how much an edge is a bridge
- [[girvan-newman-algorithm]] — removes weak ties (high-betweenness edges) to find communities
- [[embeddedness]] — strong ties are embedded; weak ties span
- [[structural-holes]] — weak ties span structural holes
- [[community-detection]] — weak ties are community boundaries
- [[network-science-l04]] — lecture overview

## Open Questions
- How do weak ties form and disappear over time?
- Can we predict which weak ties will become strong ties?
- How does the weak-tie hypothesis apply to online social networks?
