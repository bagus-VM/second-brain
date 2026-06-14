---
title: "Cloning (Context Sensitivity)"
tags: [concept, software-analyse, semester-1, context-sensitivity, cloning]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[context-sensitivity]]", "[[interprocedural-analysis]]"]
---

## One-line Summary
Cloning is the most precise [[context-sensitivity|context-sensitivity]] technique: physically duplicate a procedure's body, one copy per call site, so that each call site gets its own analysis of the procedure — at the cost of code-size explosion.

## Core Intuition
When procedure f is called from two call sites b6 and b7 with different arguments, a context-insensitive analysis merges the two calls and loses information. **Cloning** fixes this by making f_6 (the copy of f for call site b6) and f_7 (the copy for call site b7) *separate procedures*. Each is analysed once with its own call context.

The result: perfect precision. Each call site gets its own copy of the analysis, with no merging.

The cost: code-size explosion. If f is called from C call sites, the analysis runs C times. For deeply nested call chains, the blowup can be exponential.

## Formal Definition / Statement

Given a [[context-sensitivity|context-insensitive]] analysis on a procedure f called from call sites c_1, c_2, ..., c_C, the **cloning** variant produces C copies f_1, f_2, ..., f_C. The call graph is modified:
- Each call site c_i that called f now calls f_i
- Each f_i is a fresh procedure, with f_i's body identical to f's body
- The analysis is run separately on each f_i

The result is the same as running the analysis C times, once per call context.

## Key Properties

### Precision: perfect
Each call site gets its own procedure analysis, so the contexts are completely separate. There is no merging of information across call sites. This is the most precise context-sensitivity technique.

### Cost: O(C × |P|)
If f is called from C call sites and has a body of size |P|, the cloned analysis takes O(C × |P|) time and space. For deep call chains, this can be exponential in the call depth.

### When cloning is impractical
- Large programs with many call sites
- Deeply recursive procedures (cloning one recursive call at every call site still blows up)
- Memory-constrained environments (mobile, embedded)

### Cloning vs inlining
- **Cloning**: duplicate the procedure (one f_i per call site). The call graph grows.
- **Inlining**: substitute the body at the call site. The call graph shrinks (no calls to f remain).
- For non-recursive procedures, inlining is essentially cloning.
- For recursive procedures, cloning still works; inlining does not terminate.

## Worked Example

The lecture's program (slides 28-31):
```c
int a = 7;
int d = f(a, 2);    // call site b6
int e = f(1, 5);    // call site b7
int f(int x, int y) {
  int z = 0;
  if (x > y) z = x; else z = y;
  return z;
}
```

After cloning:
- f_1 is called from b6 with x = {7}, y = {2}. Analysis: z = {7}, return z = {7}. So d = {7}.
- f_2 is called from b7 with x = {1}, y = {5}. Analysis: z = {5}, return z = {5}. So e = {5}.

The cloned analysis is identical to running the intraprocedural analysis twice with different inputs. The result is precise: d = {7}, e = {5}.

## Common Pitfalls

- **Cloning is the most precise but the most expensive**. For most real programs, the code-size explosion is prohibitive.
- **Cloning interacts badly with recursion**. Cloning a recursive procedure at every call site can still blow up; you may need a hybrid approach.
- **The "perfect precision" of cloning is a *precision* property, not a *soundness* property**. Cloning is sound (it produces a sound answer) and precise (it produces the optimal answer for that call site). It is not "more sound" than context-insensitive.
- **Cloning is the *most* precise context-sensitivity technique**. Procedure summaries, call strings, and inlining can also be precise (or less precise), but cloning is the gold standard for precision.

## Connections
- [[context-sensitivity]] — the general topic
- [[inlining-context-sensitivity|Inlining]] — the related technique for non-recursive procedures
- [[call-strings]] — the practical alternative
- [[procedure-summaries]] — the compositional alternative
- [[interprocedural-analysis]] — the broader topic
- [[software-analyse-lecture-7]] — the lecture

## Open Questions
- Can cloning be combined with procedure summaries (e.g., clone the most-called procedures, summarise the rest)?
- For object-oriented programs, how does cloning interact with dynamic dispatch? The call graph is not known statically.
- Is there a "lazy cloning" approach where clones are created only as needed by a specific query?
