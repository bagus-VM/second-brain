---
title: "Policy, Mechanism, Assurance"
tags: [concept, advanced-it-security, semester-2]
course: "Advanced IT Security"
source_count: 1
status: current
last_updated: 2026-10-20
prerequisites: ["[[security-relationship-model]]"]
---

## One-line Summary
A security solution has three parts — a policy that states what must hold, a mechanism that enforces it, and assurance that shows the mechanism really does what it claims — and a solution missing the third part is a belief, not a control.

## Core Intuition

Posegga's "Elements of Security" slide gives three questions, one per element. *Policy* is specifying security: what is it supposed to do? *Mechanism* is implementing security: how does it do it? *Assurance* is correctness of security: does it really work? The questions separate three deliverables that are routinely conflated, and each fails on its own: a policy can be unimplemented, a mechanism can be implemented and wrong, a mechanism can be right and never checked.

The slide sits behind a harder claim. *"X is secure" is meaningless as an isolated statement:* a system can only be secure against something. The first job is therefore to identify threats and security goals — no mechanism selection before that. Security is a relative notion, quantified by the effort (time, money, …) an attacker must invest to compromise a system, and from that follows the cost/benefit ration of security investment as a must. The overall framing: **security technology = technical means for risk management**. Cryptography, access control and key management are instruments of risk management, not ends in themselves.

The Safeguards slide names the frameworks through which a mechanism gets specified and assessed: ETSI Baseline Security Standard, NIST Computer Security Handbook, ISO TC 68 *Banking and Related Financial Services — Information Security Guidelines*. These turn "we encrypt" into a policy with a normative reference, a mechanism with a standard, and an assurance argument with an audit trail.

## Formal Definition / Statement

For a system S, a security solution decomposes into three artifacts:

| Element | Question it answers | Content | Failure mode |
|---|---|---|---|
| **Policy** | What is it supposed to do? | The security requirements, the protection goals, the rules | A goal nobody implements, or a goal that contradicts another goal |
| **Mechanism** | How does it do it? | The technical means realising the policy (access control, encryption, training) | Implemented but wrong, misconfigured, or bypassable |
| **Assurance** | Does it really work? | The evidence that mechanism implements policy, at a stated degree of trust | Mechanism deployed on faith, unverified, at an unstated assurance level |

Two preconditions from the "What does Security Mean?" slide govern the whole decomposition:

1. **Relativity.** Security is only ever "security against X", at attacker effort level E, at cost C. A claim of security without the threat and the effort figure is unarguable and therefore worthless.
2. **Cost/benefit ration.** Since security is relative and priced, the deployment decision is a ration between investment and expected loss, and the optimum is a cost minimum, not a maximum-security point.

The three elements are ordered but not independent. Assurance is the element that closes the loop: it is the only one that can falsify the other two.

## Key Properties

- **Three separate deliverables, three separate owners.** Policy is a requirement, mechanism is engineering, assurance is verification. A team that ships mechanism has not shipped a security solution.
- **Assurance is the expensive element.** Verifying a mechanism means inspecting the system in detail, and inspection cost grows with system complexity. This is why assurance is where the cost/benefit optimum actually bites — see [[security-evaluation-and-assurance-levels]].
- **Policy without a threat list is unanchored.** The lecture's "first job: identify threats and security goals" is a sequencing rule, not a formality: goals determine which mechanism is admissible, and threats determine which goals matter.
- **Mechanism is a means of risk management, not a security property.** "TLS is deployed" describes an instrument. The security property it delivers is the one the policy names.
- **The standards supply the reference frame.** ETSI Baseline Security Standard, NIST Computer Security Handbook and ISO TC 68's *Information Security Guidelines* express safeguards normatively and auditably — the formal counterpart of the safeguard examples.
- **Residual risk never reaches zero.** So assurance is never about proving safety, only about stating a degree of trust in a known residue. The risk model's own residual-risk statement is the reason: see [[security-terminology-and-risk-model]].
- **The triple is decomposable in the exam.** "Which element is missing here?" is a common question shape; the answer must name the element and say what evidence would close the gap.

## Worked Example

Consider a university examination system that stores final grades in an LMS. Decompose it against the lecture's three questions.

**Policy (what is it supposed to do?).** *a student's grade may be read and modified only by the student concerned, the examiner, and the examination office; no other party, including the server operator's staff, may read it.* The goal is stated relative to a threat and an effort level — the implicit question is how much an attacker must invest to become that other party.

**Mechanism (how does it do it?).** Three concrete means: role-based access control on the LMS with roles `student`, `examiner`, `office`; TLS on the transport to keep the grade opaque against the network; and audit logging of every read of a grade record, so that a misuse attempt leaves a trace rather than being invisible. The mechanism is implementable and, in a textbook, correct.

**Assurance (does it really work?).** Here the gap appears. Nobody has checked that the three roles map onto the actual organisational roles, that the audit log is retained, or that the "office" role is not granted more than the policy permits. The evidence that would close the gap: a review of the role-assignment configuration against the policy, a check that log retention matches the policy's requirement, and a scoped penetration test of the access-control layer. This is the "inspection of a system at a very detailed level" the lecture's security-evaluation slide demands, and it is the only step that distinguishes "we configured it as intended" from "it behaves as intended".

Now the failure modes. Drop the role mapping check and you have policy and mechanism with no assurance — the case the ETSI, NIST and ISO TC 68 frameworks exist to prevent. Keep the role mapping but delete the audit log, and the policy is *unimplementable as stated*. Keep everything but state no assurance level, and the third question is unanswered: "does it really work?" asks for a stated degree of trust, not a yes/no.

## Common Pitfalls

- **Listing mechanisms as if they were solutions.** "We use AES and TLS" answers no policy question and no assurance question. Exam answers that start with a product name have skipped two of the three elements.
- **Conflating policy and mechanism.** "We encrypt data at rest" is a mechanism. "Data must not be readable by the host operator" is a policy. Swapping them hides the gap where the requirement actually lives.
- **Treating assurance as a formality.** Assurance without a stated degree of trust is worse than none: it creates an unearned impression of verification. The lecture's evaluation slide makes the degree of trust part of the answer.
- **Ignoring that the threat must be named first.** Choosing a mechanism before identifying threats and security goals is the "X is secure" mistake in disguise — the relative nature of security is what makes the threat list the necessary first job.
- **Treating the standards as interchangeable.** ETSI, NIST and ISO TC 68's banking guidelines come from different domains; a banking guideline is not a general-purpose baseline.
- **Forgetting that assurance is where the budget goes.** Practitioners habitually underfund verification because it produces no visible feature. The cost/balance argument of the course predicts exactly that failure.

## Connections

- [[security-relationship-model]] — the diagram that places safeguards, threats and protection requirements in relation, and that a policy answers in the "protection requirements" node.
- [[security-cost-benefit-optimum]] — the rationing constraint that determines how much assurance a project can actually buy.
- [[security-evaluation-and-assurance-levels]] — the Gollmann quote and the two properties that make assurance the expensive element of this triple.
- [[security-terminology-and-risk-model]] — the earlier, more compact statement of the same triple; this page adds the standards and the explicit policy/mechanism/assurance split.
- [[risk-assessment-frameworks]] — the formalised methods that turn the safeguard list into a repeatable assessment procedure.
- [[common-criteria]] — the assurance side of the same argument: how a product's claimed security is evaluated against a catalogue of protection goals.
- [[risk-perception-and-dread-risk]] — why the budget for assurance is allocated by a distorted signal, and why the optimum is not what gets chosen.

## Open Questions

- The lecture names ETSI, NIST and ISO TC 68 as frameworks but does not say how any of them map onto the policy/mechanism/assurance triple. Whether a specific standard is developed later in the course, or whether the triple is expected to be applied ad hoc, is not stated.
- Assurance is named as a question ("does it really work?") without a scale, a method, or an artefact that would constitute an answer. Whether an assurance argument, an evaluation report, or a certification is the expected answer is left open.
- The relationship between assurance and the residual risk the lecture also asserts is not developed: a certificate of a stated assurance level presumably bounds the residual risk, but no bound is given.
- The "Elements of Security" slide is presented without a worked decomposition of a real system, so the granularity at which policy statements are expected (system level, component level, organisational level) remains unspecified.
