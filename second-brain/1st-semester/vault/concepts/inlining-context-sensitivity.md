---
title: "Inlining (Context Sensitivity)"
tags: [concept, software-analyse, semester-1, context-sensitivity, inlining]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[context-sensitivity]]", "[[interprocedural-analysis]]", "[[cloning-context-sensitivity|Cloning]]"]
---

## One-line Summary
Inlining is a [[context-sensitivity|context-sensitivity]] technique that substitutes a procedure's body at every call site, eliminating the call and the procedure entirely from the call graph — perfectly precise, but does not terminate for recursive procedures.

## Core Intuition
[[cloning-context-sensitivity|Cloning]] duplicates a procedure (one copy per call site). **Inlining** goes further: it removes the procedure entirely by substituting its body at each call site. The result is a single big procedure with no calls to the inlined procedure.

For non-recursive procedures, inlining is essentially equivalent to cloning (the analysis is the same; only the representation differs). For recursive procedures, inlining does not terminate — substituting the body would create more calls, which would need to be substituted again, and so on.

## Formal Definition / Statement

Given a procedure f with body blocks b_0, b_1, ..., b_n, called from call sites c_1, c_2, ..., c_C, **inlining** replaces each call site c_i with a copy of f's body, with parameters bound to the call's arguments and the return value assigned to the caller's variable.

After inlining, the call graph no longer contains edges to f (or any of its transitive callees that are fully inlined). The result is a single (large) procedure.

## Key Properties / Complexity

### Precision: perfect (same as cloning)
Each call site gets the body's analysis with its own arguments. There is no merging of information. Equivalent to cloning, but with a different representation.

### Termination: fails for recursive procedures
Inlining a recursive procedure creates more calls to itself, which need to be inlined again, ad infinitum. The result is an infinite expansion.

Workarounds:
- Only inline non-recursive procedures
- Inline only up to a certain call depth
- Use partial inlining (inline the first iteration, summarise the rest)

### When inlining is appropriate
- Non-recursive procedures with small bodies and few call sites
- Performance-critical code (inlining is also a runtime optimisation)
- Static analysis where the resulting single-procedure analysis is easier

### When inlining is not appropriate
- Recursive procedures
- Procedures with large bodies or many call sites
- Programs where the resulting procedure is too large to analyse efficiently

## Worked Example

For the program:
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

After inlining f at both call sites:
```c
int a = 7;
// inlined call 1
int x_1 = a;        // bind parameter x to a
int y_1 = 2;        // bind parameter y to 2
int z_1 = 0;
if (x_1 > y_1) z_1 = x_1; else z_1 = y_1;
int d = z_1;        // assign return value to d
// inlined call 2
int x_2 = 1;
int y_2 = 5;
int z_2 = 0;
if (x_2 > y_2) z_2 = x_2; else z_2 = y_2;
int e = z_2;
```

The result: a single procedure with no calls to f. The analysis is now intraprocedural.

## Common Pitfalls

- **Inlining does not terminate for recursive procedures**. The expansion is infinite.
- **Inlining can dramatically increase code size**. If f is large and called from many sites, the inlined code is much larger than the original.
- **Inlining loses the procedure abstraction**. After inlining, debugging becomes harder, and the code is harder to read. (Runtime optimisers also inline, but they keep the original code for debugging.)
- **Inlining is a runtime optimisation in compilers**. GCC and LLVM inline hot functions for performance. This is the same algorithm but applied for different reasons.
- **Inlining can change the program's semantics if the inlined function has side effects**. For analysis, this doesn't matter (we're computing abstract values), but for code generation it does.

## Connections
- [[context-sensitivity]] — the general topic
- [[cloning-context-sensitivity|Cloning]] — the related technique
- [[call-strings]] — the practical alternative
- [[procedure-summaries]] — the compositional alternative
- [[interprocedural-analysis]] — the broader topic
- [[software-analyse-lecture-7]] — the lecture

## Open Questions
- How do production tools decide when to inline for static analysis? Are there heuristics based on procedure size, call-site count, or recursion?
- Can inlining be combined with procedure summaries (e.g., inline non-recursive procedures, summarise recursive ones)?
- For Java, how does inlining interact with dynamic dispatch? The call target may depend on the runtime type.
