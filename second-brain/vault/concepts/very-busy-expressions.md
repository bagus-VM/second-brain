---
title: "Very Busy Expressions"
tags: [concept, software-analyse, semester-1, data-flow, very-busy-expressions]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [control-flow-graph, gen-kill-analysis]
---

## One-line Summary

Very busy expressions determines, for each program point, which expressions will *definitely* be evaluated on every future path before their operands change — a backward must analysis used for code hoisting optimisation.

## Core Intuition

An expression is "very busy" at a point if, no matter which path the program takes from that point, the expression will be computed before any of its operands are modified. This means we can *hoist* (move) the computation earlier — to a point where it's very busy — potentially reducing code size or enabling other optimisations. Like [[available-expressions]], it's a must analysis, but it looks *forward* in time and propagates *backward*.

## Formal Definition / Statement

**Equations** (backward):
```
OUT(n) = ∩ IN(s)           for s ∈ succ(n)
IN(n)  = gen(n) ∪ (OUT(n) - kill(n))
```

Where:
- `gen(s) = { e | e is evaluated at statement s }`
- `kill(s) = { e | some operand of e is modified at s }`

**Initialisation**: IN(n) = set of *all* expressions for all n ≠ exit; IN(exit) = ∅
(Must analysis starts with "everything" to be conservative)

**Join operator**: ∩ (intersection) — expression is very busy only if very busy on *all* paths

## Key Properties

- **Direction**: Backward (data flows from successors to predecessors)
- **Kind**: Must (intersection at join points)
- Enables **code hoisting**: if an expression is very busy at point p, we can compute it at p and propagate the result forward
- Complementary to [[available-expressions]]: available looks backward in time (was it computed?), very busy looks forward (will it be computed?)

## Worked Example

```
     if (...) {
B1:    x = a + b;
     } else {
B2:    y = a + b;
     }
B3:  z = a + b;
```

At the branch point before B1/B2: `a + b` is very busy because on *every* path it will be evaluated before `a` or `b` changes. We could hoist `t = a + b` before the branch and reuse `t` in all three locations.

## Common Pitfalls

- Confusing with [[available-expressions]]: available is forward-must (was it computed on all paths *to* here?), very busy is backward-must (will it be computed on all paths *from* here?)
- Forgetting to initialise with the full set of expressions (must analysis)
- At join points with no successor info, the must-join (∩) with "everything" produces the empty set — correct behaviour

## Connections

- Builds on [[gen-kill-analysis]]
- Solved by [[iterative-data-flow-analysis]]
- Classified as backward-must in the [[data-flow-analysis]] matrix
- Enables **code hoisting** and **partial redundancy elimination**
- Complementary to [[available-expressions]] (forward-must vs backward-must)

## Open Questions

- How does very busy expression analysis relate to partial redundancy elimination (PRE)?
- What are the tradeoffs between hoisting (code size) and register pressure?
