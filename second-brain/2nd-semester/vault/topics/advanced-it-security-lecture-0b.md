---
title: "Advanced IT Security — Lecture 0b: Security Properties, Attackers, and Approaches"
tags: [topic, advanced-it-security, semester-2, lecture]
course: "Advanced IT Security"
source_count: 1
status: current
last_updated: 2026-10-29
prerequisites: ["[[advanced-it-security-lecture-0]]"]
---

## One-line Summary
The second half of the Basics material: the security properties that sit *beyond* the CIA triad, the
three classes of attacker, the catalogue of technical approaches a security engineer can reach for —
and then a long, concrete detour into operational security, ending with what a smartphone really is.

## Core Map

```
Advanced IT Security — Lecture 0b (20261027_0_Basics.pdf)
│
├── Recap of lecture 0: agenda, "X is secure" is meaningless, elements behind the
│   concepts -->
│       → [[advanced-it-security-lecture-0]]
│
├── Beyond CIA: the properties, and how they relate
│   ├── Data origin authentication  — was this entity the source of this data?
│   ├── Data integrity              — was it altered?
│   ├── Non-repudiation             — can the source deny it to a third party?
│   ├── Entity authentication       — is the entity active *now*?
│   ├── Contingency                 — the dual of integrity: verifiably "unknown"
│   └── the three relations that decide the exam questions -->
│       → [[security-properties-beyond-cia]]
│
├── Classifying attackers (unchanged from the first deck)
│   └── Class I clever outsiders / II knowledgeable insiders / III funded organisations
│       → [[attacker-classification]]
│
├── Security in computer science: the sub-fields
│   ├── the pre-2000 answer was "cryptography"
│   └── today: crypto, software engineering, platform security, internet/web, hardware
│
├── The approaches catalogue
│   ├── virtualization, attestation, acceleration, tagging
│   ├── formal methods, cryptography, isolation, flow approaches
│   └── moving target, diversification, anomaly detection
│       → [[security-approaches-taxonomy]]
│
└── Operational security, worked all the way through
    ├── "A smartphone is a …" (six properties, all of them adversarial)
    ├── "How would you make a private phone call?"
    └── the burner-phone procedure, step by step -->
        → [[cell-phone-opsec]]
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[security-properties-beyond-cia]] | Five authentication-adjacent properties and the exact strength ordering between them — plus contingency, the dual of integrity that almost nobody has heard of. |
| [[security-approaches-taxonomy]] | Eleven technical approaches to security, and the practical test: which one addresses which attacker, and what it leaves behind. |
| [[cell-phone-opsec]] | Why a smartphone cannot be made private by software, and what the lecture's own operational procedure looks like. |

## What This Deck Adds

The deck is titled *Basics* and carries the same agenda slide as the first one, but it is a
**different file with a different date** (`20261027_0_Basics.pdf` against `20261020_0_Basics.pdf`),
and the diff between the two is large: **164 blocks are new and only 29 are unique to the older
deck**, where almost all of those 29 differ only in bullet glyphs. This is the real Basics lecture;
the 20261020 deck is an earlier, shorter version of it.

Where the earlier deck stops — at security evaluation and the assurance dilemma — this one keeps
going into four new areas.

**1. The properties beyond CIA.** The slide series *Data origin authentication – Differences and
Relations*, *The Dual of Integrity*, *Non-Repudiation – Differences and Relations* and *Entity
Authentication – Differences and Relations* introduces five notions and then states the
*relations* between them, which is the part that is examinable. The relations are quoted from Keith
Martin's *Everyday Cryptography*: data origin authentication is stronger than data integrity;
non-repudiation of a source is stronger than data origin authentication; confidentiality implies
neither of them; and data origin authentication plus a freshness check gives entity authentication.
Full treatment on [[security-properties-beyond-cia]].

**2. The approaches catalogue.** Two slides credit `sigarch.org` for a list of eleven ways to
approach security at a technical level — from virtualization and attestation through flow
approaches and moving-target defence to anomaly detection. What makes the list useful is not the
individual names but the observation the slide leaves implicit: these are answers to *different*
questions, and the taxonomy is by mechanism, not by threat. Full treatment on
[[security-approaches-taxonomy]].

**3. Operational security, at length.** Six slides on making a private phone call. This is the
material that surprises students in a Master's security lecture, and it is not a joke: the point is
that the *six* properties of a smartphone are all adversarial by construction, so the problem is
not solved by software, and the lecture walks through what solving it actually costs. Full
treatment on [[cell-phone-opsec]].

**4. A note on where security sits in computer science.** The *Security in Computer Science*
slide states the pre-2000 answer plainly — cryptography, originally from military needs — and then
lists today's sub-fields with an ellipsis at the end, which is the honest signal that the list is
open.

## Lecture Structure

1. Agenda and the two framing slides, repeated from lecture 0.
2. *Cost vs. benefit* and the general remarks on risk — repeated.
3. GSM security and political constraints — repeated.
4. **Definitions**, then assets / threats / vulnerabilities / safeguards / risks, then the
   *Beziehungen* diagram — repeated.
5. CIA per ITSEC, confidentiality, integrity with its six competing definitions, the
   property-versus-state digression, the internal-versus-external consistency notes and the
   signed-broken-sensor question — repeated.
6. Availability, security evaluation (Gollmann), and the assurance dilemma — repeated.
7. **Security Policy** — specification of a system's security properties, goals reachable by
   security measures, often written in natural language, and it should be aligned with the real
   world it refers to. The slide's own example: two employees are needed to open the safe with the
   confidential documents, and only between 9am and 4pm — *"an electronic system might enforce an
   equivalent policy"*.
8. **More Security Properties** — the advice slide: many more properties and services are defined
   in the literature; use them when defining a security policy, make sure they are precisely
   defined, make sure real-world attacks map to the explicitly defined attacker model, and be aware
   of the subtle differences.
9. **Data origin authentication, non-repudiation, entity authentication, contingency** — the new
   properties, with their relations.
10. **Classifying attackers** — the three classes, unchanged.
11. **Security in Computer Science** — the sub-fields.
12. **Some Example Approaches to Security** — the two sigarch slides.
13. **Private phone calls / Cell Phone OPSEC** — the closing sequence.

## Exam-Relevant Points

1. **The new properties are defined by their *relations*, not their definitions.** Being able to say
   "data origin authentication is a stronger notion than data integrity" and *why* scores; reciting
   the definition of each in isolation does not.
2. **Non-repudiation needs a third party.** It is not "I can prove you sent it to me"; it is "I can
   prove it to someone else". That is why it needs asymmetric cryptography and a signature, and why
   a MAC cannot give it — a point [[non-repudiation]] already makes from the Semester 1 side.
3. **Entity authentication adds liveness.** Data origin authentication says nothing about whether
   the sender is currently active; *"data origin authentication plus a freshness check can provide
   entity authentication"*. This is the cleanest one-line answer in the deck.
4. **Contingency is the dual of integrity, and the dual is not "no integrity".** Data is in the state
   of contingency when its integrity is *intended to be unknown* — a verifiable state established by
   the mechanism, not an accident. It lets an entity repudiate the data but not its creation, and
   data origin authentication is required for "intend" to be meaningful.
5. **"Confidentiality does not imply data origin authentication" and "confidentiality does not imply
   data integrity"** are both stated explicitly. Encrypting something tells you nothing about who
   produced it or whether it was altered before encryption.
6. **The approaches catalogue is a mechanism taxonomy.** Knowing which approach addresses which
   attacker class is the practical skill; the exercise's examination-system scenario is the test.
7. **Assurance and complexity remain mutually exclusive** — the one trade-off carried over from the
   earlier deck, with security evaluation as its statement.

## Connections

- [[advanced-it-security-lecture-0]] — the earlier, shorter deck for the same topic. Its seven
  concept pages remain the primary treatment of risk, the cost/benefit optimum, the elements
  diagram, and the integrity-definition landscape.
- [[advanced-it-security-exercise-1]] — the exercise sheet that exercises this material.
- [[advanced-it-security]] — the course page: exam date, exercise rules, full agenda.
- [[integrity-definition-landscape]] — the six integrity definitions; the deck repeats them
  verbatim, so this lecture adds no new content there.
- [[security-policy-mechanism-assurance]] — policy as a deliverable; this deck adds the
  policy-specification slide.
- [[machine-learning-for-cybersecurity]] — the other course covering the same vocabulary from a
  detection angle; the attacker classes come from the same IBM Systems Journal source.
- [[advanced-it-security-exercise-1]] — the sheet's Question 3(a) is the deck's signed-broken-sensor
  question restated as a graded task.

## Open Questions

- **The deck does not say which of the two `Basics` decks is authoritative.** They carry the same
  agenda but different dates and a 164-block difference. The later one is treated here as the
  primary and the earlier one as a subset; the course page does not state which was actually
  presented.
- **The speaker notes are missing.** The slide-ordering question from the earlier deck — whether
  the 20261020 file's *"Definitions"* title-only slide was meant to introduce the elements series —
  is not resolved by the later file, which has content on it.
- **No threat model is named for the OPSEC procedure.** The six-slide phone sequence gives a
  procedure and no adversary. Section 0 does not say who the procedure defends against, and the
  slide's own framing ("for the sake of confusion", the risk-perception numbers) suggests the
  adversary is deliberately left informal.
- **The approaches list ends in an ellipsis and is unattributed beyond a blog URL.** Whether any of
  the eleven approaches is covered in more depth later in the course (attestation under PKI?
  virtualization under protocol security?) is not stated here.
- **"Security Policy" is introduced without a formalism.** The slide says policies are often written
  in natural language and should be aligned with the world they refer to; nothing in this deck
  connects that to the assurance discussion from lecture 0, and no policy language is named.
- **The exercise sheet's Topic 2 is not answered by the deck.** Ranking the three examination-system
  profiles by access privileges, and arguing why access alone does not determine danger, is left to
  the exercise; see [[advanced-it-security-exercise-1]].
