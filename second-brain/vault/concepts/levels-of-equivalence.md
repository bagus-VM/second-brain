---
title: "Levels of Equivalence"
tags: [concept, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: []
---

# Levels of Equivalence

## One-line Summary
When comparing computational experiments, different levels of equivalence define what "the same result" means—from byte-for-byte identity to merely observable behavior.

## Core Intuition
Two programs can be "the same" in different ways. Understanding these levels is crucial for reproducibility: when someone claims they reproduced your result, what exactly do they mean?

## Formal Definition / Statement
**For comparing data or program outputs:**
- **Bitwise identity:** Byte-for-byte identical representation. Same MD5 hash. The strongest form.
- **Structural equivalence:** Same content, possibly differing in order or formatting. E.g., two JSON files with the same properties in different order.

**For comparing programs:**
- **Functional equivalence:** Same outputs for the same inputs. The programs compute the same function.
- **Behavioral equivalence:** Same observable behavior under a given observation model (including I/O, timing, side effects). Stronger than functional equivalence.

## Key Properties
| Level | What it checks | Example |
|-------|---------------|---------|
| Bitwise identity | Byte-for-byte identical | Two files with same MD5 hash |
| Structural equivalence | Same content, different format | JSON with same keys, different order |
| Functional equivalence | Same input→output mapping | Java and Python programs producing same results |
| Behavioral equivalence | Same observable behavior | Same output, I/O, timing, side effects |

## Worked Example
- f(x) = x · 2 and g(x) = x + x are **functionally equivalent** (same output for all inputs).
- Two JPEG files with identical MD5 hashes are **bitwise identical**.
- Two XML files with the same entities in different order are **structurally equivalent**.
- A Java and Python program producing identical outputs for all tested inputs are **functionally equivalent** (but we can only confirm this for tested inputs, not all possible inputs).

## Common Pitfalls
- Confusing functional equivalence with bitwise identity.
- Assuming tested inputs prove functional equivalence for all inputs (induction problem).
- Ignoring floating-point differences across platforms (bitwise identity may fail even for "equivalent" programs).
- Treating structural equivalence as sufficient when bitwise identity is needed.

## Connections
- [[computational-reproducibility-in-ml]] — Equivalence levels apply directly to ML reproducibility.
- [[repeat-reproduce-replicate]] — Replication success depends on which equivalence level is expected.
- [[reproducibility-engineering-lecture-3]] — Taught in Lecture 3 of the course.

## Open Questions
- How should floating-point non-determinism be handled when bitwise identity is expected?
- What level of equivalence is "good enough" for publication?
- Can we formally verify functional equivalence for non-trivial programs?
