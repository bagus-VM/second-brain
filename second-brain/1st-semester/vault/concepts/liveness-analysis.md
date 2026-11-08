---
title: "Liveness Analysis"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[control-flow-graph]]", "[[gen-kill-analysis]]"]
---
## One-line Summary
Liveness analysis figures out, for every point in a program, which variables still have a future use — essential for knowing when a value can be thrown away or a register freed.

## Core Intuition
A variable is **live** at a program point if there exists some future execution path that will read it before redefining it. It is **dead** if every path either redefines it or exits the program without reading it. This is a backward analysis: we start from the end of the program (where nothing is live) and propagate backwards, asking "does any successor need this variable?" Liveness is the foundation for [[dead-code-elimination]] (remove assignments to dead variables) and [[register-allocation]] (only live variables need registers). The analysis is "may" — a variable is live if it *might* be used, not if it *must* be used.

## Formal Definition / Statement

**Live Variable Analysis** — a backward, may data flow analysis.

**Domain**: Sets of variables.

**Equations** (backward):
```
OUT(n) = ∪ IN(s)           for s ∈ succ(n)
IN(n)  = use(n) ∪ (OUT(n) - def(n))
```

Where:
- `use(n)` = set of variables whose values are read at statement n *before* any definition at n
- `def(n)` = set of variables defined (assigned) at statement n
- `succ(n)` = successor blocks in the [[control-flow-graph]]

**Initialisation**: OUT(exit) = ∅ (nothing is live after the program ends). All other sets: ∅.

**Join operator**: ∪ (union) — a variable is live if it's live on *any* successor path (may analysis).

**Iteration**: Process blocks in reverse depth-first order until fixed point.

## Key Properties / Complexity

- **Direction**: Backward (data flows from successors to predecessors)
- **Kind**: May (union at join points)
- **Convergence**: Guaranteed because the fact space (power set of variables) is finite and transfer functions are monotone
- **Optimal order**: Reverse postorder (reverse depth-first) for fastest convergence
- **Time complexity**: O(|V| · |vars|) per iteration, typically converges in 2-3 iterations for structured programs
- A variable is live at a point iff there is a **use-clear path** from that point to some use of the variable (no redefinition along the path)
- Liveness is the dual of [[reaching-definitions]]: forward may (reaching defs) vs. backward may (liveness)

## Worked Example

```java
// Simple program
1: x = 3;        // def = {x}, use = {}
2: y = x + 1;    // def = {y}, use = {x}
3: z = y * 2;    // def = {z}, use = {y}
4: x = z + y;    // def = {x}, use = {z, y}
5: return x;     // def = {}, use = {x}
```

Backward pass:
```
Statement 5: IN = {x}, OUT = {}        (x is used, nothing after)
Statement 4: IN = {z, y}, OUT = {x}    (z,y used; x is live from stmt 5 but killed here)
Statement 3: IN = {y}, OUT = {z, y}    (y used; z,y live from stmt 4)
Statement 2: IN = {x}, OUT = {y}       (x used; y live from stmt 3 but killed here)
Statement 1: IN = {}, OUT = {x}        (x defined here, so not live before; x live from stmt 2 but killed)
```

Results:
- Statement 1: `x = 3` — x is dead after stmt 1 (redefined at stmt 4 before next use at stmt 5)... wait, actually x is used at stmt 2. So x is live after stmt 1.
- Actually x IS live after stmt 1 (used at stmt 2). So `x = 3` is NOT dead.
- At statement 4: `x = z + y` — after this, x is live (used at stmt 5). So this is not dead either.
- All assignments are live in this example. The analysis confirms no dead code exists.

With a modification:
```java
1: x = 3;        // def={x}
2: y = 5;        // def={y}, kill y from stmt 1
3: z = y + 1;    // def={z}, use={y}
4: x = z;        // def={x}, use={z}
5: return x;
```

After stmt 2: y is live (used at stmt 3). After stmt 1: x is NOT live (redefined at stmt 4 before use at stmt 5, and not used at stmt 2 or 3). So `x = 3` at stmt 1 is a dead assignment!

## Common Pitfalls

- Confusing **liveness** (backward, "will be used in the future") with **reaching definitions** (forward, "was defined in the past")
- Forgetting that liveness is **may**: a variable is live if used on *any* future path, not *all* future paths
- Not accounting for use-before-def within the same statement: in `x = x + 1`, x is both used and defined; x is in use(n) AND def(n)
- The order of use and def matters: in `x = x + 1`, the read of x happens before the write
- Forgetting to initialise OUT(exit) = ∅ — without this, the analysis doesn't converge correctly
- Liveness analysis doesn't distinguish between "used once" and "used many times" — both are equally "live"

## Connections

- [[dead-code-elimination]] — the primary consumer: remove assignments where the variable is dead
- [[register-allocation]] — only live variables need registers; liveness determines register pressure
- [[data-flow-analysis]] — liveness is one of the four classic analyses (backward, may)
- [[reaching-definitions]] — the complementary forward may analysis
- [[gen-kill-analysis]] — liveness uses gen = use(n), kill = def(n)
- [[du-chains-ud-chains]] — DU-chains connect definitions to uses via liveness
- [[iterative-data-flow-analysis]] — the worklist algorithm that solves liveness equations
- [[monotone-framework]] — liveness can be formalized as an instance of the monotone framework
- [[software-analyse-lecture-5]] — lecture where liveness analysis is introduced

## Open Questions

- How does liveness analysis change in SSA form (where each variable is defined exactly once)?
- What is the relationship between liveness and interference graphs in [[register-allocation]]?
- How do we extend liveness analysis to handle arrays and pointers?
