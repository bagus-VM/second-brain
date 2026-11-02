---
title: "Dependable Distributed Systems — Lecture 4 Overview (Broadcast Semantics and Algorithms)"
tags: [topic, dependable-distributed-systems, semester-2, broadcast]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-30
prerequisites: ["[[dependable-distributed-systems-lecture-2]]", "[[synchronous-vs-asynchronous-models]]"]
---

## One-line Summary
The abstraction-building lecture: what safety and liveness mean, then five broadcast
abstractions (best-effort, reliable, FIFO, causal, atomic) defined by their properties, two
algorithms (the echo algorithm and the history-carrying causal broadcast), and the impossibility
remarks that bound what any of them can promise.

## Core Map

```
Lecture 4 — Broadcast semantics and algorithms (2026-11-02, 43 slides)
│
├── 1 Basics: safety and liveness                    (slides 3-7)
│   ├── safety: something bad never happens; a predicate
│   │       that is always true
│   ├── liveness: something good eventually happens;
│   │       "eventually" = will happen within an unspecified
│   │       but finite time (not the German "eventuell"!)
│   ├── worked example: factorization Fac(n) — termination is
│   │       liveness, output correctness is safety
│   └── verification prefers many minimalistic properties
│       └── → [[safety-and-liveness-properties]]
│
├── 2 Broadcast                                      (slides 8-42)
│   ├── layered architecture: application protocol over
│   │       broadcast algorithm over send/receive interface
│   ├── based on Hadzilacos & Toueg 1994 ("A modular approach
│   │       to fault-tolerant broadcasts", read to p. 16) and
│   │       RSDP (Cachin et al. 2011); definitions in green
│   │       boxes are direct citations
│   │
│   ├── best-effort broadcast (slides 11-13)
│   │       send to all via perfect links; no guarantees if the
│   │       sender crashes
│   │
│   ├── reliable broadcast rbcast (slides 14-19)
│   │   ├── properties: Validity, Agreement, Integrity
│   │   ├── message format m := (sender, seq#, data)
│   │   └── echo algorithm (slides 17-19) + correctness sketch
│   │       └── → [[reliable-broadcast-and-echo-algorithm]]
│   │
│   ├── uniform reliable broadcast (slides 20-21)
│   │   ├── uniform agreement: even a faulty process's delivery
│   │   │       commits all correct processes
│   │   └── impossible async with arbitrary crashes; possible
│   │           synchronous, or async with a majority correct
│   │
│   ├── FIFO / causal / total order (slides 22-28)
│   │   ├── rbcast: no order at all
│   │   ├── FIFO: per-sender order (slide-25 transformation)
│   │   ├── causal: m → m′ respected (slide-31 history algorithm)
│   │   └── total: same order everywhere
│   │       └── → [[broadcast-order-semantics]]
│   │       └── → [[causal-broadcast-history-algorithm]]
│   │
│   ├── atomic broadcast (slides 36-38)
│   │   ├── rbcast + total order
│   │   └── no deterministic algorithm exists async with a
│   │           single crash ("!?" — see later lectures)
│   │
│   └── combinations (slides 39-42)
│       ├── FIFO atomic broadcast, causal atomic broadcast
│       ├── plain abcast does NOT imply FIFO order
│       └── the primitives form a lattice (slide 42, figure 1)
│
└── References (slide 43): Hadzilacos-Toueg TR 94-1425;
    Défago-Schiper-Urban survey; Cachin-Guerraoui-Rodrigues
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[safety-and-liveness-properties]] | Safety is a predicate that is always true, liveness one that eventually becomes true; verification prefers many small properties over one big one. |
| [[reliable-broadcast-and-echo-algorithm]] | Deliver on first receipt, relay before delivering; Agreement is carried by the first correct deliverer, not by the sender. |
| [[broadcast-order-semantics]] | FIFO, causal and total order are three add-ons to rbcast, and none of them comes for free with another. |
| [[causal-broadcast-history-algorithm]] | Send your delivered-message history with every broadcast and deliver the history first: correct order at the price of a blocking algorithm. |
| [[synchronous-vs-asynchronous-models]] | Which impossibility holds depends on the model: ∆-timeliness needs synchrony, uniform rbcast needs a majority, abcast needs zero crashes. |

## Lecture Structure

**Safety and liveness (slides 3-7).** Safety (Sicherheit): something bad does not happen, a
predicate that is always true. Liveness (Lebendigkeit): something good eventually happens, where
"eventually" means within an unspecified but finite time, and the slide warns about the false
friend *eventuell* (German for "possibly", nearly the opposite). The running example is a
factorization algorithm `Fac(n)`: "eventually terminates" is liveness, "the output factors n into
primes" is safety. The methodological point: verify against many minimalistic properties, not one
compound one.

**The broadcast catalogue (slides 8-16).** Broadcasts are the fundamental fault-tolerant
abstraction, the semantics vary, and the algorithms depend strongly on the system model. The
chapter is explicitly built on Hadzilacos and Toueg 1994, with the green-box definitions quoted
verbatim and the article recommended at least to page 16, plus RSDP (Cachin et al. 2011). The
layering picture separates the application protocol from the broadcast algorithm and the
send/receive interface. Best-effort broadcast is just "send to all over perfect links": simple
and low-latency, no order guarantees, and delivery is only certain while the sender lives.

**Reliable broadcast (slides 14-21).** Messages carry `(sender, seq#, data)`. Three properties:
Validity (a correct broadcaster delivers its own message), Agreement (if one correct process
delivers, all do), Integrity (at most once, only if genuinely broadcast). The echo algorithm
delivers on first receipt after relaying to everyone, and the slides walk through the informal
correctness argument. Uniform agreement strengthens Agreement to cover deliveries by faulty
processes, and the slide states without proof: impossible in an asynchronous system with an
arbitrary number of faulty processes, but solvable synchronously, or asynchronously with a
majority of correct processes.

**Order properties (slides 22-35).** Reliable broadcast orders nothing. FIFO adds per-sender
order, implemented by a transformation that keeps sequence-number counters and buffers gaps.
Causal order adds respect for m → m′ (referring back to the logical-clock lecture), and the
simple algorithm FIFO-broadcasts the sender's whole delivery history with each message; the
overhead-free variant uses vector-clock-like message IDs but blocks. Causal order implies FIFO
order.

**Atomic broadcast and combinations (slides 36-42).** Atomic (total-order) broadcast is rbcast
plus Total Order. The algorithm slide asks "Algorithm?" and answers: none exists deterministically
in an asynchronous system with a single crash fault, "!?" deferred to later lectures. FIFO atomic
and causal atomic broadcast are named combinations, with the warning that plain atomic broadcast
does not necessarily imply FIFO. Slide 42 draws the six primitives as a lattice: FIFO order and
total order are independent add-ons to reliable broadcast.

## Exam-Relevant Points

1. **The property lists are the exam material.** Validity, Agreement, Integrity for rbcast; plus
   FIFO/Causal/Total order on top. Expect "state the properties of X" and "does execution E
   satisfy property P" questions (exercise 4.8 is exactly the second form).
2. **Safety vs liveness classification** of a given property (the Fac(n) pattern): termination is
   liveness, correctness of the produced value is safety.
3. **The echo algorithm and its Agreement argument**: relay before delivery, perfect links, and
   the observation that the argument never uses the sender's correctness.
4. **The three impossibility/possibility remarks** as model statements: uniform rbcast impossible
   async with arbitrary crashes (possible with majority correct), abcast impossible async with a
   single crash, timed broadcast needs the synchronous model.
5. **Causal order implies FIFO order, but total order implies neither** (slide 39 states the
   second explicitly).
6. **The uniformity prefix** is a general recipe: strengthen any Agreement by quantifying over
   deliveries of faulty processes too.
7. **Sources**: definitions in green boxes are verbatim Hadzilacos-Toueg; the article to page 16
   is named reading.

## Connections

- [[dependable-distributed-systems-lecture-2]] — logical clocks and the m → m′ causal precedence
  definition this lecture builds on.
- [[dependable-distributed-systems-lecture-3]] — the previous lecture; same course frame.
- [[dependable-distributed-systems-exercise-4]] — this lecture's exercise sheet, task for task.
- [[safety-and-liveness-properties]], [[reliable-broadcast-and-echo-algorithm]],
  [[broadcast-order-semantics]], [[causal-broadcast-history-algorithm]] — the concept pages.
- [[synchronous-vs-asynchronous-models]], [[failure-models]] — the system models that decide which
  algorithm is possible.
- Hadzilacos & Toueg, *A modular approach to fault-tolerant broadcasts and related problems*
  (TR 94-1425, Cornell, 1994) — the chapter's backbone; read at least to page 16.
- Cachin, Guerraoui, Rodrigues, *Introduction to Reliable and Secure Distributed Programming*,
  2nd ed., 2011 — the RSDP book the lecture cites.

## Open Questions

- The slide marks the async atomic broadcast impossibility with "!? (see later)", so the proof
  and its connection to consensus (FLP territory) are deferred; the lecture has not yet named the
  consensus problem in general form.
- The proof that uniform rbcast is impossible with an arbitrary number of faulty processes is
  stated "without proof" on slide 21; the course has not said whether it appears later.
- The overhead-free causal algorithm (message IDs, equivalent to vector clocks) is mentioned as
  blocking without the algorithm itself being shown; whether it is examinable is not stated.
- Slide 5a poses "Safety property or liveness property?" for `Fac(n)` and slide 6 resolves it by
  splitting the property in two; no further examples are given, so the classification skill rests
  on this single worked case.
