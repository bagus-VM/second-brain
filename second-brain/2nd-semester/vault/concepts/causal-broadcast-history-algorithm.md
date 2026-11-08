---
title: "Causal Broadcast via Message Histories"
tags: [concept, dependable-distributed-systems, semester-2, broadcast, causal-order]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-30
prerequisites: ["[[broadcast-order-semantics]]", "[[vector-clocks]]"]
---

## One-line Summary
Attach to every broadcast the list of messages you delivered since your last one, and deliver a
message only after everything in its history: causal order by construction, paid for in message
size and blocking.

## Core Intuition

A process that is about to broadcast m′ knows exactly which messages causally precede m′: the
ones it has itself delivered since its last broadcast. Writing that list into the message turns
every receiver into a causal-order enforcer. When `<m₁, …, m_q, m′>` arrives, the receiver first
delivers anything in the history it has not yet seen, then m′. No message can overtake its own
causal past, because the past travels inside the message.

## Formal Statement

The simple algorithm (lecture 4, slide 31), built on FIFO broadcast:

```
Uses: FIFO broadcast (fbcast)

upon event Init:
    rcntDeliver := ∅

upon event < CBroadcast, m >:
    trigger < fbcast.FBroadcast, <rcntDeliver || m> >;
    rcntDeliver := ∅;

upon event < fbcast.FDeliver, <m₁, …, m_q> >:
    for i := 1..q:
        if p has not previously executed Cdeliver(mᵢ):
            trigger < Cdeliver, mᵢ >;
            rcntDeliver := rcntDeliver || mᵢ
```

Why the pieces fit:

- **FIFO underneath** already guarantees each sender's messages arrive in order; the history
  handles the cross-process part of causal precedence.
- **The delivery rule** "deliver the history first, then the message, skip what you already
  delivered" makes causal order hold by construction: m′ is delivered only after every message
  that causally precedes it and that the sender knew of.
- **Causal order implies FIFO order**, so the construction delivers a cbcast as required.

The overhead analysis (slide 35): every broadcast carries all locally delivered messages since
the sender's last broadcast, which can be large. The remedy is to send only the IDs of the
messages the new message depends on (the largest ID per process), which is equivalent to labelling
messages with a vector clock. That version is more compact but **blocking**: a process cannot
broadcast until it has learned about everything it causally depends on.

## Key Properties

- **Correctness is structural, not probabilistic**: the history *is* the causal past, so the
  order property does not depend on timing assumptions.
- **The history is reset per broadcast** (`rcntDeliver := ∅` after each send), which keeps
  messages from growing without bound as long as processes broadcast regularly.
- **The algorithm is non-blocking** in its history form (a process can always broadcast, carrying
  whatever it knows) and **blocking** in its vector-clock form (it must wait to know the full
  dependency set). The lecture names this trade explicitly.
- **The ordering logic is separable from the reliability machinery.** Run the same delivery rule
  over best-effort broadcast instead of fbcast and causal order still holds for every message
  that arrives; what disappears is Agreement (exercise 4.5's point).

## Worked Example

The fbcast-vs-cbcast contrast (slides 33-34): P₁ broadcasts m₁; P₂ receives m₁, then broadcasts
m₂. Under plain FIFO, P₃ may deliver m₂ before m₁ (m₂'s broadcast does not follow m₁'s at P₂ in
any FIFO-visible way... m₁ and m₂ have different senders, so FIFO is silent). Causal order is
violated because m₁ → m₂ through P₂. The history algorithm fixes it: P₂'s broadcast of m₂
carries `m₁` in its history, so P₃ delivers m₁ (from the history) before m₂. The slide-34 drawing
shows exactly this: P₃ receives `m1, m2` and delivers m₂ after m₁.

## Common Pitfalls

- **Forgetting the reset** of `rcntDeliver` after each broadcast: histories then grow without
  bound and re-deliver everything repeatedly.
- **Confusing the two variants**: the history form is large but non-blocking; the vector-clock
  form is small but blocking. Calling the history form "the vector-clock algorithm" mixes them up.
- **Assuming causal broadcast needs consensus or a sequencer.** It needs neither; the order comes
  from the senders' own knowledge of their past.
- **Reading "deliver the history first" as re-delivering everything.** The `if not previously
  delivered` test is what makes repeated histories harmless.

## Connections

- [[broadcast-order-semantics]] — the property this algorithm implements.
- [[vector-clocks]] — what the compact variant amounts to.
- [[lamport-logical-clocks]] — the m → m′ relation the history captures.
- [[reliable-broadcast-and-echo-algorithm]] — the reliability layer underneath (or, in exercise
  4.5, deliberately absent).
- [[dependable-distributed-systems-lecture-4]] — slides 29-35.
- [[dependable-distributed-systems-exercise-4]] — task 4.5.

## Open Questions

- The blocking vector-clock variant is described in three bullet points (slide 35) without its
  algorithm; whether it appears with pseudo-code later is not stated.
- The lecture does not quantify the history size for realistic workloads; the overhead claim
  ("considerable") stays qualitative.
