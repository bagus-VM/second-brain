---
title: "Dependable Distributed Systems — Exercise 4: Broadcast Semantics and Algorithms"
tags: [topic, dependable-distributed-systems, semester-2, exercise, broadcast]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-30
prerequisites: ["[[dependable-distributed-systems-lecture-4]]"]
---

## One-line Summary
Eight tasks that turn lecture 4's broadcast definitions into working pseudo-code: stack the
abstractions on top of each other, time the echo algorithm, make it uniform, sequence an atomic
broadcast, and read four message diagrams against three different semantics.

## Core Map

```
Exercise 4 (2026-11-04) — prepare answers, present in class
│
├── 4.1 Stacking abstractions
│   ├── (a) rbcast from cbcast: a pure rename, cbcast already contains it
│   ├── (b) fbcast from rbcast: per-sender sequence numbers + buffering
│   └── (c) fbcast from abcast: same transformation; the trap is that
│           total order does not imply FIFO order
│
├── 4.2 Timed reliable broadcast
│   └── prove the echo algorithm delivers within ∆; the bound is 2d
│
├── 4.3 Uniform reliable broadcast
│   ├── main: deliver only after every non-crashed process has relayed
│   │       (uses the FAILED events of the fail-stop model)
│   └── optional: without failure detection, with a majority correct:
│           deliver after n − f distinct senders
│
├── 4.4 Atomic broadcast without crashes
│   └── sequencer assigns consecutive numbers, everyone delivers in
│           number order; solvable only because crashes are excluded
│
├── 4.5 Causal but not reliable
│   └── yes: causal-order delivery logic over best-effort broadcast
│
├── 4.6 Why the sheet's rbcast satisfies Agreement
│   └── relay precedes delivery + perfect links; the sender is irrelevant
│
├── 4.7 Consensus without faults
│   └── coordinator collects n proposals, picks one, sends DECIDE to all
│
└── 4.8 Four message diagrams
    ├── (a) best-effort: all four valid
    ├── (b) total order: A and C
    └── (c) causal order: A and C
```

## Key Concepts at a Glance

| Page | What the task exercises |
|------|------------------------|
| [[reliable-broadcast-and-echo-algorithm]] | Tasks 4.2, 4.3 and 4.6 live inside the echo algorithm and its properties. |
| [[broadcast-order-semantics]] | Task 4.1's stack and task 4.8's three semantics: FIFO, causal, total order, and what implies what. |
| [[causal-broadcast-history-algorithm]] | Task 4.5: the history-carrying delivery rule, minus the reliability machinery. |
| [[safety-and-liveness-properties]] | The vocabulary the whole sheet argues in: which properties are safety, which are liveness. |
| [[synchronous-vs-asynchronous-models]] | The d in 4.2 exists only in the synchronous model; 4.3's optional part lives in the asynchronous one. |

## Task Notes

**4.1** is the specification ladder from lecture 4 in algorithm form. Part (a) looks trivial and
is: `cbcast` = `rbcast` + causal order, so renaming the events implements `rbcast` and pays some
wasted bookkeeping. Parts (b) and (c) are the same transformation (per-sender counters plus a
buffer) applied to two different layers, and the sheet's trap sits in (c): slide 39 states that
plain atomic broadcast does not imply FIFO order, so the transformation is genuinely needed even
on top of `abcast`.

**4.2** is the sheet's one calculation. The echo algorithm delivers on first receipt, and every
first receipt traces back either to the broadcaster's own relay (arrives < d) or to the relay of
a process that received directly (arrives < 2d). So ∆ = 2d, and the Agreement argument never
mentions the sender, which is why a broadcaster crashing mid-relay does not break it.

**4.3** is where uniformity gets expensive. The main answer delays delivery until every
non-crashed process has relayed, using the model's reliable `FAILED` notifications. The optional
part drops the failure detection and pays with an assumption instead: a known bound f with n > 2f,
delivering after n − f distinct senders. The hinge of that proof is that a delivery by anyone
implies at least one correct process relayed, and one correct relay reaches all correct processes.

**4.4** only works because crashes are excluded, and the solution should say so: a sequencer
assigning consecutive numbers gives total order trivially, and the lecture's slide 38 (atomic
broadcast impossible in async with a single crash) is the reason the sheet restricts the model.

**4.5** answers "yes". Causal order is conditional on messages actually being delivered, so the
history mechanism run over best-effort broadcast still satisfies it; what breaks is Agreement,
because nothing relays a message that a crashing sender delivered to only part of the system.

**4.6** is an "explain exactly why" task about two facts: the relay loop runs before the delivery
in the receive handler, and perfect links eventually deliver everything a correct process sends.
Together they turn "some correct process delivered m" into "everyone will".

**4.7** is the model restriction doing the work: with no faults and perfect links, a coordinator
that waits for all n proposals and distributes one decision satisfies all four consensus
properties. The task is easy, and saying *why* it is easy (which assumption carries which
property) is the real content.

**4.8** is diagram reading against definitions. All four diagrams are valid best-effort
executions; only A and C survive total order and causal order. B fails because a correct process
(P₃) misses m₁ entirely; D fails because P₁ delivers m₃ before m₂ while the others deliver m₂
before m₃. The full arrow-by-arrow reading, with one stated uncertainty about diagram A, is in
the homework file.

## Exam-Relevant Points

1. **The specification slide (lecture 4, slide 40) is the answer key for every task.** Each
   algorithm above is checked property by property against Validity, Agreement, Integrity and the
   order properties; an exam answer that names which property does the work scores better than
   one that only shows code.
2. **The layering picture (slide 42) is examinable as a lattice**: FIFO order under causal order
   under nothing, total order on the right, combinations in between. Task 4.1 walks two of its
   edges.
3. **Total order does not imply FIFO** (slide 39). This single sentence is the difference between
   a correct and an incorrect answer to 4.1(c).
4. **∆ = 2d for the echo algorithm**: broadcast relay arrives within d, a second-hand relay
   within 2d, and delivery is on first receipt.
5. **Uniform vs plain Agreement** is a favourite exam distinction: plain Agreement binds only
   correct processes, uniform Agreement binds deliveries by faulty processes too, and uniformity
   costs either reliable failure detection or a majority of correct processes.
6. **The relay-before-delivery ordering** in the echo algorithm's handler is what makes Agreement
   provable; swap the two lines and the proof collapses.
7. **The impossibility remarks** (uniform rbcast with arbitrary crashes, atomic broadcast async
   with one crash) bound what the exercises may ask; both come from lecture 4's own slides.

## Connections

- [[dependable-distributed-systems-lecture-4]] — the lecture this sheet exercises.
- [[dependable-distributed-systems-exercise-3]] — the previous sheet; its CNV discussion is the
  model for "prepare answers, present in class".
- [[reliable-broadcast-and-echo-algorithm]], [[broadcast-order-semantics]],
  [[causal-broadcast-history-algorithm]], [[safety-and-liveness-properties]] — the concept pages
  behind the tasks.
- [[synchronous-vs-asynchronous-models]], [[failure-models]] — the system models the tasks move
  between.
- `study/homework/dependable-distributed-systems/exercise-04-solution.md` — the worked solution,
  with property checks for every algorithm and the diagram reading for 4.8.

## Open Questions

- **Diagram A's answer in 4.8 depends on whether P₂ receives m₃.** The drawing shows an arrowhead
  on P₂'s line from m₃, so A counts as a valid `abcast`/`cbcast` execution; if the sheet intends
  the diagram to end before that delivery, the answers to (b) and (c) shrink to "C only". This is
  worth settling in class.
- **The optional part of 4.3 says "without having reliable failure detection" without naming what
  may be assumed instead.** The answer above uses the lecture's own slide-21 remark (majority of
  processes correct, known f); whether the course wants the f-bound version or a "impossible,
  here is why" answer is not stated.
- **4.4 does not say whether the sequencer may be pre-agreed.** The algorithm above fixes P₁ as
  sequencer; a failure-free leader election would be redundant in a model without crashes.
- **The sheet gives no marks and repeats the standing instruction** (prepare, present in class);
  nothing is submitted.
