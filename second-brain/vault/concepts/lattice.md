---
title: "Lattice"
tags: [concept, software-analyse, semester-1, lattice-theory]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[monotone-framework]]", "[[data-flow-analysis]]"]
---

## One-line Summary
A lattice is a partially ordered set in which every two elements have a unique least upper bound (join ⊔) and a unique greatest lower bound (meet ⊓) — the algebraic structure that data flow analyses use to organise their facts.

## Core Intuition
A data flow analysis has a *set of possible facts* (e.g., subsets of variables, or triples of (Z, NZ, MZ) per variable) and a *notion of "more information"*. A partial order captures "more information": x ≤ y means "x has at most the information of y", or equivalently "y is a safe over-approximation of x". A lattice is a partial order that is *complete enough* — every pair of elements has a join and a meet — that the analysis can be defined purely in terms of lattice operations. The [[monotone-framework|monotone framework]] works for *any* lattice; specific analyses are obtained by instantiating the lattice.

## Formal Definition / Statement

A **partial order** (P, ≤) is reflexive (x ≤ x), antisymmetric (x ≤ y and y ≤ x implies x = y), and transitive (x ≤ y and y ≤ z implies x ≤ z).

A **lattice** is a partial order (L, ≤) such that for every pair x, y ∈ L:
- **Join** x ⊔ y (least upper bound / lub / supremum) exists and is unique
- **Meet** x ⊓ y (greatest lower bound / glb / infimum) exists and is unique

Equivalently: every finite subset has a join and a meet.

**Key elements** (when they exist):
- **Top ⊤**: the unique maximum; for all x, x ≤ ⊤
- **Bottom ⊥**: the unique minimum; for all x, ⊥ ≤ x

**Height** h(L): the length of the longest strictly ascending chain ⊥ = x₀ < x₁ < ... < x_h = ⊤. A lattice is *finite-height* if h(L) is finite.

**Complete lattice**: every subset S ⊆ L (not just pairs) has a join ⊔S and a meet ⊓S. Every finite lattice is complete.

**Monotonicity**: a function f: L → L is **monotone** if x ≤ y implies f(x) ≤ f(y).

**Distributivity**: f(x ⊓ y) = f(x) ⊓ f(y) and f(x ⊔ y) = f(x) ⊔ f(y).

**Knaster-Tarski fixed-point theorem**: on a complete lattice, every monotone function f has both a least fixed point lfp(f) and a greatest fixed point gfp(f). lfp(f) = ⊔{fⁿ(⊥) : n ≥ 0}.

## Key Properties / Common Lattices

### Two-point lattice {⊥, ⊤}
- Models a single boolean property (true/false, known/unknown, possible/certain)
- Height 1
- The simplest non-trivial lattice

### Powerset lattice ℘(U)
- Elements: all subsets of universe U
- Order: ⊆
- Join: ∪, meet: ∩
- Top: U, bottom: ∅
- Height: |U| (infinite if U is infinite)

### Flat lattice (set of values + ⊤ + ⊥)
- Used for "reaching constants" analyses: a variable's value is one of {c₁, c₂, ...} or "unknown" (⊤) or "no info" (⊥)
- For a variable with k possible constant values: height = 2 (⊥ → {c} → ⊤)
- Width may be infinite

### Type hierarchy lattice (Java example)
- Top: `java.lang.Object`
- Middle: `Number`, `Comparable`, `OutputStream`
- Bottom: unreachable type (e.g., `Number ⊓ OutputStream`)
- Join: most precise common supertype
- Meet: intersection type

### Product lattice L₁ × L₂
- ⟨a, b⟩ ≤ ⟨a', b'⟩ iff a ≤₁ a' and b ≤₂ b'
- Componentwise join and meet
- Top: ⟨⊤₁, ⊤₂⟩; bottom: ⟨⊥₁, ⊥₂⟩
- Standard for "one fact per program variable" analyses

## Worked Example

For the [[zero-analysis-worked-example|Zero Analysis]] domain over a single variable:
- Lattice elements: {⊥, Z, NZ, MZ}
- Order: ⊥ ≤ Z, ⊥ ≤ NZ, Z ≤ MZ, NZ ≤ MZ, ⊥ ≤ MZ
- Join: ⊥ ⊔ X = X; X ⊔ X = X; Z ⊔ NZ = MZ
- Meet: ⊥ ⊓ X = ⊥; Z ⊓ NZ = ⊥; Z ⊓ MZ = Z; NZ ⊓ MZ = NZ
- Top: MZ; bottom: ⊥
- Height: 2 (⊥ → {Z, NZ} → MZ)

This is the running example in the lecture — every transfer function is defined on this lattice.

## Common Pitfalls

- **Confusing lattice order with the analysis "size"**: for *may* analyses, larger sets are *higher* in the lattice; for *must* analyses, larger sets are *lower*. The direction depends on the analysis.
- **Assuming every poset is a lattice**: counter-example: a tree ordered by ancestry is a poset, but two branches have no common upper bound.
- **Assuming all lattices have ⊤ and ⊥**: infinite ascending or descending chains may have no maximum/minimum.
- **Confusing the lattice order with subset order**: the lattice order is *the* order; subset order is one *instance* of a lattice order (the powerset lattice).
- **Forgetting height is finite for termination**: infinite-height lattices ([[widening-narrowing|widening]] needed) are a separate, more advanced topic.

## Connections
- [[monotone-framework]] — every instance of the monotone framework has an underlying lattice
- [[data-flow-analysis]] — the lattice is the abstraction of "what facts can the analysis know"
- [[abstract-interpretation]] — abstract domains are lattices; the concrete semantics is also a lattice
- [[mop-vs-mfp]] — MOP and MFP are both elements of a lattice; MOP is in general larger
- [[distributive-framework]] — distributivity is a property of the lattice's transfer functions
- [[zero-analysis-worked-example]] — the lecture's running example, a small lattice
- [[iterative-data-flow-analysis]] — uses the Knaster-Tarski iteration on the lattice
- [[software-analyse-lecture-6]] — the lecture that grounds data flow in lattice theory

## Open Questions
- For infinite lattices (intervals, polyhedra), the basic Knaster-Tarski iteration may not terminate. How do [[widening-narrowing|widening operators]] rescue convergence?
- How does lattice duality (join ↔ meet) interact with the may/must distinction?
- What is the categorical structure underlying the variety of lattices used in data flow analysis?
