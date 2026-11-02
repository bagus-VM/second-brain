---
title: "Broadcast Order Semantics: FIFO, Causal, Total"
tags: [concept, dependable-distributed-systems, semester-2, broadcast]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-30
prerequisites: ["[[reliable-broadcast-and-echo-algorithm]]", "[[lamport-logical-clocks]]"]
---

## One-line Summary
Reliable broadcast orders nothing; FIFO, causal and total order are three independent add-ons,
and the specification slide assembles them into a six-primitive lattice.

## Core Intuition

Reliable broadcast answers "does everyone get the message?", never "in what order?". Two correct
processes can deliver the same set of messages in completely different sequences. The course
defines three order guarantees, each an extra property on top of the rbcast properties, and each
worth having for a different reason: FIFO because senders usually mean it, causal because
receivers reason about cause and effect, total order because replicated state machines need
identical histories.

## Formal Statement

From the lecture's order slide (slide 23) and specification summary (slide 40):

- **FIFO order**: if a process broadcasts m before it broadcasts m′, then no correct process
  delivers m′ unless it has previously delivered m.
- **Causal order**: if the broadcast of m causally precedes the broadcast of m′ (m → m′, the
  happened-before relation of the logical-clock lecture), then no correct process delivers m′
  unless it has previously delivered m.
- **Total order**: if correct processes p and q both deliver messages m and m′, then p delivers m
  before m′ if and only if q delivers m before m′.

And the composition rules (slides 40-42):

```
Reliable broadcast   = Validity + Agreement + Integrity
FIFO broadcast       = Reliable broadcast + FIFO order
Causal broadcast     = Reliable broadcast + Causal order
Atomic broadcast     = Reliable broadcast + Total order
FIFO atomic          = FIFO broadcast + Total order
Causal atomic        = Causal broadcast + Total order
```

Two implications and one non-implication carry the exam weight:

- Causal order **implies** FIFO order (same-process sends are program order, which is a
  happened-before chain).
- Total order implies **neither** FIFO nor causal order. Slide 39 says it directly: "Plain atomic
  broadcast does *not* necessarily imply FIFO order."
- FIFO implies neither causal nor total.

## Key Properties

- **The three order properties constrain different pairs**: FIFO looks at one sender's two
  messages, causal at messages connected by a happened-before chain across processes, total at
  any two messages delivered by two processes. They are independent axes, which is why the
  primitives form a lattice rather than a hierarchy.
- **Total order is about agreement between processes, not about real time or causes**: two
  causally unrelated messages may be delivered in an arbitrary but *common* order.
- **Causal order is the strongest of the three in one direction**: it subsumes FIFO and adds
  cross-process precedence.
- **Implementations differ in cost**: FIFO needs per-sender sequence counters and a buffer;
  causal needs histories or vector clocks; total order needs a sequencer or consensus, and the
  lecture defers that because consensus is impossible async with crashes.

## Worked Example

The rbcast-vs-fbcast contrast (slides 27-28): P₁ broadcasts m₁ then m₂. Under plain rbcast, P₃
may deliver m₂ first. The FIFO transformation (slide 25) fixes this with a per-sender counter
`next[s]`: a message arriving with `seq#(m) > next[s]` goes into `msgSet` and is delivered by the
drain loop only after the gap has been delivered. The same transformation stacked on abcast (not
on rbcast) yields FIFO atomic broadcast, which is exactly exercise 4.1(c), and it is necessary
precisely because abcast alone does not order a single sender's messages.

## Common Pitfalls

- **Assuming total order implies FIFO.** It does not; slide 39 exists to kill this assumption,
  and exercise 4.1(c) tests it.
- **Assuming FIFO implies causal.** Causal precedence can cross processes (m₁ received on P₂
  before P₂ broadcasts m₂); FIFO sees only same-sender pairs.
- **Confusing total order with total ordering of all messages everywhere.** The property binds
  only pairs of messages that two correct processes *both* deliver.
- **Forgetting that all order properties sit on top of rbcast**, so cbcast and abcast inherit
  Agreement; an "ordering" execution where a correct process misses a message satisfies no
  cbcast/abcast definition.

## Connections

- [[reliable-broadcast-and-echo-algorithm]] — the base layer the order properties decorate.
- [[causal-broadcast-history-algorithm]] — the algorithm that implements causal order.
- [[lamport-logical-clocks]], [[vector-clocks]] — the m → m′ relation causal order is phrased in.
- [[dependable-distributed-systems-lecture-4]] — slides 22-28, 36-42.
- [[dependable-distributed-systems-exercise-4]] — tasks 4.1 and 4.8.

## Open Questions

- The lecture presents no total-order algorithm (slide 38 asks "Algorithm?" and defers to later
  lectures); exercise 4.4 fills the gap for the crash-free case only.
- Whether the course examines the full six-primitive lattice or only the three base order
  properties is not stated.
