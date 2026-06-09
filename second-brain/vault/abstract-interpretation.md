---
title: "Abstract Interpretation"
tags: [concept, software-analyse, semester-1]
course: "Software Analyse"
source_count: 1
status: current
last_updated: 2026-06-01
prerequisites: [software-analysis, soundness-and-completeness]
---

## One-line Summary
Abstract interpretation replaces concrete program values with simplified abstract representations to make analysis computationally tractable while preserving soundness.

## Core Intuition
You can't track every possible integer value a variable might hold (there are infinitely many). Instead, just track whether it's positive, negative, or zero. You lose precision but gain the ability to actually compute the answer. The trick is designing the abstraction so it's still useful.

## Formal Definition / Statement
Given a concrete domain (e.g., all integers Z), define an abstract domain (e.g., signs {⊖, ⊚, ⊕, ⊤, ⊥}) and an abstraction function:
- abstract(i) = ⊖ if i < 0
- abstract(i) = ⊚ if i == 0
- abstract(i) = ⊕ if i > 0

Define transfer functions over the abstract domain:
- ⊕ + ⊕ = ⊕ (positive + positive = positive)
- ⊕ + ⊖ = ⊤ (positive + negative = unknown)
- {⊕, ⊖, ⊚, ⊤} / ⊚ = ⊥ (anything / zero = undefined)

The abstract domain forms a lattice ordered by:
```
    ⊤ (all ints)
   / | \
  ⊖  ⊚  ⊕
   \ | /
    ⊥ (no ints)
```
Where ⊤ ⊇ {i | i<0} ⊇ {} and similarly for other elements.

## Key Properties
- **Soundness**: if the abstract analysis says "no error," then there's no error in concrete execution
- **Over-approximation**: the abstract result may include values that never occur concretely
- **Decidability**: abstract analysis terminates (finite abstract domain)
- **Usefulness**: even simple abstractions (like sign analysis) can catch real bugs

## Worked Example
```c
a = 5;      // a = ⊕
b = -3;     // b = ⊖
c = a * b;  // c = ⊖ (positive × negative = negative)
d = 0;      // d = ⊚
e = c * d;  // e = ⊚ (anything × zero = zero)
f = 10 / e; // f = ⊥ (division by zero!)
```
The analysis detects a division-by-zero bug by looking for variables mapped to ⊥.

**False positive example:**
```c
a = 5;      // a = ⊕
b = -3;     // b = ⊖
c = a + b;  // c = ⊤ (positive + negative = unknown)
d = 0;      // d = ⊚
e = c - d;  // e = ⊤ (unknown - zero = unknown)
f = 10 / e; // f = ⊤ (no definite error)
```
Here the analysis can't prove safety (c = 2, so e = 2, f = 5) because the abstraction loses the concrete value. This is a deliberate precision/performance tradeoff.

## Common Pitfalls
- Confusing the abstract domain with the concrete domain — ⊤ doesn't mean "all values simultaneously," it means "we don't know which value"
- Assuming more precision is always better — finer abstractions are more expensive
- Forgetting that soundness is relative to the abstraction — if the abstraction is too coarse, you get false positives but never miss real errors
- Thinking abstract interpretation is only about signs — it's a general framework for any property

## Connections
- [[software-analysis]] — abstract interpretation is the mathematical foundation enabling static analysis
- [[soundness-and-completeness]] — abstract interpretation provides the sound over-approximation
- [[static-vs-dynamic-analysis]] — abstract interpretation is the key technique for static analysis
- [[rices-theorem]] — abstract interpretation is how we work around undecidability

## Open Questions
- How do we systematically design good abstractions for arbitrary properties?
- What's the relationship between abstraction precision and computational cost?
- How do modern tools (like Infer, Soot) implement abstract interpretation at scale?
