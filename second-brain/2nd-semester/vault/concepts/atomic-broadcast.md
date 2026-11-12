---
title: "Atomic Broadcast: Ordering Messages Across Processes"
tags: [concept, dependable-distributed-systems, semester-2, broadcast]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-11-10
prerequisites: ["[[broadcast-order-semantics]]", "[[reliable-broadcast-and-echo-algorithm]]"]
---

## One-line Summary
Atomic broadcast reliably delivers messages in the same total order at every correct process, but choosing that order is difficult when processes may fail.

## Core Intuition
Replicas must apply the same updates in the same order or their state can diverge. Atomic broadcast adds total order to reliable broadcast. A sequencer is a simple ordering authority, a token gives one process the right to send, communication-history methods delay delivery until earlier messages cannot still arrive, and consensus-based methods agree on the next message or batch. Each moves the ordering problem to a different mechanism; crashes expose the mechanism's weak point.

## Formal Definition / Statement
Atomic broadcast (abcast) combines reliable-broadcast properties with total order:

- **Validity, Agreement, Integrity:** the reliable-broadcast base properties.
- **Total order:** if two correct processes deliver both `m` and `m'`, they deliver them in the same relative order.

The lecture classifies implementations as:

1. **Sequencer-based:** one chosen process assigns order, either forwarding payloads (UB), assigning sequence numbers (UUB), or numbering messages that were already broadcast (BB).
2. **Token-based:** only the token holder may broadcast; the token circulates continuously or is requested on demand.
3. **Communication-history-based:** senders attach physical or logical timestamps; receivers wait until they know no earlier message can still arrive.
4. **Consensus-based:** processes propose the next message or a set of message IDs and use consensus to choose the next ordered item(s).

These are implementation families, not a claim that they have identical fault tolerance or timing guarantees.

## Key Properties
- A sequencer is simple but a bottleneck and a single point of failure unless recovery is added.
- Moving sequence-number work to the sender reduces sequencer load but can increase latency and creates sender-crash questions.
- A token serializes senders, but loss detection needs a timeout or failure detector; in a fully asynchronous system, a slow holder is indistinguishable from a crashed one.
- Communication-history delivery is safe only when the receiver has evidence that an earlier message cannot still arrive. Synchrony can provide a time bound; asynchrony alone cannot.
- Consensus-based ordering reduces the next-order decision to consensus, but does not make consensus free or solve its failure-model limits.
- Total order does not imply FIFO order; these are independent properties in the course's broadcast lattice.

## Worked Example
Suppose processes `P1`, `P2`, and `P3` concurrently broadcast `a` and `b`. A sequencer can assign `a→17` and `b→18`; all replicas deliver `a` then `b`. Another run may assign `b→17` and `a→18`; that is also valid if all correct replicas follow it. The required guarantee is agreement on the chosen order, not that the order matches real-time arrival or causality.

With UUB, the sender first sends its payload to the sequencer, receives a sequence number, then broadcasts the numbered payload. That adds a communication round compared with UB, where the sequencer forwards the payload directly.

## Common Pitfalls
- Do not call a broadcast atomic merely because it is reliable; reliable broadcast alone specifies no ordering.
- Total order is not a promise about real-time order or causal order.
- A token holder crash is not immediately distinguishable from a delayed process in an asynchronous model.
- A fixed sequencer's failure handling is not supplied by the basic classification; do not assume a failover algorithm.
- A message-count comparison must state whether it includes token circulation, retransmissions, or the sequencer's own local delivery.

## Connections
- [[broadcast-order-semantics]] — atomic broadcast is reliable broadcast plus total order; FIFO is independent.
- [[reliable-broadcast-and-echo-algorithm]] — the reliable delivery layer beneath atomic broadcast.
- [[byzantine-reliable-broadcast]] — a Byzantine-safe reliable primitive, distinct from total ordering.
- [[consensus]] — the lecture reduces ordering decisions to consensus.
- [[dependable-distributed-systems-lecture-5]] — source overview of the four algorithm families.
- [[dependable-distributed-systems-exercise-5]] — computes message and latency costs for representative approaches.

## Open Questions
- The lecture names the Défago–Schiper–Urbán taxonomy but does not provide a full fault-tolerant algorithm for any family.
- Failover, duplicate handling, and view changes for sequencers and tokens are not specified in this material.