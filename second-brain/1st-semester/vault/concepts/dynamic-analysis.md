---
title: "Dynamic Analysis"
tags:
  - concept
  - software-analyse
  - semester-1
  - dynamic-analysis
course: Software Analyse
source_count: 1
status: current
last_updated: 2026-07-02
---

## One-line Summary
Dynamic analysis observes actual program executions to collect traces, enabling instrumentation, fault localization, and debugging — trading completeness for precision.

## Core Intuition
Static analysis is conservative: it accounts for all possible executions including infeasible paths. Dynamic analysis runs the program with real inputs and watches what actually happens. This gives precise results (no false positives for observed behaviour) but only covers tested paths. Think of it as the difference between reading a recipe (static analysis) and actually cooking the dish (dynamic analysis) — you learn exactly what happens, but only for the ingredients you used.

## Formal Definition / Statement
Dynamic analysis is the examination of a program by executing it with concrete inputs and observing its runtime behaviour. Formally:

- **Input:** Program $P$, concrete input $I$, instrumentation probe set $S$
- **Execution:** Run $P(I)$, record trace $T = \langle(s_1, v_1), (s_2, v_2), \ldots\rangle$ where $s_i$ is a statement/instruction and $v_i$ is the observed state (variable values, memory, I/O)
- **Analysis:** Apply analysis function $A(T) \rightarrow R$ to extract results $R$

The key tradeoff: static analysis over-approximates (sound but imprecise), dynamic analysis under-approximates (precise but incomplete).

## Key Properties / Complexity
| Property | Detail |
|----------|--------|
| Precision | No false positives for observed behaviour |
| Completeness | Only covers tested execution paths |
| Runtime overhead | Instrumentation slows execution (2x–100x typical) |
| Storage cost | Traces can be hundreds of MB per second |
| Heisenberg effect | Observing the program changes its behaviour |
| Input dependency | Results are only as good as test inputs |
| Reproducibility | Same input → same trace (for deterministic programs) |

**Hierarchy of analysis:**
1. **Static analysis** — conservative over-approximation (all paths)
2. **Dynamic analysis** — observation of actual executions (tested paths)
3. **Formal verification** — mathematical proof of properties (complete)

## Worked Example
```c
1: int x = read_input();
2: int y = 0;
3: if (x > 0) {
4:     y = x * 2;
5: } else {
6:     y = x * -1;
7: }
8: print(y);
```

**Dynamic analysis with input x = 5:**
- Trace: T = ⟨(1, x=5), (2, y=0), (3, true), (4, y=10), (8, y=10)⟩
- Statements 5, 6 never executed — not in trace
- Precise: we know exactly what y was at each point

**Dynamic analysis with input x = -3:**
- Trace: T = ⟨(1, x=-3), (2, y=0), (3, false), (6, y=3), (8, y=3)⟩
- Statements 4 never executed — not in trace

**Combined (multiple inputs):**
- Union of traces covers more code, but never guarantees all paths
- Statement 4 and 6 are covered across both inputs
- If there's a bug only on x = 0, we'll miss it unless we test that input

**Practical application — fault localization:**
Run all tests, record which statements each test executes, compute suspiciousness scores → rank statements most likely to contain the bug.

## Common Pitfalls
- **Assuming completeness**: "All tests pass" ≠ "No bugs" — only tested paths are covered
- **Ignoring storage overhead**: Tracing everything generates enormous data — must sample or filter
- **Heisenberg effect**: Adding print statements or breakpoints changes timing, potentially hiding race conditions
- **Input bias**: Results are only as good as test inputs — random/fuzz testing helps but doesn't guarantee coverage
- **Confusing precision with correctness**: No false positives for observed behaviour, but the observed behaviour may not reveal the bug
- **Overhead in production**: Heavy instrumentation is impractical in production — use sampling profilers instead

## Connections
- [[static-vs-dynamic-analysis]] — dynamic analysis is one side of the analysis spectrum
- [[program-traces]] — dynamic analysis produces and consumes execution traces
- [[fault-localization]] — a primary application of dynamic analysis
- [[delta-debugging]] — another dynamic technique for finding failure-inducing inputs
- [[dynamic-slicing]] — computes input-specific slices from execution traces
- [[aspect-oriented-programming]] — AOP enables non-invasive instrumentation for dynamic analysis
- [[hierarchy-of-analysis]] — dynamic analysis sits between static analysis and formal verification
- [[software-analyse-lecture-9]] — source lecture

## Open Questions
- How do modern profilers (VisualVM, YourKit) implement insertion vs sampling, and what are the tradeoffs?
- What's the practical tradeoff between trace granularity and storage cost?
- Can dynamic analysis be made complete by combining it with symbolic/concolic execution?
- How do you handle non-determinism (threading, I/O) in dynamic analysis?
- Is there a theoretical limit to how much dynamic analysis can infer about untested paths?
