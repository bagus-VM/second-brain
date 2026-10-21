---
title: "Security Terminology and the Risk Model"
tags: [concept, ml-security, security-basics, semester-2]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[cia-triad]]"]
---

## One-line Summary
"X is secure" is a meaningless sentence. Security is always security *against something*, at *some cost*, with *some residual risk* — and the vocabulary of assets, threats, vulnerabilities, and safeguards is how you make that precise.

## Core Intuition
Security is not a property a system has; it is a relation between a system, an attacker, and a budget. A lock that stops a curious neighbour is not the same lock that stops a funded organisation. So the first task is never "add encryption" — it is "what are we protecting, from whom, and what does failure cost?" Everything else is engineering inside that frame. Risk management is the discipline of choosing which failures to accept.

## Formal Definition / Statement

**Elements of security:**

| Term | Definition | Examples |
|------|------------|----------|
| **Asset** | Anything with value | data, hardware, software, documents, services, trust, reputation |
| **Threat** | Anything that could harm an asset | faults, misuse, theft, malicious code, hacking, sabotage, espionage |
| **Vulnerability** | A weakness that lets a threat succeed | insecure channels, badly trained staff, trivial passwords, missing access control, no backup, software flaws |
| **Safeguard** | A measure that reduces threats or vulnerabilities | access control, encryption, employee education |
| **Risk** | A function of assets, threats, vulnerabilities, and safeguards | — |
| **Residual risk** | What remains after safeguards | always > 0 |

**Three elements of a security solution:**

1. **Policy** — what the system is supposed to do (specification).
2. **Mechanism** — how it does it (implementation).
3. **Assurance** — whether it actually works (correctness).

**Cost/benefit:** security is relative. The right question is how much effort — time, money — an attacker needs to succeed, compared with the value of the asset and the cost of the safeguard.

## Key Properties

- **Residual risk is never zero.** Every safeguard leaves something, which is why incident response and insurance exist alongside prevention.
- **Risk is a relation, not a number you can read off a system.** Changing the attacker class changes the same asset's risk without touching the asset.
- **Safeguards are many-to-many with threats.** One mechanism (encryption) covers several threats; one threat can need several mechanisms.
- **Policy, mechanism, and assurance are three separate deliverables.** A missing assurance step means nobody verified that the mechanism implements the policy.
- **Security decisions are cost/benefit decisions.** The lecture's framing is attacker effort versus asset value — not "make it as secure as possible".
- **The vocabulary is what makes risk discussable.** Without separate words for threat and vulnerability, "we are exposed" contains no actionable information.

## Worked Example — mobile phone service

The lecture's example decomposes a familiar system into threat/safeguard pairs:

| Threat | Safeguard |
|--------|-----------|
| Eavesdropping on the air interface | encryption of communication |
| Extracting information from the signalling channel | encryption of communication |
| Unauthorised use of the service | identification and authentication (GSM: IMSI) |
| Theft of the device | identification of end devices (IMEI) |

Note what this table makes obvious: two different threats are mitigated by the same mechanism, and two different *identifiers* (IMSI, IMEI) protect two different assets (service access vs. hardware). A single "security" label would hide all of that structure.

## Common Pitfalls

- **Saying "secure" without an object.** Always: secure against what, at what cost.
- **Treating vulnerability and threat as synonyms.** A vulnerability is a hole; a threat is someone or something that can use it. Patching removes holes; it does not remove threats.
- **Forgetting residual risk.** A safeguard that reduces risk to "acceptable" is not a safeguard that eliminates it. Budgets and incident response exist because residual risk is real.
- **Skipping assurance.** A mechanism that was never evaluated is a belief, not a control.
- **Confusing policy with mechanism.** "We encrypt data at rest" is a mechanism. "Data must not be readable by the host operator" is a policy. Confusing them hides gaps.

## Connections

- [[cia-triad]] — the protection goals that risk analysis is trying to preserve.
- [[attacker-classification]] — risk is a function of *who* the attacker is; the same asset has different risk against a script kiddie and a funded team.
- [[ml-for-security-domains]] — where these concepts get operationalised into detectors.
- [[risk-assessment-frameworks]] — the formal, standards-based version of this vocabulary.

## Open Questions

- The lecture gives risk as "a function of" four things without a formula. Which quantitative model does the course expect for the exam — expected loss, or a qualitative matrix?
- Where does *privacy* sit? It is treated under confidentiality, but GDPR-style privacy is a different obligation from secrecy.
