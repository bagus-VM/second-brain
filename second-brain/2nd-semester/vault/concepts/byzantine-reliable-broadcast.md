---
title: "Byzantine Reliable Broadcast"
tags: [concept, dependable-distributed-systems, semester-2, broadcast, byzantine-faults]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-11-10
prerequisites: ["[[reliable-broadcast-and-echo-algorithm]]", "[[failure-models]]"]
---

## One-line Summary
Bracha reliable broadcast uses echo and ready votes so Byzantine processes cannot make correct processes deliver different values or leave delivery half-finished.

## Core Intuition
A Byzantine sender can tell different recipients different values. A single echo threshold can stop two values from being accepted, but it cannot guarantee that everyone accepts something when the sender is faulty. Bracha adds a second vote, `ready`: enough echoes start a ready wave, and a smaller relay threshold lets that wave spread even when some processes are silent. The design separates two jobs: uniqueness of the value and all-or-nothing delivery.

## Formal Definition / Statement
Assume `n = 3f + 1`, at most `f` Byzantine processes, and reliable asynchronous links. A process handles one broadcast instance as follows:

1. The transmitter sends `(initial, v)` to all.
2. On the first initial value, or after more than `(n+f)/2` distinct `echo(v)` messages, or after `f+1` `ready(v)` messages, a process sends `echo(v)` to all (only once).
3. After more than `(n+f)/2` distinct `echo(v)` messages, or after `f+1` `ready(v)` messages, it sends `ready(v)` to all (only once).
4. After `2f+1` `ready(v)` messages, it accepts `v`.

The slide's notation prints the echo threshold as `> (n+f)/2`. For `n=3f+1`, the smallest integer meeting it is `2f+1`.

The stated guarantees are: if the transmitter is correct, all correct processes accept its value; if it is faulty, either all correct processes accept the same value or none accepts. The lecture's proof is split into four lemmas: correct processes ready for at most one value; acceptors agree; one correct acceptor causes every correct process eventually to accept; and a correct transmitter's value is accepted by all.

## Key Properties
- **Safety—unique value:** Two sets of `2f+1` ready senders intersect in at least `f+1` processes; at least one is correct, and Lemma 1 prevents that process from readying two values.
- **Liveness—ready relay:** `f+1` ready messages include at least one correct sender; that correct sender's ready eventually reaches all correct processes, and the threshold rule relays it.
- **Correct-sender validity:** At least `n-f=2f+1` correct processes echo the initial value, enough to cross the echo threshold and start the ready wave.
- **Fault bound matters:** `n=3f+1` is the minimum process count used by this protocol for `f` Byzantine faults.
- **Not a consensus algorithm by itself:** It reliably disseminates one transmitter's value; it does not choose a value among arbitrary proposals or totally order many broadcasts.

## Worked Example
Let `f=1`, so `n=4`. Acceptance requires three ready messages, and `f+1=2` ready messages trigger the relay rule. If a correct process accepts `v`, at least two of its three ready senders are correct. Those two correct ready messages reach every correct process. Each correct process then relays `ready(v)` if it has not already done so; the three correct processes therefore provide the three ready messages needed for every correct process to accept `v`.

For uniqueness, two acceptance sets each have three members among four processes, so they overlap in at least two. At least one overlapping sender is correct. It cannot send ready for both `v` and `u`; therefore `v=u`.

## Common Pitfalls
- Do not replace `f+1` with `2f+1`: `f+1` is the relay trigger, while `2f+1` is the acceptance threshold.
- “All correct processes deliver the same value” does not imply they deliver a value at all when the transmitter is faulty; the protocol permits all-or-none.
- A faulty process may send different messages to different recipients. Count distinct senders, not message copies.
- The echo-only threshold algorithm is only Byzantine best-effort broadcast; it lacks Bracha's all-or-nothing guarantee.
- The equations rely on `n=3f+1`; do not transplant the thresholds to a different fault bound without re-deriving them.

## Connections
- [[reliable-broadcast-and-echo-algorithm]] — crash-tolerant echo is the starting point; Byzantine faults require thresholds and a ready phase.
- [[failure-models]] — Byzantine processes may send inconsistent values or remain silent.
- [[safety-and-liveness-properties]] — uniqueness/agreement are safety claims; eventual acceptance is liveness.
- [[dependable-distributed-systems-lecture-5]] — slides 3–16 develop the protocol and its proof.
- [[dependable-distributed-systems-exercise-5]] — tasks 5.2(a–c) ask for the missing proof lemmas.

## Open Questions
- The lecture cites Toueg (1984) for the echo-threshold protocol and Bracha (1984) for reliable broadcast; it does not state whether the proof details beyond Lemma 1 are examinable.
- The slide extraction splits some threshold fractions across lines; the protocol notation is interpreted from the visible threshold formula and its stated `n=3f+1` assumption.