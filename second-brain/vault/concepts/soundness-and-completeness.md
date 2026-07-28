---
title: "Soundness and Completeness"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [software-analysis, rices-theorem]
---

## One-line Summary
Sound analysis reports all errors (but may include false alarms); complete analysis reports only real errors (but may miss some). Due to undecidability, no analysis can be both.

## Core Intuition
Think of a smoke detector. A sound detector goes off for every fire (never misses one) but also goes off when you burn toast (false alarms). A complete detector only goes off for real fires but might miss some smouldering ones. You can't have a detector that catches every fire AND never false alarms — that's the fundamental tradeoff.

## Formal Definition / Statement
Given program P and property φ:

**Sound analysis** (over-approximation):
- If the analysis says "φ holds," then φ definitely holds in all executions
- Reports ALL errors but may report false positives ("false alarms")
- Analogy: superset of actual errors

**Complete analysis** (under-approximation):
- If the analysis says "φ doesn't hold," then φ definitely doesn't hold
- Reports ONLY real errors but may miss some (false negatives)
- Analogy: subset of actual errors

The matrix:
```
                    Sound           Unsound
Complete        Undecidable     Reports only real errors
                                    (may miss some)
Incomplete      Reports all     May miss errors AND
                    errors      report false alarms
                    (may false alarm)
```

**Soundiness**: tools that give up soundness under specific circumstances (e.g., reflection) but achieve few false alarms. They handle the common case correctly.

## Key Properties / Complexity
- Sound + Complete = Undecidable (Rice's theorem)
- Sound + Incomplete = Decidable (most static analysers)
- Unsound + Complete = Decidable (some dynamic analysers)
- Unsound + Incomplete = Decidable (but unreliable)

## Worked Example
Sign analysis of:
```c
a = 5;      // ⊕
b = -3;     // ⊖
c = a + b;  // ⊤ (could be anything)
d = 0;      // ⊚
e = c - d;  // ⊤
f = 10 / e; // ⊤ (no definite error)
```

**Sound analysis**: reports "f might be undefined" — true, because ⊤ includes 0. But actually c = 2, so this is a false positive. The analysis is sound (doesn't miss real errors) but incomplete (reports false alarms).

**Dynamic analysis** with concrete values: sees c = 2, e = 2, f = 5. No error. But only for these specific inputs.

## Common Pitfalls
- Thinking sound means "correct" — **sound means "complete coverage, possible false alarms"**
- Thinking complete means "good" — **complete means "no false alarms, possible missed errors"**
- Forgetting that soundness is relative to the abstraction — if the abstraction is too coarse, you get more false alarms but never miss real bugs
- Confusing soundiness with soundness — soundy tools are NOT sound in the formal sense

## Connections
- [[rices-theorem]] — the fundamental reason why sound + complete is impossible
- [[abstract-interpretation]] — the technique that enables sound (but incomplete) static analysis
- [[static-vs-dynamic-analysis]] — static tends toward soundness, dynamic toward completeness
- [[software-analysis]] — every analysis tool makes a soundness/completeness tradeoff

## Open Questions
- How do modern tools balance soundness and completeness in practice?
- What's the right level of soundiness for industrial use?
- Can probabilistic guarantees (e.g., "95% sound") be formalized?
