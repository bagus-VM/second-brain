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
To use [[abstract-interpretation|abstract interpretation]] soundly, the abstract domain and concrete domain must be related in a precise way. A **Galois connection** is the standard relation: for every concrete fact c, the abstraction α(c) is a summary of c in the abstract world; for every abstract fact a, the concretisation γ(a) is the set of concrete facts it represents.

The defining property: c is below γ(a) in the concrete order iff α(c) is below a in the abstract order. This means the abstract ordering *agrees* with the concrete ordering modulo α and γ — anything provable in the abstract world is provable in the concrete world, giving soundness by construction.

Galois connections are the workhorse of abstract interpretation. The lecture's [[zero-analysis-worked-example|Zero Analysis]] example uses a Galois connection: concrete domain ℤ, abstract domain {⊥, Z, NZ, MZ}, with α(0) = Z, α(n≠0) = NZ, γ(Z) = {0}, γ(NZ) = {n: n ≠ 0}, γ(MZ) = ℤ.

## Formal Definition / Statement

A **Galois connection** between two posets (C, ⊑_C) and (A, ⊑_A) is a pair of functions α: C → A (the upper adjoint / abstraction) and γ: A → C (the lower adjoint / concretisation) such that for all c ∈ C and a ∈ A:

    α(c) ⊑_A a  ⟺  c ⊑_C γ(a)

Equivalently:
- α is monotone and γ is monotone.
- c ⊑_C γ(α(c)) — concretising an abstraction over-approximates.
- α(γ(a)) ⊑_A a — abstracting a concretisation under-approximates.

We write C ⇄^γ_α A or simply "C and A are related by a Galois connection."

A **Galois insertion** is a Galois connection where α ∘ γ is the identity on A — i.e., the abstract domain has no redundant elements. Most abstract interpretations use Galois insertions for efficiency.

## Key Properties / Complexity

### Why Galois connections are the right structure
- They guarantee that the abstract and concrete orders are compatible — abstract reasoning stays sound.
- They give a precise meaning to "abstraction" and "concretisation."
- They make soundness *automatic*: any proof in the abstract world translates to the concrete world.

### The two inequalities
- **c ⊑ γ(α(c))**: the abstract value α(c), when concretised, over-approximates c. Abstracting then concretising can lose concrete information.
- **α(γ(a)) ⊑ a**: the concrete value γ(a), when abstracted, under-approximates a. Concretising then abstracting can lose abstract precision.

### Why this matters for soundness
For an abstract operation `op_abstract` to be sound, we need:

    op_concrete(γ(a₁), γ(a₂)) ⊑_C γ(op_abstract(a₁, a₂))

Applying the abstract operation and then concretising must over-approximate applying the concrete operation directly. The Galois connection structure makes this definitional, not a theorem to prove.

### Galois connection vs Galois insertion
- **Galois connection**: α ∘ γ may not be the identity on A.
- **Galois insertion**: α ∘ γ = id on A (no redundant abstract elements).
- For practical abstract interpretation, Galois insertions are usually preferred (smaller abstract domain, same precision).

### Examples
- Concrete = ℘(Σ*) (sets of strings), Abstract = ℘(Σ) (sets of letters), α = "take first letter," γ = "extend each letter to all strings starting with it."
- Concrete = ℤ, Abstract = sign({+, −, 0, *}), α(0) = 0, α(>0) = +, α(<0) = −, γ(0) = {0}, γ(+) = {1, 2, 3, ...}, etc.
- Concrete = program states, Abstract = a chosen abstract domain.

## Worked Example

For [[zero-analysis-worked-example|Zero Analysis]]:
- Concrete domain: C = ℘(ℤ) (sets of possible integer values).
- Abstract domain: A = {⊥, Z, NZ, MZ} with order ⊥ ≤ Z ≤ MZ and ⊥ ≤ NZ ≤ MZ. Note: Z and NZ are *incomparable*.
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

**Checking the Galois connection property** — α(c) ⊑ a ⟺ c ⊑ γ(a):

- c = {0, 5}, a = MZ: α({0, 5}) = MZ (contains both 0 and non-zero), so MZ ⊑ MZ ✓; γ(MZ) = ℤ, and {0, 5} ⊆ ℤ ✓.
- c = {0}, a = Z: α({0}) = Z, so Z ⊑ Z ✓; γ(Z) = {0}, and {0} ⊆ {0} ✓.
- c = {0}, a = NZ: α({0}) = Z; Z ⊑ NZ? No — Z and NZ are incomparable in the lattice. So α(c) ⊑ a is false, and the biconditional holds vacuously on this case.

The key insight: α and γ are designed so that the biconditional holds for all (c, a). The incomparability of Z and NZ is essential — it prevents {0} from being conflated with non-zero values.

## Common Pitfalls
- A Galois connection is **not symmetric**: α goes one way, γ the other. The orders are compatible in a specific sense.
- α ∘ γ is not the identity in general; the Galois insertion is the special case where it is.
- α is the **upper** adjoint, γ is the **lower** adjoint. Some texts swap these labels — check conventions.
- "Abstraction" and "concretisation" are sometimes used in the opposite sense across textbooks — be careful with terminology.

## Connections
- [[lattice]] — the underlying structure.
- [[abstract-interpretation]] — the framework that uses Galois connections.
- [[mop-vs-mfp]] — can be formalised with Galois connections.
- [[zero-analysis-worked-example]] — uses a Galois connection.
- [[widening-narrowing]] — for infinite lattices, related but more general.
- [[software-analyse-lecture-6]] — the lecture.

## Open Questions
- Not every abstract interpretation has a Galois connection (some use a more general framework). When is the Galois connection structure necessary vs convenient?
- How do we *construct* a Galois connection for a new abstract domain? (Often by defining α and γ and checking the biconditional.)
- For infinite abstract domains (intervals, polyhedra), Galois connections can still be defined — but with care for completeness.