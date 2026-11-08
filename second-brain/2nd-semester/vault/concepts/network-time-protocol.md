---
title: "The Network Time Protocol"
tags: [concept, dependable-distributed-systems, semester-2, clock-synchronization, ntp]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[time-offset-measurement]]", "[[clock-synchronization-problem]]"]
---

## One-line Summary
NTP keeps internet hosts close to UTC by timing round trips against a redundant set of servers arranged in strata, filtering bad samples and lying servers out of the result, and handing the surviving offset to a control loop that steers the local oscillator.

## Core Intuition

NTP is not one algorithm. It is a pipeline of five stages, each solving a different failure: the round trip solves the unknown delay, the filter solves the single noisy sample, selection and clustering solve the wrong or distant server, and the discipline loop solves the oscillator that must be steered rather than set. A single measurement is worthless because the delay is unknown and the sample may be an outlier; eight from one server give a defensible value with an error estimate attached; several servers allow one liar to be detected by intersecting their correctness intervals.

Scale comes from the hierarchy. A stratum-1 server has a radio or a leased line to official time; everyone else synchronises to a server one stratum below their own. That gives an internet-sized fan-out with few primary sources, and a tree that can be re-drawn when a link dies.

## Formal Definition / Statement

**History (slide 25).** Developed since 1982 (NTPv1, RFC 1059) under the direction of David Mills. NTPv3 since 1990, still in use. NTPv4 since 1994. Mills' later research is interplanetary time synchronisation for the Interplanetary Internet, a NASA/DARPA project.

**Properties (slide 26).** Purpose: synchronise computer clocks in the existing Internet. The NTP Pool Project has more than 2000 servers worldwide. Achievable accuracy about 0.01 s in WANs, below 1 ms in LANs. Daemon available on almost all platforms. Fault tolerant.

**Stratum (slides 27-28).** Stratum 1 is a primary reference clock, synchronised by radio or leased line directly to official time standards. Stratum i > 1 is synchronised with the reference clock of stratum i − 1. Stratum changes dynamically when a connection fails.

**Architecture (slides 29-30).** Peer processes feed per-peer filters; the filters feed a selection algorithm, then a clustering algorithm, then a combination algorithm; the result drives the clock control loop, which controls a VFO. Multiple peers exist for redundancy and error diffusion. Peer filters keep the best of the last 8 offset readings per server. Selection separates "truechimers" from "falsetickers". Combination is a weighted average of offsets (older NTP versions took the single most trustworthy node).

**Per-measurement quantities (slides 32-35).** Each measurement yields an offset theta and a delay delta. Its error estimate is

```
epsilon = read accuracy + MAXDRIFT * (T4 - T1)
```

The last eight measurements are held in a buffer. On each new reading, every stored entry shifts down one index and its epsilon grows by MAXDRIFT times the elapsed time: for index i from 7 down to 1, (delta_i, theta_i, epsilon_i) becomes (delta_(i-1), theta_(i-1), epsilon_(i-1) + MAXDRIFT * elapsed time). Index 0 is the new reading. Entries are sorted by epsilon_j + delta_j/2 and the minimum is used as the reference. The filter dispersion is the weighted deviation from that reference:

```
epsilon_rho = sum over i = 0..7 of |theta_i - theta_0| * v^i ,  v = 0.5 (experimentally chosen)
```

The result for each peer is the triple (delta, theta, epsilon) = (delta_0, theta_0, epsilon_0 + epsilon_rho). NTPv4 additionally computes the jitter, the variance of the measured values.

**System process quantities (slide 36).** For each peer i: Theta_i = theta; Delta_i = RootDelay + delta; E_i = RootDispersion + epsilon + (age of measurement) * MAXDRIFT. From these, the synchronisation distance is Lambda_i = E_i + Delta_i/2, and the correctness interval is [Theta_i − Lambda_i, Theta_i + Lambda_i].

**Selection (slide 37).** DTS, the Digital Time Service and NTP's simple predecessor, computes the interval in which a maximum number of correctness intervals overlap and uses its centre as the correction. NTP's goal is different: select an interval such that the centre points of the intervals considered correct lie inside it.

**Clustering (slide 38).** Sort the references by stratum * MAXDIST + synchronisation distance. For each peer k compute the weighted scatter

```
epsilon_xi,k = sum over i of |theta_i - theta_k| * w^i ,  w = 0.75 (experimental)
```

remove the node with maximum epsilon_xi,k, and repeat while more than MINCLOCK nodes remain and that maximum still exceeds the minimum E_i.

**Combination (slide 39).** If the previously used reference survived, keep it; otherwise take the node at the top of the list. NTPv4 computes a weighted average of all remaining nodes. The resulting offset goes to the clock discipline algorithm.

## Key Properties

- **Five stages, five failure modes.** Filter (one bad sample), selection (a lying server), clustering (a distant server), combination (which of the survivors to follow), discipline (how to apply the correction).
- **The hierarchy is a distance, not an accuracy.** Stratum counts hops to a primary reference. It enters clustering as a cost term, not as a quality claim.
- **Every number carries an error.** Nothing in NTP returns a bare offset: each peer returns delta, theta and an epsilon that grows with age at MAXDRIFT.
- **The defence against a wrong server is interval intersection, not voting.** A server is a falseticker when its correctness interval cannot be made to overlap the majority's.
- **Two different weighting constants.** v = 0.5 inside a peer's filter, w = 0.75 inside clustering. Both are labelled experimental on the slides, i.e. tuned, not derived.
- **The output is an offset, not a clock setting.** Slide 39 ends by passing theta to the control loop — the clock is disciplined, not assigned.

## Worked Example

**Stratum re-drawing (slide 28).** The slide shows a three-level tree before and after one connection failure. The picture's edges do not survive text extraction; the level structure and the demotion do:

```
BEFORE                            AFTER one uplink fails
level 1:     1                    1
level 2:   2   2                  2   3     <- the failed server demoted to 3
level 3:  3 3 3                   3 3 3
```

No node becomes a new root. The node that lost its uplink moves down one level and re-parents onto a surviving stratum-2 peer.

**Peer filter, computed.** Eight stored readings with theta_0 = 12.500 s as the newest; the values are illustrative, the arithmetic is not:

| i | theta_i | abs deviation | weight 0.5^i | term |
|---|---------|---------------|--------------|------|
| 0 | 12.500 | 0.000 | 1.00000 | 0.0000 |
| 1 | 12.480 | 0.020 | 0.50000 | 0.0100 |
| 2 | 12.520 | 0.020 | 0.25000 | 0.0050 |
| 3 | 12.510 | 0.010 | 0.12500 | 0.0012 |
| 4 | 12.495 | 0.005 | 0.06250 | 0.0003 |
| 5 | 12.505 | 0.005 | 0.03125 | 0.0002 |
| 6 | 12.490 | 0.010 | 0.01562 | 0.0002 |
| 7 | 12.515 | 0.015 | 0.00781 | 0.0001 |

epsilon_rho = 0.0170 s. The entries at i = 1 and i = 2 contribute 0.0150 of that — 88 % of the dispersion comes from the two most recent samples after the reference. The oldest entry, at i = 7, carries weight 0.5^7 = 1/128 = 0.0078 and contributes 0.0001 s. The weights sum to 1.9922, so this dispersion is 1.6 times a plain mean absolute deviation over the same eight values (0.0106 s here).

The contrast with clustering matters: w = 0.75 leaves the oldest of eight entries at 0.75^7 = 0.1335, not 0.0078. The filter forgets fast because it tracks one server's noise; clustering is tolerant because it compares servers.

**Ordering peers.** Sorting by epsilon_j + delta_j/2 with the four round trips of exercise 3.4c and an assumed equal epsilon of 0.010 s gives 0.060 s for M1 and M4 and 0.110 s for M2 and M3 — the same ranking as smallest delta, which is the point of the criterion: the tighter measurement wins unless its own error estimate is much worse.

## Common Pitfalls

- **Reading stratum as a quality rank.** A crowded stratum-1 server behind a congested path can be worse than a nearby stratum-2. The slide's clustering metric uses stratum as one additive term, not as a filter.
- **Assuming stratum is fixed.** Slide 28 exists precisely to show it is not; a server's stratum is a property of its current uplink.
- **Treating truechimer selection as Byzantine agreement.** It is majority interval intersection. The slides state no bound of the n > 3m kind, and a majority of liars would win.
- **Confusing filter and selection.** The filter works within one peer over 8 samples; selection works across peers over one value each.
- **Using epsilon as the error of the measurement.** It is an estimate that already includes ageing: it grows by MAXDRIFT times elapsed time for every slot the reading moves down.
- **Assuming the constants are principled.** v = 0.5 and w = 0.75 are marked "experimental" on slides 35 and 38.
- **Inventing MAXDIST, MAXDRIFT or MINCLOCK values.** The deck names all three and gives none of their numbers.

## Connections

- [[time-offset-measurement]] — the four-timestamp method NTP uses unchanged (slide 32).
- [[ntp-clock-discipline]] — what happens to theta after combination.
- [[physical-clock-drift]] — why epsilon must grow with age, and why stratum-1 servers need radio or leased lines.
- [[tai-utc-time-scales]] — the scale NTP distributes.
- [[convergence-algorithm-cnv]] — the alternative philosophy: converge to the group instead of to a reference.
- [[dependable-distributed-systems-exercise-3]] — task 3.4 asks about protocol, layer and DST.
- [[dependable-distributed-systems-lecture-3]] — the source lecture, slides 24-39.

## Open Questions

- **Section 5, "Other algorithms", has no slides in this deck.** The table of contents promises PTP, Cristian's algorithm and Berkeley, and the extracted text ends at the clock discipline slide. Nothing about PTP is covered here and nothing should be inferred from this page about it.
- MAXDIST, MAXDRIFT and MINCLOCK are used in the formulas and never given values in the ingested material.
- The "> 2000 servers" pool figure and the 0.01 s / 1 ms accuracy figures are stated without date, conditions or measurement method.
- How RootDelay and RootDispersion are initialised at a stratum-1 server is not described.
- Authentication appears only as "each with / without authentication" (slide 27); no mechanism is described.
- How many peers are needed for selection to be sound is not stated.
