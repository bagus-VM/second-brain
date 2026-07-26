---
title: "Meet Over Valid Paths (MVP)"
tags: [concept, software-analyse, semester-1, interprocedural-analysis, mvp, valid-paths]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[valid-paths]]", "[[interprocedural-analysis]]", "[[mop-vs-mfp]]"]
---

## One-line Summary
The Meet Over Valid Paths (MVP) is the interprocedural analogue of [[mop-vs-mfp|MOP]] — the precise but undecidable data flow solution that joins the composed transfer functions over all valid interprocedural paths; the MFP solution of the interprocedural analysis gives a sound, computable under-approximation.

## Core Intuition
[[data-flow-analysis|Intraprocedural analysis]] has two ideals: the precise but undecidable [[mop-vs-mfp|MOP]] (join over all paths in the function) and the computable but possibly less precise [[mop-vs-mfp|MFP]] (least fixed point of the transfer function).

**Interprocedural analysis** has the same two ideals:
- **Meet Over Valid Paths (MVP)**: the precise ideal — join the composed transfer functions over all *valid* interprocedural paths (paths that respect call-return matching)
- **Interprocedural MFP**: the computable approximation — the least fixed point of the interprocedural transfer function

MVP is the interprocedural analogue of MOP. MFP is the interprocedural analogue of MFP. The same relationships hold: MVP is precise but undecidable; MFP is computable and sound.

## Formal Definition / Statement

For an interprocedural CFG with procedures P_1, ..., P_k, and call/return nodes:

**Valid path** (from the lecture grammar):
```
Path ::= ⟨P⟩* ⟨M⟩
P     ::= b_x | b_cy
M     ::= b_cx ⟨M⟩ b_rx | b_y ⟨M⟩ | ⟨M⟩ b_y | ε
```

**MVP at block b_i**:
MVP(b_i) = ⊔ { trans_{p_k} ∘ ... ∘ trans_{p_0} (⊥) | [p_0, ..., p_k] ∈ vpath(b_i) }

where vpath(b_i) is the set of all *valid* paths to b_i. This is the interprocedural analogue of MOP.

The **interprocedural MFP** is the least fixed point of the global interprocedural transfer function (which, after the call/return node splitting, looks like a big intraprocedural transfer function on the ICFG).

**Theorem**: MFP ⊑ MVP (MFP is a sound under-approximation of MVP).

**Theorem (Distributivity)**: MFP = MVP iff the interprocedural transfer functions are distributive.

## Key Properties / Complexity

### Why MVP is undecidable
- Programs with loops have infinitely many execution paths
- Programs with recursion have infinitely many interprocedural paths
- The set of valid paths is generally infinite
- Computing MVP exactly is not feasible

### Why interprocedural MFP is computable
- The ICFG is a finite graph (after call/return splitting)
- The lattice of facts is finite-height
- The transfer functions are monotone
- The Knaster-Tarski iteration reaches the least fixed point in h(L) steps

### The role of context sensitivity
- A *context-insensitive* analysis computes one MFP for each procedure, applied at all call sites
- A *context-sensitive* analysis computes a different MFP for each call context (or uses call strings, summaries, etc.)
- Both produce MFP solutions; the context-sensitive MFP is closer to MVP

### Valid path constraint — the formal grammar
The lecture gives the grammar:
```
Path ::= ⟨P⟩* ⟨M⟩      (a path is a prefix of unmatched calls followed by a properly nested sequence)
P     ::= b_x | b_cy   (non-call block, or unmatched call)
M     ::= b_cx ⟨M⟩ b_rx  (matched call-return pair)
      |  b_y ⟨M⟩        (non-call block before a matched sequence)
      |  ⟨M⟩ b_y        (non-call block after a matched sequence)
      |  ε              (empty)
```

The P* prefix allows for calls that never return (e.g., `exit()`, infinite loops, exceptions). The M non-terminal generates properly nested call-return sequences.

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

**MVP at b'6 (return from f at call site b6)**:
- Valid paths to b'6:
  1. [b5, b6, b0, b1, b2, b4, b'6] (x > y branch)
  2. [b5, b6, b0, b1, b3, b4, b'6] (x ≤ y branch)
- Transfer-function composition for path 1: trans_{b'6} ∘ trans_{b4} ∘ trans_{b2} ∘ trans_{b1} ∘ trans_{b0} ∘ trans_{b6} ∘ trans_{b5}
- Apply to ⊥: a = 7 → d = 7 (because x = 7, y = 2, max = 7)
- Similarly for path 2: d = 7
- MVP at b'6 = {7} ⊔ {7} = {7}

**MVP at b'7 (return from f at call site b7)**:
- Valid paths: similar, but with x = 1, y = 5
- MVP at b'7 = {5} ⊔ {5} = {5}

**Final MVP**: d = {7}, e = {5}. Precise.

**Context-insensitive MFP**: f analysed once with x = {1, 2, 5, 7}, y = {1, 2, 5, 7}. z = max(x, y) = {7}. d = e = {7}. Imprecise.

**Context-sensitive MFP with cloning**: as shown above, d = {7}, e = {5}. Same as MVP.

**Context-sensitive MFP with procedure summary**: trans_f(x, y) = max(x, y). At b6: d = max(7, 2) = 7. At b7: e = max(1, 5) = 5. Same as MVP.

## Common Pitfalls

- **MVP is undecidable**. The MFP is the computable approximation.
- **Valid paths are the constraint**. An analysis that includes invalid paths (e.g., enter f at one call, exit at another) is *unsound*.
- **MVP differs from MOP only in the interprocedural setting**. Within a single function, MVP = MOP.
- **Context sensitivity is the precision lever**. Without it, the MFP can be much less precise than MVP.
- **The "valid path" grammar is the formal definition**. The intuitive rule "calls and returns must match up" is what the grammar formalises.
- **MVP for a program with dynamic dispatch (Java, C++) is even harder** — the call graph is not known statically, so valid paths depend on runtime types.

## Connections

- [[valid-paths]] — the path definition MVP is built on
- [[mop-vs-mfp]] — MOP/MFP is the intraprocedural analogue
- [[interprocedural-analysis]] — the broader topic
- [[context-sensitivity]] — the precision lever
- [[data-flow-analysis]] — the intraprocedural foundation
- [[monotone-framework]] — guarantees MFP exists and is computable
- [[software-analyse-lecture-7]] — the lecture

## Open Questions

- For dynamic-dispatch languages, MVP requires reasoning about *all possible* call targets. How do production tools handle this?
- Demand-driven MVP — compute MVP only for a specific query, not the whole program. What are the tradeoffs?
- For very large programs, is *any* sound interprocedural analysis tractable? What approximations do production tools make?
- Can MVP be combined with [[abstract-interpretation|abstract interpretation]]'s other machinery (widening, narrowing) for more expressive interprocedural analyses?
