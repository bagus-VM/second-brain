---
title: "Heap Analysis"
tags: [concept, software-analyse, semester-1, heap-analysis, alias-analysis]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[points-to-analysis]]", "[[interprocedural-analysis]]"]
---

## One-line Summary
Heap analysis is the family of static analyses that reason about heap-allocated memory — determining which objects exist, which pointers can reach them ([[points-to-analysis|points-to analysis]]), which fields are shared ([[aliasing|aliasing]]), and which objects can be proved to be garbage (escape analysis) — all without running the program.

## Core Intuition
The heap is where dynamically allocated objects live. When you write `a = new A()` in Java or `malloc(sizeof(A))` in C, the resulting object lives on the heap, has no name (it's an anonymous allocation), and may exist arbitrarily many times. The analysis must reason about *all possible* heap states — but the number of possible states is infinite (any number of objects of any type).

**Heap analysis** abstracts the heap into a finite, computable representation. The simplest abstraction: "every `new A()` call produces the same abstract object". A more precise abstraction: "different call sites produce different abstract objects". Even more precise: "different call sites with different call contexts produce different objects", and "different fields of the same object are distinguished".

The design space for heap abstractions is large (the lecture lists nine axes). Modern tools pick combinations based on the precision/cost tradeoff they want.

The flagship heap analysis is [[points-to-analysis|points-to analysis]] — covered in detail in the lecture. Other heap analyses include:
- **Alias analysis**: which variables can refer to the same memory location
- **Escape analysis**: which objects can be accessed outside their allocating thread/method
- **Shape analysis**: the actual shape of linked data structures (linked lists, trees, graphs)
- **Purity analysis**: whether a function modifies its arguments or has side effects on the heap
- **Nullness analysis**: whether a reference can be null

## Formal Definition / Statement

A **heap abstraction** is a function
α: ℘(Concrete Heaps) → Abstract Heap
that maps the (infinite) set of possible concrete heaps to a (finite) abstract heap description.

The design space for α is parameterised by choices about:
1. **Static vs. dynamic locations**: distinguish global variables, stack-allocated locals, heap-allocated objects
2. **Naming**: how to name heap objects (allocation site, allocation site + call context, ...)
3. **Field sensitivity**: whether different fields of an object are tracked separately
4. **Array index sensitivity**: whether different array indices are tracked separately
5. **Pointer arithmetic sensitivity**: whether to model `*(p + 5)` precisely
6. **Type sensitivity**: whether to distinguish objects by their type

For [[points-to-analysis|points-to analysis]], the most important design choice is the *naming* of abstract objects. The simplest model: every `new A()` call site is one abstract object. A more precise model: every call site × call context is one abstract object.

## Key Properties / Complexity

### The three flavours of memory locations
- **Static locations**: uniquely identified by name. `int global_x` is always the same location.
- **Stack-dynamic locations**: parameters, local variables. Named, but:
  - May never exist (function not called)
  - May exist multiple times (recursion)
- **Heap-dynamic locations**: anonymous. May exist arbitrarily often.

The challenge: heap-dynamic locations are anonymous *and* unbounded.

### The aliasing problem
```c
A *a = new A();
A *b = a;       // b aliases a
A *c = new A(); // c does NOT alias a
a->x = 17;
c->x = 23;
b->x = 42;      // a->x is now 42 (b aliases a)
print(a->x);    // prints 42
print(c->x);    // prints 23
```

A sound analysis must report "a->x may be 17 or 42" (because b is an alias of a) and "c->x is 23" (because c is not an alias of a). Without points-to information, the analysis would have to assume *everything* aliases *everything* — useless.

### The "context" for heap objects
A heap object allocated at call site c, when called from call site c1 with call context C1, is (potentially) a *different object* from one allocated at the same call site c when called from c2 with context C2. The analysis can choose to merge them (losing precision) or keep them separate (gaining precision at the cost of state).

### Escape analysis
A heap object "escapes" if it can be accessed outside its allocating method/thread. If an object doesn't escape, it can be:
- Allocated on the stack instead of the heap
- Subject to scalar replacement (its fields become local variables)
- Eliminated entirely (if not used)

Escape analysis is the basis of many compiler optimisations. The Java HotSpot compiler, for example, uses escape analysis to allocate objects on the stack.

### Shape analysis
Shape analysis goes further than points-to: it tracks the *shape* of linked data structures. "This pointer always points to the head of an acyclic linked list with at most n elements" is a shape analysis result.

Shape analysis is expensive but powerful. TVLA (Three-Valued Logic Analysis) is the canonical framework; it uses 3-valued logic to track shape predicates.

### Practical tools
- **DOOP**: a points-to analysis framework for Java, built on Datalog. Uses Andersen's-style analysis with various sensitivity options.
- **WALA**: IBM's library for static analysis of Java. Includes Andersen's, Steensgaard's, and hybrid analyses.
- **Infer**: Facebook's static analyzer. Uses separation logic and bi-abduction for shape-style reasoning.
- **Soot**: a Java optimization framework with built-in points-to analysis.
- **PADDLE**: a points-to analysis framework for Java built on Prolog/Datalog.

## Worked Example

The lecture's example (slide 53):
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

**Analysis 1: naive (no aliasing awareness)**:
- a.x, b.x, c.x are "different things"
- a.x = 17, c.x = 23, b.x = 42
- print(a.x) = 17, print(c.x) = 23
- **Unsound** — b is an alias of a, so b.x = 42 should also affect a.x

**Analysis 2: knows about aliasing**:
- b is an alias of a (pts(b) = pts(a))
- c is NOT an alias of a (pts(c) = {obj_2} ≠ pts(a) = {obj_1})
- After `b.x = 42`: a.x = 42 (because b aliases a)
- print(a.x) ∈ {17, 42} (after both assignments)
- print(c.x) = 23
- **Sound but imprecise** — the analysis reports {17, 42} for a.x, when only 42 is possible

**Analysis 3: precise (with field sensitivity)**:
- a, b, c have distinct points-to sets
- The exact values are: a.x = 42, b.x = 42 (alias), c.x = 23
- print(a.x) = 42, print(c.x) = 23
- **Precise** — but this requires sophisticated tracking

The lecture's slides walk through the three analyses and explain the difference.

## Common Pitfalls

- **"Object sensitivity" is not the same as "context sensitivity"**. Object sensitivity tracks `this` instances (i.e., the receiver of a method call). Context sensitivity tracks call sites. Both are precision axes, but they capture different information.
- **Field-insensitive analyses are unsound for some code**. If your code writes `a.f = 1; b.f = 2; read(a.f)`, a field-insensitive analysis might report `a.f ∈ {1, 2}` — which is sound but loses the fact that a.f is 1 in the actual execution.
- **Points-to analysis for C is harder than for Java**. C has pointer arithmetic (`*(p + n)`), struct fields, and `void *` casts. Java has reference types, but no arithmetic on references. The constraints differ significantly.
- **The "abstract object" for `new A()` is a per-program label, not a per-execution allocation**. If a function is called twice, the analysis may treat the two allocations as the same abstract object (in the simplest model) or as different (in a more precise model).
- **Escape analysis is conservative by default**. An object that *might* escape is treated as escaping. To prove non-escape, the analysis must trace every access — expensive.
- **Java's `String` is a special case**. The `String` constant pool, interning, and `==` semantics all interact with points-to analysis in subtle ways. Most static analyzers special-case strings.

## Connections

- [[points-to-analysis]] — the flagship heap analysis
- [[steensgaards-points-to-analysis|Steensgaard's analysis]] — fast, imprecise
- [[andersens-points-to-analysis|Andersen's analysis]] — slow, precise
- [[aliasing]] — the property heap analysis enables reasoning about
- [[interprocedural-analysis]] — the interprocedural setting for heap analysis
- [[context-sensitivity]] — needed for precise interprocedural heap analysis
- [[union-find-data-structure|Union-Find]] — the data structure for Steensgaard's
- [[software-analyse-lecture-7]] — the lecture

## Open Questions

- How do production tools (DOOP, WALA, Infer, Soot) handle the heap design space? What are the engineering tradeoffs?
- Is there a meaningful "precision ladder" for heap analyses: Steensgaard < bset < Andersen < flow-sensitive < context-sensitive < object-sensitive < field-sensitive × context-sensitive × ...? With associated complexity ladders?
- Can heap analysis be made *compositional* — building a sound analysis for a whole program from sound analyses of its parts, with a clean interface between them?
- Shape analysis is powerful but expensive. Are there practical shape analyses that scale to real code? (TVLA, separation logic, ...)
- The lecture lists "object sensitivity" as a design choice. How does it interact with call-string context sensitivity? Which is better in practice for Java?
