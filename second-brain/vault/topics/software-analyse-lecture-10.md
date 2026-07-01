---
title: "Software Analyse - Lecture 10: Dynamic Symbolic Execution"
tags: [topic, software-analyse, semester-1, symbolic-execution, concolic-execution]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-07-01
prerequisites: [static-vs-dynamic-analysis, control-flow-graph]
---

## One-line Summary
Symbolic execution explores all program paths by treating inputs as symbols rather than concrete values; dynamic symbolic execution (concolic) combines concrete and symbolic execution to systematically cover feasible paths.

## Core Intuition
Static analysis approximates all possible executions but includes infeasible paths. Random testing only covers what you happen to test. Symbolic execution explores ALL paths by treating inputs as symbolic variables, building path constraints, and solving them to generate test inputs. Dynamic symbolic execution (concolic = concrete + symbolic) starts with real inputs, executes concretely while collecting symbolic constraints, then negates constraints to explore new paths. This gives systematic coverage without the infeasible-path problem.

## Symbolic Execution

### Symbolic State
At any point, symbolic execution maintains:
- **Symbolic store** (σ): maps variables to symbolic expressions (σ ∈ Var ↦ Sym)
- **Path constraint** (φ): first-order Boolean formula describing branches taken

**State = σ ∧ φ**

### Example Walkthrough
```
void foobar(int a, int b) {
    int x = 1, y = 0;
    if (a != 0) {
        y = 3 + x;
        if (b == 0)
            x = 2 * (a + b);
    }
    assert (x - y != 0);
}
```

**Initial state**: σ = {a↦A, b↦B}, φ = true

**After line 3 (if a != 0)**:
- Then branch: σ = {a↦A, b↦B, x↦1, y↦0}, φ = A≠0
- Else branch: σ = {a↦A, b↦B, x↦1, y↦0}, φ = A=0

**Continue then branch**:
- After y = 3 + x: σ = {a↦A, b↦B, x↦1, y↦4}, φ = A≠0
- After if (b == 0):
  - Then: σ = {a↦A, b↦B, x↦2(A+B), y↦4}, φ = A≠0 ∧ B=0
  - Else: σ = {a↦A, b↦B, x↦1, y↦4}, φ = A≠0 ∧ B≠0

**At assert (x - y != 0)**:
- Path A≠0 ∧ B=0: check 2(A+B) - 4 = 0 → Error if A=2 ∧ B=0
- Path A≠0 ∧ B≠0: check 1 - 4 = 0 → false (no error)
- Path A=0: check 1 - 0 = 0 → false (no error)

**Result**: assertion fails when a=2, b=0

### Implicit Checks
Before each dangerous operation, fork execution:
- **Division/modulo**: divisor = 0 vs ≠ 0
- **Pointer dereferences**: null vs not-null
- **Array indexing**: negative vs positive index
- **Assert statements**: true vs false

### Test Generation Algorithm
1. Select path
2. Generate path condition
3. Solve path condition to generate test data

### Limitations
- **Loops**: unbounded loops → infinite execution tree. Solutions: bound the loop (under-approximation) or provide loop invariant (over-approximation)
- **Constraint solvers**: some problems undecidable or too complex (integers vs strings)
- **Opaque functions**: if source unavailable, symbolic execution impossible
- **Environmental modeling**: input(), system calls require modeling
- **Recursions**: infinite execution tree
- **Path explosion**: exponentially many paths
- **Heap modeling**: symbolic data structures and pointers
- **Infeasible paths**: constraints may be unsatisfiable

## Dynamic Symbolic Execution (Concolic)

### Core Idea
**Concolic = Concrete + Symbolic**

1. Start with random concrete input
2. Execute concretely while collecting symbolic constraints
3. Negate last constraint to explore new path
4. Solve negated constraint to get new concrete input
5. Repeat until all paths covered

### Algorithm Walkthrough
```
double P(short x, short y) {
    short w = abs(y);
    double z = 1.0;
    while (w != 0) {
        z = z * x;
        w = w - 1;
    }
    if (y < 0)
        z = 1.0 / z;
    return z;
}
```

**Run 1**: input (0, 0)
- Path: A-B-C-B-D-F (loop exits immediately, y≥0)
- Constraints: abs(Y)=0, ¬(Y<0)
- Negate last: abs(Y)≠0 → satisfiable, e.g., Y=1

**Run 2**: input (0, 1)
- Path: A-B-C-B-C-B-D-F (loop twice, y≥0)
- Constraints: abs(Y)≠0, abs(Y)-1=0, ¬(Y<0)
- Negate last: abs(Y)-1≠0 → satisfiable, e.g., Y=-1

**Run 3**: input (0, -1)
- Path: A-B-C-B-C-B-D-E-F (loop twice, y<0)
- All paths covered ✓

### Simultaneous Symbolic & Concrete Execution
When symbolic expression becomes unmanageable (e.g., non-linear):
```
void test_me(int x, int y) {
    z = x*x*x + 3*x*x + 9;  // non-linear
    if (z != y) {
        printf("Good branch");
    } else {
        printf("Bad branch");
        abort();
    }
}
```

**Problem**: solver cannot handle x³ + 3x² + 9 symbolically

**Solution**: replace symbolic z with concrete value (z=9 when x=-3), proceed with constraint 9≠y, solve 9=y → y=9, execute with (-3, 9), hit abort

**Key insight**: when symbolic execution gets stuck, fall back to concrete values

### Black Box Functions
If source unavailable, execute concretely:
```
z = black_box_fun(x);  // execute concretely, make z concrete
```

## Profiling

### Types
- **Insertion**: place profiling code into program (manually or automatically)
  - Pros: cross-platform, accurate
  - Cons: may require recompiling, affects performance
- **Sampling**: monitor CPU/VM at regular intervals
  - Pros: no modification needed
  - Cons: less accurate, may miss small methods, time/accuracy tradeoff

### Optimization Metrics
- **Runtime/CPU**: which lines spend most time, which call paths used
- **Memory**: what objects on heap, where allocated, who points to them, memory leaks

### Path Profiling
**Goal**: count how often each path through a function executes

**Problem with edge profiling**: counting edge frequencies doesn't uniquely identify most frequent path

**Ball-Larus Algorithm:**
1. Assign integers to edges so sum along path = unique path number
2. Assign increment operations to minimize additions (use spanning tree)
3. Instrument chords (edges not in spanning tree)
4. At exit, increment counter for path number

**Spanning tree approach:**
- Choose maximum-cost spanning tree
- Compute increments at chords
- Based on event counting algorithm

**Regenerating path from sum:**
- Start at entry with R = path sum
- At branches, use edge with largest value v < R, set R -= v

**Cyclic CFGs:**
- For backedge n→m, add dummy edges (entry→m, n→exit)
- Remove backedges, add DAG-based increments
- Add instrumentation to each backedge: count[r]++; r=0

## Key Properties
- **Symbolic execution**: explores all paths, generates tests, but suffers path explosion
- **Concolic execution**: systematic coverage of feasible paths, avoids infeasible paths
- **Concrete fallback**: when symbolic gets stuck, use concrete values
- **Path profiling**: precise path frequencies with minimal overhead (Ball-Larus)

## Common Pitfalls
- Thinking symbolic execution is practical for large programs — path explosion makes it infeasible
- Forgetting that concolic execution still requires constraint solving (expensive)
- Confusing symbolic store (variable mappings) with path constraint (branch conditions)
- Assuming Ball-Larus works for cyclic CFGs without modification (needs dummy edges)
- Thinking profiling has no overhead — insertion profiling affects performance

## Connections

### Course lectures
- [[software-analyse-lecture-9]] — concolic execution is dynamic analysis; L9's instrumentation and traces are the machinery concolic builds upon
- [[software-analyse-lecture-8]] — program slicing and symbolic path exploration are complementary: slicing asks "what affects this statement?", symbolic asks "what inputs reach this statement?"
- [[software-analyse-lecture-6]] — abstract interpretation (static over-approximation) vs symbolic execution (exact per-path); the lattice-vs-constraint duality
- [[software-analyse-lecture-4]] — control-flow graphs introduced here; Ball-Larus path profiling operates directly on CFGs

### Concepts
- [[static-vs-dynamic-analysis]] — symbolic execution bridges static and dynamic: it reasons statically about all paths but produces concrete test inputs
- [[control-flow-graph]] — foundation for path profiling; Ball-Larus encodes paths as edge-sum integers on the CFG, using a maximum-cost spanning tree to minimize instrumentation overhead
- [[symbolic-execution]] — pure symbolic execution concept; L10 adds the dynamic/concrete dimension
- [[concolic-execution]] — the core technique: concrete execution drives, symbolic constraints steer
- [[hierarchy-of-analysis]] — symbolic execution is "deduction" (static reasoning about all paths)
- [[dynamic-slicing]] — both operate on execution paths; slicing reduces programs, symbolic execution explores them
- [[software-analysis]] — overarching field
- [[abstract-interpretation]] — static approximation vs symbolic exact exploration; Galois connection vs constraint solving
- [[soundness-and-completeness]] — symbolic execution aims for completeness (all paths); concolic sacrifices completeness for feasibility

### Coverage gaps
No dedicated concept pages exist yet for: path explosion, constraint solving/SMT, test generation, or profiling (insertion vs sampling). These topics are discussed in the body and flagged in Open Questions — they warrant their own pages.

## Open Questions
- How do modern SMT solvers (Z3, CVC4) handle the constraint solving in practice?
- What's the practical path explosion limit for real-world symbolic execution tools (KLEE, angr)?
- How does concolic execution handle concurrency and interleavings?
