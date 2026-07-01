---
title: "Symbolic Execution"
tags: [concept, software-analyse, semester-1, testing]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-07-01
prerequisites: [control-flow-graph, static-vs-dynamic-analysis]
---

## One-line Summary
Symbolic execution treats program inputs as symbolic variables rather than concrete values, exploring all possible execution paths by building path constraints and solving them to generate test inputs.

## Core Intuition
Instead of running a program with specific inputs and seeing what happens (dynamic analysis) or reasoning about all possible inputs abstractly (static analysis), symbolic execution runs the program with symbolic inputs (like algebra variables). At each branch, it forks execution — one path for the condition being true, one for false. Each path accumulates constraints (e.g., "x > 5 AND y == 0"). A constraint solver then finds concrete inputs that satisfy each path's constraints, generating test cases that cover all paths.

## Formal Definition / Statement
**Symbolic State** at any program point:
- **Symbolic store** (σ): mapping from variables to symbolic expressions (σ ∈ Var ↦ Sym)
- **Path constraint** (φ): first-order Boolean formula describing branches taken

State = σ ∧ φ

**Execution rules:**
- **Assignment** (x = expr): updates σ, φ unchanged
- **Conditional** (if cond): forks into two states:
  - Then branch: φ' = φ ∧ cond
  - Else branch: φ' = φ ∧ ¬cond
- **Assert** (assert cond): checks if φ ∧ ¬cond is satisfiable (error if yes)

## Key Properties / Complexity
- **Completeness**: explores all feasible paths (no false negatives)
- **Soundness**: may explore infeasible paths (constraints unsatisfiable)
- **Path explosion**: number of paths grows exponentially with branches
- **Constraint solving**: depends on logic fragment (linear arithmetic decidable, non-linear undecidable)
- **Termination**: unbounded loops cause infinite execution trees

## Worked Example
```c
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

**Path 1**: a=0
- σ = {a↦A, b↦B, x↦1, y↦0}, φ = (A=0)
- Check: 1 - 0 ≠ 0 → true, no error

**Path 2**: a≠0, b≠0
- σ = {a↦A, b↦B, x↦1, y↦4}, φ = (A≠0 ∧ B≠0)
- Check: 1 - 4 ≠ 0 → true, no error

**Path 3**: a≠0, b=0
- σ = {a↦A, b↦B, x↦2(A+B), y↦4}, φ = (A≠0 ∧ B=0)
- Check: 2(A+B) - 4 ≠ 0
- Error if: 2(A+B) - 4 = 0 ∧ A≠0 ∧ B=0
- Solution: A=2, B=0 → assertion fails

**Result**: test case (a=2, b=0) exposes assertion violation

## Common Pitfalls
- **Path explosion**: programs with many branches have exponentially many paths
- **Infeasible paths**: constraints may be unsatisfiable (e.g., x > 5 ∧ x < 3)
- **Loop handling**: unbounded loops cause infinite execution; solutions: bound loops or provide invariants
- **Non-linear constraints**: x² + y² = z² may be undecidable for solvers
- **Opaque functions**: if source unavailable (library calls), symbolic execution impossible
- **Heap/pointer modeling**: symbolic data structures complex to handle
- **Environmental modeling**: system calls, input() require special handling

## Connections
- [[concolic-execution]] — combines concrete and symbolic execution to avoid infeasible paths
- [[control-flow-graph]] — CFGs define the paths symbolic execution explores
- [[static-vs-dynamic-analysis]] — symbolic execution bridges static reasoning and dynamic testing
- [[abstract-interpretation]] — both approximate; symbolic is exact per path, abstract over-approximates
- [[path-profiling]] — counts path frequencies; symbolic execution generates inputs for specific paths
- [[test-generation]] — symbolic execution automatically generates test cases
- [[software-analyse-lecture-10]] — full lecture treatment with concolic execution, Ball-Larus path profiling, and worked examples

## Open Questions
- How do modern SMT solvers (Z3, CVC4) handle the constraint solving in practice?
- What's the practical path explosion limit for real-world symbolic execution tools (KLEE, angr)?
- How does symbolic execution handle concurrency and interleavings?
