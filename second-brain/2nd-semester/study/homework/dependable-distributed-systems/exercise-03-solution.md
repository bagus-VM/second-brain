---
title: "Exercise 3 — Physical Clock Synchronization (Solutions)"
tags: [homework, dependable-distributed-systems, semester-2, clock-synchronization]
course: "Dependable Distributed Systems"
source_count: 2
status: current
last_updated: 2026-10-23
prerequisites: ["[[dependable-distributed-systems-lecture-3]]"]
---

# Dependable Distributed Systems — Exercise 3

Source: `dds26-exercise03.pdf` (Reiser, WS 2026/27, discussion 2026-10-28). The sheet's instruction:
**"Prepare answers before the exercise class. In class you will present them."**

Every number below is produced by `clock-sync.py` in this folder; the full run is in
`output-clock-sync.txt`. Nothing here is arithmetic done in the head.

**One gap, stated up front.** Task 3.2 tells you to download `exercise2-cnv.py` and modify it. That
file is **not in `raw/`** — the sheet references it but it was never added to the vault. Rather than
guess at someone else's code, 3.2 below is answered by implementing CNV from the lecture's own
definition and running the four experiments against that. The consequence is recorded honestly at
the end of 3.2: I can show which scenario fails and why, but I cannot tell you which line of *their*
file is wrong.

---

## 3.1 Measuring clock differences

### (a) Unidirectional and bidirectional, and what the messages contain

**Unidirectional.** A sends its current local time `tA` in a message. B records its own local time
`tB` at reception. The offset estimate is

```
o = tA - tB
```

The message content is one number: the sender's clock reading. B needs nothing else, because it
supplies the other half of the comparison from its own clock.

**Improved unidirectional.** If A also sends, or B can estimate, the message delay `d`, the estimate
becomes `o' = tA - tB + d`. The lecture is explicit that this is still wrong, for two reasons: the
delay varies from message to message, and the estimate of `d` is itself inaccurate.

**Bidirectional.** A sends a request and B replies. Four timestamps exist:

| Timestamp | Taken by | Meaning |
|-----------|----------|---------|
| T1 | P1 | request sent |
| T2 | P2 | request received |
| T3 | P2 | reply sent |
| T4 | P1 | reply received |

Total message transmission time, with P2's own processing time removed:

```
delta = (T4 - T1) - (T3 - T2)
```

Offset estimate, taking the midpoint of each side:

```
theta = (T2 + T3)/2 - (T1 + T4)/2
```

The message content is now four timestamps: the reply carries T1, T2 and T3 back, and P1 fills in
T4 on arrival. This is exactly the structure of an NTP packet, which "always includes T1 ... T4,
filled with values during the round-trip communication".

### (b) What accuracy statement each one supports

**Unidirectional: no bound at all.** The measured offset is wrong by the one-way transmission delay,
and nothing in the message tells you what that delay was. On an asynchronous network the delay has
no upper bound, so the error has no upper bound. The improved version replaces "unknown" with "an
estimate", which is better in practice and still not a bound — you have traded an unbounded unknown
error for an unbounded error in your estimate of `d`.

The one exception worth stating in the presentation: if the system *is* synchronous, i.e. a maximum
delay `d_max` is known, then the error is bounded by `d_max`. The bound comes from the synchrony
assumption, not from the measurement.

**Bidirectional: a real bound, and exactness under one condition.** The estimate `theta` is **exact
if the transmission times are equal in both directions**. If they are not, the error is bounded by

```
|error| <= delta/2
```

where `delta` is the measured round-trip time minus the server's processing time. That is the whole
reason bidirectional measurement is worth the extra two timestamps: it converts an unbounded error
into an error proportional to a quantity you measured. Note that `delta/2` is a bound on the error
*from asymmetry*, not on the total error — clock read accuracy still applies on top.

---

## 3.2 CNV simulation

**What the sheet asks for.** Four experiments on a four-node CNV simulation: unmodified (perfect
synchrony), one node with an initial clock error, one node with a 5 % frequency error, one node
running the malicious `EVILCNV` implementation. Then two modifications: (a) fix the algorithm so it
correctly implements CNV and repeat the failing experiment, and (b) modify `EVILCNV` to cause
maximum damage.

**What I ran instead.** `clock-sync.py` (`task_3_2`) implements CNV from the lecture definition —
each correct node reads every clock with ±0.02 s noise and averages, substituting its own value for
any reading more than δ = 1 s away. A faulty node reports a value of its own choosing to each
reader. Divergence is measured over the correct nodes only, which is what the convergence property
is about.

| # | Configuration | Divergence among correct nodes after 40 rounds |
|---|---------------|-----------------------------------------------|
| 1 | 4 nodes, perfect, sync step removed | 0.0000 s — perfect by construction |
| 2 | 4 nodes, one +0.8 s offset (below δ), all correct | 0.0115 s — at the noise floor |
| 3 | 4 nodes, one +8 s offset (above δ), all correct | 8.0122 s — **frozen out, no convergence** |
| 4 | 4 nodes, one 5 % fast, all correct | 0.0115 s — at the noise floor |
| 5 | 4 nodes, 1 malicious (n = 4 > 3m = 3) | 0.3949 s — bounded, under the 0.75δ bound |
| 6 | 3 nodes, 1 malicious (n = 3 = 3m) | 0.5003 s — driven up from 0 toward the δ ceiling |
| 7 | 4 nodes, 1 malicious, clamp removed | nodes agree to 0.0085 s but the group is dragged 1000 s off true time |

**The case that "does not match the expected behaviour" is almost certainly #3.** CNV's first
assumption is that the clocks start within δ of each other. An initial error larger than δ violates
that assumption, and the algorithm then does the opposite of what one expects: every correct node
treats the outlier as faulty and substitutes its own value, so the outlier is not pulled in — it is
excluded permanently, and divergence never falls. Anyone reading the algorithm as "it averages, so
it converges" will see this as a bug. It is not: it is the assumption doing its job. This is an
inference about their file, labelled as such — I cannot see the file.

**3.2(a) — the correct implementation.** The clamp is the whole algorithm, and there are three ways
to get it wrong:

1. **Averaging without the clamp.** Scenario 7: correct nodes still converge to each other, but the
   group's common value follows whatever the liar reports. The clamp is what bounds a faulty
   reading's influence to within δ of the reader's own clock.
2. **Clipping instead of substituting.** The rule replaces a rejected reading with the *reader's own
   clock value*, not with the reading moved δ closer. The two give different averages.
3. **Using `>=` instead of `>`.** A reading exactly δ away is *kept*. The lecture's three-process
   example in 3.3 depends on this: with `>=` it does not converge (computed below).

**3.2(b) — maximum damage.** A faulty node gets the most damage by reporting a value tailored to
each reader: exactly `+delta` above the clock of the reader it wants to push up, and exactly `-delta`
below the clock of the reader it wants to push down. Both lies sit on the boundary, so both are
accepted. Scenarios 5 and 6 are that attack. The result is the honest reading of the theory: with
n > 3m the damage stays bounded below δ but does not vanish (0.39 s of a 1 s δ, close to the 0.75δ
bound), while with n = 3 = 3m the bound is δ itself and the adversary can drive correct nodes from
agreement up to the ceiling.

---

## 3.3 Lamport's CNV algorithm revisited

### (a) Three correct processes, δ = 2 h, clocks 03:00 / 04:00 / 05:00

Every pair differs by at most 2 h, and the rule discards a reading only if it differs by **more
than** δ. So no substitution happens anywhere, and all three processes average the same three values:

| Process | Own clock | Readings used | New clock |
|---------|-----------|---------------|-----------|
| P1 | 03:00 | 03:00, 04:00, 05:00 | **04:00** |
| P2 | 04:00 | 03:00, 04:00, 05:00 | **04:00** |
| P3 | 05:00 | 03:00, 04:00, 05:00 | **04:00** |

**After one round all three read 04:00 and the divergence is exactly zero.** The example is
deliberately built on the boundary: the outermost pair is exactly δ apart, so the strict inequality
is what makes it converge. Under the rival reading "differing by δ **or more**", P1 would replace
P3's 05:00 with its own 03:00 and P3 would replace P1's 03:00 with its own 05:00, giving 03:20 /
04:00 / 04:40 — 80 minutes of divergence instead of none. Computed in `task_3_3a`.

### (b) The worst behaviour for a malicious P2

Brute force over both lies, at one-minute granularity (`task_3_3b`):

```
P2 -> P1: 01:00        P2 -> P3: 07:00
P1 becomes 03:00       P3 becomes 05:00
|P1 - P3| = 120 min = 2 h = 1.0 * delta
```

Both lies sit exactly on the δ boundary and are therefore accepted:

- P1 averages 03:00, **01:00**, 05:00 → (3 + 1 + 5)/3 = 3.00 → stays at **03:00**.
- P3 averages 03:00, **07:00**, 05:00 → (3 + 7 + 5)/3 = 5.00 → stays at **05:00**.

The divergence is 2 h = δ, exactly what it was before the round. This is the maximum: each new clock
is the mean of accepted readings, so it cannot leave the interval spanned by the clocks it started
with — the adversary cannot *increase* the divergence beyond its initial value, but it can make the
synchronisation round achieve **nothing at all**, indefinitely. For comparison, a *lazy* attacker
reporting some far-away value gets it substituted by each reader's own clock and only manages 80
minutes of divergence (03:40 against 05:00). The boundary values are strictly better for the
attacker than wildly wrong ones, which is the counter-intuitive part of the answer.

### (c) Why CNV fails here

Two ways to say it, and both belong in the presentation.

**By the threshold.** CNV's guarantee needs **n > 3m** for n processes with m faulty. Here n = 3 and
m = 1, so n = 3m and the condition fails. The plausibility analysis bounds the new divergence by

```
new divergence < (3m/n) * delta = (3*1/3) * delta = delta
```

which is not an improvement: the assumed initial error was already below δ. The algorithm promises
to keep the divergence below δ, and the bound it delivers is exactly δ — no margin, no progress.

**By the mechanism.** With three processes there is no majority to outvote the liar. Each correct
process sees two other clocks, one of which is the liar's; the average is over three values, so the
lie carries a full one third of the weight in each correct process's update — and the liar can give
each correct process a *different* lie. Two honest processes plus one liar is precisely the case
where "less than one third faulty" is violated, and the example is constructed to sit on that
boundary. The general statement: 3f + 1 processes are needed to tolerate f Byzantine clock faults.

---

## 3.4 Synchronisation of physical clocks

### (a) Which transport protocol, and why

**UDP.** Four reasons, in order of importance:

1. **A clock protocol measures delay, so it must not hide delay.** TCP retransmits a lost segment
   transparently. A retransmitted segment produces a round-trip time that includes the retransmission
   timeout, and the measurement is then garbage — but indistinguishable from a genuine slow path.
2. **TCP's own timing behaviours distort the RTT.** Delayed ACKs, Nagle's algorithm, and flow
   control all add delay that belongs to the transport, not to the path being measured.
3. **The measurement is idempotent and tiny.** One request, one reply, a few dozen bytes. Reliability
   buys nothing: a lost packet is cheap to re-measure, and a stale measurement is worse than none.
4. **Timestamps want to be taken at the wire.** Hardware and kernel timestamping work on the datagram
   as it arrives; a stream protocol forces you to reason about where in the byte stream the timestamp
   was taken.

This is what NTP does: UDP port 123.

### (b) Application, operating system, or hardware

| Placement | Advantages | Disadvantages |
|-----------|------------|---------------|
| **Application** | Portable; no privileges; easy to prototype; can pick its own reference servers | Timestamps are taken far from the wire, so it inherits scheduling jitter and syscall overhead; cannot adjust the system clock without privileges; cannot discipline the oscillator's *rate*, only read it; every application that needs time must reimplement it |
| **Operating system** | One implementation shared by every process; can set *and* slew the system clock; can run the control loop against the hardware counter; can timestamp packets on arrival in the kernel | Still subject to interrupt and scheduling jitter unless it timestamps in the driver; a single misconfiguration affects every application; requires privilege |
| **Hardware** | Best accuracy — a GPS-disciplined oscillator or NIC timestamping gives nanosecond-scale error; immune to OS jitter; keeps time when the OS is stalled | Cost; per-device; needs a driver and often a daemon to feed it; you still need software above it to decide *which* reference to trust |

**The honest answer is "all three, layered"**, and NTP is the evidence: hardware timestamps where the
NIC supports them, kernel-level clock discipline (the `VFO` the lecture's clock process controls),
and a user-space daemon doing the peer selection and filtering. The trade-off is a straight
accuracy-versus-cost and accuracy-versus-portability axis, not a choice of one layer.

### (c) Choosing among four round-trip measurements

Computed in `task_3_4c`. Columns are relative to the base time of each measurement:

| Measurement | delta = RTT (s) | theta = offset (s) | Server processing (s) |
|-------------|-----------------|--------------------|-----------------------|
| M1 | 0.100 | -2.500 | 0.100 |
| M2 | 0.200 | -2.450 | 0.100 |
| M3 | 0.200 | -2.550 | 0.100 |
| M4 | 0.100 | -2.500 | 0.100 |

**Criterion 1 — smallest delay.** The measured offset is exact when the path is symmetric, and the
error from asymmetry is bounded by `delta/2`. A smaller `delta` therefore means a tighter bound. The
minimum is 0.100 s, achieved by **M1 and M4** — a tie.

**Criterion 2 — agreement with the other measurements.** M1 and M4 both give theta = -2.500 s; M2
gives -2.450 s and M3 gives -2.550 s, symmetrically around it. M1 and M4 are the same measurement
recorded twice, and they are the two lowest-delay ones. This is the NTP peer-filter idea in
miniature: **with the smallest delay, the measured offset is the most accurate**, and the
measurements that disagree with the consensus are the ones with the larger delays.

**Selection: M1 (equivalently M4), with an estimated clock offset of**

```
E = theta = -2.500 s
```

and a residual error bound from path asymmetry of `delta/2 = 0.050 s`. M3 is rejected: its delay ties
M2's, but its offset is 0.050 s off the consensus, which is exactly the asymmetry error its delay
permits — it carries no information the other three do not.

A second criterion worth naming in the presentation: **consistency across repeated measurements at
the same delay**. M1 and M4 have identical deltas and identical offsets, while M3's offset differs
from M2's by twice the noise scale. A measurement that repeats is more trustworthy than one that
does not.

### (d) Daylight saving time

**NTP never sees DST.** It distributes **UTC**, a continuous scale with no DST. The local time a user
sees is `UTC + offset(t)`, where `offset(t)` — including the ±1 hour DST shift — comes from the
operating system's timezone database, applied at the moment of display or of conversion.

So the protocol's own clock never jumps. Two consequences worth stating:

- **Monotony is preserved where it matters.** The NTP-synchronised clock is monotone (modulo leap
  seconds, see below); the discontinuity is a *presentation* transformation applied by the C library
  or the OS, and a well-written application stores UTC and converts only for output.
- **This is the opposite of the leap-second problem.** DST is a jump in the local *label*; a leap
  second is a jump in UTC itself, and NTP must handle that one (either by stepping through 23:59:60
  or by smearing the extra second over a window). That is why the lecture's characterisation list
  asks about monotony: DST does not threaten it, leap seconds do.

---

## Verification

```
$ python clock-sync.py
```

Full output in `output-clock-sync.txt`. Every figure in this page appears in that file: the
three-process averages, the brute-forced worst lie, the seven CNV scenarios, and the four
measurement rows.

## Connections

- [[dependable-distributed-systems-lecture-3]] — the lecture this sheet examines.
- [[time-offset-measurement]] — 3.1 and 3.4(c) in full.
- [[convergence-algorithm-cnv]] — 3.2 and 3.3 in full, including the same simulation table.
- [[network-time-protocol]] — 3.4(a), (b) and (d).
- [[ntp-clock-discipline]] — the PLL/FLL control loop that 3.4(b) is really asking about.
- [[tai-utc-time-scales]] — why UTC exists and why leap seconds threaten monotony.
- [[dependable-distributed-systems-exercise-2]] — the previous sheet, where logical clocks did the
  ordering that this sheet's physical clocks cannot.

## Open Questions

- **`exercise2-cnv.py` is missing from `raw/`.** Task 3.2 cannot be answered against the sheet's own
  code. 3.2 above substitutes an independent implementation and says so; the specific line that is
  wrong in their file remains unknown, and the guess offered (an initial offset larger than δ) is an
  inference, not a finding.
- **The sheet says "in one of the cases, the observed behaviour will not match the expected
  behaviour"** but does not say which. Scenario 3 is the only one in my run that fails to converge
  while every node is correct, so it is the likely candidate — but that is reasoning about a file I
  cannot see.
- **3.2(b) asks to "maximise the max diff value printed during execution"**, which is a property of
  their `EVILCNV` interface. My attack (a per-reader lie of exactly ±δ) is the theoretical maximum
  for this configuration; whether their code can express it is unknown.
- **The exercise gives no δ, no number of nodes beyond four, and no round count** for the simulation,
  so the numbers in the table are mine (δ = 1 s, 40 rounds, ±0.02 s read noise) and are stated as
  such rather than presented as the sheet's parameters.
- **3.3 does not say whether "after the synchronization" means after one round or after convergence.**
  Answered here for one round, which is what the question describes; for this configuration one round
  is also the fixed point.
- **3.4(c) asks for "two criteria" without naming them.** Smallest delay and agreement with the other
  measurements are the two the lecture supports; NTP's real filter uses dispersion as well, which is
  a third criterion the sheet does not ask for.
