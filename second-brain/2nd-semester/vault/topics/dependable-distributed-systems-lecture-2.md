---
title: "Dependable Distributed Systems — Lecture 2 Overview (Models, Time, Logical Clocks)"
tags: [topic, dependable-distributed-systems, semester-2, logical-clocks]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-21
prerequisites: ["[[dependable-distributed-systems-lecture-1]]"]
---

## One-line Summary
One lecture, three movements: what a model is and why you need one that is both faithful and
analysable, the taxonomy of failures and channels you might model, and then time — why
physical clocks cannot order events and what logical clocks do instead.

## Core Map

```
Lecture 2 — Models, time, logical clocks
│
├── Models                                           (slides 3-10)
│   ├── model = simplification; attributes + rules; also called a theory
│   ├── "There is no single correct model"
│   ├── models of the atom: billiard ball -> plum pudding ->
│   │       solar system -> electron cloud
│   ├── accurate AND tractable; feasibility and cost
│   │       -> [[model-accuracy-tractability]]
│   └── distributed systems = processes over narrow-bandwidth,
│           high-latency channels, some processes and channels faulty
│
├── Modelling processes and failures                  (slides 12-21)
│   ├── node/computer/process as synonyms; global state vector;
│   │       atomic local transition; time-space diagram
│   ├── crash, fail-stop, fail-silent, crash-recovery,
│   │       eavesdropping, Byzantine
│   │       -> [[failure-models]]
│   ├── hierarchy of fault classes (RSDP, Cachin et al. 2011):
│   │       Crash inside Omission inside Crash/Recovery inside
│   │       Eavesdropping inside Arbitrary
│   └── DSSA severity: assertive/value vs omissive
│
├── Modelling communication                           (slides 23-24)
│   ├── send queue -> channel -> receive queue -> deliver
│   └── fair-loss / stubborn / perfect / authenticated perfect
│           -> [[communication-link-models]]
│
├── Synchronous vs asynchronous                      (slides 26-31)
│   ├── asynchronous = a non-assumption; every system "is" async
│   ├── synchronous = bounded speeds and delays; enables cheaper protocols
│   │       -> [[synchronous-vs-asynchronous-models]]
│   └── spectrum: partial synchrony, timed-asynchronous, wormholes
│
├── Time and the order of events                     (slides 32-38)
│   ├── make: clock skew, stale binary, silent failure
│   ├── consistent checkpoints; C3: m's effect in S2 but not S1
│   ├── monitoring, debugging, root cause
│   └── physical clocks: offset, frequency error, environment
│           -> [[clock-synchronization-problem]]
│
└── Logical clocks                                    (slides 39-46)
    ├── Lamport: local C=C+1; receive C=max(C,tm)+1
    │       -> [[lamport-logical-clocks]]
    ├── one-way property; partial order; (C_i, i) total-order extension
    └── vector clocks: Fidge 1988, Mattern 1989; exact causal order
            at the cost of N elements per message
            -> [[vector-clocks]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[model-accuracy-tractability]] | Accuracy is easy, tractability is not, and you need both; feasibility and cost are the two questions models answer |
| [[failure-models]] | Six process-failure models and how they nest; the DSSA split into assertive and omissive |
| [[communication-link-models]] | What the channel promises: fair-loss, stubborn, perfect, authenticated perfect |
| [[synchronous-vs-asynchronous-models]] | Asynchronous is a non-assumption, so async algorithms run everywhere; synchrony is a promise that buys cheaper protocols |
| [[clock-synchronization-problem]] | Physical clocks drift in offset and rate, and a checkpoint taken across skewed clocks is a state that never existed |
| [[lamport-logical-clocks]] | One counter per process orders exactly the causally related events, and is honest about the rest |
| [[vector-clocks]] | One counter per process per peer: exact causal order, exact concurrency detection, N numbers per message |

## Lecture Structure

1. **Models** — the atom slides make the point that a model is a simplification chosen for a
   question, and that changing the model changes the answer. The "Good models" slides define
   accuracy and tractability separately and name the two questions: feasibility and cost.
2. **Modelling processes** — node, computer, and process as synonyms; global state as a vector
   of local states that is easy to use in a proof and impossible to observe; atomic local
   transitions; the time-space diagram.
3. **Modelling faulty processes** — the responsibility is assigned to processors or channels; the
   slide's distinction between counting faulty *components* and counting occurrences of faulty
   *behaviour*; the six models; the nested hierarchy of fault classes; the DSSA severity split.
4. **Modelling communication** — send and deliver as runtime calls, and the four link models
   from weakest to strongest.
5. **Synchronous versus asynchronous** — the asymmetry that carries the whole lecture: asserting
   asynchrony is a non-assumption, while asserting synchrony is a real constraint on the
   implementation, and it buys simpler and cheaper protocols.
6. **Time** — the `make` example, the consistent-checkpoint problem with its C3 case, the
   applications (monitoring, debugging, root cause), and why physical clocks cannot be trusted.
7. **Logical clocks** — Lamport's algorithm, the one-way ordering property, the partial order
   and its $(C_i, i)$ extension; then vector clocks, with the exact causal relation and the
   stated cost.

## Exam-Relevant Points

1. **The synchrony asymmetry.** "Postulating that a system is asynchronous is a non-assumption.
   Every system 'is' asynchronous." An async-correct algorithm works everywhere; a
   sync-correct algorithm works only under the promise. Exercise 2.2(a) tests this directly.
2. **The six failure models and the nesting.** The hierarchy is the load-bearing fact:
   Crash ⊂ Omission ⊂ Crash/Recovery ⊂ Eavesdropping ⊂ Arbitrary, so a protocol that tolerates
   a fault class tolerates everything inside it — but not the other way round.
3. **The difference between counting faulty components and counting faulty behaviour.** This
   is the slide's own remark about classical work, and it changes what "$t$-fault tolerant"
   means.
4. **The Lamport property and, above all, its missing converse.** $e_1 \to e_2 \Rightarrow
   t(e_1) < t(e_2)$, and the reverse does not hold. Exercise 2.3(a) is four applications of this
   one asymmetry.
5. **Vector clocks give the equivalence.** $t(e_1) < t(e_2) \Leftrightarrow e_1 \to e_2$, and
   concurrency becomes directly visible. Exercise 2.3(b) is the same four questions with the
   verdicts reversed, and the reason is the whole point of the vector.
6. **The checkpoint inconsistency (C3).** A message whose effect is in one node's checkpoint
   but not another's produces a state that never existed.
7. **The four link models and what each buys.** Perfect links are an assumption; fair-loss is
   "weak but useful"; stubborn links buy guaranteed delivery without spurious messages.
8. **Accuracy versus tractability**, and the two questions models exist to answer: feasibility
   and cost.

## Connections

- [[dependable-distributed-systems]] — the course page.
- [[dependable-distributed-systems-lecture-1]] — the fault-tolerance vocabulary this lecture
  applies to models and time.
- [[dependable-distributed-systems-exercise-2]] — the sheet that tests this lecture, with the
  computed clock assignments.
- [[lamport-logical-clocks]] and [[vector-clocks]] — the two concept pages this lecture exists
  to build toward.
- [[clock-synchronization-problem]] — the motivation for logical clocks.
- [[synchronous-vs-asynchronous-models]] — the model distinction that governs every protocol
  later in the semester.
- [[failure-models]] and [[communication-link-models]] — the assumption sets that the later
  consensus and replication lectures will choose between.

## Open Questions

- The slides promise the models of "partial synchrony", "timed-asynchronous", and "wormholes"
  and defer them with "More details see later lectures" — none is defined here.
- The physical-clock slide names WWV, DCF77, and GPS as reference sources but gives no
  accuracy figures, so the resulting error bound cannot be derived from the material.
- No protocol is given for clock drift *detection* as opposed to correction, and the
  consistency conditions for a general cut are not stated beyond the single C3 example.
- The fault hierarchy is attributed to Cachin et al. 2011, but the slides do not restate the
  precise inclusion relations — the nesting was read from the rendered diagram.
- The DSSA severity slide (assertive/value vs omissive) is a diagram whose full structure is
  not recoverable from the text layer.
- The professor's own Lamport example on slide 34 does not satisfy the rule printed on slide
  33 (his P2 starts at 3 where P1 starts at 1). This is computed and documented in
  `logical-clocks.py`, but the slides do not resolve whether it is a typo or a convention.
