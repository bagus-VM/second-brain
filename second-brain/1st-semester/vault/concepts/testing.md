---
title: Software Testing
tags:
  - concept
  - software-analyse
  - semester-1
  - testing
course: Software Analyse
source: software-analyse-lecture-9, software-analyse-lecture-10
source_count: 1
status: current
last_updated: 2026-07-02
---

## One-line Summary

Software testing validates program behaviour against expected outcomes and provides the oracle that drives dynamic analysis techniques.

## Core Intuition

Testing is the empirical counterpart to formal analysis: you run the program, observe what it does, and check whether it matches expectations. But testing is not an island — it feeds and is fed by analysis. Test results (pass/fail outcomes) are the raw data for [[fault-localization]] and [[delta-debugging]], while [[symbolic-execution]] and [[concolic-execution]] generate new test inputs automatically.

## Formal Definition / Statement

A **test case** is a tuple $(i, o)$ where $i$ is an input and $o$ is the expected output. A **test suite** $S = \{(i_1, o_1), \ldots, (i_n, o_n)\}$ is a set of test cases. A program $P$ **passes** a test case $(i, o)$ iff $P(i) = o$.

**Test coverage** measures the fraction of program structure exercised by a test suite:
- **Statement coverage** — fraction of statements executed
- **Branch coverage** — fraction of branches taken (both true and false)
- **Path coverage** — fraction of feasible execution paths explored

Testing levels:
- **Unit testing** — individual functions or methods in isolation
- **Integration testing** — interactions between modules
- **System testing** — the whole program end-to-end
- **Acceptance testing** — validation against user requirements

## Key Properties / Complexity

- **Oracle problem** — testing requires knowing the expected output, which is not always available
- **Incompleteness** — testing can show the presence of bugs but never their absence (Dijkstra)
- **Coverage-completeness trade-off** — full path coverage is generally infeasible (exponential paths)
- **Bidirectional relationship with analysis** — testing provides data for analysis; analysis generates tests for coverage
- **Fault detection vs coverage** — higher coverage does not guarantee higher fault detection (see Open Questions)

## Worked Example

```python
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x
```

A test suite for statement coverage:
| Input | Expected | Covers |
|-------|----------|--------|
| `5`   | `5`      | `if`-branch (true) |
| `-3`  | `3`      | `else`-branch |

This achieves 100% statement and branch coverage with just 2 test cases. Path coverage is also 100% here since there are only 2 feasible paths.

## Common Pitfalls

- **Confusing coverage with correctness** — 100% branch coverage says nothing about the correctness of the expected outputs
- **Ignoring the oracle problem** — tests are only as good as the assertions that define "correct"
- **Testing only happy paths** — effective testing targets boundary conditions, error handling, and corner cases
- **Over-reliance on manual test writing** — automated [[test-generation]] via [[symbolic-execution]] or [[concolic-execution]] can systematically cover paths humans miss

## Connections

- Test pass/fail results are the input to [[fault-localization]] — statements executed only in failing tests are ranked as suspicious
- [[delta-debugging]] uses test outcomes to determine whether a simplified input still triggers the failure
- [[symbolic-execution]] and [[concolic-execution]] automatically generate test inputs to maximise path coverage
- [[program-slicing]] can reduce test cases by identifying which statements affect a specific output

## Open Questions

- What coverage metric best predicts fault detection in practice — statement, branch, or something more sophisticated like modified condition/decision coverage (MC/DC)?
- How does mutation testing (injecting artificial faults and checking whether tests detect them) relate to these analysis techniques?
