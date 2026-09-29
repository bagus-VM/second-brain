---
title: "Live Variable Analysis"
tags: [concept, software-analyse, semester-1, data-flow, liveness]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [control-flow-graph, gen-kill-analysis]
---

## One-line Summary

Live variable analysis determines, for each program point, which variables *may* be read on some future path before being overwritten — a backward may analysis used for register allocation and dead code elimination.

## Core Intuition

A variable is "live" at a point if its current value might be needed later (on some execution path, before being redefined). If a variable is *dead* (not live), we don't need to keep it in a register, and assignments to it can potentially be eliminated as dead code. The analysis looks *forward in time* but propagates information *backward* through the CFG.

## Formal Definition / Statement

**Equations** (backward):
```
OUT(n) = ∪ IN(s)           for s ∈ succ(n)
IN(n)  = gen(n) ∪ (OUT(n) - kill(n))
```

Where:
- `gen(n) = { v | v is used (read) at statement n }` — variables used before being defined
- `kill(n) = { v | v is defined (modified) at statement n }` — variables whose previous value is overwritten

**Initialisation**: IN(n) = ∅ for all n (may analysis starts empty)

**Join operator**: ∪ (union) — variable is live if live on *any* path

## Key Properties / Complexity

- **Direction**: Backward (data flows from successors to predecessors)
- **Kind**: May (union at join points)
- A variable is live at point p iff there exists a path from p to a use of that variable with no intervening definition
- No variable should be live at the program **entry** point (detects uninitialized variables)
- Optimal traversal: reverse depth-first (reverse topological) order

## Worked Example

```
B1: i := 2          // gen = {}; kill = {i}
B2: j := i + 1      // gen = {i}; kill = {j}
B3: i := 1          // gen = {}; kill = {i}
B4: j := 1 + j      // gen = {j}; kill = {j}
B5: j := j - 4      // gen = {j}; kill = {j}
```

Working backward:
- After B5: nothing live
- IN(B5) = {j} (j is used before being killed)
- IN(B4) = {j} (j used, then killed — but j from B3 flows in)
- IN(B3) = {j} (j is live coming from B4)
- IN(B2) = {i} (i is used, j is dead since redefined at B3)

## Common Pitfalls

- Confusing gen/kill order in backward analysis: gen = uses, kill = defs (opposite intuition from forward)
- Forgetting that a use at a statement makes the variable live *before* that statement, not after
- Not initialising with ∅ (may analysis) — using the full set would be wrong
- A variable used and then defined in the same statement: it's in gen (used) AND kill (defined) — gen wins because it's evaluated first in `gen ∪ (OUT - kill)`

## Connections

- Builds on [[gen-kill-analysis]]
- Solved by [[iterative-data-flow-analysis]]
- Complementary to [[reaching-definitions]] (both are may analyses, but opposite directions)
- Used with [[du-chains-ud-chains]]: UD-chains connect uses to reaching definitions
- Enables **register allocation** (dead variables don't need registers) and **dead code elimination** (assignments to dead variables can be removed)
- No variable should be live at program entry — if one is, it's used before being initialized

## Open Questions

- How does liveness analysis interact with inter-procedural analysis (e.g., parameters passed by reference)?
- What's the relationship between liveness analysis and the "live range" concept in register allocation?
