---
title: "Reaching Definitions"
tags: [concept, software-analyse, semester-1, data-flow, reaching-definitions]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [control-flow-graph, gen-kill-analysis]
---

## One-line Summary

Reaching definitions determines, for each program point, which variable definitions *may* have occurred on some path from the entry — a forward may analysis used for def-use chains and detecting undefined variables.

## Core Intuition

When the compiler sees a variable use, it needs to know which assignments could have produced that value. A definition "reaches" a point if there exists a path from the definition to that point with no intervening redefinition of the same variable. This is a **may** analysis because we care about *any* possible path.

## Formal Definition / Statement

**Equations** (forward):
```
IN(n)  = ∪ OUT(m)           for m ∈ pred(n)
OUT(n) = (IN(n) \ kill(n)) ∪ gen(n)
```

Where:
- `gen(n) = { v_n | v is defined or modified at statement n }` — tagged with the definition site
- `kill(n) = { v_x | v is defined or modified at statement x, x ≠ n }` — all other definitions of the same variable

**Initialisation**: IN(entry) = ∅, OUT(n) = ∅ for all n (may analysis starts empty)

**Join operator**: ∪ (union) — a definition reaches if it reaches on *any* path

## Key Properties / Complexity

- **Direction**: Forward (data flows from predecessors to successors)
- **Kind**: May (union at join points)
- A definition d of variable v reaches point p iff there is a **definition-clear path** from d to p
- Convergence is guaranteed because the fact space is finite and transfer functions are monotone
- Optimal traversal: depth-first (topological) order on the CFG

## Worked Example

```java
// GCD example
A: def x, y, tmp    // gen = {xA, yA, tmpA}
B: while (y != 0)   // IN = OUT(A) ∪ OUT(E)
C:   tmp = x % y    // gen = {tmpC}; kill = {tmpA}
D:   x = y          // gen = {xD}; kill = {xA}
E:   y = tmp        // gen = {yE}; kill = {yA}
F: return x         // IN = OUT(D)
```

Steady-state results:
- ReachIn(B) = {xA, yA, tmpA, xC, yC, tmpC} — definitions from A and from within the loop
- ReachIn(F) = {xC, yC, tmpA} — only x from D, y from E, tmp unchanged since C

## Common Pitfalls

- Forgetting to tag definitions with their location (xA vs xD are different facts)
- Not initialising with ∅ — must analysis would initialise differently
- Confusing "reaches" with "always reaches" — reaching definitions is may, not must
- Missing that loop-back edges cause definitions from inside the loop to reach back to the loop header

## Connections

- Builds on [[gen-kill-analysis]] for local transfer functions
- Solved by [[iterative-data-flow-analysis]]
- Produces [[du-chains-ud-chains]]: the DU-chain for a definition connects it to all uses it reaches
- Complementary to [[live-variable-analysis]] (forward may vs backward may)
- Enables [[common-subexpression-elimination]] and detects potentially uninitialized variables

## Open Questions

- How does reaching definitions change with SSA (Static Single Assignment) form?
- What is the relationship between reaching definitions and def-use chains in practice?
