---
title: "Distributive Framework"
tags: [concept, software-analyse, semester-1, data-flow, distributivity]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[monotone-framework]]", "[[lattice]]", "[[mop-vs-mfp]]"]
---

## One-line Summary
A data flow framework is distributive when its transfer functions distribute over the join operator (f(x ⊔ y) = f(x) ⊔ f(y)); for distributive frameworks, the [[mop-vs-mfp|MFP and MOP solutions are equal]], so the iterative algorithm gives the optimal answer.

## Core Intuition
Data flow analysis has two ideal solutions: the precise but undecidable [[mop-vs-mfp|MOP]] (join over all execution paths) and the computable but potentially less precise [[mop-vs-mfp|MFP]] (least fixed point). The central question: when are they the same?

The answer: when the analysis is **distributive** — when transfer functions distribute over the lattice join. Distributivity is a *very strong* property. It means: combining the inputs first, then applying the transfer function, gives the same result as applying the transfer function to each input separately and combining the results.

If your analysis is distributive, the iterative worklist algorithm gives you the optimal answer — there is no precision to be gained by enumerating paths. If your analysis is *not* distributive, the iterative algorithm may give you a strictly weaker answer than MOP — this is the cost of the iteration.

The four classic data flow analyses are all distributive. The canonical non-distributive example is [[constant-propagation|constant propagation]].

## Formal Definition / Statement

A **data flow framework** is distributive if for every transfer function f_b and every pair of lattice elements x, y:
- f_b(x ⊔ y) = f_b(x) ⊔ f_b(y)

Equivalently (and equivalently in any lattice with a distributive pair):
- f_b(x ⊓ y) = f_b(x) ⊓ f_b(y)  (Galois connection property)

**Theorem (Kildall 1973 / Cousot & Cousot 1977)**: For a distributive framework, the MFP solution equals the MOP solution.

**Theorem**: Gen/Kill transfer functions are distributive.

Proof sketch: f_b(X) = gen(b) ∪ (X \ kill(b)).
- f_b(X₁) ∪ f_b(X₂) = [gen(b) ∪ (X₁ \ kill(b))] ∪ [gen(b) ∪ (X₂ \ kill(b))] = gen(b) ∪ (X₁ \ kill(b)) ∪ (X₂ \ kill(b)) = gen(b) ∪ ((X₁ ∪ X₂) \ kill(b)) = f_b(X₁ ∪ X₂) ✓

## Key Properties

### The four distributive classic analyses
All four are distributive (their transfer functions are gen/kill):

| Analysis | Direction | Kind | Join | Distributive? |
|----------|-----------|------|------|---------------|
<<<<<<< HEAD
| [[reaching-definitions\|Reaching definitions]] | Forward | May | ∪ | Yes |
| [[available-expressions\|Available expressions]] | Forward | Must | ∩ | Yes |
| [[live-variable-analysis\|Live variables]] | Backward | May | ∪ | Yes |
| [[very-busy-expressions\|Very busy expressions]] | Backward | Must | ∩ | Yes |
=======
| [[reaching-definitions|Reaching definitions]] | Forward | May | ∪ | Yes |
| [[available-expressions|Available expressions]] | Forward | Must | ∩ | Yes |
| [[live-variable-analysis|Live variables]] | Backward | May | ∪ | Yes |
| [[very-busy-expressions|Very busy expressions]] | Backward | Must | ∩ | Yes |
>>>>>>> 20ac138 (2nd week of june)

For all four, MFP = MOP, so the iterative algorithm gives the optimal answer.

### Non-distributive analyses
- [[constant-propagation|Constant propagation]] — the canonical example
- Tracking integer ranges (without widening) — also non-distributive in general
- Tracking the "sign + zero" lattice — actually distributive, but more complex
- Pointer analysis with subset-based relationships — non-distributive

### Why distributivity matters in practice
- If your analysis is distributive: implement worklist, you're done, you have the optimal answer
- If your analysis is not distributive: you must either (a) accept the precision loss, (b) use a more powerful algorithm (BDD-based, path-sensitive, etc.), or (c) modify the abstract domain to be distributive

### Distributivity is monotone-framework-independent
- Distributivity is a property of the *transfer functions*, not of the lattice
- The same lattice can support distributive and non-distributive analyses
- The same transfer-function form (gen/kill) is always distributive

## Worked Example

For [[reaching-definitions|reaching definitions]], transfer function:
f_b(X) = gen(b) ∪ (X \ kill(b))

Test distributivity:
- Let gen(b) = {d₁, d₂}, kill(b) = {d₃}
- Let X₁ = {d₁, d₄}, X₂ = {d₂, d₅}
- f_b(X₁) = {d₁, d₂, d₄}
- f_b(X₂) = {d₁, d₂, d₅}
- f_b(X₁) ∪ f_b(X₂) = {d₁, d₂, d₄, d₅}
- f_b(X₁ ∪ X₂) = f_b({d₁, d₂, d₄, d₅}) = {d₁, d₂, d₄, d₅} ✓

For [[zero-analysis-worked-example|Zero Analysis]] in [[software-analyse-lecture-6|L6]]:
- f_{x := e}(σ) = σ[x ← α(e)]
- This is the only function in the lattice that "writes" x, and the "read" parts (α(e)) are monotone
- Distributivity holds: f(σ₁) ⊔ f(σ₂) = f(σ₁ ⊔ σ₂) — both compute the abstract value of e on the joined inputs
- Therefore MFP = MOP for Zero Analysis (the lecture's MOP/MFP example uses this)

For [[constant-propagation|constant propagation]] with concrete example from L06 slides:
- Consider x = (condition ? 2 : 3); y = (condition ? 3 : 2); z = x + y
- MOP would say: "either x=2 ∧ y=3 → z=5, or x=3 ∧ y=2 → z=5"; join = z=5
- MFP iterates: σ[x] starts as ⊤ (since x is conditionally assigned different constants), σ[y] starts as ⊤, then x+y computes ⊤ + ⊤ = ⊤
- MFP loses the information that z is always 5; MOP keeps it
- Conclusion: constant propagation is non-distributive in this case

## Common Pitfalls

- **"Gen/Kill = distributive"** is the most common mnemonic, but it's a sufficient condition, not the only one. Some non-gen/kill analyses can also be distributive.
- **"Distributive ⟹ MFP = MOP"** is a theorem, not a definition. The MFP solution always exists; distributivity is what makes it equal to MOP.
- **Non-distributivity is not "wrong"** — the iterative MFP is still *sound*; it's just less precise than MOP. For analyses where the precision loss is acceptable, non-distributivity is fine.
- **Lattice structure matters for distributivity**. Some abstract domains (e.g., [[zero-analysis-worked-example|sign lattices]]) can be made distributive by careful design.
- **The four-classic-analyses-are-distributive fact** is what makes data flow analysis practical — the iterative algorithm gives optimal answers for the most common cases.

## Connections

- [[monotone-framework]] — distributivity is a strengthening of monotonicity
- [[lattice]] — distributivity is a property of lattice operations
- [[mop-vs-mfp]] — distributivity is the condition for MFP = MOP
- [[reaching-definitions]] — distributive forward may analysis
- [[available-expressions]] — distributive forward must analysis
- [[live-variable-analysis]] — distributive backward may analysis
- [[very-busy-expressions]] — distributive backward must analysis
- [[data-flow-analysis]] — the family of analyses
- [[iterative-data-flow-analysis]] — computes the MFP, which equals MOP iff distributive
- [[abstract-interpretation]] — distributivity is one of the key properties to look for in an abstract domain

## Open Questions

- The lecture claims constant propagation is non-distributive. Are there practical programs where this precision loss actually matters?
- For non-distributive analyses, is there a *practical* algorithm between MFP (imprecise but fast) and MOP (precise but undecidable)? (Examples: BDD-based, path-sensitive, etc.)
- Can we design abstract domains that are *both* expressive and distributive? Or is there a fundamental tradeoff?
- The gen/kill form is always distributive. Are there other "templates" for transfer functions that guarantee distributivity?
