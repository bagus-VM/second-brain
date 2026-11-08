---
title: "Measuring Time Offsets"
tags: [concept, dependable-distributed-systems, semester-2, clock-synchronization, measurement]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[clock-synchronization-problem]]", "[[physical-clock-drift]]"]
---

## One-line Summary
A one-way message cannot separate the clock offset from the transmission delay, so every practical measurement pays for a round trip and reports the offset plus half the round-trip asymmetry as its error bound.

## Core Intuition

You want one number: the difference between two clocks. A single message gives one equation with two unknowns — the offset and the time the message spent in flight. Nothing in the message distinguishes "your clock is 2.5 s behind mine" from "your clock is right and the packet was queued for 2.5 s". Subtracting an estimate of the delay only swaps an unbounded error for the error of that estimate.

The bidirectional method removes the unknown by measuring it. The responder echoes timestamps, the initiator times the whole exchange, and the offset appears twice with opposite signs, so the equations separate offset from delay. What remains is an assumption about symmetry: equal one-way times give an exact answer, unequal ones bound the error by half the round trip. That bound is computable from data you actually have, which is why NTP is built on this method rather than on broadcasts.

## Formal Definition / Statement

**Unidirectional, simple (slide 16).** A sends its current local time tA to B. B records its local time tB on reception. Estimate:

```
o = tA - tB
```

Error: the message transmission delay, "potentially unbounded".

**Unidirectional, improved (slide 16).** Estimate the delay d and correct:

```
o' = tA - tB + d
```

Still wrong: the delay varies per message, and the estimate of it is itself inaccurate. The slide gives no method for obtaining d.

**Bidirectional (slide 17).** Four timestamps: T1 when P1 sends, T2 when P2 receives, T3 when P2 sends the reply, T4 when P1 receives it.

```
total transmission time:  delta = (T4 - T1) - (T3 - T2)
offset:                   theta = (T2 + T3)/2 - (T1 + T4)/2
```

Exact if the transmission times in the two directions are equal. Otherwise the error is bounded by delta/2.

**Where the formulas come from.** Let d1 be the one-way delay P1→P2, d2 the delay P2→P1, and theta the amount by which P2's clock is ahead of P1's. Then

```
T2 = T1 + d1 + theta
T4 = T3 + d2 - theta
```

Subtracting cancels theta and leaves delta = d1 + d2, the round trip without the responder's turnaround. Adding cancels the delays and leaves theta + (d1 − d2)/2, so the estimate is off by exactly (d1 − d2)/2 — never more than (d1 + d2)/2 = delta/2 when both delays are non-negative.

## Key Properties

- **delta is offset-free.** It is computed from differences on each side separately, so the clock difference cancels. It measures the network, not the clocks.
- **The bound is hard but not tight.** delta/2 cannot be exceeded as long as no message arrives before it was sent; it says nothing about the actual error, which is usually far smaller.
- **Unidirectional can never bound its error.** With one message there is no second observation of the same unknown; the delay can be arbitrarily large and nothing in the data reveals it. The improved variant does not fix this — it substitutes an estimate for the unknown, and an estimate of an unbounded quantity is not a bound.
- **Bidirectional always bounds it**, because the round trip is measured and the offset is squeezed into the middle of it.
- **Sign convention matters.** theta as defined on slide 17 is (responder time − initiator time) at the midpoint of the exchange: negative theta means the responder's clock is behind.
- **Offset only.** Neither method says anything about the rate difference, which is why measurement must be repeated ([[physical-clock-drift]]).

## Worked Example

The four round-trip measurements of exercise 3 task 3.4c, all timestamps relative to a base time. Every figure below is computed from the sheet's numbers.

| m | T1 | T2 | T3 | T4 | T3−T2 | T4−T1 | delta | theta | delta/2 |
|---|----|----|----|----|-------|-------|-------|-------|---------|
| M1 | 0.000 | −2.450 | −2.350 | 0.200 | 0.100 | 0.200 | 0.100 | −2.500 | 0.050 |
| M2 | 0.000 | −2.350 | −2.250 | 0.300 | 0.100 | 0.300 | 0.200 | −2.450 | 0.100 |
| M3 | 0.000 | −2.450 | −2.350 | 0.300 | 0.100 | 0.300 | 0.200 | −2.550 | 0.100 |
| M4 | 0.000 | −2.450 | −2.350 | 0.200 | 0.100 | 0.200 | 0.100 | −2.500 | 0.050 |

**First criterion: smallest delta.** M1 and M4 tie at delta = 0.100 s, half the round trip of M2 and M3. A smaller delta means a tighter bound on the same estimate, so those two are preferred before anything else.

**Second criterion: agreement with the others.** M1 and M4 give theta = −2.500 s. M2 gives −2.450 s and M3 gives −2.550 s, both with delta = 0.200 s and both exactly 0.100 s from −2.500 — precisely their own delta/2. Their intervals [−2.55, −2.35] and [−2.65, −2.45] both contain −2.500, so the tightest measurements agree with each other and are consistent with the loose ones. Answer: M1 or M4, **theta = −2.500 s, error bound ±0.050 s**.

Splitting each row into one-way delays (d1 = T2 − T1 − theta, d2 = T4 − T3 + theta) gives 0.050/0.050 for M1 and M4 and 0.100/0.100 for M2 and M3: the dataset is perfectly symmetric, so each theta is exact and delta only says how long the exchange took. The bound still does the work — it is what you would have if the asymmetry were as large as the round trip allows, and it is the only thing separating M1 from M3.

**The same data, measured unidirectionally.** Take M1 and use only the request: tA = T1 = 0.000, tB = T2 = −2.450, so o = tA − tB = +2.450 s. The bidirectional answer is +2.500 s in the same sign convention. The one-way estimate is short by exactly 0.050 s — the outbound delay, which it cannot see. With a longer queue it would be short by that queue instead, and no arithmetic on a single message would reveal it.

## Common Pitfalls

- **Mixing up the sign convention.** Slide 17's theta is responder minus initiator; the unidirectional o on slide 16 is sender minus receiver. Comparing the two without flipping a sign produces a 4.95 s error on a 2.5 s offset.
- **Reporting delta/2 as the error.** It is an upper bound under worst-case asymmetry, not an estimate of the actual error.
- **Forgetting the responder's turnaround.** delta subtracts T3 − T2. Skip that and a slow server looks like a slow network, and the bound inflates accordingly.
- **Assuming symmetry because the route is symmetric.** The bound covers asymmetry; it does not detect it. The only evidence about asymmetry in the data is delta itself.
- **Believing more measurements tighten the bound.** They do not — each sample carries its own delta/2. More measurements let you select a smaller delta and cross-check consistency; the bound of a given sample is fixed by that sample.
- **Using a sample taken while the clock rate was wrong.** Both formulas assume the local clock runs at approximately the correct rate across the exchange; nothing checks that.

## Connections

- [[network-time-protocol]] — adopts exactly these four timestamps (slide 32) and then filters, selects and combines many such samples.
- [[convergence-algorithm-cnv]] — depends on reading another process's clock with a small maximum error; this page is where that error comes from.
- [[clock-synchronization-problem]] — the problem statement this page makes quantitative.
- [[physical-clock-drift]] — why one measurement is never enough.
- [[ntp-clock-discipline]] — what is done with theta once it has been measured.
- [[dependable-distributed-systems-exercise-3]] — tasks 3.1 and 3.4c are this page.
- [[dependable-distributed-systems-lecture-3]] — the source lecture, slides 15-17.

## Open Questions

- The improved unidirectional variant assumes an estimate d of the transmission delay; the slide never says how d is obtained, so the "improvement" is unquantified in the ingested material.
- Slide 15 raises "multiple measurements for increasing accuracy?" as a question and never answers it. The exercise supplies the selection criteria; the lecture does not.
- Exercise 3.4a and 3.4b ask which transport protocol and which layer should implement this. The slides answer neither.
- The formulas assume the two clocks tick at the same rate during the exchange. No error term for a rate difference over the round trip is given.
- Nothing is said about lost or retried messages: whether a retransmitted reply invalidates the sample, or how the responder's turnaround time is bounded.
