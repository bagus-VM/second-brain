---
title: "MOP vs MFP"
tags: [concept, software-analyse, semester-1, data-flow, mop, mfp]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[data-flow-analysis]]", "[[lattice]]", "[[monotone-framework]]"]
---

## One-line Summary
The Meet Over All Paths (MOP) is the precise but undecidable data flow solution (join over the exact transfer-function composition of every execution path); the Minimal Fixed Point (MFP) is the computable sound solution (least fixed point of the global transfer function); for [[distributive-framework|distributive frameworks]] the two coincide, so MFP is as precise as MOP.

## Core Intuition
There are two ways to think about "the answer" to a data flow problem:

1. **Execute every path precisely.** Start from ⊥ at the entry. For every execution path, compose the transfer functions exactly. Join (⊔) the results of all paths. This is the **MOP** solution. It is *the most precise sound answer possible*. The problem: a real program has infinitely many paths, so MOP is generally undecidable.

2. **Find the smallest fixed point of the equations.** Define the data flow problem as a system of equations on the lattice. Solve the system by iterating from ⊥ until no change. This is the **MFP** solution. It is computable (the lattice is finite-height, transfer functions are monotone). It is *sound*. But it may be less precise than MOP — when the same program point is reached by multiple paths, the iterative algorithm may "lose" information that the path-by-path MOP would have kept.

The central theorem: **MFP = MOP if and only if the framework is distributive** (transfer functions distribute over join). All four classic analyses ([[reaching-definitions|reaching defs]], [[available-expressions|available exprs]], [[live-variable-analysis|live variables]], [[very-busy-expressions|very busy exprs]]) are distributive, so MFP gives the optimal answer for them. [[constant-propagation|Constant propagation]] is the canonical non-distributive analysis: the iterative MFP can be strictly weaker than MOP.

## Formal Definition / Statement

For a control flow graph with blocks b_0, b_1, ..., b_n and transfer functions f_0, ..., f_n:

- **MOP at b_i**:
  MOP(b_i) = ⊔ { f_{p_k} ∘ f_{p_{k-1}} ∘ ... ∘ f_{p_0} (⊥) | [p_0, p_1, ..., p_k] ∈ path(b_i) }
  
  where path(b_i) is the (possibly infinite) set of all execution paths from entry to b_i. For backward analyses, the same definition applies with path(b_i) being paths from b_i to exit.

- **MFP**: the smallest element x of the lattice such that the system of equations
  - IN(b) = ⊔ { OUT(p) | p ∈ pred(b) }  (for forward may)
  - OUT(b) = f_b(IN(b))
  is satisfied. Equivalently, the least fixed point of the global transfer function F: L^CFG → L^CFG that updates every block at once.

- **Theorem (Kildall-Cousot)**: MFP ⊑ MOP (MFP is a sound under-approximation of MOP).

- **Theorem (Distributivity)**: MFP = MOP iff every transfer function f_b is distributive over ⊔.

## Key Properties / Complexity

### Why MOP is undecidable in general
- Programs with loops have infinitely many execution paths
- Programs with recursion have infinitely many call paths
- Programs with dynamic dispatch have a path for every possible runtime type
- Even for loop-free programs, the number of paths can be exponential in program size
- Therefore, computing MOP exactly is generally impossible

### Why MFP is computable
- MFP is the *least fixed point* of F on the product lattice L^CFG
- L is finite-height, so L^CFG is finite-height
- F is monotone (transfer functions are monotone)
- Knaster-Tarski: iterating F from ⊥ reaches the least fixed point in at most h(L^CFG) steps
- Therefore MFP is computable

### Distributive frameworks — the four classics
All four standard data flow analyses are distributive:
- [[reaching-definitions]] — f_b(X) = gen(b) ∪ (X \ kill(b)) — distributes over ∪
- [[available-expressions]] — f_b(X) = gen(b) ∪ (X \ kill(b)) — distributes over ∩ (after the lattice is flipped)
- [[live-variable-analysis|live variables]] — f_b(X) = use(b) ∪ (X \ def(b)) — distributes over ∪
- [[very-busy-expressions|very busy expressions]] — f_b(X) = use(b) ∪ (X \ def(b)) — distributes over ∩

For these, MFP gives the optimal answer.

### The non-distributive case — constant propagation
- Abstract domain: each variable is either a specific constant, ⊤ (any value), or ⊥ (no info)
- Consider: x = 2; y = 2; if (condition) x = 3; else y = 3; ... x == y?
- MOP would compute x = 2 ∧ y = 3 and x = 3 ∧ y = 2 separately, and notice both have x ≠ y
- MFP would join the two paths, getting x = ⊤ ∧ y = ⊤, and lose the information
- This is a real, common loss of precision in iterative constant propagation

### Both solutions are sound
- MOP is the *best possible sound* solution (in the partial order)
- MFP is *a* sound solution, not necessarily the best
- Neither has false positives (for the negated property); both may have false negatives (missed real bugs)

## Worked Example

For the program
```
       b0
      / \
     b1   b2
      \ /
       b3
x := 3     (b1)       x := 1   (b2)
y := 1                y := 3
       b3: z := x + y
```

With abstract domain mapping x, y, z to specific constants (or ⊤):

- **MOP at b3**:
  - Path 1: x=3, y=1, z=4 → { z ↦ 4, x ↦ 3, y ↦ 1 }
  - Path 2: x=1, y=3, z=4 → { z ↦ 4, x ↦ 1, y ↦ 3 }
  - MOP = join of both = { z ↦ 4, x ↦ ⊤, y ↦ ⊤ }  (still has the precise z=4)

- **MFP at b3** (iterative, no distributivity):
  - Iteration 1: x = ⊤, y = ⊤, z = ⊥
  - Iteration 2: same (already stabilised)
  - MFP = { z ↦ 4, x ↦ ⊤, y ↦ ⊤ }

For this example, MFP happens to equal MOP because the analysis (constant propagation with simple addition) is "almost" distributive. The lecture's MOP vs MFP slides show a more complex case where they differ.

## Common Pitfalls

- **"MFP is MOP"** is a theorem, not a definition. It holds *only* for distributive frameworks.
- **MFP being computable is what makes data flow analysis practical**. If we needed MOP, we couldn't analyse any non-trivial program.
- **"MOP is undecidable" does not mean MOP is useless**. MOP is a *theoretical ideal* — a benchmark for "how precise could we be?" that lets us measure how much precision MFP loses.
- **Constant propagation is the canonical counter-example**, but many real analyses (e.g., tracking ranges) are also non-distributive and suffer the same gap.
- **The worklist algorithm computes MFP** — it does not compute MOP, no matter how cleverly you implement it.

## Connections

- [[data-flow-analysis]] — MOP and MFP are the two answers to a data flow problem
- [[lattice]] — the partial order on which the two solutions are compared
- [[monotone-framework]] — guarantees MFP exists and is computable
- [[distributive-framework]] — the condition for MFP = MOP
- [[iterative-data-flow-analysis]] — the worklist algorithm that computes MFP
- [[zero-analysis-worked-example]] — a distributive analysis; MFP = MOP for it
- [[software-analyse-lecture-6]] — the lecture that introduces the MOP/MFP distinction
- [[abstract-interpretation]] — the framework in which MFP and MOP are both well-defined

## Open Questions

- Are there practical analyses where the MOP-MFP gap is *unacceptably* large (i.e., MFP misses real bugs because of non-distributivity)?
- For non-distributive analyses, can we do better than MFP while still being computable? (Path-sensitive analysis, BDD-based analysis, etc.)
- The lecture uses constant propagation as the non-distributive example. Are there other standard non-distributive analyses students should know?
- How do modern tools (Infer, CodeQL) handle the MOP-MFP gap in practice?
