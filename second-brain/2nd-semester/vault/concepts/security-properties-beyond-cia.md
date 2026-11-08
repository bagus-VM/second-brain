---
title: "Security Properties Beyond the CIA Triad"
tags: [concept, advanced-it-security, semester-2, security-properties, authentication]
course: "Advanced IT Security"
source_count: 2
status: current
last_updated: 2026-10-29
prerequisites: ["[[cia-triad]]", "[[integrity-definition-landscape]]", "[[non-repudiation]]"]
---

## One-line Summary
The second Basics deck adds four properties beyond the ITSEC triad — data origin authentication, non-repudiation, entity authentication and contingency, the constructed dual of integrity — and fixes each one's relation to its neighbours.

## Core Intuition

The first Basics deck gave confidentiality, integrity and availability; this deck covers the properties just outside that triad, fixing their relations to neighbours rather than listing terms.

Data origin authentication, non-repudiation and entity authentication come from Keith Martin's *Everyday Cryptography* (slides 38, 40, 41); contingency comes from Pfitzmann and Rost's "Datenschutz-Schutzziele – revisited" and is constructed rather than observed. Slide 39 calls it the "constructed Dual* of Integrity" and resolves the duality in a footnote: information can be in the state of integrity or in the state of contingency, but not both, since both at once would be a contradiction. Contingency is therefore not "no integrity" but the verifiable state in which the data's integrity is intended to be unknown.

Slide 37 gives the reason for the precision: many more properties and services are defined in the literature, so use them when defining a security policy, but make sure they are precisely defined, make sure real-world attacks map to the explicitly defined attacker model, and be aware of the subtle differences. The deck repeats the Class I/II/III attacker classification unchanged; that material is on [[attacker-classification]].

## Formal Definition / Statement

Data origin authentication — "the assurance that a given entity was the original source of received data" (slide 38). Relations on the same slide, attributed there to Keith Martin, *Everyday Cryptography: Fundamental Principles and Applications*:

- "Data origin authentication is a stronger notion than data integrity"
- "Confidentiality does not imply data origin authentication"
- "Confidentiality does not imply data integrity"

Non-repudiation (slide 40) — "the assurance that an entity cannot deny a previous commitment or action"; most commonly "the assurance that the original source of some data cannot deny to a third party that this is the case". Relation: "Non-repudiation of a source is a stronger notion than data origin authentication."

Entity authentication (slide 41) — "the assurance that a given entity is involved and currently active in a communication session". Relations: "Data origin authentication on its own is only concerned with the origin of data, not whether the sender of data is currently active"; "Data origin authentication plus a freshness check can provide entity authentication."

Contingency (slide 39, Pfitzmann & Rost) — "the verifiable state that the data's integrity is intended to be unknown. Data in that state is said to be contingent." German original on the slide: "Kontingenz: Information ist [...] gesichert nicht gesichert echt." Three consequences are stated: contingency is "a verifiable property explicitly established by the applied protection mechanism and not an accidental state"; it "allows an entity to repudiate the data, but not its creation"; and data origin authentication "is required for 'intend' to be meaningful".

## Key Properties

- The strength chain is stated, not derived: integrity < data origin authentication < non-repudiation of a source. Each step adds something — first the origin of the data, then the ability to demonstrate that origin to a third party.
- Confidentiality is orthogonal, and both quoted relations about it are negative: encrypting a channel says nothing about who produced the plaintext, or whether it was altered before encryption.
- Entity authentication concerns liveness, and the freshness check is what upgrades data origin authentication into it.
- Contingency can only be established by the protection mechanism, never by accident, and non-repudiation carries a third-party condition.

## Worked Example

Both settings below are digitally signed ([[digital-signatures]]), so any difference is in what is asserted, not in the mechanism.

| Notion | Signed IoT temperature reading | Signed purchase order |
|---|---|---|
| Data origin authentication | Yes — the device was the source | Yes — the buyer was the source |
| Integrity | Yes — no unauthorised alteration | Yes |
| Non-repudiation | Only if the key is attributable to the device and a third party can check it | Yes — the buyer cannot deny the order |
| Entity authentication | No — past data, not an active sender | No from the signature alone; needs freshness |
| Contingency | No — integrity is asserted | Yes if the mechanism hides the content's integrity on purpose |

Question 3(a) "The Faulty Sensor" (Exercise Sheet 1), also posed at slide 32: a defective sensor reports 43 °C while the true temperature is 23 °C, the device signs its readings, and the signed value reaches the server unaltered with the signature verifying.

(a) The message was not modified in transit: verification tells the server only that the value arrived unaltered from the holder of the signing key, that is, data origin authentication plus integrity of the received data — nothing about the world. (b) No. Data integrity concerns the history of the data, while measurement accuracy is external consistency, and Note 4 states that the integrity definition "is not concerned with the external consistency or veracity of the data". The sensor case is treated in full on [[integrity-definition-landscape]], the primary treatment of the six integrity definitions and of internal versus external consistency; this page adds only the relations. (c) Asset: the laboratory temperature record. Vulnerability/fault: the defective sensor. Risk: an unnoticed out-of-range temperature. Safeguard: a plausibility or range check, which acts on external consistency, not on integrity.

## Common Pitfalls

- Reading the strength chain backwards: data origin authentication is stronger than integrity, and non-repudiation of a source stronger again.
- Treating confidentiality as a superset of the others; both slide relations about it are explicit negatives.
- Using "non-repudiation" for any origin check — without a third party who can verify, the slide's common form is not achieved.
- Reading contingency as "no integrity" or as a failure of protection, when the duality footnote defines it as a designed, verifiable state.

## Connections

- [[cia-triad]] — the ITSEC basic notions this material extends.
- [[integrity-definition-landscape]] — the primary treatment of the integrity definitions.
- [[non-repudiation]] — the first-semester treatment of the property slide 40 relates.
- [[digital-signatures]] — the mechanism behind every signed setting above.
- [[authentication]] — where entity authentication and freshness sit in the course's material.
- [[attacker-classification]] — the material this deck repeats and this page does not restate.

## Open Questions

- Contingency's duality and consequences are stated, but the deck gives no example of a mechanism that establishes the contingent state, and no deployment it applies to.
- The German definition is quoted with an ellipsis — "Information ist [...] gesichert nicht gesichert echt" — so the original sentence's exact reading is not recoverable from the slide.
- No mechanism for non-repudiation is named, and whether the freshness check that upgrades origin authentication into entity authentication is a nonce, a timestamp or a challenge is not stated.
