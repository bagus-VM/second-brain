---
title: "Attacker Classification: Clever Outsiders, Knowledgeable Insiders, Funded Organisations"
tags: [concept, ml-security, semester-2, threat-model]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[security-terminology-and-risk-model]]"]
---

## One-line Summary

Abraham et al. (1991) sort attackers into three classes by knowledge of the system and equipment they can afford — and that class, not the technology, decides which safeguards are worth paying for.

## Core Intuition

Security is relative: it is measured in the effort an attacker must spend to succeed, and effort decomposes into knowledge of *this* system and resources — equipment, money, people. A clever outsider must find a hole and use it as shipped; a knowledgeable insider needs no hole, being already inside; a funded organisation needs neither, because it can pay specialists to design the attack. Each step up removes an assumption the cheaper defences rest on. The axis is capability, not motive, and it is scoped to a system: an expert on system A is an outsider on system B.

## Formal Definition / Statement

| Class | Name | Knowledge | Access / equipment | Characteristic attack |
|---|---|---|---|---|
| I | "Clever Outsiders" | intelligent, but lacks expert knowledge about the system | only moderately sophisticated equipment | exploits vulnerabilities in existing systems |
| II | "Knowledgeable Insiders" | highly educated, detailed understanding of *parts* of the system | potential access to most of the system; often highly sophisticated equipment | abuses legitimate access and knowledge |
| III | "Funded Organisations" | teams of specialists, **may include knowledgeable insiders** | backed by great funding resources | designs sophisticated attacks, uses the most sophisticated equipment |

Source: Abraham, Dolan, Double, Stevens, "Transaction Security System", *IBM Systems Journal* 30(2), 1991 (cited in L1). The classes nest: Class III can buy Class II knowledge and Class I opportunism, so defending only against the top class leaves the cheap attack open.

## Key Properties

- **The class sets the cost/benefit calculation.** A safeguard is rational when its cost is below the expected loss it removes. The same unpatched server is a nuisance against Class I and an existential problem against Class III.
- **Defence strategy shifts with class.** Class I is patching and hygiene, because the attack reuses known vulnerabilities. Class II becomes authorisation and accountability — access control, audit trails, non-repudiation — because no vulnerability need be exploited. Class III becomes detection and containment, because the attack is designed.
- **Residual risk is class-dependent.** Lowering risk against Class I does not lower it against Class III.
- **The classes do not cover non-malicious threats.** Faults count as threats in the lecture's terminology, and the opening example — a sensor update that crashed millions of machines for roughly US$10 bn *without an attack* — fits no attacker class.

## Worked Example

One database, three models.

**Class I:** the attacker exploits a known vulnerability in an unpatched web front end. Patch management, a WAF and strong authentication remove the cheap paths, and a classifier trained on past traffic works because the attack *is* past traffic reused.

**Class II:** an administrator with legitimate credentials reads the same records without exploiting anything, so input validation is irrelevant. What helps is least privilege, audit trails tying actions to a responsible party, and anomaly detection over user behaviour — an unsupervised problem, with no labels.

**Class III:** the team designs an attack for this target, possibly with an insider inside it. Per-request classification is not the defence, because the attack was built to survive it; what remains is defence in depth, segmentation, and planning for compromise.

Class III defences against a Class I threat are waste; Class I defences against a Class III threat are theatre.

## Common Pitfalls

- **Reading the classes as a skill ladder.** They are knowledge × resources; a brilliant generalist with no system knowledge is still Class I.
- **Equating "insider" with Class II.** Class III explicitly may contain insiders; the insider problem does not vanish at the top.
- **Assigning one class to a whole organisation.** The class is per asset: website, payroll database and build server differ.
- **Assuming a trained detector is class-neutral.** It learns attacks that already happened — a Class I/II detector by construction. An adversary optimising against it is the adversarial-ML topic later.

## Connections

- [[security-terminology-and-risk-model]] — risk as a function of assets, threats, vulnerabilities, safeguards; the attacker class makes "threat" concrete.
- [[ml-for-security-domains]] — each domain assumes a class: signature-like classification assumes reuse, user-behaviour anomaly detection assumes an insider.
- [[cia-triad]] — insiders lean on confidentiality and integrity; funded organisations can also buy availability (DDoS).
- [[risk-assessment-frameworks]] — where attacker capability becomes a scored input.

## Open Questions

- The taxonomy is from 1991, yet L1 notes LLM-written spearphishing that is "fluent, cheap at scale". Is a lone actor with a frontier model Class I knowledge with Class III reach?
- No slide maps class to expected loss quantitatively; the cost/benefit argument stays qualitative.
