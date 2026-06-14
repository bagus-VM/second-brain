---
title: "Lecture 6: Data Flow Analysis Part 2 — Lattice-Theoretic Framework and Abstract Interpretation"
tags: [topic, software-analyse, semester-1, lattice-theory, abstract-interpretation, data-flow]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[software-analyse-lecture-5]]", "[[monotone-framework]]", "[[data-flow-analysis]]"]
---

## One-line Summary
The [[monotone-framework]] is grounded in a [[lattice|lattice]] of facts, a join operator, and monotone transfer functions; this lecture shows why every [[iterative-data-flow-analysis|iterative data flow analysis]] must converge, defines the precise relationships [[mop-vs-mfp|MOP vs MFP]] and when they coincide ([[distributive-framework|distributivity]]), and introduces [[abstract-interpretation|abstract interpretation]] as the generalisation — using a [[zero-analysis-worked-example|Zero Analysis]] of a division-by-zero warning as the running example.

## Core Intuition

L05 showed the *mechanics* of data flow analysis: gen/kill sets, IN/OUT equations, worklist algorithm. L06 answers the *meta-question*: why does this machinery always terminate, and when does it give the *best possible* answer?

The answer has three parts:

1. **Why does it terminate?** Because the data flow facts form a [[lattice]] — a partially ordered set where every ascending chain has an upper bound. Transfer functions are monotone: if you give them *more* knowledge, they produce *at least as much* knowledge. So each iteration can only add facts, never remove them, and since the lattice is finite-height, the process must stabilise.

2. **What answer do we get?** The iterative algorithm computes the [[minimal-fixed-point-algorithm|Minimal Fixed Point (MFP)]]. The ideal would be the Meet Over All Paths (MOP) — the precise result of joining the exact output of *every* execution path. MOP is undecidable in general. MFP is the *smallest* solution of the data flow equations; it is computable; it is sound; and it is *as precise as MOP* precisely when the analysis is [[distributive-framework|distributive]].

3. **What is the general theory?** [[abstract-interpretation|Abstract interpretation]] generalises everything. The concrete semantics (real program execution) is mapped to an *abstract domain* (a smaller, computable description of program behaviour) by an *abstraction function* α. Abstract operations must agree with concrete ones modulo α — this is the [[galois-connection|Galois connection]] between concrete and abstract worlds. Data flow analysis *is* a particular choice of abstract domain.

The lecture's running example is [[zero-analysis-worked-example|Zero Analysis]]: track for each variable whether it is definitely zero, definitely non-zero, or maybe zero. The lattice has three elements Z, NZ, MZ, with the order Z ≤ MZ, NZ ≤ MZ, ⊥ ≤ everything. The "abstract domain" of (NZ, Z, MZ) abstracts away the infinite concrete domain of actual integer values. The result: we can prove the program *might* divide by zero without ever running it.

## Key Concepts

### The lattice apparatus
- [[lattice]] — partially ordered set with a unique least upper bound (⊔, join) and greatest lower bound (⊓, meet) for every pair of elements
- lattice height — length of the longest ascending chain; bounds the iteration count
- ⊤ and ⊥ — top (least precise / universal) and bottom (most precise / empty)
- product lattice — tuple of lattices with componentwise order; the standard way to model multiple variables
- powerset lattice — ℘(U) ordered by ⊆; the natural lattice for "set of X" analyses

### The monotone framework (Killdall '77)
- [[monotone-framework]] — already known; L06 anchors it in lattice theory
- monotonicity of transfer functions — x ⊑ y ⟹ f(x) ⊑ f(y)
- termination — guaranteed because the lattice is finite-height and f is monotone

### The two ideal solutions
- [[mop-vs-mfp|MOP vs MFP]] — MOP is precise but undecidable; MFP is computable and sound
- distributive framework — MFP = MOP iff the transfer functions distribute over join
- constant propagation — the classic non-distributive analysis; MFP loses precision

### The worklist algorithm
- [[minimal-fixed-point-algorithm|Minimal Fixpoint Algorithm (MFP)]] — chaotic iteration with a worklist; the practical implementation of the monotone framework
- postorder / reverse postorder — node orders that speed up convergence; backward analyses use postorder, forward use reverse postorder

### Abstract interpretation
- [[abstract-interpretation]] — the general theory: concrete semantics → abstract domain → sound abstract operations
- abstraction function α — maps concrete values into the abstract domain
- concretisation function γ — the right adjoint; recovers concrete values from abstract facts
- [[galois-connection|Galois connection]] — the formal requirement that α and γ are adjoints

### Worked example: Zero Analysis
- [[zero-analysis-worked-example|Zero Analysis]] — track for each variable whether it is Z, NZ, or MZ
- Z/NZ/MZ lattice — three-element lattice
- abstract + − × / — tables of abstract operations
- fixpoint computation — three iterations to convergence
- zero division warnings — practical output: "this program might produce a division by zero"

## Formal Statement: the MOP / MFP / Distributivity theorem

For a data flow problem with lattice L, transfer functions f_b (one per block b), and entry value ⊥:

- **MOP solution** at block b_i:
  MOP(b_i) = ⊔ { f_{p_k} ∘ ... ∘ f_{p_0} (⊥) | [p_0, ..., p_k] ∈ path(b_i) }
  MOP joins the *exact* transfer-function composition over every execution path. MOP is undecidable in general (infinitely many paths).

- **MFP solution** at block b_i: the smallest x ∈ L such that x ⊒ f_{b_i}(x) (or the analogous equation under the chosen direction). MFP is the least fixed point of the global transfer function on the product lattice.

- **Theorem (Distributivity)**: if every transfer function distributes over join — f(x ⊔ y) = f(x) ⊔ f(y) — then MFP = MOP.

- **The four classic analyses are distributive**: [[reaching-definitions]], [[available-expressions]], [[live-variable-analysis|live variables]], [[very-busy-expressions]] all satisfy distributivity, so MFP = MOP for them. *Constant propagation* is the canonical non-distributive example.

## Key Properties

### Why finite lattices guarantee termination
- Each iteration can only move "up" the lattice (by monotonicity of f and the fact that f(x) ⊒ x is preserved)
- A finite-height lattice has no infinite ascending chains
- Therefore the iteration reaches a fixed point in at most h(L) steps (per program point)
- For [[zero-analysis-worked-example|Zero Analysis]]: h(L) = 2 (bottom → {Z,NZ} → MZ = top), so the example converges in ≤ 2 iterations per program point. The lecture's worked example shows exactly 3 iterations to full convergence (the third is a "no change" verification).

### Why MOP is undecidable
- A program may have infinitely many execution paths (loops, recursion, dynamic dispatch)
- Enumerating all paths and composing transfer functions over each is not generally computable
- MOP is therefore a *theoretical ideal* — a benchmark for "how precise could we be?" — not an algorithm

### The semantic abstraction diagram
```
Concrete world         α         Abstract world
                                          
… −1 0 1 2 3 …    ──────►    NZ  Z  ⊤
                              │
                       γ
                              │
                              ▼
… −1 0 1 2 3 …
```
- α lifts concrete values into the abstract domain: α(0) = Z, α(n≠0) = NZ
- γ drops back to concrete: γ(Z) = {0}, γ(NZ) = {n : n ≠ 0}, γ(MZ) = ℤ
- The diagram commutes: applying γ to α of a concrete value is a sound over-approximation

### Traversal order matters
- reverse postorder — visits a node after all its predecessors; ideal for forward data flow because it propagates information in the natural flow direction in one pass
- postorder — visits a node after all its successors; ideal for backward data flow
- Bad order can multiply the iteration count

## Worked Example: Zero Analysis trace

For the program
```
x := 8; y := x; z := 0;
while y > -1 do
  x := x / y;
  y := y - 2;
  z := 5;
```
with abstract domain {Z, NZ, MZ} and lattice order Z ≤ MZ, NZ ≤ MZ, ⊥ ≤ everything:

| Iteration | σ after line 1 (x := 8) | after 2 (y := x) | after 3 (z := 0) | after 4 (x := x/y) | after 5 (y := y-2) | after 6 (z := 5) |
|-----------|------------------------|------------------|------------------|---------------------|---------------------|-------------------|
| 1 | [x → NZ] | [x → NZ, y → NZ] | [x → NZ, y → NZ, z → Z] | [x → NZ, y → NZ, z → Z] | [x → NZ, y → MZ, z → Z] | [x → NZ, y → MZ, z → NZ] |
| 2 | same | same | same | [x → NZ, y → MZ, z → MZ] | [x → NZ, y → MZ, z → Z] | [x → NZ, y → MZ, z → NZ] |
| 3 | same | same | same | [x → NZ, y → MZ, z → MZ] | [x → NZ, y → MZ, z → MZ] | [x → NZ, y → MZ, z → NZ] |

The third iteration is a *no-change* pass — the fixed point. The lattice height is 2 (Z, NZ → MZ), so the algorithm converges in at most 2 upward moves. The final result `[x → NZ, y → MZ, z → NZ]` means "y is *maybe* zero at the point of the division" — the warning trigger.

## Common Pitfalls

- **"MOP = MFP" is a theorem, not a definition**. It holds *only* for distributive frameworks. For non-distributive analyses (constant propagation), MFP can be strictly less precise than MOP.
- **The lattice order direction depends on the analysis**. For *may* analyses, ⊥ = ∅ and facts accumulate upward. For *must* analyses, ⊤ = universal and facts accumulate downward. The lecture shows both conventions explicitly.
- **"Monotone" is about preserving order, not about being a mathematical monotone function**. The transfer function f: L → L satisfies x ⊑ y ⟹ f(x) ⊑ f(y). It does *not* mean f is increasing in the everyday sense.
- **The lattice has to be finite for guaranteed termination**. Real abstract domains (intervals, polyhedra) are infinite; you need [[widening-narrowing|widening]] to force convergence. The lecture does not cover this — it's in [[software-analyse-lecture-7|the next lecture]] or a follow-up.
- **Abstraction must be sound**. The abstract operation ⊕ must *over-approximate* the concrete one: α(a ⊕_concrete b) ⊑ α(a) ⊕_abstract α(b). Soundness guarantees no missed warnings. Imprecise ≠ unsound.
- **The "MZ" element exists to be sound but imprecise**. NZ/NZ division is MZ because we cannot determine the sign of the result. The cost of soundness is loss of precision.
- **Abstract interpretation is a *framework*, not an algorithm**. It tells you how to *describe* an analysis soundly. The algorithm (worklist, chaotic iteration, etc.) is separate.

## Connections

- [[software-analyse-lecture-5]] — gen/kill, worklist, the *mechanics* that L06 grounds in lattice theory
- [[monotone-framework]] — the central abstraction; L06 gives it a formal foundation
- [[data-flow-analysis]] — the family of analyses; L06 shows when they are precise
- [[abstract-interpretation]] — the generalisation introduced in the second half
- [[mop-vs-mfp]] — the central precision/soundness tradeoff
- [[distributive-framework]] — the condition that makes MFP = MOP
- [[zero-analysis-worked-example]] — the running example end-to-end
- [[software-analyse-lecture-7]] — interprocedural analysis extends the same lattice machinery across function calls
- [[widening-narrowing]] — needed for infinite lattices (intervals, polyhedra) — covered later
- [[reaching-definitions]], [[available-expressions]], [[live-variable-analysis]], [[very-busy-expressions]] — the four distributive classic analyses

## Open Questions

- How do [[widening-narrowing|widening and narrowing]] operators formalize convergence for *infinite* lattices (intervals, polyhedra)? The lecture assumes finite height; real abstract domains are infinite.
- What is the formal relationship between [[abstract-interpretation|abstract interpretation's]] [[galois-connection|Galois connections]] and the [[monotone-framework|monotone framework's]] lattices? They look the same — are they?
- The lecture claims the four classic analyses are distributive. Is there a simple test for distributivity, or do you have to check by hand?
- For non-distributive analyses like constant propagation, how bad is the MFP-MOP gap in practice? Is it tolerable, or do we need a fundamentally different approach?
- Modern static analyzers (Infer, CodeQL, Semgrep) use various abstract domains. Which choices of domain give the best precision/speed tradeoff in practice?
- The lecture ends with the Zero Analysis fixpoint computation. Does the example actually warn about the *real* division-by-zero in `x := x / y`? (Hint: y = MZ at that point, so yes — but verify by tracing the lattice join carefully.)
