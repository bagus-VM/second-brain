---
title: "Dependable Distributed Systems — Exercise 3 Overview (Clock Measurement, CNV, Transport)"
tags: [topic, dependable-distributed-systems, semester-2, clock-synchronization, homework]
course: "Dependable Distributed Systems"
source_count: 2
status: current
last_updated: 2026-10-23
prerequisites: ["[[dependable-distributed-systems-lecture-3]]"]
---

## One-line Summary
Four tasks that turn lecture 3 from slides into work: measure an offset two ways and say what the
accuracy of each is, break and then repair a CNV simulation, hand-compute a CNV round that a
malicious node can neutralise, and decide how a real clock protocol should be built.

## Core Map

```
Exercise 3 (discussion 2026-10-28)
│
├── 3.1 Measuring clock differences
│   ├── (a) unidirectional o = tA − tB, and bidirectional
│   │       delta = (T4−T1) − (T3−T2), theta = (T2+T3)/2 − (T1+T4)/2
│   └── (b) unidirectional: no bound. bidirectional: exact if symmetric,
│           otherwise error <= delta/2
│           -> [[time-offset-measurement]]
│
├── 3.2 CNV simulation  (exercise2-cnv.py — NOT in raw/)
│   ├── four experiments: perfect, initial error, 5 % frequency error,
│   │       malicious EVILCNV
│   ├── (a) repair the algorithm: the δ clamp, applied per reading,
│   │       substituting the reader's own value, with strict ">"
│   ├── (b) maximise the damage: a per-reader lie of exactly ±δ
│   └── the failing case: an initial offset ABOVE δ never converges,
│           because CNV's first assumption is violated
│           -> [[convergence-algorithm-cnv]]
│
├── 3.3 Lamport's CNV revisited
│   ├── (a) δ = 2 h, clocks 03:00/04:00/05:00 -> all become 04:00
│   ├── (b) worst lie: 01:00 to P1 and 07:00 to P3 -> 03:00 vs 05:00,
│   │       divergence 2 h = δ, round achieves nothing
│   └── (c) fails because n = 3 = 3m: the bound (3m/n)δ = δ is no
│           improvement on the assumed initial error
│
└── 3.4 Synchronisation of physical clocks
    ├── (a) UDP, not TCP: retransmissions and transport delays
    │       destroy the delay measurement
    ├── (b) application vs OS vs hardware — accuracy vs cost vs
    │       privilege; real NTP uses all three layers
    ├── (c) four measurements: smallest delta wins, ties broken by
    │       agreement -> M1/M4, E = −2.500 s, bound delta/2 = 0.050 s
    └── (d) DST: NTP carries UTC; the OS applies the offset, so the
            protocol itself never jumps
            -> [[network-time-protocol]], [[ntp-clock-discipline]]
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[time-offset-measurement]] | Two timestamps give an offset with unbounded error, four give one bounded by half the round trip |
| [[convergence-algorithm-cnv]] | Average with a δ clamp and the group holds together — unless a third of it lies |
| [[network-time-protocol]] | The deployed answer: strata, eight-sample filters, and three stages of peer selection |
| [[ntp-clock-discipline]] | Phase for jitter, frequency for drift, both at once in the local clock's control loop |

## Exercise Structure

| Task | What it asks | Where it is answered |
|------|--------------|----------------------|
| 3.1(a) | Describe unidirectional and bidirectional measurement, message contents, exact formulas | `exercise-03-solution.md` §3.1(a) |
| 3.1(b) | Discuss whether an accuracy bound can be given in each case | §3.1(b) |
| 3.2 | Run and break a CNV simulation; repair the algorithm; weaponise the evil node | §3.2, `clock-sync.py` `task_3_2` |
| 3.3(a) | Compute one CNV round for three processes with δ = 2 h | §3.3(a), `task_3_3a` |
| 3.3(b) | Find the malicious P2 behaviour with the worst impact | §3.3(b), `task_3_3b` (brute force) |
| 3.3(c) | Explain why CNV fails in that example | §3.3(c) |
| 3.4(a) | Which transport protocol for a clock protocol, and why | §3.4(a) |
| 3.4(b) | Application, OS, or hardware implementation | §3.4(b) |
| 3.4(c) | Two criteria to pick the best of four measurements; compute the offset | §3.4(c), `task_3_4c` |
| 3.4(d) | How NTP accounts for daylight saving time | §3.4(d) |

## Exam-Relevant Points

- **The two formulas are the examinable core.** `delta` and `theta` from four timestamps, and the
  statement that `theta` is exact under symmetry and otherwise wrong by at most `delta/2`.
- **3.3 is the worked example to memorise.** Three processes, δ = 2 h, clocks 2 h apart: all become
  04:00 in one round because the strict `>` keeps the boundary readings. Change `>` to `>=` and it
  does not converge. That single character is the trap.
- **The n > 3m threshold, with the arithmetic.** (3m/n)·δ, and for n = 3m the bound equals δ — which
  is the assumption, so nothing is gained. This is the standard "why 3f + 1 processes" argument in
  its clock form.
- **The Byzantine attacker's best move is the boundary, not the extreme.** A lie of exactly ±δ is
  accepted and maximises damage; a wildly wrong value is discarded by the clamp. Counter-intuitive
  and therefore a good exam question.
- **UDP over TCP** with the reason (a clock protocol measures delay, so it must not hide delay) is a
  clean one-mark answer that also tests whether you understand what RTT means.
- **DST versus leap seconds.** DST is a change of local *label* applied by the OS and does not touch
  the protocol; a leap second is a jump in UTC itself. Both bear on the "monotony" characterisation
  item from the lecture.

## Connections

- **The lecture:** [[dependable-distributed-systems-lecture-3]] — every task here is a slide made
  concrete.
- **The previous sheets:** [[dependable-distributed-systems-exercise-1]] (dependability vocabulary)
  and [[dependable-distributed-systems-exercise-2]] (models, logical clocks). 3.1's opening line —
  "measuring the difference between local clocks is an important task in clock synchronization
  algorithms" — is the bridge from exercise 2's logical clocks to this sheet's physical ones.
- **The runnable artifacts:** `study/homework/dependable-distributed-systems/clock-sync.py` and
  `output-clock-sync.txt`. The CNV simulation, the brute-force attacker and the measurement table all
  come from one run.
- **The lecture's summary** deliberately puts the two clock families side by side: logical clocks
  order events in asynchronous systems, physical clocks give timestamps with limited accuracy. The
  exercise is entirely on the second half.

## Open Questions

- **`exercise2-cnv.py` is not in `raw/`.** Task 3.2 references a downloadable file that the vault
  does not have, so the answer works from an independent implementation. The sheet's "one case does
  not match the expected behaviour" therefore cannot be pinned to a line of code — only to a scenario
  (an initial offset larger than δ, which violates CNV's first assumption).
- **The sheet gives no simulation parameters**: no δ, no round count, no noise model. The numbers in
  the answer are stated with the parameters used, so they can be reproduced, but they are not the
  sheet's.
- **3.4(c) asks for "two criteria" without naming them.** The answer uses smallest delay and
  agreement with the other measurements; NTP's real filter also uses dispersion, which would be a
  third.
- **How this sheet is graded, and whether the in-class presentation is mandatory, is still not stated
  anywhere in the material** — the same gap the course page records for exercises 1 and 2.
