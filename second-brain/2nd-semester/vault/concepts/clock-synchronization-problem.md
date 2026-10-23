---
title: "The Clock Synchronization Problem"
tags: [concept, dependable-distributed-systems, semester-2, time]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-21
prerequisites: ["[[distributed-system-properties]]"]
---

## One-line Summary
Physical clocks never agree, they only disagree at different rates — and the first thing that breaks when they disagree is any snapshot of the system taken at a single moment.

## Core Intuition

A distributed system has no global present. Each machine has its own clock, and those clocks start at different times, run at slightly different rates, and respond differently to temperature and ageing. The error therefore has two independent components — a constant *offset* and a drifting *frequency* — and the second is the dangerous one: even a perfectly aligned set of clocks drifts apart over time, so synchronisation is not a one-off operation but a standing obligation.

Why does it matter? Because a large class of operations implicitly assumes a global "now": logging that orders events across machines, debugging a trace, reconstructing the root cause of an error, taking a consistent checkpoint of a set of nodes. The `make` example on the slide is the cheapest illustration — a file whose timestamp lies in the future makes the build system skip recompilation, and the resulting binary is silently stale. The system did not crash; it produced a wrong answer, which is worse.

The lecture's answer is to stop relying on physical time for ordering and use logical clocks instead. This page covers the problem itself, since it recurs for every protocol that needs a deadline, a lease, or a timeout.

## Formal Definition / Statement

Sources of divergence between physical clocks:

| Source | Nature | Symptom |
|--------|--------|----------|
| Different initialisation | constant offset | clocks agree on rate, disagree on the reading |
| Different speed (frequency error) | drift | agreement decays over time |
| Environmental conditions | drift (component ageing, temperature dependency) | agreement decays, non-uniformly |

The slide states the consequence directly: **"Without synchronization errors may continuously grow!"**

A common clock for all nodes is "usually not feasible". The alternative is a **central reference clock** — radio transmission (WWV, DCF77, GPS) — which gives "technically limited accuracy" and, being central, is itself a single point of failure.

**The checkpoint problem.** A checkpoint records the local state of a set of nodes. For it to be consistent, the states must correspond to one logical instant. With differing local clocks, the save is inconsistent. The slide's example (C3): message $m$ is sent by $P_1$ and received by $P_2$; $P_2$'s checkpoint $S_2$ includes the effect of $m$, but $P_1$'s checkpoint $S_1$ does not. Restoring both together produces a state that never existed — the system is resurrected in a configuration it was never in, which breaks any invariant that was true before the failure.

## Key Properties

- **Offset and drift are different problems.** Correcting the offset once does nothing about the rate difference.
- **Drift is unbounded without correction.** The error grows without limit; it is not a bounded quantity that can be absorbed.
- **The failure mode is silent.** A skewed clock does not announce itself. It produces wrong-but-plausible results.
- **Checkpoint consistency is a causal property, not a temporal one.** The checkpoint must respect message order, and that is exactly what logical clocks capture.
- **Central reference clocks trade accuracy for a new failure mode.** Radio sources are limited in accuracy and introduce a dependency on the broadcast.
- **The applications are monitoring, debugging, and root-cause analysis** — "Real order cannot be reconstructed if locally generated timestamps are not synchronized."

## Worked Example

The slide's `make` transcript, step by step:

```
% vi test.c
% make
make: Warning: File `test.c' has modification time 94 s in the future
cc test.c -o test
make: warning: Clock skew detected. Your build may be incomplete.
% make
make: Warning: File `test.c' has modification time 94 s in the future
cc test.c -o test
make: warning: Clock skew detected. Your build may be incomplete.
```

`make` compares the modification time of `test.c` against the modification time of the object file. The local clock says the source is 94 seconds in the future relative to the build system's own reference, so `make` concludes the source is *newer* than the object. Two things follow, and the slide names both:

1. **The tool does not recognise that `test.c` was not modified.** It recompiles unnecessarily — waste, but harmless.
2. **Or worse: modification is not detected and the file will not get compiled at all.** If the skew goes the other way, `make` believes the object is up to date and skips the compile. The build succeeds, the binary is stale, and nothing fails loudly.

The point generalises beyond `make`. Any tool that compares timestamps across machines — distributed build systems, log aggregators, cache expiry, replication conflict resolution — inherits the same hazard.

## Common Pitfalls

- **Treating a one-off correction as synchronisation.** Fixing the offset leaves the drift untouched.
- **Assuming the checkpoint is a snapshot.** A checkpoint taken at "the same wall-clock time" on unsynchronised machines is not a consistent state — it may be a state that never existed.
- **Believing the warning is the bug.** In the `make` example the warning is the *symptom*; the skipped compilation is the failure.
- **Ignoring that central time sources are themselves distributed-system components.** The lecture does not develop this, but a reference clock that everyone depends on is a single point of failure unless it is itself replicated — which is the subject of the later lectures.
- **Expecting logical clocks to solve this.** They do not; they solve *ordering*, not *deadlines*. A lease timeout still needs physical time.

## Connections

- [[lamport-logical-clocks]] — the direct alternative for ordering, avoiding physical time entirely.
- [[vector-clocks]] — the same move with exact causal information, at higher message cost.
- [[distributed-system-properties]] — "no common clock" is one of the three properties every distributed system lacks; this page is the detailed consequence.
- [[synchronous-vs-asynchronous-models]] — synchrony is a model-level promise; the slide's real-time-clock requirement follows from it.
- [[error-detection-and-recovery]] — checkpoint and rollback, the recovery mechanism that clock skew corrupts.

## Open Questions

- The slides do not quantify the accuracy of the named reference sources (WWV, DCF77, GPS) or the error a synchronised system retains.
- How the "rate-synchronized real-time clocks" required by the synchronous model are obtained is not addressed — that is presumably the NTP/PTP material planned for lecture 3.
- Whether NTP-style synchronisation is sufficient for the course's later consistency requirements (consensus, group membership) is not stated.
- No protocol is given for *detecting* that two nodes' clocks have drifted apart, as opposed to correcting it.
- The relationship between clock skew and the checkpoint problem is shown in one diagram, but no general condition for when a set of local states forms a consistent cut is given.
