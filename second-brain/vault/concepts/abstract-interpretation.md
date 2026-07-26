---
title: "Abstract Interpretation"
tags: [concept, software-analyse, semester-1, abstract-interpretation]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[monotone-framework]]", "[[lattice]]", "[[data-flow-analysis]]"]
---

## One-line Summary
Abstract interpretation is the general theoretical framework for soundly approximating the semantics of programs — it formalises the relationship between a *concrete* execution model (infinitely many states, generally uncomputable) and an *abstract* model (finitely many facts, always computable), so that data flow analysis can be defined as a *particular choice of abstract domain*.

## Core Intuition
Software is too large to analyse precisely: a single integer variable can take 2⁶⁴ values, a loop can iterate forever, a pointer can alias billions of heap objects. But we rarely need the *exact* answer — we need a *sound* one. "Will this program divide by zero?" requires knowing whether the divisor *might* be zero, not the exact runtime value.

[[abstract-interpretation|Abstract interpretation]] is the discipline of designing *sound approximations*:

- The **concrete world** is the program's actual semantics — the real set of reachable states, the real set of runtime values
- The **abstract world** is a smaller, simpler description — e.g., "the variable is definitely zero, definitely non-zero, or maybe zero"
- An **abstraction function α** maps concrete facts to abstract facts
- A **concretisation function γ** maps abstract facts back to concrete facts
- The pair (α, γ) forms a [[galois-connection|Galois connection]] — every abstract fact corresponds to a set of concrete facts
- Abstract operations must *over-approximate* concrete ones: α(operate(a, b)) ⊑ abstract_op(α(a), α(b))

When this discipline is followed, anything the abstract analysis *proves* is also true in the concrete world — the analysis is **sound**. It may miss some true facts (imprecise), but it will never claim a false fact (no false positives for the *negation* of the property).

[[data-flow-analysis|Data flow analysis]] *is* abstract interpretation with a particular choice of abstract domain ([[zero-analysis-worked-example|Zero Analysis]] uses the three-element lattice {Z, NZ, MZ}; [[reaching-definitions|reaching definitions]] uses the powerset of definition sites; [[live-variable-analysis|live variables]] uses the powerset of variables).

## Formal Definition / Statement

Let (C, ⊑_C) be the **concrete domain** (e.g., ℘(ℤ) for the set of possible values of one variable) and (A, ⊑_A) be the **abstract domain** (e.g., {⊥, Z, NZ, MZ}).

A **Galois connection** C ⇄ A consists of:
- α: C → A (abstraction)
- γ: A → C (concretisation)
such that for all c ∈ C, a ∈ A: α(c) ⊑_A a ⟺ c ⊑_C γ(a)

The semantic abstraction diagram (the lecture's central picture):

```
   Concrete (C)               Abstract (A)
   ─────────────             ──────────────
   ⋯ -2 -1 0 1 2 ⋯    α     ⊥  Z  NZ  MZ
                          ──►
                          ◄──
                          γ
```

**Soundness of abstract operations**: for a concrete operation op_concrete: C × C → C and an abstract operation op_abstract: A × A → A:
- α(op_concrete(c₁, c₂)) ⊑_A op_abstract(α(c₁), α(c₂))
- Equivalently: op_concrete(γ(a₁), γ(a₂)) ⊑_C γ(op_abstract(a₁, a₂))

This guarantees: if the abstract analysis says "property P holds", then property P holds concretely.

**Transfer function as abstract operation**: for [[data-flow-analysis|data flow analysis]], the transfer function f_b of block b is the abstract counterpart of the concrete semantics step. The lattice of abstract facts and the monotone transfer functions together form an instance of the [[monotone-framework|monotone framework]].

## Key Properties / Complexity

### Why abstract interpretation is sound by construction
- Every abstract fact γ(a) is a *set* of concrete facts
- Every abstract operation produces a γ-image that contains all concrete results
- Therefore: anything provable in the abstract world is provable in the concrete world
- The cost: false positives (the analysis may flag issues that cannot actually occur)

### The four requirements of an abstract interpretation
1. **A concrete semantics**: what does the program *actually* compute?
2. **An abstract domain**: what *facts* will the analysis track?
3. **Abstraction and concretisation**: α and γ with a Galois connection
4. **Sound abstract operations**: every abstract operation is an over-approximation

### Zero Analysis as canonical example
- Concrete: ℤ (or ℘(ℤ) for a variable's possible values)
- Abstract: {⊥, Z, NZ, MZ}
- α(0) = Z; α(n) = NZ for n ≠ 0
- γ(⊥) = ∅; γ(Z) = {0}; γ(NZ) = {n: n ≠ 0}; γ(MZ) = ℤ
- Abstract addition: Z ⊕ Z = Z (0+0=0); Z ⊕ NZ = NZ (0 + n ≠ 0 = n ≠ 0); NZ ⊕ NZ = MZ (cannot determine the result)
- Abstract division: NZ ⊘ NZ = MZ (the running concern — division by zero is NZ ⊘ Z = undefined)

### Local vs global soundness
- *Local soundness*: each transfer function is a sound abstract operation
- *Global soundness*: the composition of locally sound transfer functions is sound
- Global soundness follows from local soundness + monotonicity

## Worked Example

The lecture's [[zero-analysis-worked-example|Zero Analysis]] walk-through (see [[software-analyse-lecture-6]] for the full trace):

```
x := 8;     α(8) = NZ, so σ₁ = [x → NZ]
y := x;     σ₂ = [x → NZ, y → NZ]
z := 0;     α(0) = Z, so σ₃ = [x → NZ, y → NZ, z → Z]
y > -1;     test is "is y's abstract value compatible with y > -1?"
            y ∈ NZ: all non-zero values include both > -1 and ≤ -1
            so the test may succeed — we continue
x := x / y; abstract operation NZ ⊘ NZ = MZ
            σ₄ = [x → NZ, y → MZ, z → MZ]  ← division is the trigger
y := y - 2; α(NZ ⊖ 2) = α(any − 2) = MZ (cannot determine parity)
            σ₅ = [x → NZ, y → MZ, z → MZ]
z := 5;     α(5) = NZ, so σ₆ = [x → NZ, y → MZ, z → NZ]
```

The fixed point: at the point of the division (σ₄), y is MZ — meaning y *might* be zero. Therefore the analysis issues a warning. This is what an abstract interpretation looks like in practice: small, finite lattice; monotone transfer functions; a Galois connection back to the concrete semantics; a sound answer at the end.

## Common Pitfalls

- **Abstract interpretation is not an algorithm**. It is a *framework* for designing sound analyses. The algorithm (worklist, chaotic iteration, etc.) is a separate concern.
- **"Sound" ≠ "complete"**. A sound analysis may miss real bugs (false negatives — the property holds abstractly, but actually a bug exists). A complete analysis is too expensive (MOP) or undecidable.
- **"Over-approximation" is required, not optional**. If your abstract operation under-approximates, your analysis is unsound — it will miss real bugs.
- **The abstract domain is a design choice**. Pick a domain that is *expressive enough* to prove the properties you care about and *small enough* to be efficient. There is a precision/cost tradeoff.
- **Don't confuse α with a hash function or compression**. α loses information irreversibly. γ brings back the *set* of all concrete facts that could have produced the abstract fact — not the original.

## Connections

- [[monotone-framework]] — abstract interpretation generalises the monotone framework
- [[lattice]] — concrete and abstract domains are both lattices
- [[data-flow-analysis]] — every data flow analysis is an instance of abstract interpretation
- [[zero-analysis-worked-example]] — the lecture's running example
- [[software-analyse-lecture-6]] — the lecture that introduces abstract interpretation
- [[widening-narrowing]] — needed for infinite abstract domains (intervals, polyhedra)
- [[galois-connection]] — the formal link between concrete and abstract
- [[mop-vs-mfp]] — MOP/MFP are precision/algorithm tradeoffs in the abstract interpretation view
- [[soundness-and-completeness]] — the sound/complete distinction is foundational
- [[static-vs-dynamic-analysis]] — static analysis is enabled by abstract interpretation; dynamic analysis uses concrete execution

## Open Questions

- How do [[widening-narrowing|widening and narrowing]] operators work for *infinite* abstract domains (intervals, polyhedra, octagons)? The lecture assumes finite.
- What is the formal relationship between [[abstract-interpretation|abstract interpretation's]] [[galois-connection|Galois connections]] and the [[monotone-framework|monotone framework]]? They look equivalent — are they?
- How do modern static analyzers (Infer, CodeQL, Semgrep, Polyspace) choose abstract domains? What works in practice for finding bugs in real code?
- Can abstract interpretation be made *compositional* — building a sound analysis for a whole program from sound analyses of its parts? ([[interprocedural-analysis|Interprocedural analysis]] is one approach.)
- What is the relationship between abstract interpretation and type systems? Both can prove absence of certain bugs.
