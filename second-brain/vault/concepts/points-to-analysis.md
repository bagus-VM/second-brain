---
title: "Points-to Analysis"
tags: [concept, software-analyse, semester-1, points-to-analysis, alias-analysis, heap-analysis]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[software-analyse-lecture-7]]", "[[interprocedural-analysis]]", "[[context-sensitivity]]", "[[aliasing]]"]
---

## One-line Summary
Points-to analysis computes, for every pointer variable, the set of heap objects it may point to — the foundation for analysing memory in languages with pointers, references, and heap allocation, and a prerequisite for understanding [[aliasing|aliases]].

## Core Intuition
When you write `a = new A()`, a new object is allocated on the heap and a points to it. When you write `b = a`, b *also* points to the same object. When you write `a.x = 17; b.x = 42;`, both modifications target the same field of the same object. The analysis must know *which objects each pointer can refer to* — otherwise it cannot reason about heap effects.

**Points-to analysis** computes a map `pts(v)` for every variable v, where `pts(v)` is the set of objects v may point to. For `a = new A(); b = a; c = new A();`:
- `pts(a) = {obj_1}` (where obj_1 is the object created by `new A()`)
- `pts(b) = {obj_1}` (b is an alias of a)
- `pts(c) = {obj_2}` (c points to a different object)

Without points-to information, the analysis would have to assume that *every variable could point to every object* — uselessly imprecise.

The two canonical algorithms are [[steensgaards-points-to-analysis|Steensgaard's]] (fast but imprecise, equality-based) and [[andersens-points-to-analysis|Andersen's]] (slower but precise, subset-based). Modern tools use variants of Andersen's with clever engineering to scale.

## Formal Definition / Statement

A **points-to analysis** computes a function
pts: Variables → ℘(Objects)
such that for every program point and every variable v, pts(v) is the set of objects that v *may* point to at that point.

The analysis is built from four constraint kinds, one per pointer operation in C/Java (lecture slide 69):

| C | Java | Constraint |
|---|------|------------|
| `a = &b` | `a = new A()` | {l_b} ⊆ pts(a) — referencing |
| `a = b` | `a = b` | pts(b) ⊆ pts(a) — aliasing |
| `a = *b` | `a = b.f` | pts(*b) ⊆ pts(a) — dereferencing read |
| `*a = b` | `a.f = b` | pts(b) ⊆ pts(*a) — dereferencing write |

(For Java, `b.f` reads the field f of b; `a.f = b` writes the field f of a.)

The four algorithms differ in how they treat these constraints:
- **Steensgaard**: equality-based, pts(b) = pts(a) after aliasing
- **Andersen**: subset-based, pts(b) ⊆ pts(a) after aliasing

## Key Properties

### Why this matters
Consider:
```c
A *a = new A();
A *b = a;
A *c = new A();
a->x = 17;
c->x = 23;
b->x = 42;
print(a->x);
print(c->x);
```
- **Without points-to (sound but imprecise)**: a and c might point to the same object, so a->x and c->x might be 17, 23, or 42. Print reports {17, 23, 42} for both — but a->x is *definitely* 42, and c->x is *definitely* 23. The imprecision hides real bugs.
- **With points-to**: pts(a) = pts(b) = {obj_1}, pts(c) = {obj_2}. a and b are aliases, a and c are not. So a->x = 42, c->x = 23 — no false sharing.

### Design space for heap abstractions
The lecture lists nine ways to distinguish or merge heap locations (slide 67):
1. Don't distinguish at all
2. By type
3. By name
4. By calling context ([[context-sensitivity]])
5. By control flow (flow-sensitive)
6. By containing heap object (object sensitivity)
7. By referencing field name in objects (field sensitivity)
8. By array index (array sensitivity)
9. By pointer arithmetic

Every choice trades precision for scalability. Real tools use combinations: e.g., "context-sensitive + object-sensitive + field-insensitive" is a common Java setting.

### Three flavours of memory locations
- **Static locations**: globally unique by name (e.g., global variables)
- **Stack-dynamic locations**: parameters, local variables — named, but may not exist (function not called) or may exist multiple times (recursion)
- **Heap-dynamic locations**: anonymous, may exist arbitrarily often (heap allocation)

The most challenging design problem is heap-dynamic locations. The simplest model says "all `new A()` calls produce the same abstract object". A more precise model says "different call sites produce different abstract objects". Even more precise: "different call sites with different call contexts produce different objects".

### Aliasing
A set of variables {v₁, v₂, ..., v_k} are **aliases** if they all refer to the same memory location — i.e., there exists an object l such that l ∈ pts(v_i) for all i. The points-to analysis gives the alias information as a byproduct: the alias set for object l is {v | l ∈ pts(v)}.

## Worked Example

For the C program:
```c
int i, j, k;
int *a = &i;
int *b = &k;
a = &j;
int **p = &a;
int **q = &b;
p = q;
int *c = *q;
```

**Steensgaard's analysis** (equality-based):
- After `a = &i`: pts(a) = {i}
- After `b = &k`: pts(b) = {k}
- After `a = &j`: pts(a) = {i, j} (Steensgaard merges with previous: pts(a) = pts(a) ∪ {j} = {i, j})
- After `p = &a`: pts(p) = {a}
- After `q = &b`: pts(q) = {b}
- After `p = q`: pts(p) = pts(q) = {a, b} (union-find merges p and q)
- After `c = *q`: dereferencing: for each l ∈ pts(q) = {a, b}, pts(c) = pts(l) = pts(a) ∪ pts(b) = {i, j, k}

**Andersen's analysis** (subset-based):
- After `a = &i`: pts(a) ⊇ {i}
- After `b = &k`: pts(b) ⊇ {k}
- After `a = &j`: pts(a) ⊇ {i, j} (additive, not replacement — both subsets)
- After `p = &a`: pts(p) ⊇ {a}
- After `q = &b`: pts(q) ⊇ {b}
- After `p = q`: pts(p) ⊇ pts(q) = {b} (and also {a} from before)
- After `c = *q`: for each l ∈ pts(q) = {b}, pts(c) ⊇ pts(b) = {k}

Steensgaard: c points to {i, j, k} (merged). Andersen: c points to {k} (precise).

The slides walk through the assignments and show the graph incrementally (slides 70-78 for Steensgaard, 82-94 for Andersen).

## Common Pitfalls

- **Points-to ≠ alias**. Points-to says what objects a variable *can* point to. Alias says *which* variables are *currently* pointing to the same object. They're related but not identical.
- **Steensgaard is much faster but loses precision**. The "almost linear" complexity is a great engineering win, but the imprecision is real. For deep object-oriented programs, Steensgaard may be too imprecise to be useful.
- **Andersen's O(n³) is the worst case**. For real programs, with the right engineering, it's often O(n²) or even O(n log n) in practice. Don't reject Andersen's on asymptotic grounds alone.
- **The "abstract object" for `new A()` is just a label**. Different call sites *can* map to the same abstract object (in the simplest model) or to different ones (in a more precise model). The analysis is only as precise as its allocation-site abstraction.
- **Field sensitivity is a major design choice**. "All fields of an object share one abstract location" is the field-insensitive choice; it's much faster but loses information. "Each field has its own abstract location" is field-sensitive; more precise, more expensive.
- **Java's `String` is its own nightmare**. The `String` constant pool, interning, and `==` vs `.equals()` all interact with points-to analysis in subtle ways. Most static analyzers special-case strings.

## Connections

- [[steensgaards-points-to-analysis|Steensgaard's analysis]] — fast, equality-based
- [[andersens-points-to-analysis|Andersen's analysis]] — precise, subset-based
- [[interprocedural-analysis]] — the interprocedural setting for points-to
- [[context-sensitivity]] — needed for precise interprocedural points-to
- [[aliasing]] — the property points-to enables reasoning about
- [[heap-analysis]] — the broader topic
- [[union-find-data-structure|Union-Find]] — the data structure behind Steensgaard's
- [[software-analyse-lecture-7]] — the lecture

## Open Questions

- Are there algorithms between Steensgaard's O(nα) and Andersen's O(n³) that capture some of Andersen's precision at less cost?
- How do modern tools (DOOP, PADDLE, WALA, Soot, Infer) implement Andersen's at scale? What are the engineering tricks?
- For object-oriented programs, is *call-string* context sensitivity the right choice, or is *object sensitivity* better? (Object sensitivity tracks `this` distinctions.)
- How do escape analysis and points-to analysis interact? Can escape analysis be done independently, or does it need points-to?
- What is the relationship between points-to analysis and [[abstract-interpretation|abstract interpretation]]? Is points-to a particular abstract domain?
