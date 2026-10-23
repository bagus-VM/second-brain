---
title: "Dependable Distributed Systems — Exercise 2 Overview"
tags: [topic, dependable-distributed-systems, semester-2, exercise]
course: "Dependable Distributed Systems"
source_count: 2
status: current
last_updated: 2026-10-21
prerequisites: ["[[dependable-distributed-systems-lecture-2]]"]
---

## One-line Summary
The sheet where the models become a T/F exercise and the logical clocks become arithmetic: one
trick question about synchrony, five T/F items about models, a four-question causality test
that reverses when you swap Lamport for vector clocks, and a diagram you have to actually
compute.

## Core Map

```
Exercise 2 (21 Oct 2026) — six tasks
│
├── 2.1 Is "no request ever takes more than 1 week" synchronous?
│        -> [[synchronous-vs-asynchronous-models]]
├── 2.2 Models
│   ├── (a) five T/F statements
│   │        -> [[model-accuracy-tractability]] [[failure-models]]
│   └── (b) when are crash-recovery and fail-silent identical?
│            -> [[failure-models]]
├── 2.3 Properties of logical clocks
│   ├── (a) given C(a) < C(b) with LAMPORT: five verdicts
│   └── (b) the same five with VECTOR clocks: all five reverse
│            -> [[lamport-logical-clocks]] [[vector-clocks]]
├── 2.4 Can a crash violate the Lamport ordering property?
│            -> [[lamport-logical-clocks]]
├── 2.5 How to define a total order on vector clocks?
│            -> [[vector-clocks]]
└── 2.6 The diagram: assign Lamport timestamps, total order,
        vector timestamps, total order            [COMPUTED]
         -> [[dependable-distributed-systems-exercise-2]]
```

## The Sheet's Own Framing

> "Prepare answers before the exercise class. In class you will present them."

Same rule as Exercise 1. The preparation is the work; the presentation is the obligation.

## Key Concepts at a Glance

| Page | What the exercise exercises |
|------|------------------------------|
| [[synchronous-vs-asynchronous-models]] | 2.1 — a bound is a bound, however useless; and 2.2(a)'s "non-assumption" reading |
| [[model-accuracy-tractability]] | 2.2(a) — accuracy and tractability are independent; models answer feasibility and cost |
| [[failure-models]] | 2.2(a) and 2.2(b) — the hierarchy, and the case where crash-recovery and fail-silent coincide |
| [[lamport-logical-clocks]] | 2.3(a), 2.4 — the one-way property, and why a crash cannot break it |
| [[vector-clocks]] | 2.3(b), 2.5 — the exact causal order, and the lexicographic total-order construction |
| [[clock-synchronization-problem]] | Why any of this is necessary |

## The Three Computed Results

Everything numeric in this sheet is derived by `logical-clocks.py`, not asserted. The recorded
output is in `output-logical-clocks.txt`.

**The 2.6 diagram**, read out of the PDF's vector geometry (the text layer garbles the labels):

```
P1 :  e1,1 ------> e1,2 --------> e1,3
P2 :  e2,1 --------------> e2,2
P3 :  e3,1 -----------------> e3,2
                     m1  (e2,1 -> e3,2)
```

| Event | Lamport $C$ | Vector $V$ |
|-------|-------------|------------|
| e1,1 | 1 | (1, 0, 0) |
| e3,1 | 1 | (0, 0, 1) |
| e2,1 | 1 | (0, 1, 0) |
| e1,2 | 2 | (2, 0, 0) |
| e3,2 | 2 | (0, 1, 2) |
| e2,2 | 2 | (0, 2, 0) |
| e1,3 | 3 | (3, 0, 0) |

**Total order from the Lamport timestamps** (tuples $(C_k, k)$):

$$e_{1,1} < e_{2,1} < e_{3,1} < e_{1,2} < e_{2,2} < e_{3,2} < e_{1,3}$$

**Total order from the vector timestamps** (lexicographic, per Exercise 2.5):

$$e_{3,1} < e_{2,1} < e_{3,2} < e_{2,2} < e_{1,1} < e_{1,2} < e_{1,3}$$

**The two orders differ, and the script proves both are valid.** It enumerates all **175**
linear extensions of the happens-before relation and finds exactly **1** distinct Lamport
assignment and **1** distinct vector assignment across all of them — so the timestamps are
forced by causality, not by the order the concurrent events happen to be listed in. It also
checks both total orders against every causally related pair.

**16 of the 21 event pairs are concurrent.** e1,2 and e3,2 both carry Lamport timestamp 2, so
the scalar counter cannot tell you that they are *not* concurrent: their vectors (2,0,0) and
(0,1,2) are incomparable, and e2,1 → e3,2 makes them causally related while e1,2 is
concurrent with both.

## The Verdict Reversal in 2.3

This is the sharpest thing on the sheet. The same five questions, asked twice:

| Question | Lamport, $C(a) < C(b)$ | Vector, $V(a) < V(b)$ |
|----------|------------------------|------------------------|
| $a \to b$? | Undecidable | **Certainly true** |
| $b \to a$? | Certainly false | Certainly false |
| a before b in real time? | Undecidable | **Certainly true** |
| b before a in real time? | Undecidable | **Certainly false** |
| a ∥ b (concurrent)? | Undecidable | **Certainly false** |

Three of the five flip, and the reason is a single fact: for Lamport clocks the ordering
property is one-way ($e_1 \to e_2 \Rightarrow t(e_1) < t(e_2)$, converse does not hold), while
for vector clocks it is an equivalence ($t(e_1) < t(e_2) \Leftrightarrow e_1 \to e_2$). That is
the whole justification for the extra $N-1$ numbers in every message.

## Exam-Relevant Points

1. **2.1 is a trick about what "bounded" means.** A week is a bound, so the assumption holds —
   but exploiting a one-week bound buys nothing, and the slide's own value proposition for
   synchrony is that it enables "simpler protocols (complexity), cheaper protocols (overhead)".
2. **2.2(a)'s five T/F items each test a specific misreading**: that accuracy implies
   tractability; that models are about feasibility only and not cost; that "asynchronous" is an
   assumption rather than a non-assumption; that a stronger failure model is free; and that
   synchronous and asynchronous are symmetric.
3. **2.2(b) is the failure-detection problem in disguise.** The models coincide when the
   crashed process never recovers and the system is asynchronous — so nobody can distinguish
   crash from slow, and fail-silent adds nothing.
4. **2.3 is the one-way versus equivalence distinction.** An exam question that gives a Lamport
   timestamp pair and asks about causality has exactly one answer: you cannot know.
5. **2.4's answer is no, with a caveat.** The ordering property is proved by induction over
   program order and message passing, and neither induction step mentions whether another
   process is alive. What a crash *can* destroy is the causal information, not the property.
6. **2.5's construction and 2.6's arithmetic.** Lexicographic comparison of vectors, with the
   node ID as a redundant tie-break, and the demonstration that it extends the causal order.

## Connections

- [[dependable-distributed-systems]] — the course page.
- [[dependable-distributed-systems-lecture-2]] — the lecture this sheet tests.
- [[dependable-distributed-systems-exercise-1]] — the preceding sheet.
- [[lamport-logical-clocks]] and [[vector-clocks]] — the two algorithms the sheet makes you run.
- [[synchronous-vs-asynchronous-models]] — the model distinction behind 2.1.
- [[failure-models]] — the taxonomy behind 2.2.
- [[machine-learning-for-cybersecurity]] — the same weekly "present in class" obligation.

## Open Questions

- The sheet does not say how the presentations are graded, or whether they carry credit.
- 2.6 asks for "a total order" without saying whether the grader expects the one produced by
  the given construction or any linear extension of the causal order — and the two total orders
  in the solution differ, so the question is under-specified in a way that matters.
- The diagram's orientation (time left to right, processes stacked) is the reverse of the
  time-space diagram in lecture 2. Whether that is deliberate is not stated.
- In 2.1, whether the bound is meant to cover the whole system or only the one server changes
  the answer, and the statement does not say which is meant.
- The course's own slide 34 example does not satisfy the rule printed on slide 33, and this
  sheet asks students to apply that rule. The discrepancy is computed in `logical-clocks.py`
  but is not addressed anywhere in the slides.
