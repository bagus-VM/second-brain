---
title: "Procedure Summaries"
tags: [concept, software-analyse, semester-1, context-sensitivity, procedure-summaries, interprocedural-analysis]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[context-sensitivity]]", "[[interprocedural-analysis]]", "[[call-strings]]"]
---

## One-line Summary
A procedure summary is a single transfer function that captures a procedure's net effect on the abstract state — composable, reusable at every call site, and the practical alternative to [[cloning-context-sensitivity|cloning]] when the summary is well-defined and not too complex.

## Core Intuition
[[cloning-context-sensitivity|Cloning]] duplicates a procedure's body, one copy per call site. [[inlining-context-sensitivity|Inlining]] substitutes the body at each call site. **Procedure summaries** take a different approach: compute the procedure's *net effect* as a single transfer function `trans_f`, then apply `trans_f` at every call site without re-analysing f's body.

For a non-recursive procedure f with body blocks b_0, b_1, ..., b_n, the summary is:
trans_f = trans_bn ∘ ... ∘ trans_b1 ∘ trans_b0

This is the composition of the body's transfer functions. Once computed, it's a "black box" that can be applied to any input state at any call site.

The catch: for recursive procedures, trans_f is the *least fixed point* of the equation trans_f = F(trans_f), where F composes the body's transfer function with itself. And in the worst case, trans_f degenerates to ⊤ (no information) or to a symbolic expression as complex as f's body (useless).

## Formal Definition / Statement

A **procedure summary** for a procedure f is a transfer function trans_f: L → L such that for any input abstract state σ at f's entry, trans_f(σ) is the abstract state at f's exit.

For a non-recursive procedure f with body blocks b_0, b_1, ..., b_n:
trans_f = trans_bn ∘ ... ∘ trans_b1 ∘ trans_b0

For a recursive procedure, trans_f is the least fixed point of the equation:
trans_f = F(trans_f)
where F composes the body's transfer function with itself, treating recursive calls as applications of trans_f.

The summary is **applied** at every call site of f:
- At call site c with input state σ, the caller's exit state is updated to σ' = σ[caller ← trans_f(σ[args])]

## Key Properties

### Why procedure summaries scale
- The summary is computed *once* per procedure (not per call site)
- At every call site, applying the summary is a single function application (fast)
- The total work is O(|procedures| × |summary computation| + |call sites| × |application|)
- Compare to cloning: O(|call sites| × |procedure body|)

### The three failure modes
The lecture notes (slide 51) that procedure summaries can fail in three ways:
1. **trans_f = ⊤**: the summary gives no information. The procedure is too complex; the analysis gives up.
2. **trans_f is as complex as f's body**: the summary is not really a summary. Using it doesn't save work over analysing f's body directly.
3. **trans_f doesn't exist (for recursive procedures)**: the equation has no least fixed point, or computing it is intractable. Recursive procedures may require fixpoint computation, which is the same cost as the data flow analysis itself.

### Composing summaries
For nested procedures:
- If f calls g, and trans_g is known, then trans_f can use trans_g
- This enables **modular analysis**: summarise each procedure once, compose as needed
- The key efficiency win: don't re-analyse g at every call site in f

### Recursive procedures
For a recursive procedure, trans_f is defined as the least fixed point. The analysis:
1. Start with trans_f = identity
2. Compose the body using trans_f for recursive calls
3. Check if trans_f changed; if so, repeat
4. Terminate when trans_f stabilises

This is the same as the [[data-flow-analysis|data flow analysis]] algorithm — applied to transfer functions instead of program states.

### Modular vs monolithic analysis
- **Modular** (procedure summaries): analyse each procedure independently, store the summary, compose as needed
- **Monolithic** (cloning or inlining): analyse the whole program as one big procedure
- Modular scales better but may lose precision (if the summary is ⊤, all the per-call information is lost)
- Monolithic is more precise but doesn't scale

## Worked Example

The lecture's program (slides 49-50):
```c
int a = 7;
int d = f(a, 2);
int e = f(1, 5);

int f(int x, int y) {
  int z = 0;
  if (x > y) z = x; else z = y;
  return z;
}
```

**Computing trans_f**:
- f's body: z = 0; if (x > y) z = x; else z = y; return z;
- For input (x, y), the body's transfer function produces output (x, y, z = max(x, y))
- Composed: trans_f(x, y) = {return ↦ max(x, y)} (the return value is max of inputs)
- More precisely, trans_f = trans_b4 ∘ (trans_b2 ⊔ trans_b3) ∘ trans_b1 ∘ trans_b0
  - trans_b0: id (just an entry)
  - trans_b1: id (the conditional)
  - trans_b2: z := x
  - trans_b3: z := y
  - trans_b2 ⊔ trans_b3: z := max(x, y)
  - trans_b4: id (the return)
- So trans_f(x, y) = max(x, y) (the symbolic result)

**Applying trans_f at call sites**:
- At b6: d = trans_f(7, 2) = max(7, 2) = 7
- At b7: e = trans_f(1, 5) = max(1, 5) = 5
- Final: d = {7}, e = {5} ✓

This gives the same precision as cloning, but no code duplication.

**Recursive case**:
For a recursive procedure like factorial:
```c
int fact(int n) { if (n <= 1) return 1; return n * fact(n - 1); }
```
- trans_fact(σ) for input σ where σ(n) = k:
  - First approximation: trans_fact(σ) = {n = k, return = if k ≤ 1 then 1 else k * trans_fact({n = k - 1})}
  - This is a recursive definition of trans_fact; we need a fixpoint
  - For the abstract domain of integer values, the fixpoint may be "trans_fact(σ) = {return = k!}" — symbolic factorial
  - In practice, the summary is often too complex to be useful (the "as complex as the body" failure mode)

## Common Pitfalls

- **The composed transfer function for a recursive procedure is *itself* a fixpoint**. The algorithm is the same as data flow analysis, but applied to transfer functions.
- **The summary may degenerate to ⊤**. This happens when the procedure's body is too complex for the abstract domain to represent the symbolic result. The analysis gives up and reports "we don't know" — sound but useless.
- **Modular analysis is not always more scalable**. If the summary is as complex as the body, you've just moved the work without saving it.
- **Summaries are not free**. Computing trans_f may itself be expensive (especially for recursive procedures). The "summary once, use many times" win only applies if the procedure is called many times.
- **The summary is a property of the *abstract domain*, not the program**. A different abstract domain produces a different summary for the same procedure.
- **Procedure summaries interact with [[context-sensitivity|context sensitivity]]**. A "context-sensitive summary" distinguishes the call site (or call string) when computing trans_f. A "context-insensitive summary" merges all call sites.

## Connections

- [[context-sensitivity]] — the general topic
- [[cloning-context-sensitivity|Cloning]] — the most precise alternative
- [[inlining-context-sensitivity|Inlining]] — another precise alternative
- [[call-strings]] — the practical compromise
- [[interprocedural-analysis]] — the broader topic
- [[data-flow-analysis]] — the intraprocedural foundation
- [[monotone-framework]] — guarantees the fixpoint exists for recursive procedures
- [[software-analyse-lecture-7]] — the lecture

## Open Questions

- For very large programs, can procedure summaries be computed incrementally (recompute only when the procedure changes)?
- How do production tools (DOOP, WALA, Infer) implement procedure summaries? What are the engineering tradeoffs?
- Is there a useful *partial* summary — e.g., the summary returns ⊤ for some inputs but precise values for others? (Lazy summary computation.)
- Can summaries be composed across procedures (trans_g ∘ trans_f for f calls g) to enable true modular analysis? This is the basis of "modular verification".
