---
title: "Reliable Broadcast and the Echo Algorithm"
tags: [concept, dependable-distributed-systems, semester-2, broadcast]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-30
prerequisites: ["[[distributed-system-properties]]", "[[failure-models]]"]
---

## One-line Summary
Reliable broadcast is best-effort broadcast plus three named properties, and the echo algorithm
achieves it with one rule: relay to everyone before you deliver.

## Core Intuition

Best-effort broadcast (send to all over perfect point-to-point links) has one hole: if the sender
crashes mid-way, some processes get the message and others never do. Reliable broadcast exists to
close that hole, not to order anything. The mechanism that closes it is making every receiver a
relay: the first process to see a message forwards it to all of P before delivering it, so a
message that any correct process has delivered is already beyond the reach of any crash.

## Formal Statement

Messages have the format `m := (sender, seq#, data)`. The specification (lecture 4, slide 16,
definitions quoted from Hadzilacos-Toueg):

- **Validity**: for every correct process p, if p broadcasts m then p eventually delivers m.
- **Agreement**: if some correct process delivers m, then every correct process eventually
  delivers m.
- **Integrity**: every correct process delivers m at most once, and only if the sender(m)
  actually broadcast m.

The echo algorithm (slides 17-18), in the course notation:

```
Uses: PerfectPointToPointLink (ppp)

upon Init: delivered := empty set;

upon event < RBroadcast, m > do:
    trigger < ppp.Send, self, m >;

upon event < ppp.Receive, m > do:
    if (not delivered.contains(m)) then
        forall p in P do: trigger < ppp.Send, p, m >;
        delivered.add(m);
        trigger < RDeliver, m >;
```

A process delivers on its **first** receipt. The correctness sketch (slide 19):

- **Validity**: RBroadcast → ppp.Send(self) → ppp.Receive → RDeliver, within finite time because
  ppp delivers within finite time.
- **Agreement**: a correct process that triggers RDeliver has already triggered `ppp.Send` to
  **all** destinations (the relay precedes the delivery in the handler), so every correct process
  receives the message and, on its first receipt, delivers it. The argument never assumes the
  original sender is correct, which is why the algorithm survives the sender crashing mid-relay.
- **Integrity**: the `delivered` set blocks duplicates; delivery happens only after a
  `ppp.Send` that happens only after `RBroadcast`.

## Key Properties

- **The load-bearing line is the handler's ordering**: relay first, deliver second. Swap the two
  and a process could deliver and crash before relaying, breaking Agreement.
- **Agreement is carried by the first correct deliverer**, not by the sender. This is the point
  exercise 4.6 asks students to explain exactly.
- **rbcast says nothing about order.** Deliveries at different processes can be in completely
  different orders; the order properties are separate add-ons.
- **Uniformity is a separate strengthening.** Plain Agreement tolerates a faulty process
  delivering a message no correct process ever delivers. Uniform Agreement (uniform rbcast)
  forbids it and costs either reliable failure detection (deliver only after every non-crashed
  process has relayed) or a majority of correct processes with a known fault bound f (deliver
  after n − f distinct senders).
- **Timeliness is another optional add-on.** In a synchronous system with link delay < d, the
  echo algorithm delivers every broadcast within ∆ = 2d: the broadcaster's own relay arrives
  within d, and any second-hand relay arrives within 2d.

## Worked Example

The crash-mid-relay case, which is the algorithm's whole test: the broadcaster sends to itself,
relays to P₁ and crashes before reaching P₂. P₁ receives (first receipt), relays to all of P
before delivering, and P₂ therefore gets the message from P₁ even though the sender is gone.
Agreement holds because *some* correct process delivered, and that process did the relaying. If
nobody had delivered yet, the message is simply lost, which Agreement permits.

## Common Pitfalls

- **Believing rbcast orders messages.** It does not; that is what fbcast, cbcast and abcast are
  for.
- **Assuming Agreement needs the sender.** The proof only needs one correct delivering process
  and perfect links.
- **Conflating Agreement and Uniform Agreement.** The echo algorithm satisfies the first, not the
  second: a process delivers on first receipt and may crash immediately after, before anyone else
  has the message.
- **Forgetting the self-send.** The broadcaster delivers through its own `ppp.Send(self)`, which
  is what makes Validity work.

## Connections

- [[safety-and-liveness-properties]] — Agreement and Validity are liveness, Integrity is safety.
- [[broadcast-order-semantics]] — what gets layered on top of rbcast.
- [[synchronous-vs-asynchronous-models]] — the ∆ = 2d bound needs synchrony; uniform rbcast's
  majority condition lives in the asynchronous model.
- [[failure-models]] — which crashes are being survived.
- [[dependable-distributed-systems-exercise-4]] — tasks 4.2, 4.3 and 4.6 are all about this
  algorithm.
- Hadzilacos & Toueg, *A modular approach to fault-tolerant broadcasts and related problems*
  (1994) — the source of the definitions and of Figure 11.

## Open Questions

- The slide marks the impossibility results around uniform rbcast "without proof"; whether the
  course supplies proofs later is not stated.
- The exact delivery condition of the majority-based uniform algorithm (n − f distinct senders)
  is not on the slides; it comes from working out the exercise's optional task.
