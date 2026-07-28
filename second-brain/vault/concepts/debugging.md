---
title: Debugging
tags:
  - concept
  - software-analyse
  - semester-1
  - debugging
course: Software Analyse
source: software-analyse-lecture-9
source_count: 1
status: current
last_updated: 2026-07-02
---

## One-line Summary

Debugging is the process of finding and fixing defects, supported by automated techniques like dynamic slicing, fault localization, and delta debugging.

## Core Intuition

The classic debugging question: *"Yesterday my program worked. Today it does not. Why?"* Manual debugging (setting breakpoints, stepping through code) works for small programs but does not scale. Automated debugging techniques address this by systematically narrowing the search space, ranking suspects, and isolating minimal failure-inducing conditions.

## Formal Definition / Statement

Given a program $P$ that produces incorrect output $P(I) \neq O_{expected}$ for some input $I$, debugging seeks to identify the set of statements $S_{fault} \subseteq S_P$ responsible for the incorrect behaviour and produce a correction.

Three key automated techniques form a pipeline:

1. **Dynamic slicing** — given a failing variable $v$ at a failing statement $s$, compute the set of statements that could have influenced $v$'s value at $s$. This reduces the search space. (See [[dynamic-slicing]], [[program-slicing]])
2. **Fault localization** — given execution matrices from passing and failing test runs, rank statements by suspiciousness using formulas like Tarantula or Ochiai. This prioritises where to look. (See [[fault-localization]])
3. **Delta debugging** — given a working input $I_w$ and a failing input $I_f$, binary-search for the minimal change $\Delta$ such that $I_w + \Delta$ still triggers the failure. This isolates the trigger. (See [[delta-debugging]])

## Key Properties / Complexity

- **Pipeline approach** — narrow (slicing) → rank (fault localization) → isolate (delta debugging)
- **Complementary strengths** — slicing reduces code to examine; ranking prioritises within that reduced set; delta debugging identifies the external trigger
- **Automation level** — all three techniques operate on [[program-traces]] with minimal human intervention
- **Effectiveness** — empirical studies show fault localization can place the true fault in the top 10 candidates for many real-world bugs

## Worked Example

Consider a failing test where `result` is wrong:

**Step 1 — Dynamic slicing:**
Starting from the failing output variable `result`, backward-slice through the trace to identify only the 5 out of 200 statements that influenced `result`.

**Step 2 — Fault localization (Tarantula):**
Run 50 tests (49 pass, 1 fail). Build an execution matrix. The formula:
$$susp(s) = \frac{fail(s)/total\_fail}{fail(s)/total\_fail + pass(s)/total\_pass}$$
ranks the 5 sliced statements, placing `line 42` (a division) at the top with suspiciousness 0.95.

**Step 3 — Delta debugging:**
The failing input is `x=10, y=0`. The passing input is `x=10, y=5`. Delta debugging isolates that changing only `y` from `5` to `0` triggers the failure — revealing a division-by-zero bug at line 42.

## Common Pitfalls

- **Assuming automation replaces understanding** — these techniques narrow the search; a human must still understand the code to fix it
- **Ignoring test quality** — fault localization is only as good as the test suite; poor test diversity leads to poor rankings
- **Over-trusting single formulas** — Tarantula, Ochiai, and other formulas have different strengths on different bug types; no single formula dominates
- **Neglecting the Heisenberg effect** — instrumentation for tracing (see [[program-traces]]) can mask timing-dependent bugs

## Connections

- [[dynamic-slicing]] and [[program-slicing]] provide the search-space reduction step
- [[fault-localization]] provides the ranking step (Tarantula, Ochiai formulas)
- [[delta-debugging]] provides the isolation step
- [[program-traces]] are the common substrate — all three techniques operate on recorded execution data
- [[static-vs-dynamic-analysis]] — these debugging techniques are dynamic (trace-based); static analysis can complement them by reasoning about all possible executions

## Open Questions

- How do these automated techniques compare to interactive debuggers (IDE breakpoints, time-travel debugging) in terms of developer productivity?
- What is the human time cost of using automated debugging vs manual debugging, and at what program size does automation become worthwhile?
