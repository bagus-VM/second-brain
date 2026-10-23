---
title: "Lamport Logical Clocks"
tags: [concept, dependable-distributed-systems, semester-2, logical-clocks]
course: "Dependable Distributed Systems"
source_count: 2
status: current
last_updated: 2026-10-21
prerequisites: ["[[synchronous-vs-asynchronous-models]]"]
---

## One-line Summary
A counter per process that answers "which of these two events came first?" correctly whenever one event could have influenced the other — and refuses to answer when it could not.

## Core Intuition

Physical clocks are useless for ordering events across machines, because every machine has its own drifting clock and synchronising them precisely is the hard problem (see [[clock-synchronization-problem]]). But most questions about event order are not about physical time at all. They are about *causation*: if A sent a message to B, then A happened before B, and no clock is needed to know that — the message itself is the evidence.

Lamport's insight is that only causally related events need to be ordered. Two events on two machines that never communicated have no meaningful order relative to each other, so a clock that manufactures one is inventing information. The algorithm therefore synchronises counters *only at communication points*, where synchronisation is both possible and necessary.

The result is a partial order, not a total one. That is the point, not a limitation: a total order would have to break ties between concurrent events, and every such tie-break is an arbitrary decision the system has no basis for.

## Formal Definition / Statement

Each process $P_i$ holds a local counter $C_i$, initialised to 0. The rules:

| Event | Rule | Timestamp of the event |
|-------|------|------------------------|
| Local action or send by $P_i$ | $C_i := C_i + 1$ | the value after the increment |
| $P_i$ sends message $m$ | $m$ carries $t_m$, the timestamp of the send action | — |
| $P_i$ receives $m$ with timestamp $t_m$ | $C_i := \max(C_i, t_m) + 1$ | the value after the update |

Write $e_1 \to e_2$ for "event $e_2$ depends causally on event $e_1$" (also written $e_1 \rightsquigarrow e_2$ on the slides). The ordering property is:

$$e_1 \to e_2 \implies t(e_1) < t(e_2)$$

and the crucial converse **does not** hold: $t(e_1) < t(e_2) \not\implies e_1 \to e_2$. A smaller timestamp is *evidence of* causation, not *proof of* it. The timestamps induce a partial order over the set of all events.

**Extending to a total order.** The lecture's extension breaks the remaining ties with the process number:

$$(C_i, i) < (C_k, k) \iff C_i < C_k \ \lor\ (C_i = C_k \land i < k)$$

Every event gets a unique tuple, so a total order exists. It is consistent with causality — the extension never contradicts the partial order — but the tie-break between concurrent events is a convention, not a fact.

## Key Properties

- **Causality is respected.** If $e_1 \to e_2$, then $t(e_1) < t(e_2)$, always.
- **Timestamps are not physical time.** They measure causal depth, not elapsed seconds. A process that idles for an hour advances its counter by one.
- **The order is partial.** Concurrent events can share a timestamp; the algorithm is honest about not knowing their order.
- **The algorithm is one-directional.** The $\implies$ holds; the $\Leftarrow$ does not. This is the single most examined property in the sheet.
- **Extending to a total order costs the node ID.** Tuple comparison is lexicographic on $(C_i, i)$ and is cheap.
- **No clock synchronisation is required.** The counters are only ever compared through messages, so skew cannot accumulate.

## Worked Example

The professor's own example (lecture 2, slide 34) has $P_1$ with timestamps 1, 2, 5, 6, 7 and $P_2$ with 3, 4, 5, 6, 7, 8, and three messages: $(2)$ from $P_1$ to $P_2$, $(4)$ and $(6)$ from $P_2$ to $P_1$. The parenthesised number is the timestamp the message carries.

Walking the receive events:
- $P_1$ receives $(4)$ when its own counter is 2, so $C_1 := \max(2, 4) + 1 = 5$.
- $P_1$ receives $(6)$ when its own counter is 6, so $C_1 := \max(6, 6) + 1 = 7$.
- $P_2$ receives $(2)$ when its own counter is 6, so $C_2 := \max(6, 2) + 1 = 7$.

Every printed value satisfies the rule — **except one**. $P_1$'s first event is 1, so $P_1$'s initial counter is 0. $P_2$'s first event is printed as 3, but no message precedes it, so under the same rule it would have to be 1, i.e. $P_2$'s initial counter would be 2. The slide presents both processes side by side without stating that $P_2$ starts at 2. This is checked mechanically in `logical-clocks.py` (function `check_slide_34`).

A second worked example, on the Exercise 2.6 diagram, is computed rather than quoted — see [[dependable-distributed-systems-exercise-2]].

## Common Pitfalls

- **Assuming the converse.** $t(e_1) < t(e_2)$ does not mean $e_1 \to e_2$. Two concurrent events can carry different Lamport timestamps purely because of the order in which the processes happened to increment.
- **Reading the counter as a clock.** A Lamport timestamp is not milliseconds since boot. Comparing a Lamport timestamp against a wall-clock reading is meaningless.
- **Forgetting the `max`.** The receive rule is $\max(C_i, t_m) + 1$, not $t_m + 1$. Dropping the `max` breaks the ordering property whenever the local counter has already run ahead of the message.
- **Believing a total order is a fact.** The $(C_i, i)$ extension orders concurrent events by node number. It is a convention for making the order total, not a discovery.
- **Assuming concurrent events must share a timestamp.** They may differ. Equal timestamps are permitted, not required.

## Connections

- [[vector-clocks]] — the fix for the missing converse: a vector per process recovers the exact causal relation, at the price of message size.
- [[clock-synchronization-problem]] — the problem Lamport clocks are designed to sidestep entirely.
- [[synchronous-vs-asynchronous-models]] — logical clocks work in the fully asynchronous model; no timing assumption is needed.
- [[failure-models]] — under crash-recovery a restarted process must rejoin without breaking the order, which constrains how counters are recovered.
- [[communication-link-models]] — the channel model determines which messages a process ever sees, and therefore which causal edges exist.

## Open Questions

- **The slide's own example is inconsistent with its rule** unless $P_2$ starts at 2. Whether that is a typo, an unstated convention, or a deliberate illustration of a non-zero start is not resolved by the slides.
- The slides do not say what happens to a counter when a process crashes and recovers — whether it resumes from its old value, restarts at 0, or is re-initialised from a peer.
- No cost is given for the counter overflow case: what happens when a 32-bit counter wraps after $2^{32}$ events is not addressed.
- The relationship between Lamport timestamps and real elapsed time is never quantified, so the question of how much clock drift the scheme tolerates before timestamps become useless in practice is left open.
