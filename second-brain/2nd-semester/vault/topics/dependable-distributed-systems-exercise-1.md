---
title: "Dependable Distributed Systems — Exercise 1 Overview"
tags: [topic, dependable-distributed-systems, semester-2, exercise]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-21
prerequisites: ["[[dependable-distributed-systems-lecture-1]]"]
---

## One-line Summary
Six tasks that turn lecture 1 into something you have to argue: pick the right property, pick
the right attribute, separate dependability from reliability, name the fault, sort the measures,
and defend your own reading of the hard problems.

## Core Map

```
Exercise 1 (14 Oct 2026) — six tasks
│
├── 1.1 Which properties characterize any distributed system?  (T/F x4)
│        -> [[distributed-system-properties]]
├── 1.2 Which attributes are essential for dependability?      (T/F x4)
│        -> [[dependability-attributes]]
├── 1.3 Dependability
│   ├── (a) dependability vs reliability
│   ├── (b) the three attributes and their measures
│   └── (c) availability comparison of system A and system B   [COMPUTED]
│        -> [[dependability-attributes]]
├── 1.4 Errors, failures, faults
│   ├── (a) causal order and definitions
│   ├── (b) the uninitialized C variable
│   └── (c) a second example
│        -> [[fault-error-failure-chain]]
├── 1.5 How to get there: assign four measures to
│        prevention / removal / forecasting / tolerance
│        -> [[ways-towards-dependability]]
└── 1.6 Problems in distributed systems
    ├── (a) the important practical problems, focused on the
    │        algorithmic ones
    └── (b) which interest you, and what should the lecture cover more of
             -> [[model-accuracy-tractability]] [[failure-models]]
```

## The Sheet's Own Framing

> "Prepare answers before the exercise class. In class you will present them."

This is not a practice sheet. The lecture slides state that in the exercise classes the student
"shall try to answer all questions on your own . . . and then present your solutions", so the
preparation and the presentation are both part of the exercise class. This is the same
obligation, in a different shape, as the paper presentation in
[[machine-learning-for-cybersecurity]].

## Key Concepts at a Glance

| Page | What the exercise exercises |
|------|------------------------------|
| [[distributed-system-properties]] | 1.1 — the three absences, and why three of the four options fail |
| [[dependability-attributes]] | 1.2, 1.3 — the three attributes, the metrics, and the availability arithmetic |
| [[fault-error-failure-chain]] | 1.4 — the causal order, the three definitions, and identifying them in an example |
| [[ways-towards-dependability]] | 1.5 — the four approaches and the question each one answers |
| [[failure-models]] | 1.6(a) — the algorithmic problems, and why consensus is the hard one |
| [[model-accuracy-tractability]] | 1.6(a) — why each problem must be answered per model, not globally |

## The Computed Answer

Exercise 1.3(c) is the one arithmetic in the sheet, and it is a trap. System A fails once per
year and takes one day to repair; system B fails once per week and takes one hour to repair.

| | MTBF | MTTR | Availability = MTBF/(MTBF+MTTR) | Downtime |
|---|---|---|---|---|
| **A** | 8760 h | 24 h | **0.997268** | 0.27 % |
| **B** | 168 h | 1 h | **0.994083** | 0.59 % |

**A is more available**, by 0.318 percentage points. The intuitive answer (B, because it repairs
faster) is wrong: A's MTBF is about 52× longer, and although A takes 24× longer to repair, 24
hours is negligible against a 365-day failure interval. Both repair times are dwarfed by their
own failure intervals, so the failure rate decides. Availability is not "how often" but "how
long".

The arithmetic is in `study/homework/dependable-distributed-systems/logical-clocks.py` and its
recorded output.

## The Two Opinion Tasks

1.6 is the only part of the sheet with no unique answer, and it is the part that most rewards
preparation: 1.6(a) asks for the most important practical problems in distributed systems
"especially ... technical problems that should be solved by algorithms", and 1.6(b) asks which of
them interest you and what the lecture should cover more of. The full answer in
`exercise-01-solution.md` argues for consensus and failure detectors (where the three models
meet) and for the time models (the assumption layer under everything later in the semester),
and it explicitly answers the "which problems are not algorithmic" half — administrative cost
and hardware cost are real but are not solved by a distributed algorithm.

## Exam-Relevant Points

1. **The T/F blocks are about categories, not facts.** 1.1 and 1.2 each offer four options of
   which one is right, and in both cases the wrong options fail by mixing a real property of
   distributed systems with something that is not one (scalability, cost-effectiveness) or by
   substituting a neighbouring concept (security, integrity for the dependability attributes).
2. **Dependability is the umbrella, reliability is one attribute inside it.** "The difference"
   in 1.3(a) is scope, not degree.
3. **Availability is a ratio of a reliability metric and a maintainability metric.** It is the
   only one of the three attributes that is not a time.
4. **Fault → error → failure, and the three are three different moments.** The uninitialized
   variable example is the cleanest illustration: the fault is in the source, the error is in
   the register, the failure is the crash.
5. **The four ways towards dependability each answer a different question.** 1.5 is four
   assignments, and a student who has memorised the definitions rather than the questions
   will get at least one wrong.
6. **1.6 tests whether you can distinguish algorithmic problems from organisational ones**, and
   whether you have a defensible position at all.

## Connections

- [[dependable-distributed-systems]] — the course page.
- [[dependable-distributed-systems-lecture-1]] — the lecture this sheet tests.
- [[dependable-distributed-systems-exercise-2]] — the follow-up sheet.
- [[dependable-distributed-systems-lecture-2]] — where the models and the clock material live.
- [[machine-learning-for-cybersecurity]] — the same "present in class" obligation, and the
  same instructor.

## Open Questions

- The sheet does not say how the exercise answers are graded, whether a grade is attached to
  the presentations, or whether participation is mandatory.
- 1.6(b) asks what "you" want to learn more about, so the expected answer is tied to a moment in
  the semester and to the remaining plan.
- Whether the exercise class is recorded, or whether the presented answers are collected, is
  not stated.
- The sheet's 1.6(a) says to consider "the experience you have from other lectures and
  projects, as well as outside of the university" — which invites a personal answer, but the
  course's other three tasks are all objectively checkable. How the two are weighted against
  each other is unknown.
