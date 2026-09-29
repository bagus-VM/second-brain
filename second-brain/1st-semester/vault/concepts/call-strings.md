---
title: "Call Strings"
tags: [concept, software-analyse, semester-1, context-sensitivity, call-strings]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[context-sensitivity]]", "[[interprocedural-analysis]]"]
---

## One-line Summary
A call string is a sequence of call sites that records the calling context of a procedure invocation; using bounded-length call strings is a [[context-sensitivity|context-sensitive]] analysis technique that keeps the analysis scalable by tagging each call with its call history.

## Core Intuition
[[cloning-context-sensitivity|Cloning]] duplicates a procedure's body, one copy per call site — perfectly precise but blows up code size. [[inlining-context-sensitivity|Inlining]] substitutes the body at each call site — also perfectly precise but doesn't terminate for recursion. **Call strings** keep the procedure as a single body, but tag each invocation with a *call string* — a sequence of call sites that describes how you got there.

The analysis state becomes (abstract_value, call_string) pairs. Two invocations with the same call string share their state; two invocations with different call strings have separate state. This is precise enough for most practical purposes.

The catch: without a bound, call strings can grow unboundedly (e.g., recursive procedures), and the analysis may not terminate. The practical fix: **k-bounded call strings** keep only the k most recent call sites. This bounds the state and guarantees termination, at the cost of some precision for deeply nested call chains.

## Formal Definition / Statement

A **call string** is a sequence of call sites, typically written as [c₁, c₂, ..., c_k] where c₁ is the most recent call and c_k is the oldest. The empty call string [] represents the program entry.

A **k-bounded call string** is a call string of length at most k. When a new call c is made, the new call string is [c, c₁, c₂, ..., c_{k-1}] — drop the oldest.

A **context-sensitive analysis with call strings** tracks, for each procedure f, a set of pairs {(σ, cs) | σ is the abstract state at f's entry, cs is the call string leading to this state}. When entering f with call string cs', the analysis computes σ' as the abstract value of f's body under σ, and records the pair (σ', cs').

Two invocations of f with the same call string share their state. Two invocations with different call strings are kept separate.

## Key Properties / Complexity

### Why bounded call strings are needed
- For non-recursive programs, call strings can grow at most to the depth of the call graph (which is finite)
- For recursive programs, call strings can grow unboundedly
- Without bounding, the analysis may not terminate
- Bounded call strings (k = 1, 2, or 3 are common) guarantee termination

### Precision vs scalability
- k = 0: context-insensitive (no call string)
- k = 1: distinguish one level of calling context (e.g., [c] vs [c'])
- k = 2: distinguish two levels (e.g., [c₁, c₂] vs [c₁, c₃])
- Higher k: more precise, but more state
- For deep recursion, even k = ∞ may not be enough

### The lecture's example (slides 35-40)
For the program:
```c
int a = 7;
int d = f(a, 2);    // call 1 at b6
int e = f(1, 5);    // call 2 at b7

int f(int x, int y) {
  int z = 0;
  if (x > y) z = x; else z = y;
  return z;
}
```
With k = 1:
- At b6: call string for f's body = [b6]. f's body: x = {7[b6]}, y = {2[b6]}. After the conditional, z = {7[b6]}. Return z = {7[b6]}. d = {7}.
- At b7: call string for f's body = [b7]. f's body: x = {1[b7]}, y = {5[b7]}. After the conditional, z = {5[b7]}. Return z = {5[b7]}. e = {5}.
- The call strings distinguish the two calls: d = {7}, e = {5} ✓

With k = 0 (context-insensitive):
- f analysed once with x = {1, 2, 5, 7}, y = {1, 2, 5, 7}. z = {7}. d = e = {7} (imprecise)

### Generalisation to deeper nesting
The lecture notes that call strings support deeper nesting. For:
```c
int g(y) { return y; }
int f(x) { return g(x) + g(5); }
f(1);
f(2);
```
A 2-bounded call string distinguishes:
- f(1) → g(x): call string = [call_g_in_f, call_f_1]
- f(1) → g(5): call string = [call_g_in_f, call_f_1]
- f(2) → g(x): call string = [call_g_in_f, call_f_2]
- f(2) → g(5): call string = [call_g_in_f, call_f_2]

Two invocations of g from the same f call have the same call string; two invocations from different f calls have different call strings.

## Worked Example

Following the lecture's slides 36-40, the analysis with k = 1 call strings for:
```c
int a = 7;
int d = f(a, 2);    // call site b6
int e = f(1, 5);    // call site b7
int f(int x, int y) { ... return z; }
```

State at f's entry b0:
- From b6 (call string [b6]): x = {7[b6]}, y = {2[b6]}
- From b7 (call string [b7]): x = {1[b7]}, y = {5[b7]}

State at f's exit (b4):
- From b6: z = {7[b6]} (max of 7 and 2)
- From b7: z = {5[b7]} (max of 1 and 5)

State at caller's return sites (b'6 and b'7):
- b'6: d = {7[b6]}, then d = {7} (after removing the call string for the value)
- b'7: e = {5[b7]}, then e = {5}

Final: d = {7}, e = {5}. Correct! And we never duplicated f's body.

## Common Pitfalls

- **Bounded call strings lose precision for deep recursion**. If the recursion depth exceeds k, the analysis merges states from different recursion levels — this is *imprecise* but not *unsound*.
- **Call string ordering matters**. The convention "most recent first" is standard but not universal. The choice affects how `drop oldest` works.
- **Call strings are different from call stacks**. A call stack is the runtime structure; a call string is the static abstraction. The analysis tracks call strings, not call stacks.
- **Call strings can be expensive to store**. For k = 1 and C call sites, you have at most C distinct call strings. For k = 2, up to C². For k = 3, C³. Each step multiplies the state.
- **The composed transfer function of a recursive procedure with call strings may still be ⊤**. Call strings distinguish contexts but don't compose the function's effect into a single transfer function.

## Connections

- [[context-sensitivity]] — the general topic
- [[cloning-context-sensitivity|Cloning]] — the most precise alternative
- [[inlining-context-sensitivity|Inlining]] — another precise alternative
- [[procedure-summaries]] — the compositional alternative
- [[interprocedural-analysis]] — the broader topic
- [[data-flow-analysis]] — the intraprocedural foundation
- [[software-analyse-lecture-7]] — the lecture

## Open Questions

- What is the right k for typical Java/C++ programs? (Empirically: 1 or 2 is usually enough.)
- How do call strings interact with object sensitivity in object-oriented programs? Are they redundant or complementary?
- Can call strings be combined with procedure summaries (e.g., summarise after k levels of call string)? This is the basis of many production tools.
- Are there program analyses for which call strings are *not* enough — e.g., requiring full call-tree equivalence?
