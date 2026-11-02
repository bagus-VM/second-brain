---
title: "Dependable Distributed Systems — Exercise 4: Broadcast Semantics and Algorithms"
tags: [homework, dependable-distributed-systems, semester-2, broadcast]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-30
prerequisites: ["[[dependable-distributed-systems-lecture-4]]", "[[synchronous-vs-asynchronous-models]]"]
---

# Exercise 4 (2026-11-04) — Broadcast semantics and algorithms

Source: `dds26-exercise04.pdf` (Reiser, WS 2026/27). The sheet's instruction:
**"Prepare answers before the exercise class. In class you will present them."**

All pseudo-code uses the lecture's notation (slide 18 of lecture 4): `Uses:` names the
abstraction below this layer, handlers are `upon event`, and lower layers are invoked with
`trigger`. Every algorithm below is checked property by property against the lecture 4
specification slide (slide 40): Validity, Agreement, Integrity, and the order properties on top.
The one quantitative claim in the sheet (the ∆ bound in 4.2) is derived in full; the diagram
answers in 4.8 state exactly what the sheet's diagrams show, arrow by arrow, so they can be
re-checked against the paper.

---

## 4.1 Stacking the broadcast abstractions

### (a) Reliable broadcast from causal broadcast

`cbcast` is defined as `rbcast` plus the causal order property (lecture 4, slide 30). Anything
`cbcast` delivers, it delivers with all three `rbcast` properties already satisfied. So the
implementation is a pure rename: hand every `RBroadcast` request to the causal layer and hand
every causal delivery up unchanged.

```
Uses: CausalBroadcast (cbcast)

upon event < RBroadcast, m > do:
    trigger < cbcast.CBroadcast, m >;

upon event < cbcast.CDeliver, m > do:
    trigger < RDeliver, m >;
```

Why the properties carry over: Validity, Agreement and Integrity of `cbcast` are exactly the
`rbcast` properties (the specification slide builds every abstraction on the same three), so the
wrapper cannot break them. Causal order is satisfied as well and simply never used. The cost is
the causal bookkeeping (message histories), which `rbcast` does not need; correctness does not
depend on the overhead being useful.

### (b) FIFO broadcast from reliable broadcast

`rbcast` puts no constraint at all on delivery order, so FIFO has to be built on top. The message
format from the lecture already carries `(sender, seq#, data)`; the transformation keeps one
per-sender counter `next[s]` and buffers anything that arrives too early. This is the lecture's
own algorithm (slide 25), reproduced in context:

```
Uses: ReliableBroadcast (rbcast)

upon Init:
    msgSet := ∅;
    next[s] := 1 for each process s;

upon event < FBroadcast, m > do:
    trigger < rbcast.RBroadcast, m >;

upon event < rbcast.RDeliver, m > do:
    s := sender(m);
    if next[s] = seq#(m) then:
        trigger < FDeliver, m >;
        next[s] := next[s] + 1;
        while ∃ m′ ∈ msgSet: sender(m′) = s ∧ seq#(m′) = next[s] do:
            trigger < FDeliver, m′ >;
            msgSet := msgSet \ {m′};
            next[s] := next[s] + 1;
    else:
        msgSet := msgSet ∪ {m};
```

FIFO order: a process delivers m′ from sender s only after delivering every m from s with a
smaller sequence number, because delivery is driven by the `next[s]` counter and the drain loop.
Validity, Agreement, Integrity: inherited from `rbcast`, since every `rbcast` delivery eventually
either triggers a delivery or enters `msgSet`, and the drain loop runs whenever `next[s]`
advances, so a buffered message cannot stay stuck behind a gap (the gap itself must be delivered
first, which advances the counter).

### (c) FIFO broadcast from atomic broadcast

The trap in this part is that total order does **not** imply FIFO order (lecture 4, slide 39 says
so explicitly: "Plain atomic broadcast does *not* necessarily imply FIFO order"). `abcast`
guarantees that all processes deliver in the same order; it does not guarantee that the order
respects each sender's own sending order. The fix is the same per-sender transformation as in
(b), run on top of the atomic deliveries:

```
Uses: AtomicBroadcast (abcast)

upon Init:
    msgSet := ∅;
    next[s] := 1 for each process s;

upon event < FBroadcast, m > do:
    trigger < abcast.ABroadcast, m >;

upon event < abcast.ADeliver, m > do:
    s := sender(m);
    if next[s] = seq#(m) then:
        trigger < FDeliver, m >;
        next[s] := next[s] + 1;
        while ∃ m′ ∈ msgSet: sender(m′) = s ∧ seq#(m′) = next[s] do:
            trigger < FDeliver, m′ >;
            msgSet := msgSet \ {m′};
            next[s] := next[s] + 1;
    else:
        msgSet := msgSet ∪ {m};
```

The argument is the one from (b), with one addition: because `abcast` gives total order, every
process sees the same sequence of deliveries, so the per-sender counters advance identically
everywhere and the resulting FIFO order is also consistent across processes (the construction
yields FIFO atomic broadcast, `fabcast` in the lecture's naming, for free).

---

## 4.2 Timed reliable broadcast: the echo algorithm meets ∆ = 2d

**Setup.** Synchronous system, reliable point-to-point links with transmission delay < d, local
computation negligible. The echo algorithm for `rbcast` is the one from lecture 4 (slides 17-18):

```
upon event < RBroadcast, m > do:
    trigger < ppp.Send, self, m >;

upon event < ppp.Receive, m > do:
    if m ∉ delivered then:
        forall p ∈ P do: trigger < ppp.Send, p, m >;
        delivered := delivered ∪ {m};
        trigger < RDeliver, m >;
```

A process delivers on its **first** receipt of m and relays before delivering. The Real-Time
∆-Timeliness property requires: if m is broadcast at real time t, no correct process delivers m
after t + ∆.

**Claim.** The echo algorithm implements timed reliable broadcast with **∆ = 2d**.

**The bound.** Classify every `ppp.Send` of m by who sent it:

1. The broadcaster sends m to itself at time ≈ t (local computation is negligible). Its own
   delivery therefore happens at ≈ t.
2. The broadcaster's relay to all of P goes out at ≈ t, so every correct process that receives it
   does so before t + d, and delivers then (first receipt).
3. Any *other* process that relays does so upon its own first receipt, which by (2) happens
   before t + d (it either received directly from the broadcaster, or, if the broadcaster crashed
   before reaching it, from some process of class 2 that relays before t + d, arriving before
   t + 2d). Its relay therefore arrives before t + 2d, and delivery is on first receipt.

No delivery can happen later than a first receipt, and every first receipt falls in class 2
(before t + d) or class 3 (before t + 2d). The chain cannot grow further: a class-3 relay
recipient has already received the message by t + 2d, so a "class 4" would only re-arrive at
processes that delivered earlier. Hence no correct process delivers after t + 2d: **∆ = 2d**.

**The rest of the specification.** Timed reliable broadcast is `rbcast` plus timeliness, so the
`rbcast` properties must hold as well. Validity: a correct broadcaster's own delivery is the
self-send of step 1. Integrity: the `delivered` set admits one delivery per message. Agreement:
if a correct process p delivers m, then p triggered `ppp.Send` to **all** of P before delivering
(the relay precedes the delivery in the handler), p is correct and completes those sends, and
perfect links deliver every sent message; every correct process therefore receives m and, on
first receipt, delivers it. Note the argument never needs the broadcaster to be correct, which is
exactly why the algorithm survives the broadcaster crashing mid-relay: the copies it already sent
arrive, their recipients relay, and the bound of step 3 covers the rest.

So under the synchronous-system assumption the echo algorithm satisfies Real-Time
∆-Timeliness with ∆ = 2d, and timed reliable broadcast is implemented.

---

## 4.3 Uniform reliable broadcast

The difference that matters: plain Agreement lets a *faulty* process deliver a message that no
correct process ever delivers. Uniform Agreement closes that: if **any** process (correct or not)
delivers m, then every correct process delivers m. The echo algorithm of 4.2 does not provide
this (a process delivers on first receipt and may crash immediately after), so delivery must wait
until the message is beyond the reach of any crash.

### Main answer: with fail-stop failure detection

The model gives a `FAILED(Pᵢ)` event whenever Pᵢ crashes, and every correct process is notified.
Deliver m only when every process that has **not** crashed has relayed m:

```
Uses: PerfectPointToPointLink (ppp)

upon Init:
    delivered := ∅;
    relayed  := ∅;      /* messages this process has relayed */
    acks[m]  := ∅;      /* processes from which m was received */
    crashed  := ∅;

upon event < URBroadcast, m > do:
    trigger < ppp.Send, self, m >;

upon event < ppp.Receive, m > do:
    acks[m] := acks[m] ∪ {sender};
    if m ∉ relayed then:
        relayed := relayed ∪ {m};
        forall p ∈ P do: trigger < ppp.Send, p, m >;
    tryDeliver(m);

upon event < FAILED, Pᵢ > do:
    crashed := crashed ∪ {Pᵢ};
    forall m ∈ relayed do: tryDeliver(m);

procedure tryDeliver(m):
    if m ∉ delivered ∧ (P \ crashed) ⊆ acks[m] then:
        delivered := delivered ∪ {m};
        trigger < URDeliver, m >;
```

**Uniform Agreement.** Suppose any process q delivers m. The delivery condition says every
non-crashed process was in `acks[m]` at that moment; in particular every correct process had
received and relayed m, and each of them (being correct) completed its relay to all of P. Perfect
links then deliver m to every correct process, each of which relays it and, once all non-crashed
processes appear in its `acks[m]` (the crashed ones are removed by `FAILED`, which fail-stop
guarantees), delivers it. So all correct processes deliver m.

**Validity.** A correct broadcaster delivers once it has heard back from all other correct
processes, which happens because they all relay upon first receipt.

**Integrity.** One delivery per message via `delivered`; a message is only relayed and acked after
someone actually sent it.

### Optional: without reliable failure detection

The lecture states (slide 21, without proof) that uniform reliable broadcast is impossible in an
asynchronous system with an arbitrary number of faulty processes, and that solutions exist when a
majority of processes is correct. The majority version needs a known fault bound f with n > 2f:

```
upon Init:
    delivered := ∅; relayed := ∅; acks[m] := ∅;

upon event < URBroadcast, m > do:
    trigger < ppp.Send, self, m >;

upon event < ppp.Receive, m > do:
    acks[m] := acks[m] ∪ {sender};
    if m ∉ relayed then:
        relayed := relayed ∪ {m};
        forall p ∈ P do: trigger < ppp.Send, p, m >;
    if |acks[m]| ≥ n − f ∧ m ∉ delivered then:
        delivered := delivered ∪ {m};
        trigger < URDeliver, m >;
```

Deliver when m has been received from n − f **distinct** processes. The uniformity argument has
two steps:

1. If any process q delivers m, then q received m from n − f distinct processes, of which at
   least n − 2f are correct (at most f of all processes are faulty), and n − 2f ≥ 1 because
   f < n/2. So at least one correct process relayed m to all of P.
2. Every correct process therefore receives m, relays it (first receipt), and now every correct
   process receives m from **all** correct processes, of which there are at least n − f_actual ≥
   n − f. Its own threshold n − f is met, and it delivers.

So a delivery by a faulty process still forces delivery at all correct processes: Uniform
Agreement holds. Validity and Integrity carry over as before. What the majority buys is step 1's
"at least one correct sender"; with an unbounded number of crashes no such guarantee exists,
which is the impossibility the slide refers to.

---

## 4.4 Atomic broadcast without crashes

Atomic broadcast = `rbcast` + Total Order. The lecture notes (slide 38) that no deterministic
algorithm solves atomic broadcast in an asynchronous system *with* crashes; removing crashes is
what makes this task solvable. Without failures, plain perfect links are reliable enough, and a
single sequencer can impose the order:

```
Uses: PerfectPointToPointLink (ppp)
/* process s (wlog P1) is the distinguished sequencer */

upon Init (at every process):
    pending := ∅;  next := 1;
    (sequencer only:) sn := 1;

upon event < ABroadcast, m > do:
    trigger < ppp.Send, s, m >;

upon event < ppp.Receive, m > at sequencer s:
    /* m arrives unsequenced, exactly once, because there are no
       crashes and ppp neither loses nor duplicates messages */
    forall p ∈ P do: trigger < ppp.Send, p, < sn, m > >;
    sn := sn + 1;

upon event < ppp.Receive, < k, m′ > > do:
    pending := pending ∪ { < k, m′ > };
    while < next, m″ > ∈ pending do:
        trigger < ADeliver, m″ >;
        pending := pending \ { < next, m″ > };
        next := next + 1;
```

**Total Order.** The sequencer assigns strictly consecutive sequence numbers, and every process
delivers strictly in increasing `next` order, waiting in `pending` for the missing numbers. Two
correct processes therefore deliver m before m′ if and only if seq(m) < seq(m′): identical
orders.

**Validity.** A correct broadcaster's message reaches the sequencer (perfect links, no crashes),
gets the next number, and comes back to everyone including the broadcaster.

**Agreement.** Every sequenced message reaches every process (ppp, no crashes) and is delivered
once its number arrives.

**Integrity.** No duplication (ppp), one delivery per number via `next`.

Where the crashes would break it: if the sequencer crashes, `sn` stops advancing and nothing is
delivered any more (termination fails); and the one-step delay between "sequencer sent
`<k, m>`" and "k arrives" is exactly the window in which a crashing process could deliver a
message that others never see, which is why the uniform variant needs 4.3's machinery.

---

## 4.5 Causal order without agreement

**Yes, it is possible.** Take the lecture's causal broadcast algorithm (slide 31): every message
carries the list of messages the sender delivered since its own last broadcast, and a process
delivers a message only together with, and after, everything in its history. Run that delivery
logic over **best-effort** broadcast: no relay step, no retransmission, no echo.

Why causal order survives: the property is conditional. It says that if m causally precedes m′,
then no correct process delivers m′ without having delivered m first. The history mechanism
enforces exactly this for every message that actually arrives: a process that receives
`<m₁, …, m_q, m′>` delivers m₁, …, m_q (if it has not already) before m′. If m never arrives at
some process, that process delivers nothing that depends on it except through a later message
that carries m in its history, in which case m is delivered from the history first. The property
is never violated.

Why Agreement fails: best-effort broadcast gives nothing when the sender crashes. Let P₁
best-effort-broadcast m, deliver it to P₂ only, and then crash. P₂ (correct) delivers m. P₁ and
P₃ never receive m, and there is no relay to save them, so P₃ (correct) never delivers m while a
correct process did: Agreement of `rbcast` is violated. Nothing in the causal order property is
touched, because P₃ delivers nothing at all.

This is the general shape the lecture's stack diagram (slide 42) hints at: causal order is an
*ordering* property layered on whatever delivery machinery exists, while Agreement is a
*reliability* property of that machinery. You can have the ordering without the reliability by
keeping the first and dropping the second.

---

## 4.6 Why the sheet's algorithm satisfies Agreement

The algorithm (sheet, task 4.6): on `RBroadcast`, send to self; on `ppp.Receive` of a message not
in `delivered`, relay it to all of P, add it to `delivered`, and trigger `RDeliver`.

The Agreement property: if a message m is delivered by some correct process, then m is eventually
delivered by every correct process.

**The proof has two load-bearing facts, one from the code and one from the link abstraction.**

1. **Relay precedes delivery.** Look at the handler's order of operations: the `forall p ∈ P`
   send loop runs *before* `delivered := delivered ∪ {m}` and before `RDeliver`. So a process
   cannot deliver m without having first triggered a send of m to every process in P. If the
   delivering process p is correct, it completes every one of those sends.
2. **Perfect links deliver everything sent between correct processes.** For each correct process
   q, the message p sent to q arrives eventually. On that arrival, either q has already delivered
   m (done) or m ∉ delivered(q), and the handler runs: q relays, adds, and triggers `RDeliver`.

So "some correct process delivered m" implies "that process sent m to everyone" implies "everyone
receives m" implies "everyone delivers m". The sender's fate is irrelevant to the argument, which
is the point of the exercise: the agreement guarantee is carried entirely by the *first correct
process that delivers*, not by the original broadcaster.

(Integrity, for completeness: the `delivered` set makes the test `m ∉ delivered` fail on any
re-delivery, so each message is delivered at most once per process.)

---

## 4.7 Consensus without faults

Consensus interface (given on the sheet): `<Propose, v>` requests, `<Decide, v>` indicates, with
Termination, Validity, Integrity, Agreement. In an asynchronous system without faults, perfect
links between all n nodes, one distinguished process can collect everything and hand back one
decision:

```
Uses: PerfectPointToPointLink (ppp)
/* d (wlog P1) is the distinguished coordinator */

upon Init (at every process):
    decided := false;

upon event < Propose, v > do:
    trigger < ppp.Send, d, v >;

upon event < ppp.Receive < DECIDE, v > > do:
    if ¬decided then:
        decided := true;
        trigger < Decide, v >;

/* coordinator d only: */
upon Init (at d):
    proposals := ∅;

upon event < ppp.Receive, v > at d:      /* a plain value, not <DECIDE,…> */
    if v ∉ proposals then:
        proposals := proposals ∪ {v};
    if |proposals| = n then:             /* everyone has proposed */
        pick any v* ∈ proposals;         /* e.g. the first value received */
        forall p ∈ P do: trigger < ppp.Send, p, < DECIDE, v* > >;
```

Property check:

- **Termination.** No process crashes and ppp delivers every sent message, so d receives all n
  proposals, sends n decisions, and every decision arrives. Every correct process decides.
- **Validity.** v* is picked from `proposals`, which contains only values that some process
  proposed.
- **Integrity.** The `decided` flag makes the second `<DECIDE>` a no-op, so no process decides
  twice. (d must not also run the propose-handler's decision path on a bare value; the message
  tags keep the two apart.)
- **Agreement.** Every process decides the v* that d distributed; there is only one.

Worth stating in class: everything here leans on "without faults" twice. Termination needs d to
be correct, and the `|proposals| = n` test needs all n processes to be correct. The lecture's
slide 38 remark (atomic broadcast impossible async with a single crash) and the FLP context are
why the sheet restricts the model this way.

---

## 4.8 The four message diagrams

The sheet shows four executions with three processes each. Black arrows are delivered messages,
grey dotted arrows are messages whose destination has crashed, X marks a crash, a self-loop on a
message means the sender delivers its own message. The reading of each diagram that the answers
below rest on is stated explicitly, so it can be checked against the paper.

**What each diagram shows (the reading):**

- **A.** P₁ broadcasts and delivers m₁, then crashes. P₂ receives m₁, broadcasts and delivers m₂;
  P₃ receives m₁ and m₂, then broadcasts and delivers m₃. P₂'s delivery order: m₁, m₂, then m₃
  (m₃ is relayed to P₂ before the diagram ends). P₃'s order: m₁, m₂, m₃. The copies addressed to
  the crashed P₁ are the grey dotted arrows. Correct processes: P₂, P₃.
- **B.** P₁ broadcasts m₁ and crashes immediately; only P₂ receives it. P₂ broadcasts and
  delivers m₂; P₃ receives m₂, broadcasts and delivers m₃, which P₂ also receives. P₃ never
  receives m₁ at all. Correct processes: P₂, P₃.
- **C.** No crashes. P₁ broadcasts m₁; P₂ receives m₁, broadcasts m₂; P₃ receives m₁ and m₂,
  broadcasts m₃ then m₄. All four messages reach all three processes, and every process delivers
  in the order m₁, m₂, m₃, m₄.
- **D.** No crashes. P₁ broadcasts m₁, received by P₂ and P₃. P₃ broadcasts m₂ and then m₃. m₃
  reaches P₁ and P₂ first; m₂'s copy to P₁ is delayed (the long bracket under P₃) and arrives at
  P₁ **after** m₃. So P₁ delivers m₁, m₃, m₂, while P₂ and P₃ deliver m₂ before m₃.

### (a) Best-effort broadcast: A, B, C, D are all valid

Best-effort broadcast asks for Integrity (no message delivered unless broadcast, at most once)
and Validity for correct senders only. In all four diagrams every delivered arrow originates in a
genuine broadcast, nothing is delivered twice, and every broadcast by a process that is still
correct reaches every correct process. The failures that show up are all *permitted* under
best-effort semantics: in B the crashed P₁'s message reaches only one process (Validity says
nothing about faulty senders), in A the crashed P₁ misses m₂ and m₃, and D's odd ordering is not
best-effort's business.

### (b) Total order (abcast): only A and C

Total order: any two correct processes that both deliver m and m′ deliver them in the same order
(and `abcast` includes the `rbcast` properties, so Agreement must hold among correct processes).

- **A ✓.** The correct processes P₂ and P₃ both deliver m₁, m₂, m₃ in exactly that order. P₁
  delivered m₁ and then crashed; Agreement binds only correct processes, so its missing m₂, m₃
  violate nothing. This is the diagram's whole point: a crashed process delivering a message that
  later correct processes also deliver is consistent with `abcast`.
- **B ✗.** P₂ (correct) delivers m₁, P₃ (correct) never does. Agreement of reliable broadcast is
  already violated, and total order never gets a chance.
- **C ✓.** All three processes deliver m₁, m₂, m₃, m₄ in the same order.
- **D ✗.** P₁ delivers m₃ before m₂ while P₂ and P₃ deliver m₂ before m₃. Two correct processes,
  same two messages, different order: Total Order is violated.

### (c) Causal order (cbcast): only A and C

Causal order: if m → m′ (m causally precedes m′), no correct process delivers m′ without having
delivered m first. `cbcast` also includes the `rbcast` properties.

- **A ✓.** The causal chain is m₁ → m₂ → m₃ (each broadcast happened on a process after it
  received the previous message). Both correct processes deliver m₁, m₂, m₃ in that order.
- **B ✗.** m₁ → m₂ → m₃ holds here as well (P₂ received m₁ before broadcasting m₂; P₃ received
  m₂ before broadcasting m₃). P₃ delivers m₃ without ever delivering m₁: the causal order
  property itself is violated, regardless of Agreement.
- **C ✓.** Same chain m₁ → m₂ → m₃ → m₄ (m₃ → m₄ because P₃ broadcasts m₄ after m₃); everyone
  delivers in causal order.
- **D ✗.** Both m₂ and m₃ are broadcast by P₃, m₂ first, so m₂ → m₃ by program order on P₃. P₁
  delivers m₃ before m₂: violation.

### Summary table

| Diagram | best-effort | abcast (total order) | cbcast (causal order) |
|---|---|---|---|
| A | ✓ | ✓ | ✓ |
| B | ✓ | ✗ (Agreement: P₃ misses m₁) | ✗ (causal order and Agreement broken at P₃) |
| C | ✓ | ✓ | ✓ |
| D | ✓ | ✗ (P₁: m₃ < m₂, others m₂ < m₃) | ✗ (m₂ → m₃, but P₁ delivers m₃ first) |

One caution for the class discussion: answer (b) for A depends on the reading that P₂ receives
m₃ before the diagram ends. If the sheet intends P₂ to end without m₃, then A fails Agreement
exactly like B does, and the answer to both (b) and (c) is "C only". The drawing shows an
arrowhead from m₃ landing on P₂'s timeline, which is why A is counted as valid here.
