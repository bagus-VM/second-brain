---
title: "Safety and Liveness Properties"
tags: [concept, dependable-distributed-systems, semester-2, specification]
course: "Dependable Distributed Systems"
source_count: 1
status: current
last_updated: 2026-10-30
prerequisites: ["[[distributed-system-properties]]"]
---

## One-line Summary
Every distributed-systems property is either safety (something bad never happens) or liveness
(something good eventually happens), and the two need completely different proof techniques.

## Core Intuition

A safety property says that some event must never happen. It is a predicate P that is **always**
true: if a violation occurs, it occurs at a finite, identifiable point in the execution, and a
finite prefix of the run is enough to prove the property broken. Integrity ("a message is
delivered at most once") is safety, and so is every "never deliver before X" ordering rule.

A liveness property says that some good event eventually happens. It is a predicate P that
**eventually** becomes true. No finite prefix of a run can ever refute it, because the good event
may still be one step away; only a complete infinite execution can. Termination is the standard
example.

The lecture's warning about language: "eventually" is not the German *eventuell* (possibly). "X
eventually happens" means X **will** happen, within an unspecified but finite amount of time.
Reading "eventually" as "maybe" inverts the meaning of every liveness property in the course.

## Formal Statement

- **Safety**: a property defined by a predicate P such that P holds in every state of every
  execution. Violations are detectable in finite time.
- **Liveness**: a property defined by a predicate P that eventually holds in every execution.
  Violations are detectable only on infinite executions.

The lecture's worked example is a factorization algorithm `Fac(n)` with the compound claim: "if
`Fac(n)` is started with an argument n that is the product of two primes, `Fac` will output
p₁ > 1, p₂ > 1 with p₁ · p₂ = n." That single sentence mixes both kinds:

- *Liveness*: the algorithm eventually terminates (started with an arbitrary integer n as
  argument).
- *Safety*: if it terminates with output {p₁, …, p_k}, then every pᵢ is a prime greater than 1
  and the product of the pᵢ is n.

## Key Properties

- **Different proof burdens.** Safety is proven by induction over execution states; liveness needs
  a progress argument (well-founded ranking, fairness assumptions, or a model restriction such as
  synchrony).
- **Model restrictions buy liveness.** "Termination" fails the moment a process crashes unless
  the model excludes crashes, which is why exercise sheets keep restricting the fault model
  before promising termination.
- **Verification prefers many minimalistic properties** over one compound claim: each small
  property is either pure safety or pure liveness, and the proof technique applies cleanly. The
  broadcast catalogue of lecture 4 is built exactly this way (Validity, Agreement, Integrity as
  separate named properties).

## Worked Example

The broadcast specification slide (lecture 4, slide 40) classifies cleanly:

- Integrity (at most once, only if broadcast): safety.
- FIFO/Causal/Total order (never deliver m′ before m): safety.
- Validity (a correct broadcaster eventually delivers): liveness.
- Agreement (if one correct process delivers, all eventually do): liveness.

Exercise 4.7 shows the liveness side's dependence on the model: the coordinator algorithm
terminates only because the model promises no crashes and perfect links. Remove either and the
same algorithm has no liveness argument left.

## Common Pitfalls

- **Reading "eventually" as *eventuell***, i.e. as permission to not terminate. The lecture flags
  this as a false friend; liveness guarantees occurrence.
- **Proving a compound property in one go.** Split it; the safety half and the liveness half have
  different proofs.
- **Assuming a finite counterexample refutes liveness.** It cannot; only an infinite execution
  can.
- **Forgetting that liveness claims usually hide a fairness or model assumption.** "Every correct
  process eventually decides" assumes messages eventually arrive, which is a link property, not a
  consensus-algorithm property.

## Connections

- [[distributed-system-properties]] — the general frame the two kinds of property sit in.
- [[reliable-broadcast-and-echo-algorithm]] — the specification whose properties split cleanly
  into safety and liveness.
- [[synchronous-vs-asynchronous-models]] — the model assumptions that make liveness provable.
- [[fault-error-failure-chain]] — what "bad event" means in this course's fault taxonomy.

## Open Questions

- Slide 5a poses the classification question for `Fac(n)` and slide 6 answers it by splitting the
  property; the lecture gives no second example, so the classification skill has exactly one
  worked instance in the material.
- The course has not yet introduced formal temporal logic; the predicates remain informal.
