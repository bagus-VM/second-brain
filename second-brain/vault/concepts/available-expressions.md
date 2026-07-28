---
title: "Available Expressions"
tags: [concept, software-analyse, semester-1, data-flow, available-expressions]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [control-flow-graph, gen-kill-analysis]
---

## One-line Summary

Available expressions determines, for each program point, which expressions have been computed on *every* path from the entry and whose operands haven't changed since — a forward must analysis used for common subexpression elimination.

## Core Intuition

If `a + b` was already computed earlier on *every* path reaching this point, and neither `a` nor `b` has been modified since, we don't need to compute it again — we can reuse the previously stored result. This saves computation but requires the expression to be available on *all* paths (must), not just some.

## Formal Definition / Statement

**Equations** (forward):
```
IN(n)  = ∩ OUT(m)           for m ∈ pred(n)
OUT(n) = gen(n) ∪ (IN(n) - kill(n))
```

Where:
- `gen(s) = { e | e is computed at statement s }`
- `kill(s) = { e | some operand of e is modified at s }`

**Initialisation**: OUT(n) = set of *all* expressions for all n ≠ entry; OUT(entry) = ∅
(Must analysis starts with "everything" to be conservative)

**Join operator**: ∩ (intersection) — expression available only if available on *all* paths

## Key Properties / Complexity

- **Direction**: Forward (data flows along CFG edges)
- **Kind**: Must (intersection at join points)
- At a join point, an expression is available only if it was available on *every* incoming path
- If a variable is modified, *all* expressions containing that variable are killed
- The initialisation with "everything" (all expressions) ensures that must-facts start conservatively

## Worked Example

```
B1: x := a + b        // gen = {a+b}; OUT = {a+b}
B2: y := a * b        // gen = {a*b}; OUT = {a+b, a*b}
B3: a := a + 1        // gen = {a+1}; kill = {a+b, a*b} (operand a changed)
                         OUT = {a+1}
B4: (join)             // IN = OUT(B2) ∩ OUT(B3) — only expressions available on both paths
```

## Common Pitfalls

- Initialising with ∅ instead of the full set — this is wrong for must analyses and will give unsound (too-optimistic) results
- Forgetting that modifying *any* operand kills the expression, not just the whole expression
- Confusing with [[reaching-definitions]]: both are forward, but AE is must (∩) while RD is may (∪)
- At join points with no predecessor info, the must-join (∩) with "everything" correctly produces the empty set

## Connections

- Builds on [[gen-kill-analysis]]
- Solved by [[iterative-data-flow-analysis]]
- Enables **common subexpression elimination**: if expression is available, reuse stored result
- Classified as forward-must in the [[data-flow-analysis]] matrix
- Complementary to [[very-busy-expressions]] (forward must vs backward must)

## Open Questions

- How does available expressions interact with floating-point semantics (where reordering changes results)?
- What additional kill rules are needed for pointer aliasing?
