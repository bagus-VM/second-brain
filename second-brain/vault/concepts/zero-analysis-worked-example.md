---
title: "Zero Analysis"
tags: [concept, software-analyse, semester-1, abstract-interpretation, zero-analysis]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[abstract-interpretation]]", "[[lattice]]", "[[monotone-framework]]"]
---

## One-line Summary
Zero Analysis is the lecture's running example of [[abstract-interpretation|abstract interpretation]]: track for each variable whether its value is definitely zero (Z), definitely non-zero (NZ), or maybe zero (MZ) using a three-element abstract lattice, so that the analysis can soundly report "this program might divide by zero" without enumerating the infinite set of concrete integer values.

## Core Intuition
The goal of Zero Analysis is narrow: at every program point, for every variable, classify the value into one of three buckets:
- **Z** — definitely zero
- **NZ** — definitely non-zero
- **MZ** — might be zero (we don't know)

This is a coarser description than the concrete values, but it's enough to answer the question "will this program divide by zero?" — if at the point of a division, the divisor is Z or MZ, the program *might* divide by zero.

The three-element lattice is:
```
       MZ (top — no information)
      /  \
    Z    NZ (bottom-up: Z and NZ both approximate to MZ)
      \  /
       ⊥ (bottom — variable doesn't exist or has no info)
```
Lattice order: ⊥ ≤ Z, ⊥ ≤ NZ, Z ≤ MZ, NZ ≤ MZ, ⊥ ≤ MZ. So MZ is the *top* (most imprecise), Z and NZ are *middle* (more precise than MZ but incomparable to each other), and ⊥ is the *bottom* (most precise — but the program has no info here yet).

## Formal Definition / Statement

**Abstract domain** for a single variable: L_ZI = {⊥, Z, NZ, MZ}
- ⊥: variable has no information (program entry, or after declaration)
- Z: variable is definitely 0
- NZ: variable is definitely not 0
- MZ: variable might be 0 (we don't know which)

**Lattice order**:
- ⊥ ≤ Z, ⊥ ≤ NZ, ⊥ ≤ MZ
- Z ≤ MZ, NZ ≤ MZ
- Z and NZ are incomparable

**Join (⊔)** and **meet (⊓)** for single-variable:
- ⊔: ⊥ ⊔ X = X, X ⊔ X = X, Z ⊔ NZ = MZ, X ⊔ MZ = MZ
- ⊓: ⊥ ⊓ X = ⊥, X ⊓ X = X, Z ⊓ NZ = ⊥, Z ⊓ MZ = Z, NZ ⊓ MZ = NZ

**Abstract operations** (over-approximations of concrete arithmetic):
- +: see the full table below
- −: same structure as +
- ×: Z × Z = Z, Z × NZ = Z, NZ × NZ = MZ (could be anything)
- /: NZ / NZ = MZ, NZ / Z = undefined (warning), Z / anything = Z, etc.

**Abstract transfer function for assignment** `x := e`:
F_{x:=e}(σ) = σ[x ← α(e)]

where α(e) is the abstract value of expression e (computed by recursively abstracting sub-expressions and applying the abstract operations).

**Program lattice** (one fact per variable):
L_Z = L_ZI^Var, with pointwise order, join, meet, top, bottom.

**Fixed-point computation**:
- Start: σ = ⊥ (all variables have no info)
- Iterate: at each block, IN = ⊔ OUT(pred), OUT = transfer(IN)
- Stabilises when no change

## Key Properties / Complexity

### Abstract addition table (lecture slide 66)
```
   +  | ⊥  Z   NZ  MZ
  ────┼────────────────
   ⊥  | ⊥  ⊥  ⊥   ⊥
   Z  | ⊥  Z   NZ  MZ
   NZ | ⊥  NZ  MZ  MZ
   MZ | ⊥  MZ  MZ  MZ
```
Reading: Z + NZ = NZ (0 + anything non-zero is non-zero); NZ + NZ = MZ (we can't tell — could be any value).

### Abstract division table (the bug detector)
```
   /  | ⊥  Z   NZ  MZ
  ────┼────────────────
   ⊥  | ⊥  ⊥  ⊥   ⊥
   Z  | ⊥  ⊥  Z   ⊥    ← Z / Z = ⊥ (or "undefined")
   NZ | ⊥  ⊥  NZ  MZ
   MZ | ⊥  ⊥  MZ  MZ
```
The crucial cell: NZ / Z = ⊥. The analysis flags this as "division by zero is possible" — the warning the lecture wants to demonstrate.

### Lattice height
- Single variable: h(L_ZI) = 2 (⊥ → {Z, NZ} → MZ)
- For |Var| = n variables: h(L_Z) = 2n
- For the lecture's program with 4 variables (x, y, z, w or similar): h = 8

### Soundness
Every abstract operation over-approximates the concrete one:
- α(0 + 5) = α(0) ⊕ α(5) = Z ⊕ NZ = NZ; α(5) = NZ ✓
- α(3 + 5) = α(3) ⊕ α(5) = NZ ⊕ NZ = MZ; α(8) = NZ ⊑ MZ ✓ (over-approximation, sound)
- α(3 × 0) = α(3) ⊗ α(0) = NZ ⊗ Z = Z; α(0) = Z ✓

### Termination in h(L) iterations
The lecture's program converges in 3 iterations total. Iteration 1 reaches the "first information", iteration 2 reaches the "second information", iteration 3 confirms no change (fixed point).

## Worked Example: full lecture trace

The lecture walks through the program
```
x := 8;
y := x;
z := 0;
while y > -1 do
  x := x / y;
  y := y - 2;
  z := 5;
```

Iterating the abstract interpretation:

| Step | σ after line | Why |
|------|-------------|-----|
| Initial | [ ] | Empty map at program entry |
| x := 8 | [x → NZ] | α(8) = NZ |
| y := x | [x → NZ, y → NZ] | y assigned x's abstract value |
| z := 0 | [x → NZ, y → NZ, z → Z] | α(0) = Z |
| (entering while) | [x → NZ, y → NZ, z → Z] | y ∈ NZ ⊆ {… -1, 1, 2, 3, …} — y > -1 is *possible* |
| x := x / y | [x → NZ, y → MZ, z → Z] | NZ / NZ = MZ (the **warning trigger** — y might be 0) |
| y := y - 2 | [x → NZ, y → MZ, z → Z] | α(MZ - 2) = MZ (we can't tell) |
| z := 5 | [x → NZ, y → MZ, z → NZ] | α(5) = NZ |

Join across loop iterations propagates the MZ forward. After 2 iterations, the lattice stabilises:
- x = NZ (definitely not zero, since x is initialised to 8 and only NZ / NZ results)
- y = MZ (could be anything by the time we re-enter the loop)
- z = NZ (last assignment is 5)

**The warning**: at `x := x / y`, the abstract value of y is MZ (and later confirmed MZ). The abstract division NZ / MZ = MZ. But the more precise analysis NZ / Z = ⊥ would also trigger. Either way: **division by zero is possible** — the analysis issues a warning.

## Common Pitfalls

- **MZ is a "give up" element**. The analysis gives up tracking precise information for y once y might be zero. This is sound (over-approximates) but imprecise — a more precise abstract domain (e.g., parity + zero + sign) could keep more information.
- **"Z and NZ" are not symmetric**. NZ covers "any non-zero value" — including, e.g., 2⁶⁴-1, π-as-int, etc. The analysis does not track magnitudes.
- **The transfer function for `x := e` only updates x**. Other variables keep their values. This is the per-variable aspect of the program lattice.
- **Abstract operations must be sound** (over-approximate). An under-approximation would miss bugs.
- **The lattice height bounds the iteration count**. For the 4-variable lecture example: h = 8, so convergence in at most 8 iterations. The lecture shows it converges in 3.

## Connections

- [[abstract-interpretation]] — Zero Analysis is the lecture's concrete example of abstract interpretation
- [[lattice]] — the three-element domain is a small lattice
- [[monotone-framework]] — the lattice + monotone transfer functions form an instance of the framework
- [[data-flow-analysis]] — Zero Analysis is a data flow analysis (forward, may, with per-variable lattice)
- [[mop-vs-mfp]] — Zero Analysis is distributive, so MFP = MOP
- [[iterative-data-flow-analysis]] — the worklist algorithm that computes the fixpoint
- [[software-analyse-lecture-6]] — the lecture where this is the running example

## Open Questions

- Could we use a more precise abstract domain (e.g., a "sign + zero" lattice with {+, −, 0, *}) to keep more information for the lecture program?
- For real programs, what is the typical lattice height? How does it scale with the number of tracked variables?
- The lecture assumes the abstract operations are sound but does not prove it. How do we *verify* that Z ⊕ NZ = NZ is a sound over-approximation of concrete 0 + n (n ≠ 0)?
- How do we extend Zero Analysis to handle floating point, pointers, and dynamic memory?

## Worked Example

*To be filled.*
