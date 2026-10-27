---
title: "The Convergence Algorithm CNV"
tags: [concept, dependable-distributed-systems, semester-2, clock-synchronization]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[time-offset-measurement]]", "[[clock-synchronization-problem]]"]
---

## One-line Summary
Every process sets its clock to the average of everyone's clock, replacing readings that differ from
its own by more than δ — and the group stays within δ of itself as long as fewer than a third of the
clocks are faulty.

## Core Intuition

There is no reference clock in CNV. It is a *convergence* algorithm, not a *synchronisation* one:
the goal is that the correct processes agree with each other, not that they agree with true time.
That distinction is the whole point, and it is what makes the algorithm fault-tolerant — you cannot
be dragged to a wrong value by a liar if you never had a true value to be dragged away from.

The mechanism is one line: take the mean, but refuse to believe a reading that is too far from your
own. The δ threshold is what turns a plain average — which a single Byzantine node can bend
arbitrarily — into something with a provable bound. The average pulls the group together; the
clamp stops any single member from pulling it apart.

The price is stated as an assumption on slide 20 and it is easy to miss: **the clocks must already
be within δ of each other before the algorithm starts.** CNV maintains a bound, it does not create
one. A node that is further than δ out is not pulled in — every other node treats it as a liar and
substitutes its own value, so the outlier stays out forever. That behaviour is reproduced in the
simulation in `clock-sync.py` (scenario 3).

## Formal Definition / Statement

**Source:** L. Lamport, P. M. Melliar-Smith, *Synchronizing Clocks in the Presence of Faults*,
Journal of the ACM 32(1), January 1985, pp. 52-78. The lecture cites this as the sole reference of
the whole lecture.

**Tasks the algorithm sets itself:** prevent unbounded growth of divergence between multiple clocks,
and tolerate faulty clocks.

**Assumptions (slide 20):**

1. Initially all processes have approximately synchronised clocks, with error < δ.
2. The clocks of all correct processes run at approximately the correct rate.
3. A correct process can read another correct process's clock with a small maximum error ε.

**Goal:** at any time, all correct processes have approximately the same local time, with error < δ.

**Procedure (slide 21):**

1. Each process reads the clocks of all other processes.
2. It sets its local clock to the average of all values, **including its own**.
3. In that average it substitutes its own value for every reading that deviates by **more than δ**.

**The theorem, as stated on slide 21:** the desired properties — convergence to a common clock and
tolerance of faulty clocks — hold if **fewer than one third of the clocks are wrong**, i.e. if
n > 3m for n processes of which m are faulty.

**The plausibility analysis (slides 22-23).** Let p and q be correct processes and r any process,
and let C<sub>p,q</sub> denote q's clock as read by p.

- If r is correct, C<sub>p,r</sub> ≈ C<sub>q,r</sub> — the same clock, read with small error.
- If r is faulty, |C<sub>p,r</sub> − C<sub>q,r</sub>| < 3δ. The 3δ comes from the clamp: p's copy of
  r's reading lies within δ of p's own clock (either it was accepted, or it was replaced by p's own
  value), and likewise for q, so the two copies differ by at most |C<sub>p</sub> − C<sub>q</sub>| + 2δ,
  which is below 3δ whenever p and q are themselves within δ.

Every process sets its clock to the mean of its readings, so the new difference between p and q is
bounded by the same average of per-process differences: (n−m) terms near 0, and m terms below 3δ.
Hence

```
new divergence  <  (3m/n) · δ
```

and with n > 3m this is strictly below δ — which is exactly the invariant the algorithm promises to
maintain.

## Key Properties

- **Convergence, not accuracy.** CNV makes correct clocks agree. It makes no claim that the agreed
  value is close to real time. A Byzantine node cannot split the group, but it can still drag the
  whole group's common value within the δ window.
- **The threshold is one third, and it is exact.** n > 3m. With n = 3 and m = 1 the bound is
  (3·1/3)·δ = δ, which is the assumed initial error — a round that guarantees nothing.
- **The clamp is applied per reading, not to the average.** The substitution happens before the mean
  is formed, and it substitutes the reading process's *own* value, not a clipped value.
- **"More than δ" is strict.** A reading exactly δ away is accepted. This single character decides
  whether the lecture's three-process example converges (see the worked example).
- **The assumptions are load-bearing, not decoration.** Violating assumption 1 (initial error < δ)
  produces permanent divergence, not slow convergence.
- **Two errors are explicitly neglected** (slide 23): the execution time of the algorithm itself,
  and the error caused by not reading all clocks simultaneously.
- **No reference clock, no monotonicity guarantee.** A synchronisation round can move a clock
  backwards. Whether that matters is one of the characterization questions on slide 13.

## Worked Example

**The lecture's own three-process example, computed.** δ = 2 hours, and in one round P1 reads 03:00,
P2 reads 04:00, P3 reads 05:00. Every pair differs by at most 2 h, so no substitution happens
anywhere:

| Process | Own | Values averaged | New clock |
|---------|-----|-----------------|-----------|
| P1 | 03:00 | 03:00, 04:00, 05:00 | **04:00** |
| P2 | 04:00 | 03:00, 04:00, 05:00 | **04:00** |
| P3 | 05:00 | 03:00, 04:00, 05:00 | **04:00** |

One round, exact agreement, divergence 0. Verified by `clock-sync.py` (`task_3_3a`).

**The same example with the rival reading of the rule.** If "differing by more than δ" is read as
"differing by δ or more", then P1 replaces P3's 05:00 with its own 03:00 and P3 replaces P1's 03:00
with its own 05:00:

| Process | Values averaged | New clock |
|---------|-----------------|-----------|
| P1 | 03:00, 04:00, **03:00** | 03:20 |
| P2 | 03:00, 04:00, 05:00 | 04:00 |
| P3 | **05:00**, 04:00, 05:00 | 04:40 |

Divergence goes from 2 h to 80 minutes instead of to zero. The example is engineered so that the
strict inequality is the difference between "converges in one round" and "does not converge at all",
which is presumably why the sheet chooses δ = 2 h and clocks exactly 2 h apart.

**What a malicious node does to it.** Exercise 3.3(b) asks for the worst lie by P2 in that same
three-process configuration. Brute force over both lies (`task_3_3b` in `clock-sync.py`) gives
**01:00 to P1 and 07:00 to P3** — both exactly on the δ boundary, so both are accepted:

- P1 averages 03:00, **01:00**, 05:00 → stays at 03:00.
- P3 averages 03:00, **07:00**, 05:00 → stays at 05:00.

Divergence is 2 h = δ, exactly the value it started at. The adversary cannot make it worse — the
mean of accepted readings is a convex combination, so no clock can leave the interval it started
in — but it can make the round achieve **nothing at all**, indefinitely. That is what "no
convergence guarantee" means in practice.

**And the simulation.** `clock-sync.py` (`task_3_2`) runs a correct CNV implementation against a
max-damage Byzantine node that reports its own clock ± δ, personalised per reader:

| Configuration | Divergence among correct nodes after 40 rounds |
|---------------|-----------------------------------------------|
| 4 nodes, all correct, one +0.8 s offset | 0.0115 s (noise floor) |
| 4 nodes, one +8 s offset (> δ) | 8.0122 s — frozen out, assumption violated |
| 4 nodes, one 5 % fast, all correct | 0.0115 s (noise floor) |
| 4 nodes, 1 malicious (n=4 > 3m=3) | 0.3949 s — bounded, below the 0.75δ bound |
| 3 nodes, 1 malicious (n=3 = 3m) | 0.5003 s — driven up toward the δ ceiling from zero |
| 4 nodes, 1 malicious, clamp removed | nodes agree to 0.0085 s but the group is dragged 1000 s off true time |

The last row is the argument for the clamp: without it the group still converges — to whatever the
liar says.

## Common Pitfalls

- **Reading "convergence" as "synchronisation with true time".** CNV has no reference. A group of
  correct clocks can converge to a value that is wrong, and that is still a success by CNV's
  contract.
- **Assuming n ≥ 3m is enough.** The condition is strict: n > 3m. With n = 3m the bound equals δ
  and no progress is guaranteed — which is precisely what the exercise's three-process case
  demonstrates.
- **Treating the δ clamp as clipping.** The substitute is the reading process's own clock value, not
  δ-away-from-the-reading. Clipping and substitution give different averages.
- **Forgetting that δ is an assumption on the *initial* spread.** CNV maintains; it does not repair.
- **Using ≥ instead of >.** The lecture's example only converges under the strict reading.
- **Expecting the algorithm to defend against a Byzantine node inside the δ window.** Any lie within
  δ of the reader's own clock is indistinguishable from an honest reading. CNV bounds the damage; it
  does not detect the liar.
- **Ignoring the two neglected errors.** Execution time and non-simultaneous reads both eat into the
  margin, and the slides give no bound for either.

## Connections

- [[time-offset-measurement]] — how the readings C<sub>p,q</sub> are obtained in the first place,
  and where the error ε in assumption 3 comes from.
- [[clock-synchronization-problem]] — the lecture-2 statement of why any of this is needed.
- [[failure-models]] — CNV's "faulty clock" is a Byzantine fault, not a crash: a lying clock keeps
  answering.
- [[fault-error-failure-chain]] — a clock that lies is the fault; the wrong timestamps it produces
  are the error; a violated ordering invariant downstream is the failure.
- [[network-time-protocol]] — the practical alternative: instead of averaging everyone, elect a
  hierarchy and discipline a local oscillator. NTP gives accuracy relative to real time, which CNV
  does not.
- [[redundancy-forms]] — CNV's fault tolerance is value redundancy: n clocks for the information
  content of one.
- [[dependable-distributed-systems-lecture-3]] — the lecture this page belongs to.
- [[dependable-distributed-systems-exercise-3]] — tasks 3.2 and 3.3 are this page, turned into
  questions.

## Open Questions

- **Why 3δ and not something tighter?** The bound follows from the clamp (each copy within δ of its
  reader's own clock, plus the readers' own spread). The lecture states the result without the
  intermediate step, so the 3 is worth re-deriving on paper.
- **The plausibility analysis is not a proof.** It bounds a single round's new difference in terms of
  the current one, and the slides say so by listing what is neglected. Whether the bound is preserved
  under repeated rounds with a fresh lie each time is not argued in the slides — the simulation in
  `clock-sync.py` suggests it holds empirically, which is not the same thing.
- **What happens with m clocks that are merely wrong rather than malicious?** A drifting clock
  re-enters the δ window periodically and is treated as honest in between; the slides do not discuss
  this case.
- **Does CNV appear in practice?** The lecture presents NTP as the deployed protocol and CNV as the
  theory; no deployment of CNV is mentioned.
