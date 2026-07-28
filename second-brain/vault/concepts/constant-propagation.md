---
title: "Constant Propagation"
tags: [concept, software-analyse, semester-1, data-flow, constant-propagation, non-distributive]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[data-flow-analysis]]", "[[mop-vs-mfp]]", "[[distributive-framework]]"]
---

## One-line Summary
Constant propagation is a [[data-flow-analysis|data flow analysis]] that tracks, for each variable, whether its value is a known constant at each program point — the canonical example of a *non-distributive* analysis, where [[mop-vs-mfp|MFP loses precision compared to MOP]].

## Core Intuition
The analysis: for each program point and each variable, determine whether the variable is a known constant (and which one) or "unknown" (⊤). When a variable is assigned `x := 5`, the analysis says "x is 5". When a variable is conditionally assigned (`if (c) x = 2; else x = 3;`), the analysis says "x is unknown" (we don't know which branch was taken).

Constant propagation is *useful* — compilers use it to fold constants, eliminate dead branches, and enable other optimisations. But it's also *hard* in a precise sense: the iterative [[mop-vs-mfp|MFP]] can lose precision compared to the ideal [[mop-vs-mfp|MOP]].

The classic example:
```c
if (c) x = 2; else x = 3;
if (c) y = 3; else y = 2;
// x and y are always different (one is 2, the other is 3)
z = x + y;  // z is always 5
```
- MOP tracks the two paths separately: along path 1, x=2, y=3, z=5; along path 2, x=3, y=2, z=5. Join: z=5.
- MFP joins the paths at the if: x ∈ {2, 3} (the join loses the "2 if path 1, 3 if path 2" information). Then z = x + y = {2, 3} + {2, 3} = unknown.

MFP loses the fact that z is always 5. This is the non-distributivity of constant propagation in action.

## Formal Definition / Statement

**Abstract domain** (for a single variable): L_CP = {⊥} ∪ {c : c is a constant} ∪ {⊤}
- ⊥: no information
- c: known constant c
- ⊤: unknown (might be any value)

**Lattice order**:
- ⊥ ≤ c, ⊥ ≤ ⊤
- c ≤ ⊤ for all c
- c₁ and c₂ are incomparable (c₁ ≠ c₂)

**Join** (⊔):
- ⊔ c, c = c
- ⊔ c, ⊤ = ⊤
- ⊔ c₁, c₂ = ⊤ (if c₁ ≠ c₂)
- ⊔ ⊥, x = x

**Transfer function for `x := e`**:
- If e is a known constant: f(σ) = σ[x ← e]
- If e is a known operation on known constants: f(σ) = σ[x ← eval(e)]
- If e involves ⊤: f(σ) = σ[x ← ⊤]

**Conditional branches** (`if (c) S1 else S2`): the analysis joins the results of S1 and S2, losing the per-path precision.

## Key Properties / Complexity

### Why constant propagation is non-distributive
The non-distributivity comes from conditional branches. The transfer function for `if (c) S1 else S2` essentially does:
- After S1: σ₁ (specific to path 1)
- After S2: σ₂ (specific to path 2)
- After the join: σ₁ ⊔ σ₂ (loses path-specific information)

For the same statement applied to two different inputs:
- f(σ₁) at one point, f(σ₂) at another, then join: gives the joined result
- Join the inputs first, then apply: gives a possibly different result

This asymmetry is the source of the MOP-MFP gap.

### Why it's still useful
- Even the MFP solution is useful: it tells us "x is definitely 5" or "x is definitely not 5", etc.
- The lost precision is in *conditional* assignments, which are common but not universal
- For programs without conditionals on the tracked variables, MFP = MOP

### Practical implementations
- GCC and LLVM use **conditional constant propagation** (also called "sparse conditional constant propagation" or SCCP) — a more precise analysis that tracks constants *along the CFG paths* and only joins at merge points when actually needed
- SCCP is more expensive than naive constant propagation but much more precise
- Modern compilers use SCCP by default; "constant propagation" usually means SCCP in practice

### Why the Lattice is infinite
The lattice L_CP for a single variable is finite (assuming the variable type is finite, like int). But for a program with n variables, the program lattice is L_CP^n, which is huge. And for floating-point or symbolic constants, the lattice is infinite.

## Worked Example

The lecture's MOP vs MFP example:
```c
       b0
      / \
     b1   b2
      \ /
       b3
x := 3     (b1)       x := 1   (b2)
y := 1                y := 3
       b3: z := x + y
```

**MOP at b3**:
- Path 1: x=3, y=1, z=4 → σ₁ = {z ↦ 4, x ↦ 3, y ↦ 1}
- Path 2: x=1, y=3, z=4 → σ₂ = {z ↦ 4, x ↦ 1, y ↦ 3}
- MOP = σ₁ ⊔ σ₂ = {z ↦ 4, x ↦ ⊤, y ↦ ⊤}  (still has z=4)

**MFP at b3** (iterative, no distributivity):
- Initial: all variables ⊤
- Iteration 1: b0 sets x={l0}, y={l1}, z={l2} (just the definitions)
  - At b1: x=3, y=1
  - At b2: x=1, y=3
  - Join at b3: x ∈ {1, 3}, y ∈ {1, 3}, z=⊥
  - z := x + y: z ∈ {2, 4, 4, 6} = ⊤
  - MFP at b3: x ∈ {1, 3}, y ∈ {1, 3}, z = ⊤
- For this particular program, MFP happens to be the same as MOP because x+y always gives 4 along both paths. But for `z = x * y` or other non-linear operations, MFP would lose precision.

## Common Pitfalls
- **"Constant propagation" can mean two things**: the simple data flow analysis (lose precision at conditionals) or SCCP (preserve precision by tracking paths). The lecture describes the simple one.
- **MFP = ⊤ does not mean the program has no constants**. It means the *iterative* algorithm couldn't track them. A path-sensitive analysis (SCCP) might find the constants.
- **Non-distributive does not mean "broken"**. MFP is still *sound*; it just may be less precise than MOP. For many programs, the precision loss is acceptable.
- **Distinguishing ⊤ from "definitely not this constant"** matters. A variable in {2, 3} is not in {5, 6}, which the analysis should distinguish.
- **The lattice has to be finite for guaranteed termination**. For real programs with arbitrary integer constants, the lattice is large but finite (assuming fixed-width types).

## Connections
- [[data-flow-analysis]] — the family of analyses
- [[mop-vs-mfp]] — the precision/algorithm tradeoff
- [[distributive-framework]] — the condition for MFP = MOP
- [[reaching-definitions]] — distributive; can be combined with constant propagation
- [[software-analyse-lecture-6]] — the lecture

## Open Questions
- How much precision is lost in practice for real programs? (Empirically, SCCP recovers most of the lost precision.)
- Can we design a constant-propagation analysis that is both distributive and precise? (No, by the definition of distributivity — but the practical workaround is SCCP.)
- How do modern compilers (GCC, LLVM) handle constant propagation? (SCCP by default, with various tradeoffs.)
