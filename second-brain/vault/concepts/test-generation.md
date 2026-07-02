---
title: Test Generation
tags:
  - concept
  - software-analyse
  - semester-1
  - testing
  - symbolic-execution
course: Software Analyse
source: software-analyse-lecture-10
source_count: 1
status: current
last_updated: 2026-07-02
---

## One-line Summary

Test generation creates concrete input values that exercise specific program paths, primarily through symbolic execution and constraint solving.

## Core Intuition

Manual test writing is labour-intensive and often misses edge cases. Test generation automates this by reasoning about the program's control flow: for each branch point, ask "what input would make the program take this branch?" Symbolic execution answers this question by replacing concrete values with symbolic variables, collecting constraints along each path, and using a solver to find concrete inputs that satisfy those constraints.

## Formal Definition / Statement

In symbolic-execution-based test generation, the process has three steps:

1. **Path selection** — choose a path $\pi$ through the [[control-flow-graph]] of the program
2. **Path condition construction** — derive the path condition $PC(\pi)$, a first-order Boolean formula describing the branch decisions along $\pi$
3. **Constraint solving** — use an SMT solver to find a satisfying assignment for $PC(\pi)$; each solution produces a concrete test input

Formally, if $\pi$ is a sequence of branches $(b_1, b_2, \ldots, b_k)$ where each $b_i$ guards a condition $c_i$, then:
$$PC(\pi) = \bigwedge_{i=1}^{k} \begin{cases} c_i & \text{if } b_i \text{ takes the true branch} \\ \neg c_i & \text{if } b_i \text{ takes the false branch} \end{cases}$$

A satisfying assignment $\sigma \models PC(\pi)$ gives concrete values for the program's inputs that force execution along $\pi$.

## Key Properties

- **Path explosion** — programs with loops or nested conditionals have exponentially many paths, making exhaustive exploration infeasible
- **Constraint complexity** — some path conditions involve non-linear arithmetic, floating-point operations, or string manipulations that are undecidable or expensive for solvers
- **Implicit checks** — constraint solvers automatically generate path conditions for implicit failure points: division by zero, null dereference, array index out of bounds
- **Soundness** — if the solver returns a satisfying assignment, the corresponding concrete input is guaranteed to exercise the specified path (modulo environment modelling)
- **Incompleteness** — the solver may return "unsatisfiable" even when a path is feasible, due to over-approximation or solver timeouts

## Worked Example

```python
def f(x, y):
    if x > 10:           # c1
        if y < x:        # c2
            return 1
    return 0
```

**Target path:** `x > 10` (true) → `y < x` (true) → `return 1`

**Path condition:** $PC = (x > 10) \wedge (y < x)$

**Solver output:** e.g., $x = 11, y = 5$ → concrete test input `(11, 5)` exercises the target path.

To cover all paths, we also need:
- Path `x > 10` (true) → `y < x` (false): $PC = (x > 10) \wedge (y \geq x)$ → e.g., `(11, 11)`
- Path `x > 10` (false): $PC = (x \leq 10)$ → e.g., `(5, 5)`

## Common Pitfalls

- **Ignoring path explosion** — symbolic execution on programs with loops can enumerate infinitely many paths; loop bounding or [[concolic-execution]] is needed
- **Over-trusting the solver** — SMT solvers are powerful but not omnipotent; complex arithmetic or string constraints can cause timeouts
- **Neglecting environment interactions** — file I/O, network calls, and system libraries are difficult to model symbolically
- **Confusing coverage with correctness** — generating inputs that cover all paths does not mean the program is correct; the oracle (expected output) is still needed (see [[testing]])

## Connections

- [[symbolic-execution]] is the core technique — test generation is its primary application
- [[concolic-execution]] (also called DSE — Dynamic Symbolic Execution) addresses path explosion by starting from concrete inputs and systematically negating constraints
- The [[control-flow-graph]] defines the paths that test generation targets
- Generated tests feed into [[testing]] suites, which in turn enable [[fault-localization]] and [[delta-debugging]]
- Practical tools: KLEE (LLVM-based), SAGE (Microsoft, x86 binary), CREST (C programs)

## Open Questions

- How do modern SMT solvers (Z3, CVC5) handle string constraints, and what fragment of string theory is decidable in practice?
- What is the practical path limit before solvers time out on real-world programs, and how does this compare across different constraint types?
