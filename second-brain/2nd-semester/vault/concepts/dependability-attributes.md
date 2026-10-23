---
title: "Dependability Attributes"
tags: [concept, dependable-distributed-systems, semester-2, metrics]
course: "Dependable Distributed Systems"
source_count: 6
status: current
last_updated: 2026-10-21
prerequisites: ["[[fault-error-failure-chain]]"]
---

## One-line Summary
Dependability is measured on three axes — reliability, maintainability, and availability — which describe how long a system works, how fast it gets fixed, and how much of the time it is actually usable.

## Core Intuition

Laprie's 1993 definition anchors the whole vocabulary: "Computer system dependability is the quality of a delivered service such that reliance can justifiably be placed on this service." The key word is *justifiably*. Dependability is not a property of hardware alone; it is a claim about the relationship between a delivered service and the reliance placed on it. And the service must be judged against a specification: "A dependable system is a system that with high probability works according to its specification."

That definition immediately generates the open questions the slide lists, and they are the honest content of the concept: how is the service specified, what exactly is specified (the service itself, or the environment too), and what counts as a "high probability"? A metric like MTTF only means something relative to a specification and a mission period.

The three DSSA attributes separate three questions that are easily conflated. *How often* does it break? That is reliability. *How long* is it down once it breaks? That is maintainability. *How much of the time is it up?* That is availability — the composite that engineers actually care about when they make an availability promise to a user. The worked comparison below shows that the composite can be dominated by either term depending on the numbers.

The adjacent properties — integrity, security, resilience — sit on a separate slide in the source and are *not* part of the DSSA attribute triple. Keeping them apart is worth more than one exam point.

## Formal Definition / Statement

**Dependability (Laprie 1993).** Computer system dependability is the quality of a delivered service such that reliance can justifiably be placed on this service.

**Dependable system (slide).** A system that with high probability works according to its specification.

### The three DSSA attributes

| Attribute | Definition as given | Metrics |
|---|---|---|
| **Reliability** | Measure of the continuous delivery of correct service | MTTF (Mean Time To Failure); MTBF (Mean Time Between Failures); probability the system does not fail during a mission period; probabilistic failure rate (e.g. 10^-9 failures/hour) |
| **Maintainability** | Measure of the time to restoration of correct service | MTTR (Mean Time To Repair) |
| **Availability** | Measure of the delivery of correct service with respect to the alternation between correct and incorrect service | Availability = MTBF / (MTBF + MTTR) |

Note the two different "time to" quantities: MTTF measures how long the system survives before it fails, MTBF measures the interval between failures (and in a repairable system equals MTTF + MTTR), and MTTR measures the down time. The availability formula follows directly: over a cycle of length MTBF + MTTR, the fraction spent delivering correct service is MTBF.

### Other properties (a separate slide, not the DSSA triple)

| Property | Definition as given |
|---|---|
| **Integrity** | Absence of improper system alterations |
| **Security** | Ability to guarantee confidentiality, integrity, and availability in service provision (cf. [[cia-triad]]) |
| **Resilience** | Ability to recover from external faults; frequently used when considering applications that require interactions through their surrounding environment (cf. [[resilience-vs-dependability]]) |

### Context: why distribution makes this hard

Lamport's line frames the whole course: "A distributed system is one in which the failure of a computer you did not even know existed can render your own computer unusable." Concretely, a failure of one component may influence others; communication happens over unreliable networks with unpredictable delays. If a single component fails on average once per year and all components fail independently, a datacenter of 1000 of them sees about 1000 failures per year. Malicious faults make it worse: errors are no longer independent, they are more serious, and error models become inaccurate.

## Key Properties

- **Reliability is about continuity, not uptime.** It describes the stretch of correct service, not the fraction of it.
- **Maintainability is about repair time.** A perfectly reliable but unrepairable system is not maintainable in this sense.
- **Availability is a ratio, so it is scale-free.** A system that is down half the time but that you can always get back to is more available than one that is up most of the time and hangs for a week.
- **MTTF and MTBF differ by MTTR** in the repairable case: MTBF = MTTF + MTTR.
- **Metrics are specification-relative.** "Correct service" is defined against a specification, and the slide's open questions show that pinning that down is nontrivial.
- **Component counts multiply failure exposure.** Independence is what makes 1000 components tolerable; independence is exactly what attackers destroy.
- **Security and integrity overlap but are not identical.** Security is the umbrella that guarantees confidentiality, integrity and availability of the service; integrity alone is only the absence of improper alterations.

## Worked Example

Two systems are compared on the same workload. The question is which one a user should trust to be *available*.

**System A:** fails once per year, and each repair takes one day.
- MTBF = 8760 h (one year), MTTR = 24 h
- Availability = 8760 / (8760 + 24) = 8760 / 8784 = **0.997268**

**System B:** fails once per week, and each repair takes one hour.
- MTBF = 168 h (one week), MTTR = 1 h
- Availability = 168 / (168 + 1) = 168 / 169 = **0.994083**

**A is more available than B by about 0.318 percentage points** (99.7268% vs 99.4083%).

The instructive part is the ratio decomposition. A's MTBF is roughly 52 times longer than B's (8760/168 ≈ 52.1), but A also needs roughly 24 times longer to repair (24 h vs 1 h). Because the repair time is negligible compared with *either* interval, the MTTR term almost disappears from the denominator, and the failure rate decides the comparison.

This is the teaching point: **availability is not "how often" but "how long"**. B fails 52 times more often than A, and A is still the more available system, because 24 hours is negligible against a 365-day interval while 1 hour is also negligible against a 7-day interval — the MTTR term never gets to matter. The intuition that "the system that repairs faster is the more available one" fails here precisely because neither system is repair-bound. If instead MTTR had been comparable to MTBF — say A's repair took months — the conclusion would flip. Availability only rewards fast repair when repairs are frequent enough for the repair time to be a significant share of the cycle.

## Common Pitfalls

- **Confusing MTTF with MTBF.** MTTF is time to first failure; MTBF is the interval between failures, and the availability formula uses MTBF.
- **Using MTBF in the numerator with the wrong denominator.** Availability = MTBF/(MTBF+MTTR); a ratio of the two without the sum is not availability.
- **Assuming the more reliable system is automatically the more available one.** The exercise above shows availability is a trade-off, and both terms matter.
- **Treating integrity, security, and resilience as the DSSA triple.** They are on a separate slide, and the exam distinguishes the "attributes (source: DSSA)" slide from the "other properties" slide.
- **Reading "availability" as uptime percentage without accounting for repair time.** The failure frequency alone decides the comparison whenever MTTR is small relative to MTBF.
- **Forgetting the independence assumption.** The 1000-components calculation assumes independent failures; the slide says malicious faults break that.
- **Ignoring the specification.** A metric without a stated specification has no referent, which is exactly the slide's first open question.

## Connections

- [[fault-error-failure-chain]] — the failure event whose timing MTTF, MTBF and MTTR measure.
- [[ways-towards-dependability]] — the four intervention strategies are chosen to move these metrics.
- [[error-detection-and-recovery]] — MTTR is only as good as the recovery machinery.
- [[redundancy-forms]] — the classic lever for raising availability by shortening effective repair or covering failures.
- [[availability]] — the general availability notion these metrics instantiate.
- [[dependable-distributed-systems]] — the course framing.

## Open Questions

- The slides never quantify "high probability" nor say what mission period the probability metric should be evaluated over.
- It is not stated whether availability in this framework includes the security dimension, given that security is defined as guaranteeing availability of the service.
- The slides do not say how availability should be aggregated across a distributed system from per-component MTTF and MTTR, and independence is asserted as an assumption rather than defended.
- The relationship between resilience (recovering from external faults) and the DSSA attributes is left implicit; the source gives no criterion for when the "other properties" slide should be preferred over the DSSA triple.
- The exercise's numbers for the two systems appear in the lecture material, but the slides do not show the full worked arithmetic, so the exact rounding convention for the 0.318 percentage point difference is not specified.
