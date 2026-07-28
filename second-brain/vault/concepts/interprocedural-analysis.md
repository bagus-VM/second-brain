---
title: "Interprocedural Analysis"
tags: [concept, software-analyse, semester-1, interprocedural-analysis, context-sensitivity]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[software-analyse-lecture-5]]", "[[data-flow-analysis]]", "[[monotone-framework]]"]
---

## One-line Summary
Interprocedural analysis extends [[data-flow-analysis|data flow analysis]] beyond a single function so that information flows across procedure calls — but the moment you have calls, the analysis must decide *which* call context to use, which is the [[context-sensitivity|context sensitivity]] problem.

## Core Intuition
[[data-flow-analysis|Intraprocedural analysis]] looks at one function at a time. At every call site, it has to be *conservative*: it doesn't know what the callee does, so it either assumes the worst (⊤ — any value) or knows nothing (⊥). This is a precision killer.

Consider:
```c
int a = 7;
int d = f(a, 2);
int e = a + d;
```
Without interprocedural information, d ∈ ⊤, so e ∈ ⊤. But f(x, y) actually returns max(x, y), so d = 7 and e = 14. The intraprocedural analysis misses this entirely.

**Interprocedural analysis** traces the call graph, propagates information across call/return edges, and re-analyses the callee at each call site (or uses some cheaper approximation). The price: more work and new precision/scalability tradeoffs.

The central new problem: [[context-sensitivity|context sensitivity]]. If f is called from two different call sites with different arguments, a *context-insensitive* analysis merges the two calls and loses information. A *context-sensitive* analysis distinguishes them — but at the cost of complexity.

## Formal Definition / Statement

An **interprocedural analysis** operates on an **interprocedural control flow graph (ICFG)**:

- For every call site b_x that calls procedure f, split b_x into two nodes: b_cx (the call, with the in-edges) and b_rx (the return, with the out-edges)
- Add an edge from b_cx to f's entry (passing parameters)
- Add an edge from f's exit to b_rx (passing return value)
- All other edges remain as in the intraprocedural CFG

A **valid path** in the ICFG is a path that respects call-return matching: if you enter procedure f at call site c, you must exit f at the return site of c, in the same order. Invalid paths (e.g., enter f from c₁, exit at c₂'s return) are ignored.

The **Meet Over Valid Paths (MVP)** solution at block b_i is the join over all valid paths to b_i of the composed transfer functions — the interprocedural analogue of [[mop-vs-mfp|MOP]]. MVP is the precise ideal but undecidable in general.

A **context-sensitive** analysis computes different abstract states for the same procedure at different call sites. A **context-insensitive** analysis does not.

## Key Properties / Complexity

### The four parts of interprocedural analysis
1. **Call graph construction**: which procedures can be called from which call sites?
2. **ICFG construction**: split call sites, add call/return edges
3. **Data flow propagation**: apply the data flow framework on the ICFG
4. **Context sensitivity**: distinguish different call contexts of the same procedure

### Why intraprocedural fails
At a call site b_x = call f(args), the intraprocedural analysis must compute:
- After the call: the value of f's return is unknown
- Variables modified by f: the analysis must assume they may have been modified
- The analysis loses any information about the callee

This is *sound* (no false positives) but *imprecise*. The imprecision propagates: if d is unknown, anything depending on d is unknown, etc.

### Valid paths — the key constraint
A "real" interprocedural execution respects call-return matching. The grammar from the lecture:
```
Path ::= ⟨P⟩* ⟨M⟩
P     ::= b_x | b_cy          (non-call blocks, or unmatched calls)
M     ::= b_cx ⟨M⟩ b_rx | b_y ⟨M⟩ | ⟨M⟩ b_y | ε   (matched call-return pairs and other blocks)
```

The intuition: M is a sequence of matched call-return pairs and non-call blocks, all properly nested. The P* prefix allows for "unmatched" calls (calls to functions we never return from, like exit()), but M must be properly nested.

### The compose transfer function for a procedure
If procedure f has body blocks b_0, b_1, ..., b_n, the *composed transfer function* is:
trans_f = trans_bn ∘ ... ∘ trans_b1 ∘ trans_b0

This is the net effect of executing f. If you can compute trans_f, you can apply it at every call site of f without re-analysing f's body.

The catch: trans_f may not exist (for recursive procedures, you need a fixpoint), and the symbolic result may be too complex to be useful (e.g., trans_f = ⊤, or trans_f is an expression as complex as f's body).

## Worked Example

The lecture's program:
```c
int a = 7;
int d = f(a, 2);
int e = a + d;

int f(int x, int y) {
  int z = 0;
  if (x > y) z = x; else z = y;
  return z;
}
```

**Intraprocedural analysis** of the main function:
- After `a = 7`: a = {7}
- After `d = f(a, 2)`: d = ⊤ (unknown — callee's effect unknown)
- After `e = a + d`: e = {7} + ⊤ = ⊤

**Interprocedural, context-insensitive** (analyse f once):
- f's body: z = max(x, y)
- At call site 1: d = max(7, 2) = {7}
- At call site 2: e = {7} + d = {7} + {7} = {14}... wait, e = a + d where d comes from the first call, so e = 7 + 7 = {14} ✓

**Interprocedural, context-sensitive** (analyse f twice):
- f_1 with x={7}, y={2}: z = {7} → return {7} → d = {7}
- f_2 with x={1}, y={5}: z = {5} → return {5} → e = {7} + {5} = {12}

The context-sensitive analysis correctly identifies the difference between the two call sites.

**Interprocedural, context-sensitive with procedure summary**:
- trans_f(x, y) = {max(x, y)}
- At call site 1: d = trans_f(7, 2) = {7}
- At call site 2: e = trans_f(1, 5) = {5}; then e = a + e = 7 + 5 = {12}

Same result as cloning, but no code duplication. The summary is the magic.

## Common Pitfalls

- **Interprocedural is not always more precise**. A poorly designed interprocedural analysis can be *less* precise than an intraprocedural one (e.g., if the context-sensitivity is too coarse).
- **Call graph construction is its own problem**. Without a sound call graph, the analysis is unsound. Object-oriented programs with dynamic dispatch and reflection make this hard.
- **Recursive procedures need fixpoint computation**, not just composition. The transfer function trans_f for a recursive f is defined as the least fixed point of the equation trans_f = F(trans_f), where F composes the body's transfer function with itself.
- **The context-sensitivity decision is a precision/scalability tradeoff**. Context-insensitive is fastest but imprecise. Cloning is most precise but explodes code size. The four techniques are intermediate points.
- **A context-insensitive analysis is *still sound***. It just may be too imprecise to be useful. Don't confuse "imprecise" with "wrong".

## Connections

- [[data-flow-analysis]] — the intraprocedural foundation
- [[monotone-framework]] — extends naturally to interprocedural
- [[abstract-interpretation]] — the general framework
- [[mop-vs-mfp]] — MVP is the interprocedural analogue of MOP
- [[context-sensitivity]] — the central new problem
- [[call-strings]] — one technique for context sensitivity
- [[procedure-summaries]] — another technique
- [[cloning-context-sensitivity|Cloning]] — the most precise (and most expensive) technique
- [[inlining-context-sensitivity|Inlining]] — cloning at the call site, not in the procedure
- [[points-to-analysis]] — needed for OO languages, related but distinct
- [[software-analyse-lecture-7]] — the lecture

## Open Questions

- How do production static analyzers (Infer, CodeQL, Semgrep, Polyspace) implement interprocedural analysis? What context-sensitivity choices do they make?
- The compose-transfer-function trick doesn't work for recursive procedures without fixpoints. Is there a general way to handle recursion?
- For very large programs, is *any* sound interprocedural analysis tractable? What approximations do production tools make?
- Demand-driven interprocedural analysis (compute only what's needed for a specific query) — what are the precision/scalability tradeoffs?
