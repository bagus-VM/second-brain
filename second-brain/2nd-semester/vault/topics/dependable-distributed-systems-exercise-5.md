---
title: "Dependable Distributed Systems — Exercise 5: Consensus and Broadcast"
tags: [topic, dependable-distributed-systems, semester-2, exercise, broadcast, consensus]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-11-10
prerequisites: ["[[dependable-distributed-systems-lecture-5]]"]
---

## One-line Summary
Three tasks connect the new consensus and Byzantine-broadcast material: build consensus when nobody fails, prove Bracha's remaining lemmas, and compare the communication costs of atomic-broadcast families.

## Core Map

```
Exercise 5 (discussion 2026-11-11)
│
├── 5.1 Consensus without faults
│   ├── coordinator gathers n proposals and broadcasts one valid choice
│   └── prove termination, agreement, validity, integrity
│       └── [[consensus]]
│
├── 5.2 Bracha reliable broadcast
│   ├── Lemma 2: acceptance implies unique value
│   ├── Lemma 3: one correct acceptor -> all correct accept
│   └── Lemma 4: correct transmitter -> all correct accept
│       └── [[byzantine-reliable-broadcast]]
│
└── 5.3 Atomic-broadcast costs
    ├── UB / UUB / BB sequencer variants
    ├── circulating token: already held vs must travel
    └── communication history: n messages, no fixed asynchronous latency bound
        └── [[atomic-broadcast]]
```

## Key Concepts at a Glance

| Page | What the task exercises |
|------|-------------------------|
| [[consensus]] | A failure-free coordinator algorithm and a property-by-property proof. |
| [[byzantine-reliable-broadcast]] | The threshold intersections and propagation argument behind Bracha's protocol. |
| [[atomic-broadcast]] | The four algorithm families and the difference between messages sent and delivery latency. |
| [[broadcast-order-semantics]] | Why total order is the relevant abstraction for replicas. |
| [[lamport-logical-clocks]] | Timestamp ordering in the communication-history option. |

## Exercise Structure

**5.1 — Failure-free consensus.** The simplest valid construction uses a fixed coordinator: gather all `n` proposals, deterministically select one of them, and broadcast the decision. The protocol terminates because all nodes and links work; waiting for all proposals would be unsafe with crashes, but crashes are excluded here.

**5.2 — Bracha proof.** The exercise fills in the lecture's missing Lemmas 2–4. Lemma 2 intersects two acceptance sets and invokes Lemma 1. Lemma 3 turns one correct acceptor's `2f+1` ready messages into an `f+1` ready trigger at every correct process, then into acceptance. Lemma 4 starts the ready wave with the correct transmitter's `2f+1` correct echoes.

**5.3 — Latency and message complexity.** Under the sheet's explicit cost model, UB is 2 steps and `n+1` messages; UUB is 3 steps and `n+2`; BB is 2 steps and `2n`. A continuously circulating token costs 1 step/`n` messages if already held, or `n` steps/`2n−1` messages in the worst pre-broadcast position. Communication history disseminates one payload in `n` messages, but asynchronous delays give no fixed small delivery bound.

## Exam-Relevant Points

- Distinguish termination from agreement: the failure-free coordinator proof needs eventual delivery and all `n` proposals.
- For Lemma 2, each acceptance set has at least `f+1` correct ready senders; two such subsets among `2f+1` correct processes must intersect.
- For Lemma 3, explain both threshold transitions: `2f+1` at the first acceptor implies `f+1` correct ready senders; propagation then yields `2f+1` ready messages everywhere.
- For Lemma 4, compute the echo threshold under `n=3f+1`: `2f+1 > (n+f)/2`.
- Count each broadcast as `n` unicast messages, as specified; state clearly whether token transfers are included.
- Asynchronous means no known delay upper bound, not that messages never arrive. It removes a fixed safe-delivery deadline.

## Connections

- [[dependable-distributed-systems-lecture-5]] — all definitions and protocols used by this sheet.
- [[dependable-distributed-systems-exercise-4]] — previous sheet's failure-free consensus task and sequencer construction.
- [[byzantine-reliable-broadcast]], [[atomic-broadcast]], [[consensus]] — the three ideas tested directly.
- [[broadcast-order-semantics]], [[lamport-logical-clocks]] — total order and timestamp context.
- `study/homework/dependable-distributed-systems/dds-exercise-05-solution.md` — worked solutions with explicit assumptions and cost counts.

## Open Questions

- The cost model does not state whether self-delivery is discounted; this overview follows its explicit `n`-unicasts broadcast cost.
- The sheet excludes consensus-based atomic broadcast because its cost depends on the underlying consensus algorithm.
- No failure-recovery or token-loss protocol is included in the cost comparison.