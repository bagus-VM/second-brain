---
title: "Dependable Distributed Systems"
tags: [course, semester-2, dependable-distributed-systems]
professor: "Prof. Dr. Hans P. Reiser"
semester: "WS 2026/27"
exam_date: "TBD"
credits: "TBD"
language: "English"
source_count: 8
status: active
last_updated: 2026-10-23
prerequisites: []
---

## One-line Summary
The same professor as Machine Learning for Cybersecurity, but a different discipline: how to build
distributed systems that keep working when machines crash, lie, or vanish — and the price of
every assumption you make about timing and failure.

## Course Information

- **Instructor:** Hans P. Reiser (ITZ 137, hr@sec.uni-passau.de), Chair for Digital Security, FIM
- **Secretary:** Anuschka Loibl (ITZ 130), digisec@uni-passau.de
- **Course number:** 5880V/UE
- **Format:** weekly — **lecture Monday**, **exercise class Wednesday**
- **Language:** English (unless all participants agree otherwise)
- **Prerequisite:** "Good basic understanding of computers, networks, operating systems, and
  distributed systems"
- **Material:** slides as PDF on Stud.IP; exercise questions published on Stud.IP
- **Exercise rule:** "In the exercise classes, YOU shall try to answer all questions on your own
  . . . and then present your solutions." **Preparation and presentation are both required.**
- **Literature:** Cachin/Guerraoui/Rodrigues, *Introduction to Reliable and Secure Distributed
  Programming* (Springer, 2nd ed. 2011); Raynal, *Concurrent Programming* (2013);
  Veríssimo/Rodrigues, *Distributed Systems for System Architects* (2001, Parts I and II); Garg,
  *Elements of Distributed Computing* (2002); Koren/Krishna, *Fault-Tolerant Systems* (2007)

## Goals of the Lecture

From the slides: in-depth understanding of distributed systems which consist of many
participants, have a high level of complexity, process large amounts of data, must be
fault-tolerant, and must be secure. **Main focus: distributed algorithms.**

## Semester Overview (preliminary plan)

1. Basic concepts of dependable distributed systems
2. Models, logical and physical clocks, and time synchronization
3. Network Time Protocol and Precision Time Protocol
4. Fault tolerant group communication
5. Consensus and failure detectors
6. Replicated systems
7. Paxos algorithm
8. Byzantine fault-tolerant replication
9. Blockchain / Distributed Ledger Technology
10. Eventual consistency and CRDTs
11. Distributed coordination services (Zookeeper) and data storage (GFS etc.)
12. Decentralized self-organizing systems (P2P systems)

Only items 1–3 have slides in `raw/`; the rest are announced but not yet delivered. Item 3 was
delivered as NTP only — the deck's own section 5, "Other algorithms", has no slides, so **PTP is not
in the ingested material** despite being promised by this plan.

## Lecture Index

Overview pages:
- [[dependable-distributed-systems-lecture-1]] — Organisation, distributed systems, fault tolerance
  basics, ways towards dependability
- [[dependable-distributed-systems-lecture-2]] — Models of distributed systems, the relevance of
  time, logical clocks
- [[dependable-distributed-systems-lecture-3]] — Physical clock synchronization: offset measurement,
  CNV, NTP
- [[dependable-distributed-systems-exercise-1]] — Exercise 1 (14 Oct 2026)
- [[dependable-distributed-systems-exercise-2]] — Exercise 2 (21 Oct 2026)
- [[dependable-distributed-systems-exercise-3]] — Exercise 3 (28 Oct 2026)

| # | Topic | Source | Status |
|---|-------|--------|--------|
| 1 | Organisation, Introduction: distributed systems, fault tolerance basics, ways towards dependability | `dds2026w-01-intro.pdf` | ingested → [[dependable-distributed-systems-lecture-1]] |
| 2 | Models of distributed systems, relevance of time, logical clocks | `dds2026w-02-time.pdf` | ingested → [[dependable-distributed-systems-lecture-2]] |
| 3 | Physical clock synchronization: background, offset measurement, CNV, NTP, clock discipline | `dds2026w-03-ntp.pdf` | ingested → [[dependable-distributed-systems-lecture-3]] |
| E1 | Exercise 1: distributed systems, dependability, fault/error/failure | `dds26-exercise01.pdf` | ingested → [[dependable-distributed-systems-exercise-1]] |
| E1 | Official solutions to exercise 1 | `dds26-exercise01-sol.pdf` | cross-checked against the written answer — see below |
| E2 | Exercise 2: models, logical clocks, fault tolerance | `dds26-exercise02.pdf` | ingested → [[dependable-distributed-systems-exercise-2]] |
| E2 | Official solutions to exercise 2 | `dds26-exercise02-sol.pdf` | cross-checked against the written answer — see below |
| E3 | Exercise 3: clock measurement, CNV simulation, transport choice | `dds26-exercise03.pdf` | solved → [[dependable-distributed-systems-exercise-3]], `study/homework/…/exercise-03-solution.md` |

## The official solutions, and what they changed

Both solution PDFs arrived after the written answers were produced, and both were used as a
cross-check rather than as an answer key. Three differences came out of it:

- **1.3(c) availability arithmetic.** The written answer uses a 168-hour cycle for "fails once per
  week" (MTBF 168 h, MTTR 1 h → 0.994083). The official solution uses MTBF = 167 h, MTTR = 1 h →
  0.994048, i.e. it counts the repair hour inside the weekly cycle. Same verdict (system A is more
  available), slightly different number. The official convention is the cleaner one.
- **2.1 is genuinely ambiguous, and the official solution says so.** Its answer splits the question:
  read as "is the *process behaviour* synchronous", yes — a week is a finite bound; read as "is the
  *distributed system* synchronous", no — the statement says nothing about the network. The written
  answer led with "formally yes" and reached the same second half by a different route; the official
  framing is sharper and is the one to present.
- **2.2(a) carries an asterisk on the second statement.** The official marking is F/T*/F/F/T, with
  the note that one might argue a model does not let you answer *all* questions about feasibility and
  cost. Everything else agrees, including the Lamport/vector verdicts in 2.3 and the total-order
  construction in 2.5.


## Concept Pages

| Page | One-line idea |
|------|---------------|
| [[distributed-system-properties]] | What makes a system distributed: the network is not the system, and the three things every distributed system lacks |
| [[dependability-attributes]] | Reliability, maintainability, availability — and the metric that belongs to each |
| [[fault-error-failure-chain]] | Fault causes error causes failure, and the chain repeats at every level of the system |
| [[ways-towards-dependability]] | Prevention, removal, forecasting, tolerance — four answers to "how do we get dependability" |
| [[error-detection-and-recovery]] | Detecting the error, then handling it: roll-back, roll-forward, or mask it |
| [[redundancy-forms]] | Space, time, and value redundancy — the three ways to have something to spare |
| [[failure-models]] | Crash, fail-stop, fail-silent, crash-recovery, eavesdropping, Byzantine — and how they nest |
| [[communication-link-models]] | Fair-loss, stubborn, perfect, authenticated perfect — what the channel promises |
| [[synchronous-vs-asynchronous-models]] | Asynchronous is a non-assumption; synchronous is a promise that buys cheaper protocols |
| [[lamport-logical-clocks]] | A counter per process that orders events without a clock, and only where it must |
| [[vector-clocks]] | One counter per process: exact causal order, paid for in message size |
| [[clock-synchronization-problem]] | Physical clocks drift, and a consistent checkpoint is the first thing that breaks |
| [[resilience-vs-dependability]] | Two definitions of resilience that do not mean the same thing |
| [[model-accuracy-tractability]] | Accuracy is easy, tractability is not, and you need both |
| [[physical-clock-drift]] | Offset, frequency error, environment — and the seven questions you ask of any synchronisation algorithm |
| [[tai-utc-time-scales]] | The second is caesium, the day is the Earth, and leap seconds are the patch between them |
| [[time-offset-measurement]] | One timestamp gives an unbounded error, four give one bounded by half the round trip |
| [[convergence-algorithm-cnv]] | Average with a δ clamp and the group holds together — unless a third of it lies |
| [[network-time-protocol]] | Strata, eight-sample filters, and three stages of peer selection |
| [[ntp-clock-discipline]] | Phase control for jitter, frequency control for drift, both at once |

## Homework

| Sheet | Deliverable | State |
|-------|-------------|-------|
| Exercise 1 (14 Oct 2026) | `study/homework/dependable-distributed-systems/exercise-01-solution.md` | written, every task answered; **cross-checked** against `dds26-exercise01-sol.pdf` |
| Exercise 2 (21 Oct 2026) | `study/homework/dependable-distributed-systems/exercise-02-solution.md` + `logical-clocks.py` | **run**: Lamport and vector timestamps computed and verified over all 175 linear extensions; **cross-checked** against `dds26-exercise02-sol.pdf` |
| Exercise 3 (28 Oct 2026) | `study/homework/dependable-distributed-systems/exercise-03-solution.md` + `clock-sync.py` | **run**: CNV implemented and simulated over 7 scenarios, the worst Byzantine lie brute-forced, all four measurements computed |

## Connections

- [[machine-learning-for-cybersecurity]] — the same instructor, the same chair, the same Stud.IP
  culture; that course is a portfolio with in-class presentations, this one has a weekly
  presentation obligation built into the exercise format.
- [[security-relationship-model]] — the security vocabulary from the Advanced IT Security course,
  which this lecture's dependability taxonomy sits next to.
- [[cia-triad]] — the Semester 1 availability definition, which this lecture re-derives as a
  quantitative metric.
- [[availability]] — the Semester 1 treatment of availability as a security property.
- [[fault-tree]] — the Semester 1 failure-analysis technique, complementary to this course's
  fault → error → failure chain.
- [[runtime-system]] — the Semester 2 Virtual Machines course, which supplies the process and
  memory substrate this lecture assumes.

## Open Questions

- **Exam format, date, and credit points are not in the slides.** The course number carries
  "V/UE" (lecture/exercise), and the exercises are presented in class, but no exam announcement
  has arrived. It is not guessed here.
- **Which of the twelve semester topics will actually be delivered?** The plan is called
  "preliminary".
- **How is the weekly exercise presentation graded?** The slides say "in class you will present
  your solutions" but give no weighting, no credit points, and no statement of whether
  participation is mandatory.
- **The professor's own Lamport example on slide 34 does not satisfy the rule printed on slide 33.**
  His P2 begins at 3 where P1 begins at 1. The discrepancy is computed and documented in
  `logical-clocks.py`; whether it is a typo or an unstated convention is unresolved.
- **PTP is promised by the semester plan and absent from the deck.** Lecture 3's own outline lists a
  section 5, "Other algorithms", and then goes straight to the summary. PTP, Cristian's algorithm and
  the Berkeley algorithm are therefore not in the ingested material. Whether they are delivered in
  the exercise class or dropped is not stated.
- **`exercise2-cnv.py` is referenced by exercise 3 but is not in `raw/`.** Task 3.2 asks for
  modifications to that file, so it can only be answered from an independent implementation — which
  is what `clock-sync.py` does, with the substitution recorded on the sheet.
- **Exam format for this course is still unknown**, unlike Introduction to Deep Learning, where
  lecture 1 specified a 90-minute written exam. Nothing in the three lectures or three exercise
  sheets gives a date, a length, a weighting, or whether the exercise presentations count.
