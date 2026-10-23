---
title: "Fault, Error, Failure Chain"
tags: [concept, dependable-distributed-systems, semester-2, dependability]
course: "Dependable Distributed Systems"
source_count: 5
status: current
last_updated: 2026-10-21
prerequisites: ["[[dependability-attributes]]"]
---

## One-line Summary
A fault is a broken part, an error is the broken state that part creates, and a failure is what the user finally notices when the service stops doing its job.

## Core Intuition

The distinction is a chain of responsibility. Hardware does not "fail" in the sense a user cares about; it first *misbehaves* in a way that may or may not propagate. A single flipped bit in a register is not yet a problem for the person using the service. It becomes a problem when that wrong value is read back and the answer handed out is wrong.

Dependability engineering exists to interrupt this chain at the earliest affordable link. Detecting the fault early is cheap; detecting the failure late is expensive and user-visible. This is why the lecture puts error detection at the front of the fault-tolerance machinery (see [[error-detection-and-recovery]]): the sooner the chain is broken, the less of the system needs repairing.

The word *adjudged* in the definition of fault matters. A fault is not an intrinsic physical property of a component but a *cause assigned by an observer*. Two engineers can look at the same wrong output and disagree about whether the cause was a memory cell, a software bug, or a bad input. The fault notion only exists relative to a system and to a level of analysis — which is why the slide insists that "these notions are for a system".

## Formal Definition / Statement

For a given system, the lecture (DSSA lineage) gives three linked notions:

| Notion | Definition as given | Where it lives |
|---|---|---|
| **Failure** | Occurs when the delivered service deviates from fulfilling the system function | The service boundary, as observed by the user |
| **Error** | That part of the system state which is liable to lead to subsequent failure | The internal state of the system |
| **Fault** | The adjudged cause of an error | Somewhere in the environment, the hardware, or the software |

The propagation direction is therefore:

```
fault  ->  error  ->  failure
(cause)    (latent state)   (observable deviation)
```

A fault may or may not produce an error. A fault that is dormant, or that is masked before it can corrupt anything, never becomes a failure. Conversely, an error need not be caused by a hardware fault; a pure software defect produces an error just as legitimately, with the "fault" adjudged as the defective program or design.

The chain is **recursive**. The slide attributes this observation to Paulo Verissimo: the same three notions apply one level down, so a "fault" in a component is an "error" in the containing system. That is exactly the question the slide poses back: "What is a system? What is a component?" Whether a given unit is the system under study or a component of it is a modelling decision, and the same event can be a failure at one level and a fault at the next.

## Key Properties

- **Failure is external, error is internal.** A failure is defined by the deviation of the *delivered service* from the system function; an error by a property of internal state.
- **Errors are latent.** An error is "liable to lead to" failure — it is a risk, not yet a fact.
- **Faults are adjudged, not observed.** The cause is a judgement made about a symptom.
- **Not every fault becomes an error.** Faults can be dormant, avoided, or masked.
- **The chain is level-relative.** Faults of components are errors of the system; errors of the system are failures of the service.
- **Distribution multiplies the chain's length.** A failure of one component can influence others, and communication over unreliable networks with unpredictable delays can turn a local error into a remote failure (see [[communication-link-models]] and [[synchronous-vs-asynchronous-models]]).
- **Malicious faults break the statistical model.** Attacker-induced errors are no longer independent, are more serious, and make error models inaccurate (see [[security-relationship-model]]).

## Worked Example

The slide's own example takes the system to be a **RAM memory**, and the component to be a single memory register.

1. **Fault.** One register is *stuck at '0'*. Physically, the cell can no longer hold a 1. Nothing is wrong yet with the service; the register is simply degraded.
2. **Error.** The program writes '1' into that register. The write appears to succeed, but the internal state of the memory now differs from the intended state — the register holds '0' where it should hold '1'. That divergence is the error: a part of the system state liable to lead to failure.
3. **Failure.** Later the program reads the register back and receives '0'. The delivered service now deviates from the system function of returning what was written, so the memory has failed.

Note the ordering. A system can be failing repeatedly while the error stays constant — each read re-observes the same corrupted state. And a recovery action that simply rewrites '1' would be a roll-back style fix, one of the strategies described in [[error-detection-and-recovery]].

The recursivity is visible in the same example: viewed at the level of a larger machine, the register's stuck-at-'0' is a *fault*; viewed at the level of the register itself, it is a *failure* of that component. The labels slide with the zoom level, and that is the point Verissimo is making.

## Common Pitfalls

- **Using the three terms interchangeably.** Exam questions target exactly this. If a component is broken, that is a fault for the system, not a failure of the system.
- **Saying a fault "is" an error.** They are related by propagation, not by identity. A fault can exist with no error at all.
- **Forgetting the observer.** A fault is the *adjudged* cause, so two observers can disagree about the same event. Answers that give a cause without naming the system boundary are incomplete.
- **Ignoring the recursion.** Treating fault/error/failure as a flat one-way list for the whole system misses the slide's explicit point that the relation is recursive.
- **Assuming every fault is a hardware fault.** Software defects and bad designs also produce errors, and design faults are exactly what [[redundancy-forms]] and error masking cannot cover.
- **Overreading "failure".** A failure requires a deviation of the *delivered service*, not merely a change in internal state. No failure means the service was still correct.

## Connections

- [[dependability-attributes]] — the metrics (MTTF, MTTR, availability) are all defined in terms of the failure event that this chain defines.
- [[ways-towards-dependability]] — fault prevention, removal, and forecasting are all interventions on the fault end of the chain; fault tolerance is an intervention after the fault appears.
- [[error-detection-and-recovery]] — detection is about catching the error before it becomes a failure, and recovery is about reversing the propagation.
- [[failure-models]] — a failure model is a probabilistic statement about where in this chain faults enter and how often.
- [[dependable-distributed-systems]] — the course that introduces the whole vocabulary.

## Open Questions

- The slides give the RAM example but never say how one decides, in a concrete system, at which point in the chain a given observation should be adjudged a fault rather than a design issue. The adjudication step is left to the engineer with no procedure supplied.
- The recursion is asserted but not resolved: the slides do not say where the recursion should be cut, i.e. what the "system" boundary is in practice for a given distributed service.
- The slides do not say how the fault-error-failure chain should be extended when faults are malicious; they only assert that the classical error models become inaccurate, without proposing a replacement (see [[model-accuracy-tractability]]).
- How much the failure notion changes when the "system" includes the network is not settled — the slides note that communication is unreliable, but do not say whether a lost message is a fault of the network, an error of the sender, or a failure of the service.
