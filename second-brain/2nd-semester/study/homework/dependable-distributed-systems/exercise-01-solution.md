---
title: "Exercise 1 — Distributed Systems and Dependability (Solutions)"
tags: [homework, dependable-distributed-systems, semester-2]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-21
prerequisites: []
---

# Dependable Distributed Systems — Exercise 1

Source: `dds26-exercise01.pdf` (Reiser, WS 2026/27, discussion 14 October 2026).
The sheet's instruction: **"Prepare answers before the exercise class. In class you will present
them."** Every task below is answered; 1.3(c) is computed and the arithmetic is checked
mechanically in `logical-clocks.py`.

---

## 1.1 Which group of properties is characteristic for any distributed system?

T = true, F = false.

| Statement | Answer | Why |
|-----------|--------|-----|
| Independent computers, connected by a communication network, **synchronized clocks** | **F** | Garg's three defining absences include "No common clock — distributed local clocks can be synchronized with only limited accuracy". Synchronised clocks are not a property any distributed system has. |
| Independent computers, **common shared memory**, asynchronous communication network | **F** | "No shared memory — common state not stored centrally; observing global system properties difficult". |
| Messages-based communication, common task, **common shared memory** | **F** | Same absence. Note the trap: a "common task" is a property of the *application*, not a distributed-system property. |
| Multiple independent computers, **no common clock, no shared memory** | **T** | This is Garg's list, minus the third item ("No exact failure detection"), and every item is correct. |

**Three of the four are false, and they are false for the same reason.** The exercise is testing
whether "distributed" is understood as a set of *absences* rather than a set of features. A
distributed system is defined by what it does not have: no common clock, no shared memory, no
exact failure detection.

---

## 1.2 Which attributes are essential characteristics of a dependable distributed system?

| Statement | Answer | Why |
|-----------|--------|-----|
| **Reliability, Maintainability, Availability** | **T** | These are exactly the three DSSA dependability attributes, with MTTF/MTBF, MTTR, and MTBF/(MTBF+MTTR) as their metrics. |
| Portability, Scalability, Reliability | **F** | Only one of the three is a dependability attribute. Scalability is a *motivation* for distribution, not a measure of dependability. |
| Safety, Security, Integrity | **F** | These are the "other properties" slide, not the three dependability attributes. Security is explicitly *not* one of the three in this course's framing. |
| Timeliness, Availability, Cost-effectiveness | **F** | Only availability is on the list. "Cost-effectiveness" is not a dependability attribute. |

The distinction the exercise wants: the three **dependability attributes** are reliability,
maintainability, and availability. Integrity, security, and resilience appear on a *separate*
slide as "other properties" — adjacent, but not the core three.

---

## 1.3 Dependability

### (a) How does dependability differ from reliability?

**Dependability** is the umbrella: the quality of a delivered service such that reliance can
justifiably be placed on it (Laprie 1993). **Reliability** is one attribute *inside* that
umbrella: the continuous delivery of correct service.

The difference is scope, not degree. Reliability asks "does it keep working?" and is measured by
MTTF, MTBF, and the probability of no failure during a mission period. Dependability asks the
larger question: "can you *rely* on this service?" — which also requires that a failure be
*repairable* (maintainability) and that correct service be *delivered* rather than merely
attempted (availability). A system that never fails is trivially reliable and not necessarily
dependable, because nothing says it can be kept running.

### (b) The three attributes and their measures

| Attribute | Definition (slide) | Measure |
|-----------|--------------------|---------|
| **Reliability** | Measure of the continuous delivery of correct service | MTTF (Mean Time To Failure), MTBF (Mean Time Between Failures), probability of no failure during a mission period, probabilistic failure rate (e.g. 10⁻⁹ failures/hour) |
| **Maintainability** | Measure of the time to restoration of correct service | MTTR (Mean Time To Repair) |
| **Availability** | Measure of the delivery of correct service with respect to the alternation between correct and incorrect service | Availability = MTBF / (MTBF + MTTR) |

Note the structure: availability is *derived* from a reliability metric and a maintainability
metric. It is the only one of the three that is a ratio rather than a time.

### (c) Which system is more available?

| | MTBF | MTTR | Availability = MTBF/(MTBF+MTTR) | Downtime fraction |
|---|---|---|---|---|
| **A** — fails once per year, one day to repair | 8760 h | 24 h | **0.997268** | 0.002732 |
| **B** — fails once per week, one hour to repair | 168 h | 1 h | **0.994083** | 0.005917 |

**System A is more available**, by 0.318 percentage points.

The interesting part is *why*, because the naive intuition gets it wrong. A's MTBF is about 52×
longer than B's, but A also needs 24× longer to repair. One might expect those to cancel. They
do not: 24 hours is negligible against a 365-day failure interval (0.27% downtime), and 1 hour is
negligible against a 7-day interval (0.59%). Both repair times are dwarfed by their own failure
intervals, so the failure rate decides the comparison outright.

**Availability is not "how often" but "how long."** MTTR only becomes decisive when repair time
approaches the failure interval — which is the regime of a system that fails constantly and
takes a long time to fix. The slide's own framing is the same: availability measures "the
alternation between correct and incorrect service", so it is a *duty cycle*, not a failure count.

---

## 1.4 Errors, failures, and faults

### (a) Causal order and definitions

The causal order is **fault → error → failure**. The fault comes first in time and last in
consequence: it is the cause whose visible effect is a failure.

| Term | Definition (slide) | In one sentence |
|------|--------------------|-----------------|
| **Fault** | "The adjudged cause of an error" | The underlying defect — the thing that was wrong to begin with. |
| **Error** | "That part of the system state which is liable to lead to subsequent failure" | The corrupted internal state, which *may* but need not yet be visible. |
| **Failure** | "The delivered service deviates from fulfilling the system function" | The user-visible deviation from the specification. |

"Adjudged" is the operative word for fault: a fault is the cause *we have identified*. And note
the slide's warning: **"These notions are for a system!"** — a given event can be a failure of
one component and a fault of the larger system it belongs to. The chain is recursive, which is
why the "What is a system? What is a component?" question on the slide has no final answer: it
depends on the level you are reasoning at.

### (b) The uninitialized C variable

```c
int f() { int x; return x; }   /* x never initialized */
```

| Element | Identification |
|---------|----------------|
| **Error** | The function reads `x` while it holds an indeterminate garbage value — the erroneous part of the system state, liable to lead to failure. |
| **Failure** | The program crashes. The delivered service (running the program correctly) deviates from the system function. |
| **Fault** | The programmer's omission of the initialisation — the adjudged cause of the error. |

The ordering is the teaching point: the fault (a missing line of code) is present from the
moment the program is written, the error (a garbage register value) exists only in the instant
the function is called, and the failure (the crash) is the only one an observer of the running
system sees. The three are three different moments, which is exactly why the taxonomy needs
three words.

### (c) A second example

**A fan bearing seizes in a server.** The fault is the physical bearing wear; the error is the
rising temperature and the resulting erroneous fan-speed readings; the failure is the machine
throttling itself and dropping requests. The observation from the slides' RAM example carries
over: identifying the fault is a different activity from detecting the error, and both differ
from the failure the user sees.

---

## 1.5 How to get there

The lecture distinguishes four approaches. Assigning each measure:

| Measure | Approach | Justification |
|---------|----------|---------------|
| **(a)** Code review and testing before release | **Fault removal** | It reduces the *number/severity* of faults by verification and validation in the design phase — the slide's own pairing of V&V with the design phase. (It also reduces design defects, which is prevention, but the primary act is finding and removing faults that already exist in the code.) |
| **(b)** Storing the same data on three disks and reading a majority | **Fault tolerance** | It delivers correct service *in the presence of* faults, using space redundancy and error masking. No fault is prevented, removed, or forecast — the system simply continues. |
| **(c)** Estimating how often a disk model fails, from field data | **Fault forecasting** | It estimates the *future incidence* of faults, using historical data from real systems. |
| **(d)** Choosing a language in which an uninitialized variable does not compile | **Fault prevention** | It prevents the *occurrence* of faults by avoiding design defects through tooling and good process. |

The four-way split is worth memorising as four different questions: prevention asks "how do we
stop it happening?", removal "how do we reduce what is already there?", forecasting "how often
will it happen?", and tolerance "how do we cope when it does?". Each measure answers exactly one
of them, and (b) is the one this course is about — fault tolerance is the lecture's stated main
topic.

---

## 1.6 Problems in distributed systems

### (a) The most important practical problems, focusing on those that algorithms should solve

The lecture's own property list is the backbone: independent failures, unreliable communication,
variable delays, and only a partial ordering of events. Layered on top are the problems the
semester plan names. Ranked by how much they demand from algorithms:

**Consensus and agreement.** When several nodes must all decide the same thing, and some of them
may fail, a protocol must guarantee that the correct nodes agree, that they do not agree on
something wrong, and that a decision eventually happens. This is the problem that motivates
failure detectors: you cannot distinguish a crashed node from a slow node without making a
timing assumption, and every consensus protocol is therefore a statement about which failure
model it assumes. The exercise 2 sheet's fail-silent model makes this concrete: in an
asynchronous system, "failure not distinguishable from slow node" is a modelling fact, not a
technical inconvenience.

**Replicated systems and consistency.** Replication buys availability and fault tolerance at the
price of agreement. Which updates may be kept, which must be discarded, and what a client
observes after a partition are all algorithmic questions. The course plan's "eventual
consistency and CRDTs" is the resolution — a data type designed so that concurrent updates
converge without needing to be ordered, which is exactly what [[vector-clocks]] makes detectable.

**Group communication and ordering.** A broadcast that all nodes receive in the same order
requires agreement on the order, and the rules for who may broadcast what (membership changes
make this hard) are algorithmic. This is where the causal order from logical clocks stops being
an academic exercise and becomes a protocol requirement.

**Byzantine faults.** Under arbitrary behaviour — including malicious — the requirement on
replication changes fundamentally, and the guarantees that hold under crash failure no longer
hold. Because the fault hierarchy is nested (see [[failure-models]]), every protocol that
tolerates Byzantine faults also tolerates everything below it, but the reverse is false: a
crash-tolerant protocol is not automatically Byzantine-tolerant. The cost of that extra
generality is the practical content of lecture 8.

**Partially synchronous behaviour.** Real systems are neither fully synchronous nor fully
asynchronous. Partial synchrony — the network is asynchronous for a while, then behaves — is
the model under which most practical protocols are correct, and getting the timing assumptions
right is an algorithmic problem rather than a modelling preference.

**Distributed coordination and self-organisation.** Mutual exclusion, leader election, and
termination detection all need to work when the participants may fail, and the Zookeeper-style
services in the plan are the industrial form of that.

**What is not an algorithmic problem.** Administrative cost, the sheer price of the hardware,
and the difficulty of operating a large fleet are real problems, but they are not solved by a
distributed algorithm. The exercise explicitly asks for the algorithmic subset, and the list
above is that subset.

### (b) Which of these are especially interesting, and what should the lecture cover more of?

Two, for different reasons.

**Consensus and failure detectors**, because they are where the three models meet. Every
consensus algorithm is a bet on a failure model, and the failure detector is the mechanism that
makes the bet explicit. A protocol that works under crash but not Byzantine, or under
synchronous but not asynchronous, is not a weaker protocol — it is a protocol with a different
contract. Understanding which contract you have bought is more valuable than knowing any single
protocol.

**Partially synchronous behaviour and the time models**, because the course opens with the
synchronous/asynchronous dichotomy and the semester plan promises NTP and PTP in the same
breath. The synchrony material is not a preliminary to be got through; it is the assumption
layer underneath consensus, group communication, and the Byzantine work. More coverage of the
partial-synchrony spectrum — the slide mentions partial synchrony, timed-asynchronous, and
wormholes and then defers them — would pay off several times over in the later lectures.

I would also like the course to keep returning to the **fault → error → failure** chain, because
it is the frame that makes the failure-model hierarchy concrete: choosing a failure model is
choosing where in the chain you promise the system will behave correctly.

---

## Connections

- [[dependable-distributed-systems-exercise-2]] — the follow-up sheet, which applies the same
  reasoning to models and logical clocks.
- [[dependability-attributes]] — the definitions 1.2 and 1.3 test.
- [[fault-error-failure-chain]] — the taxonomy 1.4 applies, including its recursive nature.
- [[ways-towards-dependability]] — the four approaches 1.5 asks you to assign.
- [[distributed-system-properties]] — the property list behind 1.1.
- [[failure-models]] — the hierarchy behind 1.6(a).
- [[model-accuracy-tractability]] — why 1.6(a) must be answered per model, not globally.

## Open Questions

- The sheet does not say how the exercise answers are graded, whether a grade is attached to the
  presentations at all, or whether the 1.6 opinion question is assessed on the opinion or on the
  supporting argument.
- 1.6(b) explicitly asks what "you want to learn more in this lecture" — an answer that is
  correct in April may be wrong in December once the later lectures are known.
- The 12-topic semester plan is explicitly preliminary, so the balance 1.6 asks about is not
  fixed.
