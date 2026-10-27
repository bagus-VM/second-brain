---
title: "Dependable Distributed Systems — Lecture 3 Overview (Physical Clock Synchronization)"
tags: [topic, dependable-distributed-systems, semester-2, clock-synchronization, ntp]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[dependable-distributed-systems-lecture-2]]"]
---

## One-line Summary
Lecture 2 said physical clocks cannot order events and handed the ordering job to logical clocks;
this lecture goes back and makes the physical clocks themselves agree — measuring an offset between
two nodes, the CNV averaging algorithm that keeps a group from drifting apart, and NTP, the
protocol that actually runs the internet.

## Core Map

```
Lecture 3 — Physical clock synchronization (42 slides)
│
├── 1 Background                                        (slides 3-13)
│   ├── no two physical clocks are identical: offset, frequency error,
│   │       environment (ageing, temperature)
│   ├── ⇒ without synchronization the error grows without bound
│   ├── TAI (caesium second) / UT1 (astronomy) / UTC (TAI + leap seconds)
│   │       -> [[tai-utc-time-scales]]
│   ├── official time by radio: DCF77 50µs, WWV 1ms, GPS 0.3µs
│   ├── software: master/slave broadcast or poll, or consensus
│   └── how to characterize an algorithm: monotony, official time,
│           partition robustness, fault tolerance, loyalty, traffic, error estimate
│               -> [[physical-clock-drift]]
│
├── 2 Measuring time offsets                            (slides 15-17)
│   ├── unidirectional: A sends tA, B records tB, o = tA − tB,
│   │       error = unknown transmission delay (unbounded)
│   ├── bidirectional: T1..T4, δ = (T4−T1) − (T3−T2),
│   │       θ = (T2+T3)/2 − (T1+T4)/2
│   ├── exact if the two directions are symmetric, otherwise error ≤ δ/2
│   └── -> [[time-offset-measurement]]
│
├── 3 Convergence algorithm CNV                         (slides 19-23)
│   ├── Lamport & Melliar-Smith 1985, JACM 32(1)
│   ├── each process averages all clocks, substituting its own value
│   │       for readings more than δ away
│   ├── converges if fewer than one third of clocks are faulty: n > 3m
│   └── -> [[convergence-algorithm-cnv]]
│
├── 4 Network Time Protocol                             (slides 25-40)
│   ├── Mills, since 1982; v4 since 1994; pool of >2000 servers
│   ├── strata 1..i, dynamic re-stratification on connection failure
│   ├── per peer: 8-sample filter, ε = read accuracy + MAXDRIFT·(T4−T1),
│   │       dispersion ερ, triple (δ, θ, ε)
│   ├── system process: selection (truechimers vs falsetickers, DTS intervals),
│   │       clustering (stratum·MAXDIST + distance, drop worst),
│   │       combination (weighted average of surviving offsets)
│   ├── accuracy ≈ 10 ms WAN, < 1 ms LAN
│   └── -> [[network-time-protocol]]
│       └── clock discipline: hybrid PLL/FLL, VFO
│               -> [[ntp-clock-discipline]]
│
└── 5 Other algorithms                                  (announced, slides absent)
    └── the outline lists section 5 and then goes straight to the summary:
            no PTP, no Cristian, no Berkeley — despite the semester plan
            promising "NTP and Precision Time Protocol"
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[physical-clock-drift]] | Offset and frequency error are different faults, and only the second one grows without limit |
| [[tai-utc-time-scales]] | The second is defined by caesium, the day by the Earth, and leap seconds are the patch that keeps them together |
| [[time-offset-measurement]] | One timestamp gives an offset with unbounded error; four timestamps give one with error ≤ δ/2 |
| [[convergence-algorithm-cnv]] | Average everyone's clock, discard outliers beyond δ, and the group stays together if fewer than a third lie |
| [[network-time-protocol]] | A hierarchy of servers, eight-sample filters and three selection stages that turn noisy measurements into a disciplined clock |
| [[ntp-clock-discipline]] | Phase control fixes short-term jitter, frequency control fixes long-term drift, and NTP runs both at once |

## Lecture Structure

| Slides | Section | What happens |
|--------|---------|--------------|
| 1-2 | Title, agenda | Five sections: background, offset measurement, CNV, NTP, other algorithms |
| 3-4 | Problem statement | No identical clocks; central reference clocks; error grows |
| 5, 12-13 | Open question, then answer | "Which properties could characterize an algorithm?" — posed twice, answered once, with a seven-item list |
| 6a-8 | TAI, UT1, UTC | Caesium definition, astronomical time, leap seconds, and the 2026 CGPM decision |
| 9-11 | Dissemination | DCF77/WWVB/WWV/GPS accuracies; master-slave or consensus |
| 15-17 | Offset measurement | Unidirectional, then bidirectional with the T1..T4 derivation |
| 19-23 | CNV | Assumptions, procedure, plausibility analysis, the n > 3m threshold |
| 25-31 | NTP overview | History, properties, strata, architecture, the three process types |
| 32-35 | NTP peer filtering | Offset measurement reused, the 8-sample buffer, dispersion |
| 36-39 | NTP system process | Selection, clustering, combination |
| 40 | Clock discipline | Hybrid PLL/FLL |
| 41-42 | Summary, references | The whole lecture compressed; one reference |

## Exam-Relevant Points

- **The bidirectional formulas are the most likely thing to be asked for**, and they are the only
  place in the lecture where a derivation is done twice (once generically on slide 17, once as NTP
  on slide 32). Be able to write δ and θ from the four timestamps and to say when θ is exact.
- **The n > 3m condition of CNV** is stated as a fact on slide 21 and justified by the plausibility
  analysis on slides 22-23. Both are quotable; the arithmetic is in
  [[convergence-algorithm-cnv]].
- **The three-stage NTP system process** (selection → clustering → combination) is a naming
  question as much as a conceptual one. The names and the order are examinable.
- **Truechimer / falseticker** and the DTS interval-overlap idea are named explicitly and are easy
  to confuse with the clustering step.
- **NTP's accuracy figures** are given: about 0.01 s in WANs, below 1 ms in LANs.
- **The characterization list on slide 13** is a ready-made exam question ("which properties can
  be used to characterize a clock synchronization algorithm?") — seven items.
- **Leap seconds are not a detail.** The lecture gives the count (27), the last one
  (31.12.2016) and the CGPM 2026 decision to move to a continuous UTC in 2027. A question about
  monotony connects directly to this.

## Connections

- **Prerequisite:** [[dependable-distributed-systems-lecture-2]] — models, the relevance of time,
  and the logical clocks that this lecture deliberately does not use. The lecture's own summary
  puts both halves side by side: logical clocks order events, physical clocks give you a
  timestamp.
- **Homework:** exercise 3 (`dds26-exercise03.pdf`) is entirely this lecture — offset measurement,
  a CNV simulation, the three-process CNV example, and the choice of transport for a clock
  protocol. Solved in `study/homework/dependable-distributed-systems/exercise-03-solution.md`,
  with the arithmetic and the simulation in `clock-sync.py`.
- **The lecture's own summary** frames the two families as complementary rather than competing:
  logical clocks for ordering in asynchronous systems, physical clocks where a real timestamp is
  needed and where accuracy is technically limited.
- **Later lectures:** the semester plan puts fault-tolerant group communication and consensus
  next, and both need timeouts — which need the synchrony assumption that this lecture's
  algorithms try to buy.
- **[[synchronous-vs-asynchronous-models]]** — a synchronous system is defined by bounded delays;
  NTP is the practical mechanism that makes bounded clock error plausible.
- **[[clock-synchronization-problem]]** — the lecture-2 statement of the problem, which this
  lecture answers. That page's open question about the accuracy of radio time sources is now
  answered here (DCF77 50 µs, WWV 1 ms, GPS 0.3 µs).

## Open Questions

- **Section 5, "Other algorithms", has no slides.** The outline on slides 1, 14, 18, 24 and 317
  lists it, and the deck then jumps to the summary. PTP, Cristian's algorithm and the Berkeley
  algorithm are therefore *not* in the ingested material, even though the course's semester plan
  promises "Network Time Protocol and Precision Time Protocol". Whether they are delivered in the
  exercise class or dropped is not stated.
- **The lecture does not say how the error estimate ε in NTP is calibrated**, only that it is
  `read accuracy + MAXDRIFT·(T4−T1)`. The constants MAXDRIFT, MAXDIST, MINCLOCK and the weights
  v = 0.5, w = 0.75 are given as "experimentally chosen" with no derivation.
- **The CNV plausibility analysis neglects two things and says so**: the time taken to execute
  the algorithm, and the error from not reading all clocks simultaneously. No bound is offered
  for either.
- **UTC's future is stated but not analysed**: continuous UTC from 20 May 2027, with |UT1 − UTC|
  allowed to reach 3600 s. What that does to software that assumes |UT1 − UTC| < 0.9 s is not
  discussed.
- **No mention of security.** NTP is described as "fault tolerant" but the slides do not cover
  spoofing or authentication, beyond noting that each mode exists "with / without
  authentication".
