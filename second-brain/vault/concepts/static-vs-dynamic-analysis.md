---
title: "Static vs Dynamic Analysis"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [software-analysis]
---

## One-line Summary
Static analysis examines code without running it (reasoning about all possible executions); dynamic analysis observes actual program executions.

## Core Intuition
Think of static analysis as reading a recipe and predicting all possible outcomes, while dynamic analysis is actually cooking the dish and tasting it. Static catches more potential issues but may warn about things that never happen; dynamic gives precise results but only for what you actually tested.

## Formal Definition / Statement
**Static analysis** operates on the program source code (or bytecode) without execution. It deduces properties from the code itself. The main challenge: choosing a good abstraction function.

**Dynamic analysis** observes an actual program run — tracing, monitoring, profiling, or debugging. The main challenge: selecting a representative set of test cases.

Key difference in coverage:
- Static: over-approximates — covers all behaviours of P (including impossible ones)
- Dynamic: under-approximates — covers only the behaviours exercised by test cases

## Key Properties / Complexity
| Aspect | Static | Dynamic |
|--------|--------|---------|
| Execution required? | No | Yes |
| Coverage | All possible runs | Only observed runs |
| Soundness | Can be sound (reports all errors) | Only sound for observed runs |
| False positives | Possible | Impossible (facts from real runs) |
| Main challenge | Abstraction function | Test case selection |
| Typical use | Bug finding, verification | Debugging, profiling, testing |

## Worked Example
```python
def foo(a):
    b = -3
    c = a + b
    d = 0
    e = c - d
    f = 10 / e
    return f
```

**Static analysis** (sign analysis): reports that `f` may be ⊥ (undefined) — a potential division by zero. This is a false positive because `c - 0 = c` is never zero for the given inputs.

**Dynamic analysis** with `foo(5)` and `foo(3)`: both return valid results, no error detected. But this doesn't prove the function is safe for all inputs.

## Common Pitfalls
- Thinking static analysis is "better" because it covers more — it trades precision for coverage
- Thinking dynamic analysis is "complete" because it uses real data — it only covers tested paths
- Confusing soundness with completeness — see [[soundness-and-completeness]]
- Forgetting that static analysis results are about *all possible* executions, not just likely ones

## Connections
- [[software-analysis]] — the overarching field
- [[soundness-and-completeness]] — the formal framework for understanding the tradeoff
- [[abstract-interpretation]] — the mathematical foundation enabling static analysis
- [[hierarchy-of-analysis]] — deduction (static) vs observation (dynamic) vs induction (summarising dynamic into static)
- [[code-clones]] — clone detection can be both static (text/token matching) and dynamic

## Open Questions
- Can hybrid approaches (combining static and dynamic) give the best of both worlds?
- How do modern tools like fuzzers blur the line between static and dynamic?
- What role does neural analysis play — is it static, dynamic, or something new?
