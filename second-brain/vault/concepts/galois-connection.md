---
title: "Galois Connection"
tags: [concept, software-analyse, semester-1, abstract-interpretation, lattice-theory]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[lattice]]", "[[abstract-interpretation]]"]
---

## One-line Summary
A Galois connection C ⇄ A between a concrete domain C and an abstract domain A is a pair of monotone functions α: C → A (abstraction) and γ: A → C (concretisation) such that α(c) ⊑_A a ⟺ c ⊑_C γ(a) — the formal link that makes [[abstract-interpretation|abstract interpretation]] sound.

## Core Intuition
To use [[abstract-interpretation|abstract interpretation]] soundly, the abstract domain and concrete domain must be related in a precise way. A **Galois connection** is the standard relation: for every concrete fact c, the abstraction α(c) is a "summary" of c in the abstract world; for every abstract fact a, the concretisation γ(a) is the set of concrete facts it represents.

The defining property: c is "below" γ(a) in the concrete order iff α(c) is "below" a in the abstract order. This means the abstract ordering *agrees* with the concrete ordering modulo α and γ. Anything provable in the abstract world is provable in the concrete world — soundness by construction.

Galois connections are the workhorse of abstract interpretation. The lecture's [[zero-analysis-worked-example|Zero Analysis]] example uses a Galois connection: concrete domain ℤ, abstract domain {⊥, Z, NZ, MZ}, with α(0) = Z, α(n≠0) = NZ, γ(Z) = {0}, γ(NZ) = {n: n ≠ 0}, γ(MZ) = ℤ.

## Formal Definition / Statement

A **Galois connection** between two posets (C, ⊑_C) and (A, ⊑_A) is a pair of functions α: C → A (the upper adjoint / abstraction) and γ: A → C (the lower adjoint / concretisation) such that for all c ∈ C and a ∈ A:

    α(c) ⊑_A a  ⟺  c ⊑_C γ(a)

Equivalently:
- α is monotone and γ is monotone
- c ⊑_C γ(α(c)) (concretising an abstraction over-approximates)
- α(γ(a)) ⊑_A a (abstracting a concretisation under-approximates)

We write C ⇄^γ_α A or simply "C and A are related by a Galois connection".

A **Galois insertion** is a Galois connection where α ∘ γ is the identity on A — i.e., the abstract domain doesn't have redundant elements. Most abstract interpretations use Galois insertions for efficiency.

## Key Properties

### Why Galois connections are the right structure
- They guarantee that the abstract and concrete orders are "compatible" — abstract reasoning stays sound
- They give a precise meaning to "abstraction" and "concretisation"
- They make soundness *automatic*: any proof in the abstract world translates to the concrete world

### The two inequalities
- **c ⊑ γ(α(c))**: the abstract value α(c), when concretised, over-approximates c. Abstracting then concretising *loses* some concrete information (potentially).
- **α(γ(a)) ⊑ a**: the concrete value γ(a), when abstracted, under-approximates a. Concretising then abstracting *can* lose some abstract precision.

### Why this matters for soundness
For an abstract operation op_abstract to be sound, we need:
    op_concrete(γ(a₁), γ(a₂)) ⊑_C γ(op_abstract(a₁, a₂))

This says: applying the abstract operation and then concretising is an over-approximation of applying the concrete operation directly. The Galois connection structure makes this definitional, not a theorem to prove.

### Galois connection vs Galois insertion
- **Galois connection**: α ∘ γ may not be the identity on A
- **Galois insertion**: α ∘ γ = id on A (no redundant abstract elements)
- For practical abstract interpretation, Galois insertions are usually preferred (smaller abstract domain, same precision)

### Examples
- Concrete = ℘(Σ*) (sets of strings), Abstract = ℘(Σ) (sets of letters), α = "take first letter", γ = "extend each letter to all strings starting with it"
- Concrete = ℤ, Abstract = sign({+, −, 0, *}), α(0) = 0, α(>0) = +, α(<0) = −, γ(0) = {0}, γ(+) = {1, 2, 3, ...}, etc.
- Concrete = program states, Abstract = a chosen abstract domain

## Worked Example

For [[zero-analysis-worked-example|Zero Analysis]]:
- Concrete domain: C = ℘(ℤ) (sets of possible integer values)
- Abstract domain: A = {⊥, Z, NZ, MZ} with order ⊥ ≤ Z ≤ MZ, ⊥ ≤ NZ ≤ MZ
- α: C → A:
  - α(∅) = ⊥
  - α({0}) = Z
  - α(S) = NZ if S ⊆ {n: n ≠ 0} and S ≠ ∅
  - α(S) = MZ otherwise
- γ: A → C:
  - γ(⊥) = ∅
  - γ(Z) = {0}
  - γ(NZ) = {n: n ≠ 0}
  - γ(MZ) = ℤ

Check the Galois connection property:
- α(c) ⊑ a ⟺ c ⊑ γ(a)
- Example: c = {0, 5}, a = MZ
  - α({0, 5}) = MZ (since it contains 0 and non-zero, "maybe zero")
  - α({0, 5}) ⊑ MZ ✓
  - γ(MZ) = ℤ; {0, 5} ⊆ ℤ ✓
- Example: c = {0}, a = Z
  - α({0}) = Z
  - Z ⊑ Z ✓
  - γ(Z) = {0}; {0} ⊆ {0} ✓
- Example: c = {0}, a = NZ
  - α({0}) = Z; Z ⊑ NZ ✓
  - γ(NZ) = {n: n ≠ 0}; {0} ⊆ {n: n ≠ 0}? NO, because 0 is in c but not in γ(NZ)
  - So α(c) ⊑ a holds but c ⊑ γ(a) does NOT hold
  - This is a *valid* implication: the "if and only if" is satisfied because both directions need to agree
  - Wait, let me recheck: Z ⊑ NZ? Yes (in the lattice). {0} ⊆ {n: n ≠ 0}? No (0 is missing). So α ⊑ a holds but c ⊑ γ(a) does NOT — this *violates* the Galois connection!

Let me re-examine. The issue is that Z is below NZ in the lattice (both ≤ MZ, but Z and NZ are incomparable to each other — they share only the lower bound ⊥).

Actually, Z and NZ are *incomparable* in the lattice (Z ⊑ MZ and NZ ⊑ MZ, but neither Z ⊑ NZ nor NZ ⊑ Z). So Z ⊑ NZ is FALSE. My analysis was wrong.

Recheck: c = {0}, a = NZ:
- α({0}) = Z
- Z ⊑ NZ? NO (Z and NZ are incomparable)
- So α(c) ⊑ a is FALSE
- The biconditional is vacuously true on this case

OK, the example checks out after all. The key insight: α and γ are designed so that the biconditional α(c) ⊑ a ⟺ c ⊑ γ(a) holds for all (c, a).

## Common Pitfalls
- A Galois connection is **not symmetric**: α goes one way, γ the other. The orders are "compatible" in a specific sense.
- The α ∘ γ is not the identity in general (Galois insertion is the special case where it is)
- α is the **upper** adjoint (joins to the left of γ), γ is the **lower** adjoint (meets to the left of α)
- Some texts use "abstraction" and "concretisation" in the opposite sense — be careful

## Connections
- [[lattice]] — the underlying structure
- [[abstract-interpretation]] — the framework that uses Galois connections
- [[mop-vs-mfp]] — can be formalised with Galois connections
- [[zero-analysis-worked-example]] — uses a Galois connection
- [[widening-narrowing]] — for infinite lattices, related but more general
- [[software-analyse-lecture-6]] — the lecture

## Open Questions
- Not every abstract interpretation has a Galois connection (some use a more general framework). When is the Galois connection structure necessary vs convenient?
- How do we *construct* a Galois connection for a new abstract domain? (Often by defining α and γ and checking the biconditional.)
- For infinite abstract domains (intervals, polyhedra), Galois connections can still be defined — but with care for completeness.
