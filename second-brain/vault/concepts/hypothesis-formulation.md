---
title: "Hypothesis Formulation"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

# Hypothesis Formulation

## One-line Summary
A research hypothesis must be precise, specific, unambiguous, and state its limitations to be testable and reproducible.

## Core Intuition
If a hypothesis is vague ("our system improves performance"), no experiment can definitively confirm or refute it, and no other researcher can reproduce the test. Good formulation is the first step toward reproducibility.

## Formal Definition / Statement
Following Zobel (*Writing for Computer Science*), a good research hypothesis has these properties:
1. **PRECISE** — stated so that two readers interpret it identically.
2. **SPECIFIC** — targets a concrete, measurable outcome.
3. **UNAMBIGUOUS** — no room for multiple interpretations.
4. **States LIMITATIONS** — makes clear what is *not* being claimed.

A bad hypothesis is **LOOSE** (too vague to test) or **CONTRADICTORY** (internally inconsistent).

## Key Properties
| Good | Bad |
|------|-----|
| Precise | Loose |
| Specific | Contradictory |
| Unambiguous | |
| States limitations | |

## Worked Example
- **Bad:** "Our system improves database performance." — Too loose; what metric? What workload? By how much?
- **Good:** "Our system reduces average query latency by at least 20% on TPC-C workloads under high contention." — Specific metric (latency), specific workload (TPC-C), specific threshold (20%), specific condition (high contention).

## Common Pitfalls
- Claiming too broadly ("in most realistic scenarios").
- Not defining what "improvement" means.
- Failing to state what is *not* being claimed (e.g., not claiming lower latency under all conditions).

## Connections
- [[null-and-alternative-hypothesis]] — Formal statistical framing of hypotheses.
- [[p-values]] — How to evaluate evidence for/against a hypothesis.
- [[presenting-experiments]] — How to structure the experiments section that tests the hypothesis.
- [[reproducibility-engineering-lecture-3]] — Part of the lecture on hypotheses.

## Open Questions
- How do you formulate hypotheses for exploratory research where the outcome is unknown?
- What happens when a hypothesis is technically precise but practically untestable due to resource constraints?
