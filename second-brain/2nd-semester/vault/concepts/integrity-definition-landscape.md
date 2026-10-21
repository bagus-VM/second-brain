---
title: "The Integrity Definition Landscape"
tags: [concept, advanced-it-security, semester-2]
course: "Advanced IT Security"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[cia-triad]]"]
---

## One-line Summary
Integrity has at least six competing standard definitions, and they disagree along two axes — property or state, and detection or prevention — which is why a signed-but-wrong sensor reading can pass an integrity check without the data being true.

## Core Intuition

Posegga puts one slide title next to six definitions of the same word: Clark and Wilson, the Orange Book (TCSEC), the communications tradition, ISO 7498-2, ISO 27000, RFC 4949. The exercise is not to pick a winner; it is to make you see the *axes* along which they differ. The lecture repeats the same six definitions under three headings — "Property or state, or?", "Detection or prevention?", "What to detect?" — and the three axes are worked out below.

That is the method. When six authorities disagree about a term, do not average them; find the dimensions on which they disagree. The pay-off is the internal/external consistency distinction. Integrity, as ISO 10181-6 frames it, is "a specific invariant on data"; the protection mechanism "detects the violation of internal consistency". And then Note 4: the integrity definition "is not concerned with the external consistency or veracity of the data." Integrity is about the *history* of the data, not the *truth* of the data — and that single sentence is what decides the lecture's exam question.

## Formal Definition / Statement

The six definitions, as quoted on the slide:

| Source | Definition |
|---|---|
| Clark and Wilson | "No user of the system, even if authorized, may be permitted to modify data items in such a way that assets or accounting records of the company are lost or corrupted." |
| Orange Book (TCSEC) | "Data Integrity - The state that exists when computerized data is the same as that in the source document and has not been exposed to accidental or malicious alteration or destruction." |
| In communications | "detection (and correction) of modifications of transmitted data, including both intentional modifications and random transmission errors." |
| ISO 7498-2 | "The property that information has not been modified or destroyed in an unauthorized manner." |
| ISO 27000 | "property of accuracy and completeness" |
| RFC 4949 | "The property that data has not been changed, destroyed, or lost in an unauthorized or accidental manner." |

**Axis 1 — property or state?** A property is *any characteristic or attribute which can be
quantitatively evaluated* (the slide's physics examples: pressure, temperature, velocity, energy);
the state of an object is *its condition described by a list of properties* (temperature and
pressure may describe the state of a gas). Verdict: **integrity is a property** (of data, of a
system, of hardware, …); **data integrity is a specific state of data that is verifiable**.

**Axis 2 — detection or prevention?** Clark and Wilson is the *preventative* variant, explicitly
marked as such. The remaining five are detection-oriented: a state to be checked, a condition to
be verified, or a modification to be detected.

**Axis 3 — what to detect?** The communications definition covers *both* intentional modifications
and random transmission errors, and demands detection *and correction*. The others address
unauthorised modification only, with accuracy and completeness (ISO 27000) as a separate,
truth-flavoured criterion.

**Internal versus external consistency.** Note 3: the integrity definition sees data integrity as
"a specific invariant on data" [ISO 10181-6]; the integrity protection mechanism "detects the
violation of internal consistency" [ISO 10181-6]; "A datum is internally consistent if and only if
all modifications of this item satisfy the relevant integrity security policies" [ISO 10181-6].
Note 4: the integrity definition "is not concerned with the external consistency or veracity of
the data."

**Basic Notions slide, according to ITSEC:** Confidentiality — no unauthorized access to
information. Integrity — no unauthorized modification of information / resources. Availability —
no unauthorized denial of access to information / resources. The separate "Integrity" slide adds
the informal gloss "Everything is as it is supposed to be..." (the slide spells it "Everyting")

**Confidentiality slide.** Historically, security and secrecy were closely related; sometimes
security and confidentiality are used as synonyms. Confidentiality = prevent unauthorised
disclosure of information (prevent unauthorised reading). Privacy = protection of personal data.
Secrecy = protection of data belonging to an organisation.

## Key Properties

- **The disagreement is structural, not terminological.** No two definitions can be merged without losing a commitment. Clark and Wilson forbids authorised modification; ISO 7498-2 and RFC 4949 forbid unauthorised modification; the communications definition covers accidental transmission errors as well; ISO 27000 talks about accuracy and completeness.
- **Authorisation is the fault line.** "Even if authorized" appears only in Clark and Wilson. A mechanism that lets an authorised user corrupt accounting records satisfies ISO 7498-2 and violates Clark and Wilson.
- **Property versus state is decidable by testability.** "Data integrity is a specific state of data that is verifiable" is not a contradiction: integrity *as a concept* is a property, one particular checkable condition of a data set is a state.
- **Internal consistency is a property of the modification history.** A datum is internally consistent if and only if *all* its modifications satisfy the relevant integrity security policies — the check is on the set of permitted modifications, not the current value alone.
- **External consistency and veracity are explicitly out of scope.** This is the load-bearing sentence for the exam question. Integrity does not certify that data reflects reality.
- **Detection and prevention are different services.** Clark and Wilson is the prevention variant. A detection-oriented definition still leaves prevention as a design goal.
- **Confidentiality, integrity and availability are not synonyms for security**, though historically security and secrecy were closely related.

## Worked Example

The lecture poses this question verbatim, and it is the exam point of this page:

> Q: Assume a temperature sensor that is attached to an IoT device is broken, i.e. readings are too high. Assume the IoT device signs the temperature measurements data, i.e. readings are digitally signed. Should an integrity verification of the signed but wrong temperature value fail or succeed?

**Step 1 — the data flow.** The sensor produces a value m. The device signs it: sig = Sign_sk(m). The verifier holds pk and computes Verify_pk(sig, m). The question asks whether this verification must report a failure.

**Step 2 — what the mechanism actually checks.** Under ISO 10181-6 the mechanism "detects the violation of internal consistency", and a datum is internally consistent if and only if all modifications of it satisfy the relevant integrity security policies. The relevant policy here is about *modification*, not about sensor health. The broken sensor produces m by a legitimate, unmodified path: the sensor reads too high, the device faithfully transmits and signs that reading, nobody modifies the value in transit or at rest. Every modification satisfies the integrity policy — there were no unauthorised modifications.

**Step 3 — apply Note 4.** The integrity definition "is not concerned with the external consistency or veracity of the data." The reading is externally wrong, and no signature can detect that, because the wrongness was introduced upstream, before signing, by a faulty (not adversarial) component. External consistency is out of scope by definition.

**Conclusion: the integrity verification SUCCEEDS.** The signature verifies. The data is internally consistent. The value is externally wrong. There is no contradiction, because the two statements are about different consistency properties — and this is exactly the gap Note 4 names.

**Where the failure actually lies.** The broken sensor is a *vulnerability* in the lecture's risk vocabulary, and the *lack of a plausibility check* is the missing safeguard. A range check on the reading operates on external consistency, not on integrity in the ISO 10181-6 sense.

**What would make the verification fail?** Only an unauthorised modification after signing, or a forged signature. A tampered reading (m changed to m', signature left unchanged) makes verification fail. A re-signed wrong reading does not. That is the whole distinction.

**The trap.** "Fail, because the temperature is wrong" silently adopts an external-consistency criterion that Note 4 explicitly excludes. "Succeed, so the mechanism is broken" misreads it too: the mechanism is doing exactly what an integrity mechanism does.

## Common Pitfalls

- **Collapsing property and state.** The slide's own resolution is that integrity *is* a property, while data integrity is a *state* that is verifiable.
- **Reading Note 4 as a loophole rather than a scope limit.** Integrity never certified truth. A system that only protects integrity cannot detect a lying sensor.
- **Treating "integrity" as one definition.** The lecture's whole point is that six authorities define it differently; an answer that quotes one and moves on has missed the landscape.
- **Forgetting the authorisation clause in Clark and Wilson.** It is the only definition covering authorised misuse, and the only one marked preventative.
- **Forgetting the communications definition's error half.** It covers *random transmission errors* as well as intentional modification, and demands correction, not only detection.
- **Conflating privacy and secrecy.** Privacy = protection of personal data; secrecy = protection of data belonging to an organisation. Historically close, and sometimes used as synonyms, but the three are distinct.
- **Assuming the ITSEC triad covers everything.** The three are the *basic notions*; the lecture's cost/benefit and evaluation material shows a security argument is much more than the triad.

## Connections

- [[cia-triad]] — the ITSEC definitions of confidentiality, integrity and availability, and where "integrity" sits among them.
- [[security-relationship-model]] — the vocabulary in which a broken sensor and a missing plausibility check appear as vulnerability and safeguard.
- [[security-policy-mechanism-assurance]] — detection versus prevention is a policy question, and integrity is where the distinction bites.
- [[digital-signatures]] — the mechanism in the worked example; it protects modification history, not truth.
- [[iot-security-hardware]] — where sensor and firmware integrity meet, and where external-consistency checks must be added.
- [[iot-lecture-5]] — the IoT lecture the signed-sensor question anticipates.
- [[common-criteria]] — the structured place where protection goals like data integrity are formally stated.

## Open Questions

- The slide cites ISO 10181-6 Notes 3 and 4 but not the surrounding note numbering or the full text of the definition those notes qualify. Which exact definition sentence they annotate is not recoverable from the material.
- The third-axis slide, "What to detect?", marks only Clark and Wilson as preventative and leaves the other five unmarked. Whether the rest differ among themselves on that axis — e.g. ISO 27000's accuracy and completeness pointing towards external consistency — is not resolved.
- The lecture poses the signed-sensor question without answering it. The reasoning above follows from Notes 3 and 4, but the course's official line (the lecturer's, a slide's, or an exercise's) is not stated.
- How an "integrity verification" is supposed to *fail* on a wrong-but-correctly-signed value is not discussed — which safeguard, if any, the lecture would place on the external-consistency side of the boundary, is left open.
