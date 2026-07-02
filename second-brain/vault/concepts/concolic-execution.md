---
title: "Concolic Execution"
tags: [concept, software-analyse, semester-1, testing]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-07-01
prerequisites: [symbolic-execution, control-flow-graph]
---

## One-line Summary
Concolic execution (concrete + symbolic) combines real program execution with symbolic constraint collection, systematically exploring feasible paths by negating constraints and solving for new inputs.

## Core Intuition
Pure symbolic execution explores all paths but wastes time on infeasible ones (constraints that can't be satisfied). Pure random testing only covers what you happen to test. Concolic execution gets the best of both: execute the program with real inputs (concrete execution) while simultaneously tracking symbolic constraints. After each run, negate the last constraint to force a different path, solve for new inputs, and repeat. This guarantees you only explore feasible paths (because you just executed them) while systematically covering all reachable code.

## Formal Definition / Statement
**Algorithm:**
1. Generate random concrete input
2. Execute program concretely, collecting symbolic path constraints
3. Select a constraint to negate (typically the last branch)
4. Solve negated constraint for new concrete input
5. If satisfiable, execute with new input; repeat from step 2
6. If unsatisfiable, try next constraint
7. Continue until all paths covered or resources exhausted

**Key insight**: concrete execution ensures feasibility; symbolic tracking enables systematic exploration

## Key Properties / Complexity
- **Feasibility**: only explores paths that are actually executable (no infeasible paths)
- **Completeness**: covers all reachable paths (given sufficient time/resources)
- **Constraint solving**: still required, but only for feasible constraints
- **Concrete fallback**: when symbolic gets stuck (non-linear), use concrete values
- **Termination**: guaranteed to terminate when all paths covered (finite programs)

## Worked Example
```c
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

**Run 1**: input (x=0, y=0)
- Concrete: w=0, loop doesn't execute, y≥0 so z=1.0
- Symbolic constraints: abs(Y)=0, ¬(Y<0)
- Negate last: Y<0 → unsatisfiable with abs(Y)=0
- Negate previous: abs(Y)≠0 → satisfiable, e.g., Y=1

**Run 2**: input (x=0, y=1)
- Concrete: w=1, loop executes once (z=0, w=0), y≥0 so z=0
- Symbolic constraints: abs(Y)≠0, abs(Y)-1=0, ¬(Y<0)
- Negate last: Y<0 → unsatisfiable with abs(Y)-1=0 and Y≥0
- Negate previous: abs(Y)-1≠0 → satisfiable, e.g., Y=-1

**Run 3**: input (x=0, y=-1)
- Concrete: w=1, loop executes once (z=0, w=0), y<0 so z=1/0=∞
- Symbolic constraints: abs(Y)≠0, abs(Y)-1=0, Y<0
- All paths covered ✓

### Concrete Fallback Example
```c
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

**Solution**: 
- Execute concretely with x=-3: z = -27 + 27 + 9 = 9
- Replace symbolic z with concrete value 9
- Constraint: 9 ≠ y (then branch), 9 = y (else branch)
- Solve 9 = y → y=9
- Execute with (-3, 9): hits abort()

## Common Pitfalls
- **Thinking concolic avoids all path explosion**: it doesn't — still exponential in worst case
- **Forgetting concrete fallback**: when symbolic gets stuck, must use concrete values
- **Confusing with pure symbolic execution**: concolic only explores feasible paths
- **Assuming termination**: concolic terminates only when all paths covered (may not happen for infinite-state programs)
- **Ignoring constraint solver limitations**: non-linear arithmetic, bit-vectors, strings may be undecidable

## Connections
- [[symbolic-execution]] — pure symbolic execution explores all paths (feasible and infeasible)
- [[control-flow-graph]] — CFGs define the paths concolic execution explores
- [[test-generation]] — concolic execution systematically generates test cases
- [[static-vs-dynamic-analysis]] — concolic bridges static reasoning and dynamic testing
- [[path-profiling]] — counts path frequencies; concolic generates inputs for specific paths
- [[software-analyse-lecture-10]] — full lecture treatment with algorithm walkthrough, concrete fallback, and black-box handling

## Open Questions
- How do modern concolic execution tools (KLEE, angr, S2E) handle large programs?
- What's the practical limit for constraint solving in concolic execution?
- How does concolic execution handle concurrency and interleavings?
