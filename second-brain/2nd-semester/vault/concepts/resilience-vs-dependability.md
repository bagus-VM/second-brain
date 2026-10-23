---
title: "Resilience vs Dependability"
tags: [concept, dependable-distributed-systems, semester-2, dependability]
course: "Dependable Distributed Systems"
source_count: 3
status: current
last_updated: 2026-10-21
prerequisites: ["[[distributed-system-properties]]", "[[fault-error-failure-chain]]"]
---

## One-line Summary
Dependability is the quality of a service you can justifiably rely on, while resilience adds the requirement that this reliability survives whatever changes the system runs into.

## Core Intuition

The two terms differ by one clause, and the clause is everything: *when facing changes*.

The lecture's baseline is Laprie's 1993 definition of dependability — the quality of a delivered service such that reliance can justifiably be placed on it — sharpened to the operational reading "a dependable system is a system that with high probability works according to its specification". That is a statement about a service under the conditions the specification assumes; it is not a promise that the service keeps working when the assumptions are violated.

Resilience is the extension. Laprie's own later formulation (DSN 2008) is the shortest: the persistence of service delivery that can justifiably be trusted, when facing changes. The word *persistence* matters — it is not that the service never breaks, but that its delivery persists across the disruption. And the changes in question are not only faults: the same word covers the environment around the system, which is why the other lecture slide describes resilience as the ability to recover from external faults, frequently used for applications that require interaction through their surrounding environment.

The Berger et al. formulation (ACM CSUR 2021, a survey on resilience in the IoT) makes the relationship to dependability explicit and adds security: resilience is the property of preserving the dependability *and security* of a system when the system encounters changes, thus withstanding or recovering from impairments. So resilience is not a replacement for dependability; it is dependability plus a requirement about behaviour under change, spelled out as a pair of outcomes: withstanding the change, or recovering from the impairment it caused. This is why the course can teach a fault taxonomy ([[failure-models]]) and still insist that dependability is a quality of a *service*, not of a component. What has to persist is the service.

## Formal Definition / Statement

**Dependability (Laprie 1993):** "Computer system dependability is the quality of a delivered service such that reliance can justifiably be placed on this service."

Restated in the lecture's simple operational form: a dependable system is a system that with high probability works according to its specification.

**Resilience (Laprie, DSN 2008):** "The persistence of service delivery that can justifiably be trusted, when facing changes."

**Resilience (Berger et al., ACM CSUR 2021):** "Resilience is the property of preserving the dependability and security of a system when the system encounters changes, thus withstanding or recovering from impairments."

**Resilience in the property list (lecture 1, slide on other properties):** the ability to recover from external faults; frequently used when considering applications that require interactions through their surrounding environment.

| | Dependability | Resilience |
|---|---|---|
| Object of the claim | The quality of a delivered service | The persistence of service delivery when facing changes |
| Reference point | The specification, under its assumed conditions | The specification, plus changes and impairments |
| What may fail | Components, under the modelled fault assumptions | The environment changes as well as the components |
| Security | Not part of the 1993 formulation | Explicitly included, alongside dependability |
| Outcome language | Works according to its specification, with high probability | Withstanding the change, or recovering from the impairment |
| Source | Laprie 1993 | Laprie, DSN 2008; Berger et al., ACM CSUR 2021 |

## Key Properties

- **Both are claims about a delivered service**, not about a machine. The machine is the vehicle; the service is what is relied upon.
- **Dependability is conditional.** Its force is defined relative to a specification and the fault assumptions under which that specification is meant to hold.
- **Resilience adds a temporal clause:** service delivery must persist while changes occur.
- **Persistence, not perfection.** Resilience does not demand that the service never be interrupted; it demands that delivery can be trusted to persist.
- **"Changes" is broader than "faults".** The environment-facing slide places external faults in scope, and mentions applications that interact with their surrounding environment.
- **Withstanding or recovering.** The Berger formulation allows either outcome: ride through the change, or come back from it.
- **Security is folded in.** Resilience preserves dependability *and* security, so a system that keeps serving but leaks information is not resilient in this sense.
- **The vocabulary follows a fault taxonomy:** dependability is a quality of service, and faults, errors, and failures are the chain through which component defects reach the service.

## Worked Example

Take the gateway/IoT cloud with sensors, actors, edge, core, and IoT services — the architecture shown in lecture 1 as an example of a distributed system — and ask the dependability and resilience questions separately.

Step 1 — the dependability question. Does the service delivered to the user work according to its specification, with high probability, under the assumed fault conditions? Suppose the specification says an actuator command sent to a sensor node is executed, or reported as failed, within a stated deadline, provided that at most t components are faulty and the model assumptions hold. If the system satisfies that, it is dependable in the Laprie sense. The analysis is entirely inside the assumed envelope: a stated t, a stated failure model ([[failure-models]]), a stated link model ([[communication-link-models]]).

Step 2 — change the conditions. The environment changes: the site loses backend connectivity for an hour, a firmware update changes edge-node timing behaviour, or a supplier changes a sensor's calibration. The assumptions may no longer hold. A system can be perfectly dependable under the old conditions and deliver nothing under the new ones, and dependability as defined in 1993 does not speak to this case.

Step 3 — the resilience question. Does service delivery persist, and can it still be justifiably trusted, when facing those changes? Under the Berger formulation, the system must preserve dependability *and security* while withstanding or recovering from the impairment. Concrete strategies this framing suggests: the edge layer buffers and continues to serve locally during the outage (withstanding), the core re-synchronises state when connectivity returns (recovering), and authentication of reconnected devices is enforced so the recovery path does not become a security hole.

Step 4 — check the security half explicitly. Imagine the outage handling is implemented by allowing unauthenticated devices to attach on the local network. The service persists — delivery is trusted and continuous — but the system has not preserved its security. Under Berger et al., such a system is not resilient, however available it is. This is the clearest difference between the two definitions and a natural exam discriminator.

Step 5 — apply Laprie's shorter wording. "The persistence of service delivery that can justifiably be trusted, when facing changes." Persistence is the operative noun: delivery continues to be trustworthy. An implementation that drops service entirely during a change and never tells the user has not delivered persistent service, whatever else it may have preserved. And since the property-list entry says resilience is frequently used for applications that interact with their surrounding environment, the IoT cloud is such an application: it sits in a physical environment that changes independently of the system, so resilience is the natural lens.

## Common Pitfalls

- **Treating resilience as a stronger word for dependability rather than an extension.** Resilience presupposes dependability (Berger: "preserving the dependability and security") and adds the clause about change.
- **Reading resilience as "never fails".** It is about *persistence* of service delivery, not immunity to failure.
- **Dropping the security half.** A common summary drops "and security" from the Berger definition; the source is explicit.
- **Narrowing "changes" to software faults only.** The property-list entry places external faults and environmental interaction in scope.
- **Confusing persistence with continuity.** Persistence of *delivery that can justifiably be trusted*; an unnotified silent degradation of service is a failure of resilience even if the process never crashed.
- **Using the 1993 definition as if it already covered change.** The lecture keeps the 1993 dependability and 2008 resilience definitions on separate slides precisely because they answer different questions.
- **Assuming resilience implies a specific mechanism.** The definitions state an outcome (withstand or recover), not an implementation; redundancy, replication, and graceful degradation are candidates, not the definition.

## Connections

- [[distributed-system-properties]] — the structural weaknesses of distribution that resilience must absorb.
- [[fault-error-failure-chain]] — how component defects become the failure of a service, and hence what resilience must persist.
- [[failure-models]] — the assumed fault envelope that dependability is stated relative to.
- [[ways-towards-dependability]] — the mechanisms for building dependable service, and the natural toolkit for resilience.
- [[redundancy-forms]] and [[error-detection-and-recovery]] — the concrete means of withstanding or recovering from impairments.
- [[availability]] — the dependability attribute closest to the "persistence of service delivery" wording.

## Open Questions

- The two resilience definitions are given side by side, but the lecture does not say which it treats as authoritative, nor whether they are meant to be equivalent; Berger's adds security and explicit outcomes, Laprie's is shorter.
- Neither definition states how the "changes" are bounded or classified — the slides give no taxonomy of environmental changes, though the Berger survey cited alongside has one the lecture does not reproduce.
- The relationship between the Laprie 1993 dependability definition and the "simple definition" (works according to its specification with high probability) is not discussed; the slide labels the latter simple without reconciling the two.
- The lecture does not say whether resilience is an attribute of the system, of the service, or of the deployed system in a specific environment; the wording shifts between "a system" and "service delivery".
- It is not stated how the security-preservation clause relates to the other dependability attributes, or whether security-preservation is weighed against them in a trade-off.
