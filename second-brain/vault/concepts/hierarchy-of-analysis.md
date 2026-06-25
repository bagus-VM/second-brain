---
title: "Hierarchy of Analysis"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [software-analysis]
---

## One-line Summary
Program analysis uses four reasoning paradigms — deduction (static), observation (dynamic), induction (generalizing from runs), and experimentation (isolating causes) — each with different strengths.

## Core Intuition
When you want to understand a program, you can: (1) read the code and reason about it (deduction), (2) run it and watch what happens (observation), (3) run it many times and find patterns (induction), or (4) systematically change inputs to find what causes a bug (experimentation). These four approaches form a hierarchy from abstract to concrete.

## Formal Definition / Statement
**Deduction** — reasoning from the general to the particular:
- Analyzes program code (or abstractions) to deduce what can/cannot happen in concrete runs
- Does NOT require running the program → static analysis
- Example: from the code, deduce that variable x is always positive

**Observation** — inspecting an actual program run:
- Requires execution → dynamic analysis
- Provides actual facts that cannot be denied (unless the observation is flawed)
- Example: tracing, monitoring, profiling, debugging

**Induction** — reasoning from the particular to the general:
- Summarizes multiple program runs into abstractions (invariants)
- Bridges dynamic → static: turns observations into general rules
- Example: "in all observed runs, a < 2054567 || a % 2 == 1"

**Experimentation** — isolating causes of effects:
- Formulates program understanding as a search for causes
- Requires two experiments: one where cause+effect occur, one where neither does
- Cause must precede effect and be a minimal difference
- Example: "buf contains 'a = 0' because format is '%d' but a is a float"

## Key Properties
- Deduction is purely static (no execution needed)
- Observation is purely dynamic (execution required)
- Induction bridges dynamic to static (from concrete runs to general rules)
- Experimentation is systematic testing (not random)
- Each level is useful for different analysis goals

## Worked Example
```c
char* format = "a = %d";
int a = compute_value(); // returns a float
sprintf(buf, format, a);
```

**Deduction**: analyze the code statically — "format expects %d but a might be a float → type mismatch"
**Observation**: run the program — "buf contains 'a = 0' (error!)"
**Induction**: run many times — "a < 2054567 || a % 2 == 1 (invariant)"
**Experimentation**: change format to "%f" — error disappears → "a = %d" is the cause

## Common Pitfalls
- Thinking deduction is always better than observation — deduction may produce false positives
- Thinking observation is always more reliable — it only covers observed runs
- Confusing induction with deduction — induction generalizes from examples, deduction reasons from rules
- Skipping experimentation when debugging — systematic cause isolation is more effective than random tries

## Connections
- [[static-vs-dynamic-analysis]] — deduction = static, observation = dynamic
- [[abstract-interpretation]] — deduction uses abstract interpretations
- [[soundness-and-completeness]] — each paradigm makes different soundness/completeness tradeoffs
- [[software-analysis]] — the overarching framework

## Open Questions
- How do modern tools combine multiple paradigms (e.g., static + dynamic)?
- Can machine learning be seen as a form of induction?
- What's the relationship between experimentation and property-based testing?
