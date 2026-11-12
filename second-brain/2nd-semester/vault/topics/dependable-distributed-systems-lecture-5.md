---
title: "Dependable Distributed Systems — Lecture 5 Overview (Byzantine Broadcast, Atomic Broadcast, Consensus)"
tags: [topic, dependable-distributed-systems, semester-2, broadcast, consensus]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-11-10
prerequisites: ["[[dependable-distributed-systems-lecture-4]]", "[[synchronous-vs-asynchronous-models]]"]
---

## One-line Summary
The lecture strengthens broadcast against Byzantine senders, surveys ways to impose total order, defines consensus, and shows that atomic broadcast and consensus can implement each other.

## Core Map

```
Lecture 5 — Broadcast semantics and algorithms (part 2), 2026-11-09
│
├── 1 Byzantine reliable broadcast (slides 3–16)
│   ├── Byzantine sender can send inconsistent values
│   ├── n > 3f; commonly n = 3f + 1
│   ├── echo threshold alone -> same delivered value, but not all-or-nothing
│   └── Bracha protocol: initial → echo → ready → accept
│       └── [[byzantine-reliable-broadcast]]
│
├── 2 Implementing atomic broadcast (slides 17–24)
│   ├── sequencer: UB / UUB / BB
│   ├── token: circulating or on-demand
│   ├── communication history: timestamps and safe-delivery knowledge
│   └── consensus-based: agree on next message or batch
│       └── [[atomic-broadcast]]
│
└── 3 Consensus (slides 25–31)
    ├── properties: termination, agreement, validity, integrity
    ├── variants: uniform agreement/integrity and stronger validity
    ├── atomic broadcast → consensus: decide first delivered proposal
    └── reliable broadcast + multi-consensus → atomic broadcast
        └── [[consensus]]
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[byzantine-reliable-broadcast]] | Echo and ready thresholds provide value agreement and all-or-nothing delivery despite up to `f` Byzantine processes when `n=3f+1`. |
| [[atomic-broadcast]] | Total-order delivery can be implemented with a sequencer, token, communication history, or consensus. |
| [[consensus]] | Processes propose values and correct processes terminate with one common valid decision, at most once. |
| [[broadcast-order-semantics]] | Atomic broadcast adds total order to reliable broadcast; total order does not imply FIFO. |
| [[synchronous-vs-asynchronous-models]] | Without timing bounds, silence cannot distinguish a crash from a slow process. |

## Lecture Structure

**Byzantine reliable broadcast (slides 3–16).** A faulty sender can equivocate. The simple echo-threshold method prevents correct processes from accepting different values, but a faulty sender may still cause some to accept and others to accept nothing. The lecture derives the `n>3f` requirement, presents Toueg's echo threshold, then gives Bracha's two-phase echo/ready protocol. Bracha's ready propagation yields all-or-nothing delivery. Lemma 1 is sketched; Lemmas 2–4 are assigned as an exercise.

**Atomic-broadcast implementation families (slides 17–24).** A sequencer assigns the order (UB forwards payloads, UUB returns a sequence number to the sender, BB numbers a payload already broadcast). Token methods serialize senders but need a way to recover a lost token. Communication-history methods use timestamps and deliver only when earlier messages can be ruled out; asynchronous round-robin blocks if a process crashes. Consensus-based methods decide the next message or batch.

**Consensus and reductions (slides 25–31).** Consensus is defined by termination, agreement, validity, and integrity, followed by uniform variants. Atomic broadcast solves consensus by broadcasting each proposal and deciding the first delivered value. In the reverse direction, reliable broadcast collects candidates while a sequence of multi-consensus instances chooses message sets for deterministic delivery.

## Exam-Relevant Points

- Keep the Bracha thresholds distinct: more than `(n+f)/2` echoes, `f+1` ready messages to relay ready, and `2f+1` ready messages to accept. Under `n=3f+1`, the echo threshold is also `2f+1`.
- The first simple Byzantine echo algorithm is best-effort, not reliable: it may have inconsistent delivery completion when the sender is faulty.
- For consensus, state all four properties and name which assumption each proof uses.
- Atomic broadcast supplies agreement on the *first* delivered proposal via total order; reliable broadcast alone does not.
- In a purely asynchronous system, a timeout is not proof of a crash. Token recovery and timestamp-based safe delivery therefore need more than the basic asynchronous model.
- Know the four atomic-broadcast families and their bottleneck/failure mode.

## Connections

- [[dependable-distributed-systems-lecture-4]] — defines reliable and atomic broadcast and the ordering properties this lecture implements.
- [[dependable-distributed-systems-exercise-5]] — exercises Bracha's proof, consensus, and communication costs.
- [[dependable-distributed-systems-exercise-4]] — first sequencer construction and consensus-without-faults exercise.
- [[reliable-broadcast-and-echo-algorithm]], [[broadcast-order-semantics]] — crash-tolerant base semantics and order guarantees.
- [[failure-models]], [[synchronous-vs-asynchronous-models]] — fault and timing assumptions behind the impossibility remarks.

## Open Questions

- Slides 14–15 leave Bracha Lemmas 2–4 as an exercise; the proof is recorded in the exercise-5 solution.
- The slide states that deterministic atomic broadcast is impossible asynchronously with one crash; the proof is deferred.
- The survey classification does not specify full crash-recovery or Byzantine fault-tolerant implementations for the four families.
- The slides' extracted fractions are split across text lines; threshold notation is transcribed from the displayed equations and cross-checked against `n=3f+1`.