---
title: "The Security Approaches Taxonomy"
tags: [concept, advanced-it-security, semester-2, security-engineering, attack-modelling]
course: "Advanced IT Security"
source_count: 2
status: current
last_updated: 2026-10-29
prerequisites: ["[[attacker-classification]]", "[[security-relationship-model]]"]
---

## One-line Summary
The Basics deck maps security onto five sub-fields of computer science and eleven example approaches from a SIGARCH piece, and Exercise Sheet 1 Topic 2 turns that vocabulary into an analysis of three attacker profiles against an online examination system.

## Core Intuition

"Security in Computer Science" says the standard answer until 2000 was cryptography, initiated originally from military needs, then lists today's sub-fields and ends in an ellipsis, so the list stays open. The two "Some Example Approaches to Security" slides, credited to sigarch.org's piece on the state of security today, list eleven approaches. They are not alternatives to choose between; they sit at different layers, each answering a different weak point.

Exercise Topic 2 poses three profiles — external observer on public Wi-Fi, student account holder, system administrator — against one examination system, and asks not who is strongest but who threatens what. Access privileges are one input; the rest comes from the vocabulary wired in [[security-relationship-model]]. The reasoning in Topic 2(a) is the Class I/II/III distinction of capability and resources on [[attacker-classification]], not privilege alone.

## Formal Definition / Statement

Sub-fields of security in computer science: cryptography (encryption, authentication, watermarking; algorithms, protocols; PKI); software engineering (avoiding bugs, secure coding, evaluation/certification); platform security and security architectures (OS, browser, Java); Internet and web security (bugs in protocols, secure web server and browser, firewalls, online payments); hardware security (smartcards, secure tokens) — then an ellipsis.

Example approaches, in the deck's order: virtualization (the illusion that code runs in an environment other than the one executing it); attestation (systems can attest or verify the integrity of their components — needs a root of "trust"); acceleration (hardware support cutting the runtime overhead of security features); tagging (memory locations carry metadata signalling data types or permission levels); formal methods (logical proofs of properties about a system); cryptography (encrypt/protect information with cryptosystems); isolation (keep trusted and untrusted components separate and monitor their interaction); flow approaches (everything is an object with data and metadata; shadow computations on the metadata detect and report illegitimate modification); moving target approaches (minimize the attacker's advantage by changing how the system and defences work over time); diversification (distinct systems force bespoke exploits, raising attacker cost and lowering profit); anomaly detection (systems will always be insecure, so monitor for abnormal behaviour).

## Key Properties

- The sub-field list is open by design; the ellipsis means the slide does not fix the field's boundary.
- The approaches differ in kind, not only in layer: prevention (isolation, tagging), verification (attestation, formal methods), economics (moving target, diversification, acceleration) and detection (anomaly detection).
- Attestation needs a root of trust, stated as a requirement rather than a detail, and acceleration adds speed rather than strength.
- Virtualization gives code an illusion of a different environment; isolation separates trusted from untrusted components and monitors their interaction.
- Anomaly detection assumes systems will always be insecure, which is why it monitors instead of preventing.

## Worked Example

Exercise Sheet 1, Topic 2(c): an online examination system with three profiles — A, external observer, can monitor traffic on public Wi-Fi and has no account; B, student account holder, can submit examination registrations but cannot change grades; C, system administrator, privileged access to system and database, bound by university policy.

**(a) Ranking and the limits of access.** By access privileges: C > B > A. Access alone does not rank danger: C's privilege is bounded by policy and visible in audit trails; B holds process knowledge and a legitimate foothold from which a workflow bug can be probed; A has no privilege yet can still mount a network-level attack, as the IMSI-catcher example on [[gsm-security-political-constraints]] shows for an unauthenticated counterpart. Danger also depends on capability, opportunity and impact on the asset — the [[attacker-classification]] distinction between a clever outsider, a knowledgeable insider and a funded organisation.

**(b) Misuse and threatened goal.** A can read session tokens off unencrypted Wi-Fi, threatening confidentiality of credentials. B can submit registrations they are not entitled to, threatening integrity of the examination record — an authorised user misusing valid rights. C can alter grades despite policy, threatening integrity of the grades, and the same access also reads every student record, threatening confidentiality.

**(c) Safeguards and residual risk.** A: encrypt the traffic, e.g. HSTS with a validated certificate; residual risk — a rogue or compromised certificate still allows interception, and metadata still leaks. B: server-side authorisation checks with input validation and audit logging; residual risk — a logic flaw passes validation unnoticed, and logging detects after the fact rather than preventing. C: least privilege, separation of duties, a two-person rule for grade changes and append-only logs outside the administrator's reach; residual risk — an administrator who colludes, or who reaches the log store, defeats it. C's misuse also maps to the gap on [[integrity-definition-landscape]]: an authorised modification satisfies a definition that forbids only unauthorised ones.

**(d) Why one defence cannot serve all three.** Each profile sits at a different point in the system, so a control that observes one is blind to another: network encryption is irrelevant to an insider holding authorised access, and least privilege does nothing against a party with no account. Anomaly detection fits the privileged user who deviates from routine and is noisy against a student's ordinary-looking submissions. The deck's advice slide requires real-world attacks to map to an explicitly defined attacker model, so the defender must say which profile a control is meant to stop.

## Common Pitfalls

- Treating the eleven approaches as a menu of alternatives, when they are complementary layers.
- Memorising the five sub-fields as a closed list, ignoring the slide's ellipsis.
- Ranking attackers by privilege alone and dropping motive, skill, opportunity and asset value.
- Assuming inside access is harmless because policy forbids misuse; a policy is not a mechanism.

## Connections

- [[attacker-classification]] — the Class I/II/III capability ranking used for Topic 2(a).
- [[security-relationship-model]] — the assets, threats and safeguards vocabulary of the worked example.
- [[defense-in-depth]] — the layered reading of the eleven approaches.
- [[virtual-machines-and-runtime-systems]] — where virtualization as a security approach is studied in depth.
- [[machine-learning-for-cybersecurity]] — the home of anomaly detection as a security mechanism.
- [[advanced-it-security-exercise-1]] — Topic 2, the source of the examination scenario.

## Open Questions

- The deck lists the eleven approaches without saying which layer each belongs to, how they combine, or how a defender chooses among them.
- The ellipsis after hardware security leaves the sub-field list's boundary undefined; no completeness claim is made.
- Profile C is privileged but bound by policy, and the sheet never says whether C is assumed honest, which changes the answer to (b).
