---
title: "Fault Localization"
tags: [concept, software-analyse, semester-1, debugging]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-07-01
prerequisites: [dynamic-slicing, program-traces]
---

## One-line Summary
Fault localization ranks program statements by suspiciousness based on which statements are executed by failing tests vs passing tests, narrowing down the likely bug location.

## Core Intuition
When a test fails, the faulty code must have been executed. If a statement is executed by many failing tests but few passing tests, it's likely the bug. Fault localization builds an execution matrix (statements × tests), computes a suspiciousness score for each statement, and ranks them. The developer then inspects the top-ranked statements first, dramatically reducing debugging time.

## Formal Definition / Statement
**Input:**
- Test suite T with passing tests T_pass and failing tests T_fail
- Execution matrix M where M[s][t] = 1 if statement s executed by test t, 0 otherwise

**Output:**
- Ranked list of statements by suspiciousness score

**Suspiciousness formulas:**

**Tarantula:**
```
Susp(s) = (fail(s) / total_fail) / (fail(s) / total_fail + pass(s) / total_pass)
```
where:
- fail(s) = number of failing tests that execute s
- pass(s) = number of passing tests that execute s
- total_fail = total number of failing tests
- total_pass = total number of passing tests

**Ochiai:**
```
Susp(s) = fail(s) / sqrt(total_fail * (fail(s) + pass(s)))
```
Equivalent to cosine similarity between execution vector and error vector.

**Other formulas:** Op2, Barinel, Dstar (variations on the same idea)

## Key Properties / Complexity
- **Precision**: ranks statements, doesn't guarantee finding THE bug
- **Dependence on test suite**: quality of localization depends on test coverage
- **Multiple faults**: may not handle multiple independent bugs well
- **Statement-level**: can be applied at method, class, or line granularity
- **Visualization**: colour-code statements (red = high suspiciousness, green = low)

## Worked Example
```c
int mid(int x, int y, int z) {
    int m;
    m = z;                          // line 3
    if (y < z) {                    // line 4
        if (x < y)                  // line 5
            m = y;                  // line 6
        else if (x < z)             // line 7
            m = y;                  // line 8 (BUG: should be m = x)
    } else {
        if (x > y)                  // line 10
            m = y;                  // line 11
        else if (x > z)             // line 12
            m = x;                  // line 13
    }
    return m;                       // line 15
}
```

**Test suite:**
| Test | Input | Expected | Actual | Result |
|------|-------|----------|--------|--------|
| T1 | mid(3,3,5) | 3 | 3 | Pass |
| T2 | mid(1,2,3) | 2 | 2 | Pass |
| T3 | mid(3,2,1) | 2 | 2 | Pass |
| T4 | mid(5,5,5) | 5 | 5 | Pass |
| T5 | mid(5,3,4) | 4 | 4 | Pass |
| T6 | mid(2,1,3) | 2 | 1 | **Fail** |

**Execution matrix:**
| Statement | T1 | T2 | T3 | T4 | T5 | T6 | fail(s) | pass(s) | Susp (Tarantula) |
|-----------|----|----|----|----|----|----|---------|---------|------------------|
| line 3 (m=z) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | 5 | 0.5 |
| line 4 (if y<z) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | 5 | 0.5 |
| line 5 (if x<y) | ✓ | ✓ | | ✓ | ✓ | | 0 | 3 | 0.63 |
| line 6 (m=y) | ✓ | ✓ | | ✓ | ✓ | | 0 | 3 | 0 |
| line 7 (else if x<z) | | | ✓ | | | ✓ | 1 | 1 | 0.71 |
| line 8 (m=y) | | | ✓ | | | ✓ | 1 | 1 | **0.83** |
| line 10 (if x>y) | | | | ✓ | ✓ | ✓ | 0 | 3 | 0 |
| line 11 (m=y) | | | | ✓ | ✓ | ✓ | 0 | 3 | 0 |
| line 12 (else if x>z) | | | | | | ✓ | 0 | 1 | 0 |
| line 13 (m=x) | | | | | | ✓ | 0 | 1 | 0 |
| line 15 (return m) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | 5 | 0.5 |

**Ranking (by Tarantula suspiciousness):**
1. line 8 (m=y): 0.83 ← **BUG IS HERE**
2. line 7 (else if x<z): 0.71
3. line 5 (if x<y): 0.63
4. line 3, 4, 15: 0.5
5. line 6, 10, 11, 12, 13: 0

**Result**: fault localization correctly identifies line 8 as most suspicious

## Common Pitfalls
- **Thinking it finds THE bug**: it ranks statements, doesn't guarantee finding the actual fault
- **Ignoring test suite quality**: poor test coverage → poor localization
- **Multiple faults**: may not handle multiple independent bugs well
- **Coincidental correctness**: passing tests that execute the bug (mask the fault)
- **Confusing correlation with causation**: high suspiciousness ≠ guaranteed bug
- **Statement vs method level**: statement-level more precise but more expensive

## Connections
- [[dynamic-slicing]] — dynamic slicing identifies statements that affect a specific output; fault localization ranks all statements by suspiciousness
- [[program-traces]] — fault localization requires execution traces from test runs
- [[delta-debugging]] — delta debugging finds minimal failure-inducing input; fault localization finds suspicious statements
- [[testing]] — both require test suites
- [[debugging]] — fault localization is an automated debugging technique

## Open Questions
- How do different suspiciousness formulas (Tarantula vs Ochiai vs Dstar) compare in practice?
- How does fault localization handle multiple independent bugs?
- What's the practical limit for statement-level localization in large codebases?
