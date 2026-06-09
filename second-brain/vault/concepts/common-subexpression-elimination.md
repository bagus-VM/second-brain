---
title: "Common Subexpression Elimination"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: ["[[available-expressions]]"]
---

## One-line Summary
If the same calculation appears twice and nothing changed in between, the compiler reuses the first result instead of recomputing it.

## Core Intuition
Compilers waste time when they compute the same expression multiple times. If you write `x = a + b` and later `y = a + b` without any assignment to `a` or `b` in between, the second `a + b` produces the same result. Common subexpression elimination (CSE) detects these redundant computations and replaces the second occurrence with a reference to the already-computed value. The key question is: how does the compiler *know* that `a + b` hasn't changed? This is exactly what [[available-expressions]] analysis answers — it tracks which expressions have been computed on *every* path to a given point and haven't been invalidated since. CSE is one of the most impactful compiler optimizations because it reduces both instruction count and register pressure.

## Formal Definition / Statement

**Common subexpression elimination** is a compiler optimization that:

1. Identifies expressions that are **available** at a program point (computed on all paths, no operands redefined since)
2. Replaces the redundant computation with a reference to the previously computed value

**Algorithm**:
1. Run [[available-expressions]] analysis on the [[control-flow-graph]]
2. For each assignment `x = expr`:
   - If `expr` is in IN(b) for block b (i.e., available at that point):
     - Find the previously computed value `t` where `t = expr` was executed
     - Replace `x = expr` with `x = t`
   - Otherwise: record that `expr` is now available with value `x`

**Condition for elimination**: Expression `e` at statement s can be eliminated iff e ∈ IN(s) — meaning e was computed on *every* path reaching s, and no operand of e was redefined along any of those paths.

**Relationship to [[available-expressions]]**: CSE is the direct consumer of available-expressions analysis. The "must" (intersection) nature of available expressions is critical — we can only eliminate an expression if it's been computed on *all* paths, not just some.

## Key Properties / Complexity

- **Safe**: CSE never changes program semantics (replacing a computation with its result)
- **Forward, must** analysis dependency: requires available-expressions (intersection at join points)
- Can increase register pressure: saved values must be kept alive longer
- May introduce new temporary variables (need [[register-allocation]] to manage them)
- Interacts with aliasing: in languages with pointers, a store through a pointer may invalidate expressions involving memory locations
- Global CSE (across basic blocks) is more powerful than local CSE (within a single block)
- The optimization is idempotent: applying CSE twice yields the same result as applying it once

## Worked Example

```java
// Before CSE
a = b + c;      // compute b+c, store in a
d = b + c;      // b+c is available! Use a instead
e = b + c;      // b+c is still available! Use a instead
```

Available-expressions analysis:
- After `a = b + c`: IN contains nothing (start), OUT = {b+c}
- Before `d = b + c`: IN = {b+c} → b+c is available → eliminate
- Before `e = b + c`: IN = {b+c} → b+c is available → eliminate

```java
// After CSE
a = b + c;
d = a;           // reuse
e = a;           // reuse
```

With a conditional branch:
```java
if (cond) {
    x = a + b;   // computes a+b
} else {
    y = a + b;   // a+b NOT available (not on all paths) → cannot eliminate
}
z = a + b;       // a+b available (computed on both branches) → eliminate
```

## Common Pitfalls

- Confusing **available expressions** (must, intersection) with **reaching definitions** (may, union) — CSE needs the "must" variant
- Forgetting that assigning to a variable *kills* all expressions involving that variable
- Not considering pointer aliasing: `*p = 5` may kill expressions involving `a` if `p` could point to `a`
- CSE can increase register pressure, potentially causing spills — the net effect may be negative
- Local CSE (within a block) is trivial; global CSE (across blocks) requires the full data flow analysis
- CSE and [[dead-code-elimination]] are complementary: CSE creates new definitions that DCE might clean up

## Connections

- [[available-expressions]] — the data flow analysis that powers CSE (which expressions are guaranteed to be computed?)
- [[data-flow-analysis]] — CSE is a direct application of the must-analysis framework
- [[iterative-data-flow-analysis]] — the algorithm that solves the available-expressions equations
- [[dead-code-elimination]] — complementary optimization: CSE may create dead assignments that DCE removes
- [[register-allocation]] — CSE increases the number of live values, putting pressure on register allocation
- [[gen-kill-analysis]] — CSE uses gen/kill sets to track expression availability
- [[software-analyse-lecture-5]] — lecture where CSE is introduced as an application of data flow analysis

## Open Questions

- How does CSE interact with loop-invariant code motion (a related optimization)?
- What happens to CSE in the presence of exception handling (try/catch)?
- How do modern compilers (LLVM, GCC) implement CSE at the SSA level?
