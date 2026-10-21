---
title: "The Security Relationship Model"
tags: [concept, advanced-it-security, semester-2]
course: "Advanced IT Security"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[security-terminology-and-risk-model]]"]
---

## One-line Summary
The lecture's "Beziehungen" diagram is the causal backbone of risk management: threats exploit vulnerabilities, both raise risk, risk indicates protection requirements, and safeguards exist to protect against the threats those requirements name.

## Core Intuition

Posegga puts one dense slide between the risk definitions and the cost curve, and it turns a glossary into a model. The glossary tells you what assets, threats, vulnerabilities, safeguards and risks *are*; the relations diagram tells you *how they cause each other*, and therefore where an intervention lands.

The spine is a causal chain with two inputs and one output. Threats exploit vulnerabilities; vulnerabilities expose assets; both increase risk; risk increases the value at stake. Off to the side sits the requirement side: risks indicate protection requirements, and safeguards are met by (i.e. answer) those requirements while protecting against the threats. A safeguard is not a random hardening step — it is the response to a requirement the risk analysis produced.

Read the arrows as causal claims. "Safeguards protect against threats" states what the safeguard is *for*; "Risks indicate protection requirements" states that the requirement set is *derived from* the risk, not chosen independently. A security architecture that skips that derivation is guessing.

## Formal Definition / Statement

The lecture's relations, with the arrow directions made explicit:

```
   ┌───────────────┐      exploit      ┌───────────────────┐
   │    Threats    │ ────────────────▶ │   Vulnerabilities │
   └───────┬───────┘                   └─────────┬─────────┘
           │ increase                             │ increase
           │                                     │
           │        ┌─────────┐                   │
           └───────▶│  Risks  │◀──────────────────┘
                    └────┬────┘
                         │ increase
                         │              ┌─────────┐
                         └─────────────▶│ Values  │
                                        └────┬────┘
                                             │ have
   ┌──────────────────────────┐        ┌───────▼──────┐
   │ Protection Requirements  │        │    Assets    │◀── expose ── Vulnerabilities
   └────────────▲─────────────┘        └──────────────┘
                │ met by
      ┌─────────┴─────────┐
      │     Safeguards    │ ──────── protect against ────────▶ Threats
      └───────────────────┘
```

Written out as the nine relations of the slide:

1. Threats **exploit** Vulnerabilities.
2. Safeguards **protect against** Threats.
3. Threats **increase** Risks.
4. Vulnerabilities **increase** Risks.
5. Vulnerabilities **expose** Assets.
6. Safeguards **met by** Protection Requirements.
7. Risks **indicate** Protection Requirements.
8. Risks **increase** Values.
9. Assets **have** Values.

The eight elements the "Elements auf Security" slide lists are: assets, threats, vulnerabilities, safeguards, risk, residual risk, impact, constraints. The first five appear as nodes in the diagram; residual risk, impact and constraints are the modifiers that qualify the picture.

**Definitions slide content.**

- **Assets** — everything that has a value: information and data, hardware, software, other equipment, documents, services, "trust" in services, personnel, an organization's image.
- **Threats** — everything that potentially harms assets: errors, faults, misuse and theft, malicious code, hacking, sabotage, espionage.
- **Vulnerabilities** — "weaknesses which allow a threat to occur"; the slide notes explicitly that vulnerabilities do not necessarily cause damage. Examples: insecure communication, poorly trained staff, trivial passwords, poor access control, lack of back-ups.
- **Safeguards** — means to reduce threats or vulnerabilities: access control, encryption, training of personnel.
- **Risks** — risk is a function of assets, threats, vulnerabilities and safeguards; and there always remains a residual risk.

## Key Properties

- **The model is causal and directional.** Every arrow names a mechanism: exploit, increase, expose, indicate, met by, have. The directions are not symmetric; treating "threats and vulnerabilities" as interchangeable is wrong.
- **Vulnerabilities are opportunities, not events.** A vulnerability is the opening a threat uses. The slide says vulns "allow a threat to occur" and notes they do not necessarily cause damage: trivial passwords and poor access control sit harmlessly next to an asset until some threat arrives.
- **Threats and vulnerabilities are the two independent inputs to risk.** Both arrows point into Risks, and neither suffices alone: a threat without a vulnerability has nothing to exploit, a vulnerability without a threat may never be used. Risk is a function of all four elements — assets, threats, vulnerabilities, safeguards.
- **Safeguards act in two directions at once.** They protect against Threats, and they are met by Protection Requirements — the justification link: a safeguard exists because a requirement demanded it.
- **Requirements are derived from risk, not intuition.** The analysis is only as good as its threat and vulnerability identification.
- **Value is where risk lands.** Assets have Values; Risks increase Values — risk inflates what is at stake, the quantity the cost/benefit optimum trades against mechanism cost.
- **Residual risk is structural.** The slide's flat statement — there always remains a residual risk — means the diagram never closes; a perfect safeguard set is not in the model. Impact and constraints are listed among the eight elements but appear as no nodes, so they are factors qualifying risk rather than entities in the graph.

## Worked Example

Take a concrete university asset and run the model.

**Asset and value.** A staff member's grade list in the examination system. It *has* a value: personal consequence for the students named, and damage to the organization's image if leaked or altered.

**Threat.** "Misuse and theft" — an authenticated staff member, or someone holding a staff member's credentials, reads the list for a purpose other than duty. A threat, not a vulnerability: an actor with intent.

**Vulnerability.** "Poor access control" — the grade list is readable by roles that do not need it. Vulnerabilities *expose* the asset, and this one *increases* risk independently of the threat. Add a second: "trivial passwords" (a reused or guessable credential), which the theft threat can *exploit*.

**Risk.** The threat increases risk. The vulnerability increases risk. Both arrows hold at once, so the risk is a function of all four elements, and the loss lands on the value of the asset.

**Requirements and safeguards.** The risk *indicates* a protection requirement — "only roles with a duty to know may read a grade list". The safeguard, access control, is *met by* that requirement, and it *protects against* the threat. Encryption does not serve here: it protects contents in transit, but the threat acts through an over-permissive role assignment, not interception. Picking the wrong safeguard is a mapping error in the model.

**Residual.** The safeguard reduces the risk; it does not annihilate it. A misconfigured role, a standing administrator account, a compromised legitimate account — all leave residual risk, which is why the model is a management framework and not a proof.

## Common Pitfalls

- **Drawing the arrows the wrong way.** The most common error: safeguards *are* requirements, or requirements *produce* risks, or assets *expose* vulnerabilities. The slide says vulnerabilities expose assets, and risks indicate requirements. Get the direction wrong and the whole derivation inverts.
- **Reading "Risks increase Values" as a claim that risk is valuable.** It is a claim that risk amplifies what is at stake, i.e. it operates on the value side of the cost/benefit trade.
- **Forgetting "met by".** The link from protection requirements to safeguards is the one that justifies a safeguard's existence. Without it, safeguards are unmotivated tinkering.
- **Treating a vulnerability as an incident.** The slide states plainly that vulnerabilities do not necessarily cause damage. A trivial password is a hole, not a breach.
- **Dropping the residual risk.** Every analysis that ends with "risk eliminated" has misread the risk slide.
- **Assuming the diagram includes impact and constraints.** They are on the eight-element list but not in the relations graph. Do not draw them as nodes.
- **Reusing the vocabulary without the model.** [[security-terminology-and-risk-model]] already gives the definitions; this page is about the causal wiring, and an answer that only recites definitions does not answer it.

## Connections

- [[security-terminology-and-risk-model]] — the definitional half of the same lecture material: what assets, threats, vulnerabilities, safeguards and residual risk are.
- [[security-policy-mechanism-assurance]] — the policy/mechanism/assurance triple is the delivery side of this model: safeguards are the mechanisms, protection requirements are the policy.
- [[security-cost-benefit-optimum]] — the value node ("Assets have Values", "Risks increase Values") is what the cost/benefit optimum trades against the cost of safeguards.
- [[cia-triad]] — confidentiality, integrity and availability are the standard protection goals that protection requirements are typically phrased in terms of.
- [[risk-assessment-frameworks]] — the formalised procedures that perform the derivation this diagram describes, from threats to requirements.
- [[threat-modeling]] — the practical method of identifying threats and vulnerabilities, i.e. filling the left half of the graph.
- [[attacker-classification]] — populates the threat node with a structured taxonomy of who or what can realise the threat.
- [[risk-perception-and-dread-risk]] — the psychological layer that determines how the indicated protection requirements are actually funded.

## Open Questions

- The slide's own typography makes "Safeguards protect against Threats" and "Safeguards met by Protection Requirements" read as two arrows leaving Safeguards, but the underlying source model is not shown. Whether "met by" should be read as "satisfies", "is selected in response to", or "is required by" is not settled by the slide.
- Impact and constraints are listed among the eight elements of security but appear nowhere in the relations diagram. Whether the lecture intends them as modifiers of risk, as constraints on safeguard selection, or as a topic deferred to a later lecture is not stated.
- The diagram contains no arrow into or out of safeguards except threats and requirements. There is no explicit feedback loop from safeguards back onto vulnerabilities, even though a safeguard plainly reduces a vulnerability. Whether that omission is a simplification of the slide or a deliberate modelling choice is unclear.
- Residual risk is asserted but not placed in the graph. It could be modelled as the risk remaining after the safeguard arrow, as a property of the risk node, or as a separate node with its own indicator. The lecture does not say.
