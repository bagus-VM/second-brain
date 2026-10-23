---
title: "Vector Clocks"
tags: [concept, dependable-distributed-systems, semester-2, logical-clocks]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-21
prerequisites: ["[[lamport-logical-clocks]]"]
---

## One-line Summary
Lamport's counter tells you that one event might have caused another; the vector version tells you exactly which — and what it costs you in every message.

## Core Intuition

A single Lamport counter compresses the causal history into one number, and in doing so it throws away the *reason* for the order. When two processes compare counters and see $C(a) < C(b)$, they cannot tell whether $a$ actually caused $b$ or whether the two events merely happened to be numbered that way. That missing information is exactly what a distributed system needs in order to detect *conflicting* updates — two writes to the same item that were made concurrently and therefore cannot both be kept.

The fix is to stop compressing. Each process keeps a vector of $N$ counters, one per known process, instead of a single number. The vector records not just "how far along am I" but "how far along is everyone, according to what I have seen". Two vectors compared component by component reveal whether one strictly dominates the other — which means causation — or whether they are incomparable — which means genuine concurrency.

The price is arithmetic and bandwidth. The comparison becomes $O(N)$ instead of $O(1)$, and every message now carries $N$ numbers instead of one. That is a good trade when you need to detect conflicts, and a bad one when you do not.

## Formal Definition / Statement

Independently described by Fidge (1988) and Mattern (1989). Each process $P_i$ holds a local clock that is a **vector of $N$ values**, where $N$ is the number of existing nodes.

- **Initialisation:** every vector starts at the zero vector.
- **Local event on $P_i$:** increment the component belonging to $P_i$:
  $$C_i[i] := C_i[i] + 1$$
- **Send:** the message carries the sender's current vector $t := C_i$.
- **Receive on $P_i$:** increment the own component, then merge component-wise with the received vector:
  $$C_i[i] := C_i[i] + 1$$
  $$\forall k = 1 \dots N:\quad C_i[k] := \max(C_i[k], t[k])$$

**The order relation.** For $t(e_1) = (a_1, \dots, a_n)$ and $t(e_2) = (b_1, \dots, b_n)$:

$$t(e_1) < t(e_2) \iff (\exists i:\ a_i \le b_i) \ \land\ (\exists i:\ a_i < b_i)$$

That is: $e_1$'s vector is component-wise at most $e_2$'s, and strictly less in at least one component. This is exactly the relation "it is possible that $e_1$ happened before $e_2$", and unlike the Lamport case it is an **equivalence** with causality:

$$t(e_1) < t(e_2) \iff e_1 \to e_2$$

The converse of Lamport's one-way implication is what the vector buys.

## Key Properties

- **Exact causal order.** $t(e_1) < t(e_2)$ holds if and only if $e_1 \to e_2$. No false positives, no false negatives.
- **Concurrency is directly visible.** Two events are concurrent exactly when neither vector dominates the other. This is the property Lamport clocks cannot express.
- **Merge is idempotent and commutative.** The component-wise `max` makes the result independent of the order in which messages arrive, so a process's vector does not depend on its delivery schedule.
- **Cost: message overhead.** Every message carries $N$ numbers, so the overhead scales linearly with the number of nodes and "scales poorly for large $N$" — the slide's own words.
- **Cost: comparison.** Determining the order of two events is $O(N)$ rather than $O(1)$.
- **Component-wise dominance is a partial order**, so a total order over vector timestamps is not automatic; the Exercise 2.5 sheet asks precisely how to construct one.

## Worked Example

The Exercise 2.6 diagram, computed mechanically in `logical-clocks.py` (all 175 linear extensions of happens-before give the same assignment, so the result is forced by causality and not by the order in which the events are listed):

| Event | Process | Lamport $C$ | Vector $V$ |
|-------|---------|-------------|------------|
| e1,1 | P1 | 1 | (1, 0, 0) |
| e3,1 | P3 | 1 | (0, 0, 1) |
| e2,1 | P2 | 1 | (0, 1, 0) |
| e1,2 | P1 | 2 | (2, 0, 0) |
| e3,2 | P3 | 2 | (0, 1, 2) |
| e2,2 | P2 | 2 | (0, 2, 0) |
| e1,3 | P1 | 3 | (3, 0, 0) |

The single message $m_1$ goes from e2,1 to e3,2. At e3,2 the receiver increments its own component to 1 and then merges the sender's $(0,1,0)$, giving $(0, 1, 2)$: component 2 is inherited from P2, which is precisely the record of the message that was received.

Note the contrast with the Lamport column. e1,2 has $C = 2$ and e3,2 also has $C = 2$, yet they are not concurrent: the vector distinguishes them, because $(2,0,0)$ and $(0,1,2)$ are incomparable.

## Common Pitfalls

- **Forgetting the merge after the increment.** The receive rule is "increment own component, *then* take the component-wise max with the received vector". Incrementing after the merge loses the record of the incoming message.
- **Expecting a total order.** Vector clocks give a partial order. Exercise 2.5 asks how to extend it, and the answer is not "compare lexicographically" without thought — that is a total order but it is not the causal order.
- **Comparing vectors element-wise instead of component-wise.** The relation requires *all* components to be $\le$ and *at least one* to be $<$. A lexicographic comparison is a different relation and will disagree with causality.
- **Ignoring the $O(N)$ message cost.** The scheme is elegant and the slide says plainly that it "scales poorly for large $N$". A system with thousands of nodes pays for every message.
- **Assuming vector clocks need synchronised physical time.** They do not, like all logical clocks.

## Connections

- [[lamport-logical-clocks]] — the single-counter version this extends; the missing converse is precisely what the vector restores.
- [[clock-synchronization-problem]] — vector clocks sidestep physical time entirely, which is what makes them usable in an asynchronous system.
- [[synchronous-vs-asynchronous-models]] — the model in which vector clocks are useful: no timing assumption, only causal structure.
- [[failure-models]] — under crash-recovery, the recovered process's vector must be reconstructed, and a stale vector silently breaks the causal order.
- [[dependable-distributed-systems-exercise-2]] — Exercise 2.5 and 2.6 are exactly the vector-clock exercise, with the computed answer.

## Open Questions

- The slides do not state how a process rebuilds its vector after a crash and restart.
- The number of processes $N$ is stated to be "the number of existing nodes", but membership management — joining nodes, and what happens to the vectors of everyone else when one joins — is not addressed.
- No concrete example of a *conflicting write* detection is given, even though that is the motivation the lecture implies for the extra information.
- The overhead is called out qualitatively ("scales poorly") but no threshold is given at which the vector becomes impractical.
