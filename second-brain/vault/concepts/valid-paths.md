---
title: "Valid Paths (Interprocedural)"
tags: [concept, software-analyse, semester-1, interprocedural-analysis, valid-paths, mvp]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[interprocedural-analysis]]", "[[context-sensitivity]]", "[[call-strings]]"]
---

## One-line Summary
A valid path in an interprocedural control flow graph is a path that respects call-return matching — if you enter a procedure at call site c, you must exit at the return site of c, in the same order; the [[meet-over-valid-paths|MVP]] ideal joins the composed transfer functions over all valid paths.

## Core Intuition
In a single function, every path is "valid" — you can go anywhere. Across function calls, paths are constrained by call-return matching. A path that enters f at call site c₁ and exits at the return site of c₂ is *not* a real execution path — it's a fictional path that breaks call-return semantics.

**Valid paths** are the paths that respect call-return matching. They form the basis of [[meet-over-valid-paths|MVP]] (Meet Over Valid Paths), the interprocedural analogue of [[mop-vs-mfp|MOP]] — the precise but undecidable ideal.

The lecture gives a grammar for valid paths:
```
Path ::= ⟨P⟩* ⟨M⟩
P     ::= b_x | b_cy          (non-call blocks, or unmatched calls)
M     ::= b_cx ⟨M⟩ b_rx | b_y ⟨M⟩ | ⟨M⟩ b_y | ε   (matched call-return pairs and other blocks)
```

The intuition: M is a sequence of matched call-return pairs and other blocks, all properly nested. P* allows for "unmatched" calls (calls to functions we never return from, like `exit()`), but M must be properly nested.

## Formal Definition / Statement

A **path** in an interprocedural CFG is a sequence of blocks. A path is **valid** (a "realizable interprocedural path") if:
- It respects the call-return matching: if you enter procedure f at call site c, you must exit f at the return site of c, in the same order
- More precisely, the path can be derived from the grammar above

The **vpath(b)** set for a block b is the set of all valid paths from the program entry to b.

The **Meet Over Valid Paths (MVP)** solution at block b is:
MVP(b) = ⊔ { trans_{p_k} ∘ ... ∘ trans_{p_0} (⊥) | [p_0, ..., p_k] ∈ vpath(b) }

MVP is the interprocedural analogue of [[mop-vs-mfp|MOP]] — precise but undecidable in general.

## Key Properties

### Why valid paths matter
- "Real" interprocedural executions respect call-return matching
- An analysis that doesn't respect this would be *unsound* — it would report values that no real execution could produce
- The valid path constraint is the *minimum* requirement for a sound interprocedural analysis

### Why MVP is undecidable
- Programs with loops have infinitely many execution paths
- Programs with recursion have infinitely many call-return sequences
- Programs with dynamic dispatch have exponentially many call graphs
- The set of valid paths is generally infinite, so computing MVP exactly is not feasible

### The interprocedural MFP
The MFP solution of the interprocedural analysis gives a sound *and* computable under-approximation of MVP. The algorithm:
1. Build the interprocedural CFG
2. Apply the data flow framework on the ICFG (with the chosen context-sensitivity technique)
3. Iterate until stable

This is what production tools compute.

### Call-return matching — the formal rule
For every call site b_x that calls procedure f:
- The edge from b_cx (call) to f's entry passes parameters
- The edge from f's exit to b_rx (return) passes the return value
- In a valid path, if b_cx appears, the corresponding b_rx must appear later, with the matching f in between
- Multiple calls can be nested (e.g., f calls g calls h, and all return in reverse order)

### Grammar recap (lecture slide 22)
```
Path ::= ⟨P⟩* ⟨M⟩
P     ::= b_x | b_cy          (prefix: non-call blocks, or unmatched calls)
M     ::= b_cx ⟨M⟩ b_rx        (matched call-return pair: enter f at c, return from f at r)
      |  b_y ⟨M⟩               (non-call block before a matched sequence)
      |  ⟨M⟩ b_y               (non-call block after a matched sequence)
      |  ε                     (empty)
```

The M non-terminal generates a properly nested sequence of calls and returns, possibly interspersed with non-call blocks. The P* prefix allows "unmatched" calls (e.g., calls to `exit()` or `throw`) that never return.

## Worked Example

The lecture's running program (slides 17-21):
```c
int a = 7;
int d = f(a, 2);     // call site b6
int e = f(1, 5);     // call site b7
int f(int x, int y) {
  int z = 0;
  if (x > y) z = x; else z = y;
  return z;
}
```

The ICFG blocks: b5 (a=7), b6 (d=f(a,2)), b'6 (return from f), b7 (e=f(1,5)), b'7 (return from f), plus f's body blocks b0-b4.

**Valid path examples** (going from b5 to b'6):
- [b5, b6, b0, b1, b2, b4, b'6]: enters f at b6, takes the "x > y" branch (b2), returns at b'6 ✓
- [b5, b6, b0, b1, b3, b4, b'6]: enters f at b6, takes the "x ≤ y" branch (b3), returns at b'6 ✓
- [b5, b6, b0, b1, b2, b4, b'7]: enters f at b6, but returns at b'7 (different call site) ✗ **Invalid**
- [b5, b7, b0, b1, b2, b4, b'6]: enters f at b7, but returns at b'6 (different call site) ✗ **Invalid**

Only the first two are valid paths to b'6. MVP at b'6 joins the transfer functions of both valid paths.

**MVP for d at b'6**:
- Path 1: trans_{b'6} ∘ trans_{b4} ∘ trans_{b2} ∘ trans_{b1} ∘ trans_{b0} ∘ trans_{b6} ∘ trans_{b5}(⊥) = {d = 7}
- Path 2: trans_{b'6} ∘ trans_{b4} ∘ trans_{b3} ∘ trans_{b1} ∘ trans_{b0} ∘ trans_{b6} ∘ trans_{b5}(⊥) = {d = 7}
- MVP(d) = {7} ⊔ {7} = {7} (both paths give d = 7 because the parameters a=2, so x=7, y=2, and max(7,2) = 7)

**MVP for e at b'7**:
- Path 1 (x > y branch): d = max(1, 5) = 5
- Path 2 (x ≤ y branch): d = max(1, 5) = 5
- MVP(e) = {5} ⊔ {5} = {5}

Both d and e are precisely determined by MVP.

## Common Pitfalls

- **Every "path" is not a "valid path"**. A path that breaks call-return matching is invalid and should be ignored.
- **Invalid paths can give wrong results**. If the analysis includes invalid paths, it may compute values that no real execution could produce — *unsound*.
- **MVP is undecidable**. The MFP is the *computable* approximation. For distributive frameworks, MFP = MVP; for non-distributive, MFP ⊑ MVP (MFP is a sound under-approximation).
- **Valid paths can be infinite for recursive programs**. The MVP ideal is the limit over all (infinitely many) valid paths. In practice, the analysis only considers paths up to a fixpoint.
- **The grammar in the lecture is the formal definition**. The intuitive rule "calls and returns must match up" is what the grammar formalises.

## Connections

- [[interprocedural-analysis]] — the broader topic
- [[context-sensitivity]] — the precision question for interprocedural analysis
- [[call-strings]] — one context-sensitivity technique
- [[procedure-summaries]] — another context-sensitivity technique
- [[mop-vs-mfp]] — MOP/MFP is the intraprocedural analogue
- [[data-flow-analysis]] — the intraprocedural foundation
- [[monotone-framework]] — the underlying lattice theory
- [[software-analyse-lecture-7]] — the lecture

## Open Questions

- The grammar defines valid paths formally, but checking validity in an implementation is non-trivial. How do production tools check that a path is valid?
- For dynamic-dispatch languages (Java, C++), the call graph is not known statically. How do valid paths and MVP work in this setting?
- Can valid paths be enumerated lazily (only as needed by a specific query)? This is the basis of demand-driven interprocedural analysis.
- Is there a useful *partial* MVP — e.g., MVP for a subset of valid paths, or MVP up to a certain depth? This would be a "bounded MVP" analogue to bounded call strings.
