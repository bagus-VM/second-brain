---
title: "TAI, UT1 and UTC Time Scales"
tags: [concept, dependable-distributed-systems, semester-2, time, time-scales]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-23
prerequisites: ["[[physical-clock-drift]]", "[[clock-synchronization-problem]]"]
---

## One-line Summary
TAI counts atomic seconds from a definition fixed in 1967, UT1 follows the Earth's actual rotation, and UTC is the atomic scale bent to stay within 0.9 s of the astronomical one by inserting leap seconds — which is why UTC is not monotone.

## Core Intuition

Two different questions hide behind the word "time". How long is a second — that is a physics question, answered by a caesium transition and nothing else. What time of day is it — that is an astronomy question, answered by where the sun is over the zero meridian.

The two answers drift apart, because the Earth's rotation is irregular and the SI second is not. A scale built purely on the atomic second therefore slowly stops agreeing with sunrise. UTC is the compromise: keep the atomic second, and bend the scale back toward the astronomical one whenever the difference approaches a second.

The bending is done in whole seconds, and that is the whole trouble. A correction of exactly one second cannot be applied smoothly to a clock that is being read by software; the scale either repeats a second or skips one. Everything else on this page follows from that single design choice, and it is the reason "monotony" is the first item on the lecture's characterisation list.

## Formal Definition / Statement

**TAI — the atomic second (slide 6).** The definition, quoted from the International Bureau of Weights and Measures:

> "The second is 9 192 631 770 times the period of the radiation corresponding to the transition between the two hyperfine levels of the ground state of atoms of the nuclide 133Cs."

Valid since 1967. Before that the second was defined by the duration of the Earth's rotation (until 1956), or by the duration of an Earth circulation of the sun. The slide's point is that the unit of time used to be astronomical and is now atomic — the reference moved from the sky to the laboratory.

One period of that radiation is 1 / 9 192 631 770 s ≈ 0.109 ns, i.e. the transition sits at about 9.19 GHz. The number is a definition, not a measurement: it fixes the second, so it cannot be wrong.

**Accuracy of caesium clocks:** up to about 10⁻¹⁴, "equivalent to ≈ 0.9 ns/day".

**UT1 (slide 6):** time defined by astronomical observation — mean solar time at the zero meridian. It is measured, not generated.

**UTC (slide 6):** a scale based on the atomic second, kept within |UT1 − UTC| < 0.9 s by inserting leap seconds. Previously 27 leap seconds; the last was on 31.12.2016.

**CGPM 2026 (slide 6a):** continuous UTC becomes effective on 20 May 2027, and the maximum |UT1 − UTC| will be 3600 s.

## Key Properties

- **TAI is a count of seconds; UTC is a count plus a policy.** TAI has no leap seconds and never jumps. UTC's whole definition is a bound on its distance from UT1, maintained by discrete corrections.
- **The 0.9 s bound is tighter than the correction.** A leap second moves the scale by 1.0 s, yet the maintained bound is 0.9 s. That only works because the correction is applied before the drift reaches the bound — the bound describes the residual, not the step.
- **UTC is not monotone in general.** At an insertion, a second is repeated; at a removal, a second would be skipped. Anything that timestamps with UTC inherits that.
- **The Earth is the noisy component, not the clock.** At 10⁻¹⁴ a caesium standard needs about 2.85 million years to accumulate 0.9 s of error. The leap second exists because UT1 wobbles, not because atomic clocks are bad.
- **Continuous UTC abandons the mechanism.** 3600 s is 4000 times the old bound: one hour of tolerated difference, which is a way of saying the scale will no longer be corrected to follow the Earth.
- **The scales are what a synchronisation protocol distributes.** NTP's job is to deliver a UTC-based offset; which scale that offset refers to is a decision made above the protocol.

## Worked Example

**Check the slide's own equivalence.** 0.9 ns per day as a fractional rate:

```
0.9e-9 s / 86400 s = 1.0417e-14
```

So "up to about 10⁻¹⁴" and "≈ 0.9 ns/day" are the same statement. Run it the other way: 10⁻¹⁴ × 86400 s = 0.864 ns/day, and the slide's 0.9 is that rounded up. Both numbers are consistent; neither is a measurement of a specific device.

**What 10⁻¹⁴ costs over a year.** 10⁻¹⁴ × 365 × 86400 s = 3.1536 × 10⁻⁷ s = 315.36 ns ≈ 0.32 µs. A year of free running puts a caesium standard a third of a microsecond out — the same order as the 0.3 µs accuracy that GPS dissemination achieves ([[physical-clock-drift]]). The clock and the broadcast are comparably good, which is why a GPS-disciplined node does not gain much from a better oscillator.

**How long the 0.9 s window would last unsynchronised.** 0.9 s / 10⁻¹⁴ = 9 × 10¹³ s ≈ 1.04 × 10⁹ days ≈ 2.85 million years. The UTC bound is not a statement about clock quality at any human timescale.

**The leap-second trace.** A reader sampling UTC every half second across an insertion sees:

```
23:59:59.0
23:59:59.5
23:59:60.0     <- the inserted second, given its own label
23:59:60.5
00:00:00.0
```

Five distinct labels, strictly increasing: monotone, provided the extra second gets a label of its own. It stops being monotone the moment an implementation has no room for a 61st second in the minute and repeats 23:59:59 instead — which is exactly what happens when UTC is stored as a plain seconds-since-epoch counter and the leap second is applied as a shift. The slide states the mechanism (leap seconds) but not this consequence; the consequence is what the characterisation item "monotony" is asking about.

**The size of the change in 2027.** 3600 / 0.9 = 4000. The tolerated difference grows by a factor of four thousand, and the last leap second before the change is, at the effective date, 3792 days — about 10.4 years — old.

## Common Pitfalls

- **Conflating TAI with UTC.** The slide defines the atomic second and the UT1 bound; it never states the current TAI − UTC offset, and neither should you invent one.
- **Reading |UT1 − UTC| < 0.9 s as "UTC never moves more than 0.9 s".** A leap second moves it by 1.0 s. The bound is checked on the residual, and the correction is made early enough to keep it.
- **Assuming UTC timestamps are monotone.** They are, under the 23:59:60 convention; they are not under a naive epoch counter.
- **Assuming leap seconds are routine.** 27 of them in total and none since 31.12.2016 — long enough that most software has never executed the path.
- **Reading "maximum |UT1 − UTC| will be 3600 s" as a looser accuracy target.** It is the abandonment of the correction, not a relaxation of it.
- **Treating UT1 as the more accurate scale.** UT1 is the one with unpredictable rate; that is the reason UTC exists.

## Connections

- [[physical-clock-drift]] — the drift figures that make the 10⁻¹⁴ comparison meaningful.
- [[clock-synchronization-problem]] — why a shared time scale is needed at all.
- [[network-time-protocol]] — the protocol that distributes a UTC-based offset to hosts.
- [[ntp-clock-discipline]] — where the local-time/DST question lands: the protocol carries UTC, the operating system renders it.
- [[dependable-distributed-systems-lecture-3]] — the source lecture, slides 6, 6a, 7 and 8.

## Open Questions

- The current TAI − UTC offset is not stated in the slides, nor whether all 27 leap seconds were insertions.
- How a host should represent the inserted second (repeat a label, widen the counter, smear the correction) is not discussed in the ingested material.
- Why 3600 s was chosen as the new bound, and whether the resulting scale keeps the name UTC, is not stated.
- How UT1 is actually measured, and at what precision, is not stated — only that it comes from astronomical observation.
- The CGPM 2026 decision is asserted without a citation in the deck; the slide gives the effective date and the bound, nothing about the resolution behind them.
