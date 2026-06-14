---
title: "Context Sensitivity"
tags: [concept, software-analyse, semester-1, context-sensitivity, interprocedural-analysis]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[interprocedural-analysis]]", "[[data-flow-analysis]]"]
---

## One-line Summary
Context sensitivity is the property of an [[interprocedural-analysis|interprocedural analysis]] that distinguishes different calling contexts of a procedure — when a procedure is called from multiple call sites, a context-sensitive analysis keeps the call sites separate, while a context-insensitive analysis merges them.

## Core Intuition
When procedure f is called from two different call sites with different arguments, a context-insensitive analysis merges the two calls — it analyses f's body once with the union of all possible arguments. This loses information: anything specific to one call site gets mixed with the other.

A context-sensitive analysis keeps the calls separate — it analyses f's body once per call context (or uses an equivalent technique). This is more precise but more expensive.

The lecture presents four techniques for context sensitivity:
1. **Cloning** — physically duplicate f's body, one copy per call site
2. **Inlining** — substitute f's body at each call site
3. **Call strings** — keep f as one body, but tag each call with a context (sequence of call sites)
4. **Procedure summaries** — compute f's net effect as a single transfer function, apply it at each call site

Each has a different precision/scalability tradeoff.

## Formal Definition / Statement

An [[interprocedural-analysis|interprocedural analysis]] is **context-sensitive** if, for every procedure f, the analysis state at f's entry depends on which call site invoked f. It is **context-insensitive** if the state is the union over all call sites.

More precisely: a context-insensitive analysis computes
σ(f's entry) = ⊔ { σ(caller's state at call site c) | c is a call to f }
and then analyses f once.

A context-sensitive analysis with cloning computes
σ(f_c's entry) = σ(caller's state at call site c)  (one copy f_c per call site)
and then analyses each f_c separately.

A context-sensitive analysis with call strings computes
σ(f's entry at depth k) = σ(caller's state tagged with the k-deep call string)

A context-sensitive analysis with procedure summaries computes
trans_f = least fixpoint of f's body's transfer function
and then applies trans_f at each call site as a single "black box" operation.

## Key Properties

### Why context-insensitive is imprecise — a concrete example
```c
int d = f(a, 2);   // call 1: f sees x={7}, y={2}
int e = f(1, 5);   // call 2: f sees x={1}, y={5}
```
Context-insensitive: f analysed once with x = {1, 2, 5, 7}, y = {1, 2, 5, 7}. If f's body computes `z = max(x, y)`, the result is `z = {7}` (the max of the merged values). The analysis reports d = e = {7} — wrong. In reality, d = 7 and e = 5.

Context-sensitive (cloning): f_1 with x = {7}, y = {2} → z = {7} → d = {7}. f_2 with x = {1}, y = {5} → z = {5} → e = {5}. Correct.

### Cloning vs inlining
- **Cloning**: duplicate the procedure's body, one copy per call site. Each clone is a separate procedure. The result is more procedures, each analysed once.
- **Inlining**: substitute the procedure's body at each call site. The result is one big procedure with the callee's code at each call. The CFG grows, but no new procedures.
- For non-recursive procedures, inlining is equivalent to cloning (modulo call graph).
- For recursive procedures, inlining does not terminate (you'd substitute infinitely). Cloning works, but you get one clone per call site of every recursive call.

### Call strings — the practical compromise
A **call string** is a sequence of call sites that describes the current call context. The most recent call is at one end (typically the leftmost); the older calls are deeper in the sequence.

A **k-bounded call string** keeps only the k most recent call sites. This bounds the analysis state size (at most k × |call sites| states) and ensures termination.

The lecture's example (slides 35-40):
- Call 1 at b6, then call 2 at b7 (with f's body at b0-b4)
- The call string for f's body when called from b6: `[b6]`
- The call string for f's body when called from b7: `[b7]`
- Inside f, the analysis keeps `(abstract_value, call_string)` pairs

### Procedure summaries — the compositional approach
For a non-recursive procedure f with body blocks b_0, ..., b_n:
trans_f = trans_bn ∘ ... ∘ trans_b0

This single transfer function captures f's net effect. Apply it at every call site without re-analysing f's body.

For a recursive procedure, trans_f is the least fixpoint of the equation
trans_f = F(trans_f)
where F composes the body's transfer function with itself.

The catch: the symbolic result may be too complex to be useful. The lecture notes that trans_f can degenerate to ⊤ (no information) or to an expression as complex as f's body (useless).

## Worked Example

The lecture's program (slides 7-14):
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

**Context-insensitive (one analysis of f)**:
- f's body: x, y ∈ {1, 2, 5, 7}, z = max(x, y) = {7}
- d = f(7, 2) → d = {7}  (by trans_f applied at call 1)
- e = f(1, 5) → e = {7}  (by trans_f applied at call 2 — same value because the analysis doesn't distinguish calls)
- Result: d = e = {7}

**Context-sensitive with cloning (one f per call site)**:
- f_1: x = {7}, y = {2} → z = {7} → return {7} → d = {7}
- f_2: x = {1}, y = {5} → z = {5} → return {5} → e = {5}
- Result: d = {7}, e = {5} ✓

**Context-sensitive with call strings (k=1)**:
- At b6: call string = [b6]. f's body: x = {7[b6]}, y = {2[b6]}. return z = {7[b6]}. d = {7}
- At b7: call string = [b7]. f's body: x = {1[b7]}, y = {5[b7]}. return z = {5[b7]}. e = {5}
- Result: d = {7}, e = {5} ✓
- The call string tags distinguish the two call contexts

**Context-sensitive with procedure summary**:
- trans_f(x, y) = {max(x, y)}
- At b6: d = trans_f(7, 2) = {7}
- At b7: e = trans_f(1, 5) = {5}
- Result: d = {7}, e = {5} ✓
- One procedure, one analysis, two applications — the most efficient context-sensitive option

## Common Pitfalls

- **Cloning and inlining are different**. Cloning duplicates the procedure (one f per call site). Inlining substitutes at the call site (no f at all). Inlining doesn't terminate for recursion; cloning does.
- **Call strings must be bounded to ensure termination**. Without bounding, recursive programs produce infinitely long call strings, and the analysis never terminates.
- **Procedure summaries can degenerate**. The composed transfer function of a complex procedure may be ⊤ (no information) or as complex as the original code. In that case, the summary is useless, and you might as well analyse the body.
- **Context-sensitive is not always better**. A poorly designed context-sensitive analysis (e.g., k=0 — context-insensitive) may be less precise than one that picks a good k.
- **The "context" in context sensitivity is a call context, not a heap context**. Heap objects (e.g., in OO programs) are a separate design dimension — see [[heap-analysis|heap analysis]] and object sensitivity.
- **Object-oriented languages add another axis**: each call site may dispatch to multiple methods. The call graph is not just "call site → procedure" but "call site → set of procedures". This is *dynamic dispatch*, and it's the practical pain point of Java/C++ interprocedural analysis.

## Connections

- [[interprocedural-analysis]] — context sensitivity is the central new problem
- [[cloning-context-sensitivity|Cloning]] — one of four techniques
- [[inlining-context-sensitivity|Inlining]] — one of four techniques
- [[call-strings]] — one of four techniques
- [[procedure-summaries]] — one of four techniques
- [[monotone-framework]] — extends to interprocedural with context sensitivity
- [[data-flow-analysis]] — the intraprocedural foundation
- [[software-analyse-lecture-7]] — the lecture
- [[points-to-analysis]] — needed for OO languages, where call targets depend on runtime types
- [[aliasing]] — heap analysis is the other half of interprocedural precision

## Open Questions

- How do production static analyzers choose the context-sensitivity technique? Is it configurable per analysis?
- For object-oriented programs, is call-string context sensitivity enough, or do you also need object sensitivity (distinguishing different `this` instances)?
- Can you combine cloning and procedure summaries — clone for the most-called procedures, summarise the rest?
- How does context sensitivity interact with the "composed transfer function" trick for recursion? Are there special techniques for recursive procedures?
