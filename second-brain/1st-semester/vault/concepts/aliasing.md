---
title: "Aliasing"
tags: [concept, software-analyse, semester-1, aliasing, points-to-analysis, heap-analysis]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[points-to-analysis]]", "[[heap-analysis]]"]
---

## One-line Summary
Aliasing occurs when multiple names (variables, references, pointers) refer to the same memory location; alias analysis determines which names can be aliases of which — a prerequisite for reasoning about heap effects and the reason [[points-to-analysis|points-to analysis]] matters.

## Core Intuition
In languages with references and pointers, a single memory location can be referred to by multiple names. When you write `a = new A(); b = a;`, both `a` and `b` refer to the same object. A subsequent `a.x = 17` is *also* a write to `b.x`. A read of `b.x` after the write yields 17, not whatever `b.x` was before.

Without aliasing information, the analysis must assume *every* write to *any* field of *any* object could affect *every* read — uselessly imprecise. Alias analysis provides the missing information: "a and b are aliases; a and c are not".

**Alias sets** are the central concept: for each abstract object l, the alias set is `{v | l ∈ pts(v)}` — all variables that *might* point to l. The complement (variables that *cannot* point to l) are *known not to be aliases*.

## Formal Definition / Statement

A set of variables {v₁, v₂, ..., v_k} are **aliases** (at a given program point) if they all refer to the same memory location. More precisely: they are aliases if there exists an object l such that l ∈ pts(v_i) for all i.

Two equivalent ways to compute alias information from [[points-to-analysis|points-to]]:
- **Alias sets**: for each abstract object l, alias_set(l) = {v | l ∈ pts(v)}
- **Alias pairs**: set of pairs (v_i, v_j) such that v_i and v_j might be aliases

The two are equivalent; the alias-set view is usually more useful.

## Key Properties / Complexity

### The three kinds of pointer operations
The lecture identifies three kinds of pointer behaviour (slide 64):
- **Referencing**: creating a pointer/reference. `&x` in C, `new A()` in Java
- **Dereferencing**: reading through a pointer/reference. `*p` in C, `a.f` in Java
- **Aliasing**: two names referring to the same object

| C | Java | |
|---|------|---|
| `my_t *p = &var;` | `A a = new A();` | Referencing |
| `int x = *ptr;` | `int x = a.f;` | Dereferencing |
| `my_t *pa; pa = pb;` | `A b = a;` | Aliasing |

### Why aliasing breaks naive analysis
```c
a = new A();
b = a;
c = new A();
a.x = 17;
c.x = 23;
b.x = 42;
print(a.x);
print(c.x);
```
- **Naive (no alias awareness)**: prints 17 and 23. *Unsound* — it ignores that b aliases a, so a.x is 42.
- **Alias-aware (with [[points-to-analysis|points-to]])**: prints 42 and 23. *Sound* — it knows b aliases a.

The lecture's slide 53 makes this point exactly.

### The four points-to analysis constraints
Alias information is computed by [[points-to-analysis|points-to analysis]]. The four constraint kinds (per the lecture's slide 69):
- Referencing `a = &b` / `a = new A()`: {l_b} ⊆ pts(a)
- Aliasing `a = b` / `a = b`: pts(b) ⊆ pts(a) (Andersen) or pts(a) = pts(b) (Steensgaard)
- Dereferencing read `a = *b` / `a = b.f`: pts(*b) ⊆ pts(a)
- Dereferencing write `*a = b` / `a.f = b`: pts(b) ⊆ pts(*a)

The dereferencing constraints use the "points-to of points-to" — the set of objects reachable from the points-to set of the dereferenced variable.

### May-alias vs must-alias
- **May-alias**: a set of variables that *might* be aliases (i.e., there exists an execution in which they refer to the same object)
- **Must-alias**: a set of variables that *must* be aliases (i.e., in *every* execution, they refer to the same object)

The lecture focuses on may-alias. Must-alias is harder and less commonly used.

### Where aliasing matters in practice
- **Compiler optimisations**: aliasing prevents the compiler from reordering memory accesses. The C `restrict` keyword is a programmer-supplied aliasing assertion.
- **Bug detection**: use-after-free, double-free, data races all depend on aliasing.
- **Verification**: proving the absence of certain bugs requires proving that two pointers are *not* aliases.
- **Garbage collection**: tracing collectors follow pointers; aliasing affects reachability.

## Worked Example

The lecture's example (slide 65):
```c
A *a = new A();
A *b = a;
A *c = new A();
```
After execution, the points-to sets are:
- pts(a) = {l_1} (where l_1 is the first `new A()` object)
- pts(b) = {l_1}
- pts(c) = {l_2} (where l_2 is the second)

**Alias sets**:
- alias_set(l_1) = {a, b, *a, *b, *c} (the variables that may point to l_1, including the dereferenced forms)
- alias_set(l_2) = {c, *a, *b, *c} (only c might point to l_2, but the dereferenced forms of a, b, c could all read from l_2 if they were assigned to it)

**Points-to pairs**: (a → l_1), (b → l_1), (c → l_2).

**May-alias pairs**: (a, b), (a, *a), (a, *b), (b, *a), (b, *b), (*a, *b), (a, *c), (b, *c), (*a, *c), (*b, *c), (c, *a), (c, *b), (c, *c) — anyone might be an alias of anyone if you only consider "might point to the same set".

**Definite non-alias pairs**: (a, c) — a *cannot* alias c, because pts(a) = {l_1} and pts(c) = {l_2} with l_1 ≠ l_2. Similarly, (b, c) is a definite non-alias.

This is the value of points-to analysis: it tells you *which* aliases are possible and *which* are impossible. The "impossible" information is what enables precise reasoning.

## Common Pitfalls

- **May-alias is not transitive**. If a may-alias b, and b may-alias c, then a may-alias c — *if* the points-to sets overlap pairwise. But "may-alias" is usually defined as "share a common points-to object", and the transitivity requires the common object to be the *same*.
- **Aliasing and points-to are not the same**. Points-to says what objects a variable can point to. Alias says which variables are *currently* pointing to the same object. They're related but not identical.
- **Field-insensitive analysis loses field-aliasing information**. If two field accesses might alias (e.g., `a.f` and `b.f` where a and b might be aliases), a field-insensitive analysis cannot distinguish them.
- **Java's `==` on objects is reference equality, not value equality**. Aliasing matters more in Java than in C because Java objects are always accessed through references. A Java static analyzer must reason about references carefully.
- **The C `restrict` keyword changes the aliasing rules**. With `restrict`, the programmer asserts that two pointers are *not* aliases — the compiler can then optimise more aggressively. The analysis must respect `restrict` (and warn if it's violated).

## Connections

- [[points-to-analysis]] — the analysis that produces alias information
- [[steensgaards-points-to-analysis|Steensgaard's analysis]] — fast, imprecise aliasing
- [[andersens-points-to-analysis|Andersen's analysis]] — slow, precise aliasing
- [[heap-analysis]] — the broader topic
- [[interprocedural-analysis]] — the interprocedural setting
- [[context-sensitivity]] — a precision axis
- [[software-analyse-lecture-7]] — the lecture

## Open Questions

- Must-alias analysis is harder and less common. When is it worth the cost?
- For object-oriented programs, *object sensitivity* (tracking `this` instances) is a separate axis from call-string context sensitivity. How do they interact with aliasing?
- Can [[abstract-interpretation|abstract interpretation]] be used to formalise aliasing as a particular abstract domain (e.g., the "may-alias lattice" with subset relations)?
- The C `restrict` keyword is a programmer-supplied aliasing assertion. How do static analyzers verify that `restrict` is used correctly?
