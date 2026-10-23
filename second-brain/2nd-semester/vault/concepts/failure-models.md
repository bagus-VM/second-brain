---
title: "Failure Models"
tags: [concept, dependable-distributed-systems, semester-2, failure-models]
course: "Dependable Distributed Systems"
source_count: 3
status: current
last_updated: 2026-10-21
prerequisites: ["[[distributed-system-properties]]"]
---

## One-line Summary
A failure model is an assumption about how a component in a distributed system is allowed to misbehave, ranging from "stops forever" up to "does anything at all".

## Core Intuition

Every fault-tolerant protocol must answer one question before it can do anything: what kind of badness am I defending against? Answer it badly and the protocol is either useless or needlessly expensive; answer it well and it becomes small.

The lecture frames failure models around *responsibility* rather than components. Every failure model assigns the responsibility for faulty behaviour to a named part of the system — a processor or a communications channel — and then says which behaviours that part may exhibit; everything else is forbidden. The slides underline the point: these are models, that is, assumptions. A failure model is a contract, not a description of reality.

The second framing decision is about what gets counted. Classical work on fault-tolerant computing systems counted *occurrences* of faulty behaviour; this lecture counts *faulty components*. Three faulty processes that each misbehave a thousand times are still three faulty components, so the quantity that matters for a guarantee is a count of nodes — which is why the t-fault tolerant definition speaks of "no more than t of its components being faulty". The taxonomy then nests the fault classes from the weakest (crash) to the strongest (arbitrary): a protocol correct under the arbitrary model is automatically correct under the weaker ones, at a cost.

## Formal Definition / Statement

**Scope.** There are many failure models for distributed systems; all are based on assigning responsibility for faulty behaviour to system components: processors and communications channels.

**Counting convention.** We count faulty components, not occurrences of faulty behaviour. In classical work on fault-tolerant computing systems, occurrences of faulty behaviour are counted.

**t-fault tolerant:** a system satisfies its specification, provided that no more than *t* of its components are faulty. The notation also uses *f* or *k* instead of *t*, and *n* for the total number of nodes.

**Crash.** A process fails by stopping, executing no further steps, and remaining in the crash state forever.

| Variant | Meaning |
|---|---|
| Fail-stop | All other operational processes reliably detect the crash |
| Fail-silent | Other processes are not reliably notified about the crash; if the communication system is not synchronous, it is hard to distinguish a crashed from a slow process |

**Crash-recovery.** A correct process can fail and recover again, for a finite number of times. A process is faulty if it stops forever, or if it infinitely often fails and recovers. Special case **omission**: the fault causes only loss of messages, not loss of local state.

**Eavesdropping faults.** Faulty processes behave as in the crash-recovery model — interactions with other processes occur according to specification or not at all — but in addition faulty processes may pass internal information to an external third party.

**Byzantine faults.** Faulty processes can exhibit arbitrary behaviour. Usually "arbitrary" is restricted to computationally feasible operations; the slide's example is that one cannot break strong cryptography.

**Hierarchy of fault classes** (per RSDP, Cachin et al. 2011). Each outer class is a strict superset of the inner ones.

```
+---------------------------------------------+
|                  Arbitrary                    |
|  +-----------------------------------------+  |
|  |            Eavesdropping                |  |
|  |  +-------------------------------------+|  |
|  |  |         Crash/Recovery              ||  |
|  |  |  +-------------------------------+  ||  |
|  |  |  |          Omission             |  ||  |
|  |  |  |  +-------------------------+   |  ||  |
|  |  |  |  |         Crash          |   |  ||  |
|  |  |  |  +-------------------------+   |  ||  |
|  |  |  +-------------------------------+  ||  |
|  |  +-------------------------------------+|  |
|  +-----------------------------------------+  |
+---------------------------------------------+
```

**Severity of faults (DSSA classification).** A more detailed differentiation of some faults:

- **Assertive faults / value faults:** data in protocol-conforming interactions is modified syntactically or semantically.
- **Omissive faults:** actions do not take place, or take place too late or too early.

## Key Properties

- **Models are assumptions, not observations.** The lecture says so explicitly; a model is a chosen contract.
- **Faults are attributed to components.** Processors and channels are the two places responsibility can be placed.
- **Components are counted, not events.** t is a node count, n the total node count.
- **Detectability is part of the model.** Fail-stop and fail-silent are the same crash behaviour with different observer guarantees.
- **Crash-recovery can repeat.** A finite number of recoveries is tolerated; infinitely often failing and recovering makes a process faulty.
- **Omission is the mildest non-crash case** — messages can be lost, but local state survives.
- **Arbitrary subsumes everything.** A Byzantine-tolerant protocol is automatically valid for the weaker models.
- **Severity is a second axis.** DSSA splits faults into assertive and omissive, orthogonal to the process-level classes.

## Worked Example

Three nodes run a replicated log (n = 3) and the protocol guarantees a service as long as at most t = 1 component is faulty.

Step 1 — fix the model. Assume crash with fail-stop detection: a crashed node stops, and every other node is reliably told. Under that assumption a t = 1 guarantee is implementable — the remaining two nodes hold the majority, and each dead node's slot can be taken over.

Step 2 — check against a stronger model. Raise the assumption to fail-silent and the guarantee no longer follows automatically: without reliable notification, a crashed node and a merely slow node look identical, exactly as the slide warns. The setup would then need timeouts to convert "silent" into "declared dead", and a timeout trades detection accuracy for false positives.

Step 3 — raise it to crash-recovery. A node may now stop and come back, finitely many times. Its local state may or may not have survived, depending on whether the fault is an omission (messages lost, local state kept) or something stronger. The protocol must now tolerate a node rejoining with stale state, which the crash-only design did not need.

Step 4 — raise it to Byzantine. The faulty node may now send arbitrary messages, including conflicting values to different peers. The simple majority rule breaks, and a Byzantine-agreement-style mechanism is needed, which is more expensive. Every step raised the model to a class strictly containing the previous one, so the protocol had to be strengthened; had the original design been written for Arbitrary, all weaker cases would have been covered automatically.

Step 5 — apply the severity axis. A node sending a corrupted value is assertive; a node that never answers is omissive. Both are "arbitrary" behaviour at the process level, but the classification tells an implementation which defence applies.

## Common Pitfalls

- **Treating a failure model as a description of what actually breaks.** These are models, i.e. assumptions; claiming "processes can crash" as a fact about a system conflates the contract with the world.
- **Mixing up fail-stop and fail-silent.** Both are crash; the difference is entirely in what other processes learn, and fail-silent is where the synchrony dependency bites.
- **Misreading the nesting direction.** The source shows nested boxes with Arbitrary outermost and Crash innermost. A common error is to claim Crash is the strongest model, or that the classes are a flat list of alternatives.
- **Counting misbehaviours instead of components.** A process that misbehaves many times is still one faulty component.
- **Overclaiming Byzantine behaviour.** "Arbitrary" is normally restricted to computationally feasible operations — strong cryptography cannot be broken. Absolute arbitrariness would make many guarantees vacuous.
- **Ignoring omission.** Because it appears as a "special case" of crash-recovery, students miss it, though it is a distinct rung of the hierarchy.
- **Expecting the DSSA slide to yield a full diagram.** The text layer gives the two categories with the syntactic/semantic/timing distinctions; the diagram itself is an image, undescribed.

## Connections

- [[distributed-system-properties]] — the structural properties (independent failures, unreliable communication) that failure models quantify.
- [[communication-link-models]] — the channel half of the responsibility assignment; links and processors fail differently.
- [[synchronous-vs-asynchronous-models]] — decides whether a crashed process can be distinguished from a slow one.
- [[fault-error-failure-chain]] — separates the fault assumption from the error and the resulting failure.
- [[model-accuracy-tractability]] — why a weaker, more tractable model is preferred when it suffices.

## Open Questions

- The hierarchy slide cites RSDP (Cachin et al., 2011) but gives no formal inclusion statement beyond the nested boxes, so it is unclear whether Eavesdropping sits strictly inside Arbitrary or is a separate dimension.
- The DSSA severity slide is an image; the text layer does not indicate which other categories the diagram places alongside assertive and omissive faults.
- The slides do not say whether crash-recovery retains local state across a crash in general — omission is described as the one where only messages are lost, which implies the general case may lose state, but this is never stated.
- No numbers are given for how *t* is chosen or bounded relative to *n* per failure class, for crash, Byzantine, or eavesdropping thresholds.
- Whether the exam expects the nested diagram drawn, a "contains" table, or both is not specified in the source.
