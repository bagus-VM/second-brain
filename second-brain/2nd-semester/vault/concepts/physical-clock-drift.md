---
title: "Physical Clock Drift"
tags: [concept, dependable-distributed-systems, semester-2, clock-synchronization, time]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[clock-synchronization-problem]]"]
---

## One-line Summary
No two physical clocks start at the same reading or run at the same rate, so without synchronisation the difference between them grows without limit — and every available reference clock caps how small that difference can be made.

## Core Intuition

Two independent error components. An offset is a constant disagreement about what time it is; a frequency error is a disagreement about how fast time passes. Correcting the first leaves the second untouched, and the second never stops producing new error.

Slide 4 splits the causes three ways: different initialisation (constant offset), different speed (frequency error), and environmental conditions — component ageing and temperature dependency — which change the frequency error over the device's life. The third is the awkward one: the rate is not a constant you measure once, it moves.

Hence the flat statement: without synchronisation, errors may continuously grow. There is no restoring force, and the growth rate is set by the frequency difference, not by the initial gap.

One clock for everybody is dismissed in one line: a common clock for all nodes is "usually not feasible" — a physical claim, not an economic one, since nodes in different buildings, cities and power domains share no oscillator. What remains is a central reference (radio: WWV, DCF77; satellite: GPS) or software. Slide 9 puts numbers on the references, and those numbers matter more than the clock numbers on slide 6, because they set the floor: a node synchronised to DCF77 is not better than 50 µs from official time however good its own oscillator. Slide 11 gives the software options: master/slave distribution of a reference time by broadcast or poll, or distributed consensus.

## Formal Definition / Statement

**Sources of divergence (slide 4):**

| Cause | Error type | Behaviour over time |
|-------|------------|---------------------|
| Different initialisation | constant offset | constant; fixable with one measurement |
| Different speed (frequency error) | drift | linear growth; a measurement fixes only the value at that instant |
| Environmental conditions (ageing, temperature) | drift with a changing rate | growth at a rate that itself moves |

**Dissemination accuracies of official time (slide 9), quoted as "maximum accuracy":**

| Medium | Examples | Maximum accuracy |
|--------|----------|------------------|
| Long wave | DCF77 (Mainflingen, Germany), WWVB (Boulder, USA) | about 50 µs |
| Short wave | WWV, WWVH (Hawaii) | about 1 ms |
| Satellite | GPS | about 0.3 µs |

**Software-based synchronisation (slide 11):** master/slave distribution with a reference time, either broadcast or poll; or distributed consensus. The slide gives those two families and no more.

**The seven characterisation items (slide 13).** The slide asks "which properties could be used to characterize an algorithm?" and then lists seven nouns without explanation. One clause each:

1. **Monotony** — does synchronisation ever move a clock backwards, i.e. cause a jump in time?
2. **Synchronisation with official time** — does the algorithm aim at a national or international reference, or only at agreement among the nodes?
3. **Robustness against network partitioning** — does it keep working, or fail safely, when the network splits into isolated groups?
4. **Fault tolerance against wrong reference clocks** — can a reference that reports bad time corrupt the nodes that trust it?
5. **Loyalty of reference** — how strongly does a node hold on to its chosen reference instead of switching under noise?
6. **Generated network traffic** — how many messages per node per unit time does the protocol cost?
7. **Error estimate** — does the algorithm produce a bound on its own accuracy, or only a value?

Item 5 is the one the slide leaves undefined; that clause is a reading, not a quotation.

## Key Properties

- **Offset and rate are different faults with different fixes.** Setting a clock removes the offset and changes nothing about the rate.
- **Drift is unbounded and non-stationary.** Linear at constant frequency error, unpredictable when the rate itself moves; no tolerance absorbs it.
- **Reference accuracy is a floor, not a target.** Receiver, interrupt latency and the protocol's own message delay all add to the 50 µs or 0.3 µs.
- **The seven items trade off.** Monotony and synchronisation with official time pull against each other: the cheapest way to be correct is to jump, and a jump is what monotony forbids.
- **No numbers for commodity hardware.** The deck quantifies caesium standards and radio dissemination, never a crystal oscillator.

## Worked Example

Frequency errors chosen for illustration — the deck gives none. Every figure below is computed from that choice.

| Frequency error | per hour | per day | per week | per year |
|-----------------|----------|---------|----------|----------|
| 1 ppm | 3.6 ms | 86.4 ms | 0.605 s | 31.5 s |
| 10 ppm | 36 ms | 0.864 s | 6.05 s | 315 s |
| 100 ppm | 0.36 s | 8.64 s | 60.5 s | 3154 s |

Read the middle row: at ten parts per million, a free-running clock is 0.864 s out after one day. Any protocol that assumes millisecond agreement has to resynchronise far more often than daily.

Now the other direction — how long a given frequency error takes to reach the accuracy of a reference source:

| Frequency error | reaches 50 µs (DCF77, WWVB) | reaches 1 ms (WWV) | reaches 0.3 µs (GPS) |
|-----------------|------------------------------|---------------------|-----------------------|
| 1 ppm | 50 s | 1000 s | 0.3 s |
| 100 ppm | 0.5 s | 10 s | 3 ms |
| 10⁻¹⁴ (caesium, slide 6) | 158 years | 3169 years | 0.95 years |

The last row is the argument of the lecture. A free-running caesium clock at 10⁻¹⁴ needs about 158 years to drift past what a long-wave broadcast delivers, and under one year to drift past what GPS delivers. With a GPS receiver attached, the oscillator is no longer the limiting component; the dissemination accuracy is.

## Common Pitfalls

- **Reading "constant offset" as harmless.** It is the easy component, but only once you can measure it — and the measurement error of [[time-offset-measurement]] is unbounded even where the offset is constant.
- **Treating 50 µs / 1 ms / 0.3 µs as the accuracy of a synchronised host.** They describe the dissemination path, before the receiver and the protocol add their delay.
- **Assuming drift is linear over long horizons.** The slide names temperature and ageing, so the rate is a function of the environment and of time.
- **Assuming a common clock is merely expensive.** "Usually not feasible" is a statement about physics; there is no wire to run.
- **Reading "distributed consensus" as Byzantine agreement about time.** The slide spends four words on it; the only consensus-style algorithm the lecture develops is CNV, and CNV converges to the group average, not to true time.

## Connections

- [[clock-synchronization-problem]] — lecture 2 states the problem qualitatively; this page is the quantitative background it lacked.
- [[tai-utc-time-scales]] — what "official time" is, that the reference clocks disseminate.
- [[time-offset-measurement]] — drift is why the offset must be measured repeatedly; the measurement error is a separate problem.
- [[network-time-protocol]] — the deployed form of slide 11's master/slave option.
- [[convergence-algorithm-cnv]] — the lecture's consensus-style option: bounded divergence, no reference.
- [[dependable-distributed-systems-lecture-2]] — the lecture whose open question on unquantified reference accuracy this page closes.
- [[dependable-distributed-systems-lecture-3]] — the source lecture.

## Open Questions

- The deck gives no frequency-error figure for ordinary hardware, so "how often must a node resynchronise" cannot be computed from these slides alone.
- The three dissemination figures are labelled "maximum accuracy" but the slides do not say maximum over what — one reception, one day, one class of receiver.
- "Loyalty of reference" is listed and never defined; whether it means hysteresis, stickiness, or resistance to falsetickers is not stated in the ingested material.
- Whether a GPS receiver counts as a trusted component is not stated. Item 4 implies it should not be, but the lecture never applies item 4 to the sources on slide 9.
