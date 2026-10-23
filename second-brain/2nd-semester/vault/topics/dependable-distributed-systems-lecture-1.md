---
title: "Dependable Distributed Systems — Lecture 1 Overview (Introduction and Fault Tolerance)"
tags: [topic, dependable-distributed-systems, semester-2, fault-tolerance]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-21
prerequisites: []
---

## One-line Summary
The first lecture does two jobs: it establishes what a distributed system is and what it
therefore cannot have, then it builds the vocabulary for dependability and the machinery for
achieving it.

## Core Map

```
Lecture 1 — Organisation, Introduction
│
├── Organisation                                    (slides 1-9)
│   ├── Reiser, Chair for Digital Security; Mon lecture, Wed exercise
│   ├── 5880V/UE, English, Stud.IP for slides + questions
│   ├── "In the exercise classes, YOU shall try to answer all questions
│   │    on your own . . . and then present your solutions"
│   └── 12-topic preliminary semester plan
│
├── Introduction: distributed systems                (slides 11-34)
│   ├── "A computer network is not a distributed system"
│   │       -> [[distributed-system-properties]]
│   ├── Tanenbaum: appears to the users as a single computer
│   ├── Garg: no common clock / no shared memory / no exact failure detection
│   └── centralized vs distributed trade-offs
│
├── Fault tolerance: basics                         (slides 36-54)
│   ├── dependability (Laprie 1993)
│   │       -> [[dependability-attributes]]
│   ├── fault -> error -> failure, recursively
│   │       -> [[fault-error-failure-chain]]
│   └── distribution multiplies failures (Lamport's quote)
│
├── Ways towards dependability                      (slides 56-68)
│   ├── prevention / tolerance / removal / forecasting
│   │       -> [[ways-towards-dependability]]
│   ├── error detection, fault handling, error handling, masking
│   │       -> [[error-detection-and-recovery]]
│   ├── space / time / value redundancy
│   │       -> [[redundancy-forms]]
│   ├── Dependability Tree (DSSA), Fault Tolerance Tree (Avizienis et al.)
│   └── resilience vs dependability
│           -> [[resilience-vs-dependability]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[distributed-system-properties]] | A network is infrastructure; a distributed system is processes running a common protocol. What every distributed system lacks: a common clock, shared memory, exact failure detection |
| [[dependability-attributes]] | Reliability (MTTF, MTBF), maintainability (MTTR), availability (MTBF/(MTBF+MTTR)) — and integrity, security, resilience as "other properties" |
| [[fault-error-failure-chain]] | Fault causes error causes failure, and the chain is recursive because a component's failure is the containing system's fault |
| [[ways-towards-dependability]] | Prevention, removal, forecasting, and tolerance answer four different questions about faults |
| [[error-detection-and-recovery]] | Reactive vs proactive detection; then fault handling, roll-back, roll-forward, and masking |
| [[redundancy-forms]] | Space, time, and value redundancy — the three ways to have something to spare |
| [[resilience-vs-dependability]] | Two published definitions of resilience that do not mean the same thing |

## Lecture Structure

1. **Organisation** — instructor, format, literature (Cachin/Guerraoui/Rodrigues as main text),
   the 12-topic preliminary plan, and the instruction that exercise answers are prepared
   individually and then presented in class.
2. **Distributed systems** — a long worked sequence of examples (a car, the Sun datacenter,
   BitTorrent, Sandvine, an Intel system, a gateway/IoT cloud) converging on the definition; the
   slide "A computer network is not a distributed system" separates the two; then Tanenbaum's
   and Garg's definitions, and the centralized-vs-distributed comparison.
3. **Fault tolerance basics** — J. Gray's "everything that works will fail"; the Laprie
   definition; the slide's own open questions about what "high probability" means; Lamport's
   warning that distribution lets a stranger's failure break your machine; the 1000-nodes
   arithmetic; and the note that malicious faults break the independence assumption that the
   arithmetic depends on.
4. **Faults, errors, failures** — the three definitions, the stuck-at-0 RAM example, and the
   recursive structure.
5. **Ways towards dependability** — the four approaches; the elements of fault tolerance
   (detection, recovery, fault handling, error handling, masking); the three forms of
   redundancy; the two taxonomy trees; and two competing definitions of resilience.
6. **Summary** — what to remember: what characterizes a distributed system, the dependability
   attributes, the fault/error/failure chain, the four ways towards dependability.

## Exam-Relevant Points

1. **"A computer network is not a distributed system"** is the highest-yield sentence in the
   lecture. The network is infrastructure; the distributed system is the set of processes and
   the shared protocol. Confusing the two is the classic mistake.
2. **The three absences** (no common clock, no shared memory, no exact failure detection) and
   **the seven properties** built up on the properties slide. Exercise 1.1 tests exactly this.
3. **The three dependability attributes with their metrics**, and the fact that availability is
   *derived* from MTBF and MTTR rather than measured separately. Exercise 1.2 tests the
   distinction between the three attributes and the "other properties" slide.
4. **The fault → error → failure chain, its definitions, and its recursiveness.** Exercise 1.4
   asks for the order, the definitions, and a worked identification.
5. **The four ways towards dependability, each matched to its question.** Exercise 1.5 asks
   you to assign four concrete measures to them.
6. **Availability = MTBF/(MTBF+MTTR)** and the counterintuitive comparison in Exercise 1.3(c):
   the system that fails far less often is more available, because repair time is negligible
   against either failure interval.
7. **The three forms of redundancy** and the specific mechanisms under each.
8. **The difference between error masking and explicit recovery** — masking needs no detection
   and gives the user no glitch, but assumes independent failures and does not handle design
   faults.

## Connections

- [[dependable-distributed-systems]] — the course page.
- [[dependable-distributed-systems-lecture-2]] — the models, time, and logical clocks.
- [[dependable-distributed-systems-exercise-1]] — the exercise sheet that tests this lecture.
- [[machine-learning-for-cybersecurity]] — the same instructor and the same "present in class"
  obligation, in portfolio form.
- [[cia-triad]] — the Semester 1 page on availability as a security property; this lecture
  re-derives availability as a quantitative ratio.
- [[security-relationship-model]] — the Advanced IT Security vocabulary, which shares the
  "safety/security/dependability" conceptual neighbourhood.
- [[fault-tree]] — the Semester 1 failure-analysis technique, complementary to the chain here.
- [[runtime-system]] — the substrate the process and failure models assume.

## Open Questions

- **No exam date, format, or credit points appear anywhere in the slides.** The course number
  says "V/UE"; the rest is not announced.
- The two taxonomy trees (Dependability Tree, Fault Tolerance Tree) are shown as images on
  slides 67–68 with no readable structure in the text layer, so their internal organisation is
  not captured here.
- The "Computer failures" slide cites J. Gray (1985) but gives no figures, so the quantitative
  side of why hardware is "generally overestimated" is not in the material.
- The 12-topic semester plan is explicitly "preliminary", so the course may not cover all of it.
- Whether the exercise presentation obligation carries credit is never stated.
