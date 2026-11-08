---
title: "Advanced IT Security — Exercise 1: Terminology, Attackers, and the Faulty Sensor"
tags: [topic, advanced-it-security, semester-2, exercise]
course: "Advanced IT Security"
source_count: 2
status: current
last_updated: 2026-10-30
prerequisites: ["[[advanced-it-security-lecture-0b]]"]
---

## One-line Summary
The first real exercise sheet: match the security vocabulary, put it in a relation diagram, explain
the three elements of a security solution, rank three attackers by capability rather than by access
— and answer the signed-broken-sensor question the lecture posed without answering.

## Core Map

```
Advanced IT Security — Exercise Sheet 1 (discussion 29.11.2026, supervisor Emiliia Geloczi)
│
├── Topic 1: Elements and Terminology
│   ├── 1a match 8 terms to 8 definitions
│   ├── 1b concrete examples for each
│   ├── 1c put them in relation (Figure 1, 7 relation verbs given)
│   └── 1d the three elements of security, in your own words
│       → [[security-relationship-model]]
│       → [[security-policy-mechanism-assurance]]
│
├── Topic 2: Classification of Attackers
│   ├── 2a why classify attackers at all?
│   ├── 2b one example per class
│   └── 2c the online examination system
│       ├── Profile A external observer (no account, can sniff public Wi-Fi)
│       ├── Profile B student account holder (can register, cannot change grades)
│       └── Profile C system administrator (privileged, policy-bound)
│       → [[attacker-classification]]
│
└── Question 3: Information Security
    ├── 3a The Faulty Sensor — signed but wrong, and the signature verifies
    │       → [[integrity-definition-landscape]]
    └── 3b Policy, Mechanism and Assurance — the grade-modification example
            → [[security-policy-mechanism-assurance]]
```

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[security-relationship-model]] | The seven relation verbs in task 1c — exploit, increase, protect against, expose, have, are met by, indicate — and which arrow each labels. |
| [[attacker-classification]] | Clever outsiders, knowledgeable insiders, funded organisations: the axis is capability and knowledge, not position. |
| [[integrity-definition-landscape]] | Task 3(a) is the signed-sensor question: verification succeeds, because integrity never certified truth. |
| [[security-policy-mechanism-assurance]] | Task 3(b) is the three-element decomposition applied to a grade-modification rule. |

## The Sheet

**Organisational facts, as printed** — and they matter because this sheet is where they appear:

- *"No obligation to work on sheets."*
- *"No amount of points required for exam participation."*
- *"No compulsory attendance."*
- Weekly exercise courses, around **90 minutes**.

So: nothing must be submitted and nothing must be attended. The exercise course exists for the
written exam on 05.04.2027, and the sheet's own instruction is that answers are *discussed*.

The discussion date is **29 November 2026**, supervisor **Emiliia Geloczi**.

## Topic 1 — Elements and Terminology

### 1(a) The matching task

The sheet gives eight terms and eight definitions, deliberately not in corresponding order:

| # | Term | The definition the sheet pairs it with |
|---|---|---|
| 1 | Asset | **C.** Something worth protecting. |
| 2 | Threat | **D.** A potential source of harm to an asset. |
| 3 | Vulnerability | **A.** A weakness that may allow a harmful event to occur. |
| 4 | Safeguard | **B.** A measure that reduces threats or vulnerabilities. |
| 5 | Risk | **G.** The possibility and consequences of harm, depending on assets, threats, vulnerabilities and safeguards. |
| 6 | Residual risk | **H.** Risk that remains after safeguards are applied. |
| 7 | Protection requirement | **F.** A need for protection arising from identified risk. |
| 8 | Value | **E.** An indication of the importance of an asset. |

Two of these are worth noticing against the lecture's own wording. The sheet's *risk* is explicitly
*conditional* — "depending on assets, threats, vulnerabilities and safeguards" — which is the same
claim as the lecture's "risk is a function of" the four. And the sheet's *value* is distinct from
*asset*: value is the indication of importance, the asset is the thing. The lecture's asset slide
gives examples (information and data, hardware, software, documents, services, trust in services,
personnel, an organisation's image) and never uses the word value; the sheet supplies the
distinction.

### 1(b) Concrete examples

| Term | Example (the sheet asks for one each; these are the ones that carry the threats) |
|---|---|
| Asset | The examination system's grade database. |
| Threat | A student account holder motivated to raise a grade. |
| Vulnerability | Grades are writable by any account the access-control list has not been reviewed for. |
| Safeguard | Role-based access control plus an append-only audit log. |
| Risk | A grade is altered and the alteration is not noticed before results are published. |
| Residual risk | The system administrator, who can alter the database directly and whose actions the log records but does not prevent. |
| Protection requirement | Only authorised examiners may modify grades. |
| Value | A published degree's credibility depends on the grades; the asset's importance is high. |

The useful discipline: every row has to name something a real system has. A "threat" of "hackers"
is not an example, it is a category.

### 1(c) Putting them in relation

The sheet supplies exactly seven relation verbs and says multiple usage is allowed:
**exploit, increase, protect against, have, expose, are met by, indicate.** The lecture's
*Beziehungen* diagram is the answer key. Reading the arrows as subject → object:

| Relation | From | To | Reading |
|---|---|---|---|
| exploit | Threat | Vulnerability | a threat *exploits* a vulnerability |
| increase | Vulnerability | Risk | a vulnerability *increases* risk |
| protect against | Safeguard | Threat | a safeguard *protects against* a threat |
| expose | Vulnerability | Asset | a vulnerability *exposes* an asset |
| have | Asset | Value | assets *have* value |
| indicate | Risk | Protection requirement | risk *indicates* the protection requirement |
| are met by | Protection requirement | Safeguard | protection requirements *are met by* safeguards |

[[security-relationship-model]] is the full treatment, including the two arrows the verbs imply but
the list does not name (protection requirements, and where safeguards attach to vulnerabilities as
well as to threats).

### 1(d) The three elements of security

**Policy, mechanism, assurance** — and the sheet asks for them in your own words, which is the test:
can you say what each one *is* without reciting the slide?

- **Policy** is the statement of what the system is supposed to do — the security properties, in
  the language of the real world it governs.
- **Mechanism** is the machinery that implements the policy: the access control, the encryption, the
  audit log.
- **Assurance** is the evidence that the mechanism actually implements the policy — the testing, the
  evaluation, the certification. It is the element that is almost never budgeted for.

[[security-policy-mechanism-assurance]] carries the full argument, including why a mechanism with no
assurance is a belief rather than a control.

## Topic 2 — Classification of Attackers

### 2(a) Why classify at all?

Because security is **relative** and the cost/benefit optimum depends on the adversary. The three
classes are not a taxonomy for its own sake; they are a way to state which assumptions a defence
rests on. Defending against a clever outsider and defending against a funded organisation are
different engineering problems with different price tags, and choosing between them requires naming
the adversary first. The lecture's cost/benefit picture — a U-shaped total cost whose minimum is
well short of 100% — only becomes computable once the threat is quantified, and the class is the
first step of that quantification.

The classification is by **capability and knowledge**, not by motive or by location:
knowledge of *this* system, and resources — equipment, money, people. An expert on system A is an
outsider on system B.

### 2(b) One example per class

| Class | Name | Example |
|---|---|---|
| I | Clever Outsiders | Someone running a published exploit against an unpatched public service. |
| II | Knowledgeable Insiders | A developer with legitimate repository access who uses it to exfiltrate data. |
| III | Funded Organisations | A team with a dedicated budget and specialist staff, targeting a specific organisation over months. |

### 2(c) The online examination system

Three profiles:

| Profile | What it can do |
|---|---|
| **A — External observer** | monitors traffic on public Wi-Fi; no authorised account |
| **B — Student account holder** | has a valid account, can submit examination registrations; not authorised to change grades |
| **C — System administrator** | privileged access to the system and its database, but must follow university policy |

**(a) Ranking by access privileges, and why access alone does not determine danger.**

Ranked by *access*: **C > B > A**. C is inside the system's trust boundary by design; B is a
legitimate user with limited rights; A has no rights at all and only what the network leaks.

**Access alone does not determine danger, and the three profiles show why in three different ways:**

- **A has the least access and is not harmless.** Passive interception on public Wi-Fi needs no
  account, is invisible, and if any part of the session is unauthenticated or unencrypted A learns
  credentials *and* gains B's capability. Low access, high leverage.
- **C has the most access and is not automatically the greatest threat.** The administrator's
  privileges are an *authorised* capability; the security question is what constrains their use. The
  lecture's own integrity slide makes this precise: Clark and Wilson is the one definition that
  forbids modification by an authorised user too, whereas ISO 7498-2 speaks only of *unauthorised*
  modification. Change the definition and the administrator's risk changes without their access
  changing at all.
- **B is the interesting middle.** B's legitimate capability is exactly the kind of thing a defence
  forgets to bound: submitting registrations is authorised, but mass-registering, or registering
  others, or using the registration endpoint to enumerate the exam roll, may all be possible with
  the same access.

So the ranking by *danger* is context-dependent and the ranking by *access* is not. What actually
determines danger is the combination of capability, **policy** (what the actor is supposed to be
allowed to do) and **assurance** (whether that is enforced) — the three elements from Topic 1.

**(b) One plausible misuse per profile, and the security goal primarily threatened:**

| Profile | Misuse | Goal primarily threatened |
|---|---|---|
| A | Intercept an examiner's session credentials on public Wi-Fi and reuse them | **Confidentiality** (and, once reused, integrity) |
| B | Mass-register for examinations, or alter a registration after the deadline | **Integrity** of the registration records |
| C | Modify a grade directly in the database, or restore an old backup that undoes a correction | **Integrity** — by an *authorised* party, which is the hard case |

**(c) A safeguard for each, and one important limitation of it:**

| Misuse | Safeguard | Limitation (residual risk) |
|---|---|---|
| A intercepts on Wi-Fi | TLS on every endpoint, with certificate validation | Does nothing against a compromised client, a malicious certificate authority, or an examiner who ignores the warning |
| B tampers with registrations | Role-based access control + server-side validation of every field and deadline | The legitimate path is still legitimate: B can still register truthfully, repeatedly, within their rights. Validation bounds *what* they change, not *how much* |
| C modifies grades | Separation of duties + append-only audit log + dual authorisation for grade changes | The administrator can often alter the log too; the safeguard converts a silent change into a logged one, which is detection, not prevention. Cf. the lecture's own claim that denial-of-service and misuse by the privileged are "hard to prevent in real life" |

**(d) Why one defence cannot address all three equally well.**

Because the three misuses have **different capabilities, different legitimate paths, and different
trust boundaries**:

- A is *outside* and must be defended at the boundary. A boundary control (TLS, authentication,
  network filtering) does nothing at all against B or C — they are already inside.
- B is *inside with limited rights*. A boundary control is irrelevant; the defence has to be
  authorisation and validation on the operations B may perform.
- C is *inside with full rights*. Authorisation cannot constrain C, because C can change the
  authorisation. The only defences left are separation of duties, physical/organisational controls,
  and tamper-evident logging — and each of those bounds *detection*, not capability.

A control that helps one row actively hurts another: locking the network against A is invisible to
C; demanding dual authorisation for every grade change slows the examiners who are not attackers at
all. That trade-off — expressed as the cost/benefit optimum from lecture 0 — is the real answer to
"why not one defence".

This is also the lecture's attacker-class argument in operational form. Class I, II and III nest:
Class III can buy Class II knowledge and Class I opportunism, so a defence aimed only at the top
class leaves the cheap attack open.

## Question 3 — Information Security

### 3(a) The Faulty Sensor

> An IoT temperature sensor in a university laboratory is defective and reports 43 °C when the
> actual temperature is 23 °C. The device digitally signs its measurements. The signed value reaches
> the server without alteration, and the signature verifies successfully.

**(a) Has the signed message been modified in transit? What does successful verification tell the
server?**

**No — nothing was modified in transit.** The message that arrived is byte-identical to the message
that was signed. Successful verification tells the server three things and no more:

1. the message content is exactly what was signed;
2. the signature was produced by the holder of the signing key;
3. nothing was altered, added or removed between signing and verification.

It does **not** tell the server that the value is true.

**(b) Does the reported temperature necessarily describe the real world correctly?**

**No.** This is the distinction between **data integrity** and **measurement accuracy**, and the
lecture's own Note 4 is the authority: the integrity definition *"is not concerned with the external
consistency or veracity of the data"* [ISO 10181-6]. Integrity is about the data's *history* — the
set of modifications it underwent — while accuracy is a claim about the *world* the reading
describes. The 20 °C error was introduced upstream, by a faulty (not adversarial) component, before
the signing operation; every modification after that satisfies the integrity policy, so integrity
holds and truth fails.

The signature protects the *chain of custody*, not the *correspondence to reality*. Detecting a
20 °C lie requires a plausibility check — a range check, a comparison with a second sensor, a
physical model — and every one of those is an external-consistency control, not an integrity
control. [[integrity-definition-landscape]] is the full treatment.

**(c) An asset, a vulnerability or fault, a possible risk, one safeguard:**

| Element | For this scenario |
|---|---|
| **Asset** | The measurement data, and the decision that depends on it (a laboratory experiment, a safety interlock, a stored experimental record) |
| **Vulnerability / fault** | The sensor is defective — a hardware fault, not an attack. The absence of any plausibility check on the reported value is the second one, and it is the one a defender can act on |
| **Risk** | The server accepts 43 °C as true, and a downstream decision is taken on a value that is 20 °C wrong — an experiment is spoiled, an alarm does not fire, or a record is permanently wrong |
| **Safeguard** | A range/plausibility check on the received value, plus cross-checking against a second sensor; both operate on external consistency, which is exactly the gap the signature leaves |

Note what the safeguard is *not*: it is not a better signature scheme. No improvement to the
cryptography addresses this, which is the point of the question.

### 3(b) Policy, Mechanism and Assurance

> A university states: *"Only authorised examiners may modify students' grades."* It enforces this
> with access controls. Before deploying the system, administrators test that student accounts
> cannot modify grades.

**(a) The three elements:**

| Element | In this scenario |
|---|---|
| **Policy** | "Only authorised examiners may modify students' grades." — a statement of the system's security properties, in natural language |
| **Mechanism** | The access controls that enforce it |
| **Assurance** | The administrators' pre-deployment test that student accounts cannot modify grades |

**(b) Why a mechanism alone is not sufficient to claim the system is secure:**

1. **A mechanism is a claim about implementation, and the claim can be false.** "We deployed access
   controls" and "student accounts cannot modify grades" are different statements; only testing
   connects them. That is what assurance *is*.
2. **The mechanism implements only what the policy says.** The policy here is about *who* may
   modify grades. It says nothing about whether a modified grade is detectable, whether the
   modification is logged, or whether an authorised examiner can modify a grade they have no
   business touching. A perfect mechanism for a thin policy gives a thin guarantee.
3. **The policy may not match the world.** The lecture's own slide says a policy should be aligned
   with the real world it refers to. If the real attacker is a system administrator rather than a
   student, this policy and this mechanism address neither.
4. **One test is not assurance.** The exercise describes a single pre-deployment check. Assurance is
   an *argument* with evidence, and the lecture pairs it with the evaluation slide: a high assurance
   level implies inspection at a very detailed level, and complex systems and high assurance levels
   tend to be mutually exclusive.
5. **Residual risk is always non-zero.** Something remains after the safeguard — this is stated on
   the lecture's own risks slide and is the reason "secure" is meaningless without a "against what".

## The Official Solutions (Exercise_1_with_solutions.pdf)

The official solution deck, 24 slides, dropped after the sheet was written up here. It confirms
most of the answers above and adds three things the sheet-only reading could not have: two tasks
that were not on the sheet PDF, and the wording of the model answers.

**Confirmed by the official deck:**

- **1(a) matching**: the table above is exactly the official pairing (Asset→C, Threat→D,
  Vulnerability→A, Safeguard→B, Risk→G, Residual risk→H, Protection requirement→F, Value→E). The
  open question below about the pairing being an inference is resolved: it was correct.
- **1(b) examples**: the model answers use the same shape as the table above, built on an
  examination database: asset "examination database and student records", threat "unauthorised
  grade modification or disclosure", safeguard "role-based access control, MFA, backups,
  monitoring", residual risk "account compromise may still occur despite MFA and monitoring".
- **2(a) ranking**: C > B > A, as above.
- **2(b)/(c) misuses and safeguards**: the official table matches the one above in substance: A
  reads unencrypted traffic (confidentiality), defended by authenticated encrypted connections,
  residual risk compromised endpoints or metadata leakage; B submits another student's
  registration or exploits flawed authorisation (integrity), defended by server-side
  authorisation checks, residual risk logic errors or stolen credentials; C illegitimately edits
  examination records (integrity), defended by least privilege, separation of duties and audited
  actions, residual risk privileged misuse, collusion, logging failure.
- **3(a) sensor**: no modification in transit; verification means the data was not modified after
  signing and was produced with the corresponding key; 43 °C is still wrong because cryptographic
  integrity does not establish real-world correctness; asset/vulnerability/risk/safeguard as in
  the table above (the official safeguard: independent reference sensor, calibration, plausibility
  checks).
- **3(b)**: policy/mechanism/assurance identified as above; a mechanism alone is insufficient
  because it can be misconfigured, defective, or fail under unexpected conditions, so its
  behaviour must be assessed against the policy.

**Corrected by the official deck:**

- **1(c) relation diagram**: the official diagram puts the verb *increase* on three arrows, not
  one: threats increase risks, vulnerabilities increase risks, **and values increase risks**
  (assets have value, and high value raises the risk). The table above lists only the
  vulnerability→risk arrow, so the values→risks and threats→risks arrows are the addition.

**New in the official deck (tasks the sheet PDF does not show):**

- **A CIA-classification task**: five situations, name the primary affected property. Official
  answers: reading private exam records → confidentiality (unauthorised disclosure); changing a
  grade in the database → integrity (unauthorised alteration); an unreachable registration service
  → availability; a file accidentally altered in transit → integrity; a confidential report made
  publicly downloadable → confidentiality.
- **An attacker-profile task (S1-S5)**: for each scenario, position, behaviour, motivation, and
  the CIA goals threatened. Official answers: S1 employee selling exam records → insider, active,
  financial gain, C; S2 visitor capturing unencrypted wireless traffic → outsider, passive,
  information collection, C; S3 ransomware on a company server → unspecified position/often
  outsider, active, extortion, A+I; S4 administrator changing a colleague's permissions → insider,
  active, disruption/retaliation, A+I; S5 unauthorised password guessing at a login portal →
  outsider (no account stated), active, curiosity/research, potential C+A. The deck's notes: an
  attacker can belong to multiple categories, and one incident can threaten multiple CIA
  properties.
- **A word-search task** (ten security terms hidden in a letter grid), with the solved grid. The
  found terms trace the same vocabulary: among the visible solved words are RISK, ASSURANCE and
  TESSA-style rows; the exercise is vocabulary drilling, not analysis.

The classification wording in the official 2(b) answer is also worth noting: alongside the
Rivest-style Class I/II/III definitions (clever outsiders, knowledgeable insiders, funded
organisations), the model examples run on the position/behaviour/motivation axes (insider vs
outsider, passive vs active, financial vs espionage), with the remark that one attacker can sit in
several categories at once. The [[attacker-classification]] concept page records the Class I-III
axis; the model answer treats the two axes as complementary.

## Connections

- [[advanced-it-security-lecture-0b]] — the deck this sheet exercises.
- [[advanced-it-security-exercise-0]] — the course-organisation sheet; this is the first sheet with
  actual tasks.
- `raw/lectures/Advanced IT Security/Ubung/Exercise_1_with_solutions.pdf` — the official solution
  deck (24 slides), summarised in the section above.
- [[security-relationship-model]] — Topic 1(c) in full.
- [[security-policy-mechanism-assurance]] — Topic 1(d) and Question 3(b) in full.
- [[integrity-definition-landscape]] — Question 3(a) in full, including the same broken-sensor
  question as the lecture posed it.
- [[attacker-classification]] — Topic 2.
- [[security-cost-benefit-optimum]] — the reason Topic 2 asks "why classify attackers".
- [[advanced-it-security]] — the course page.

## Open Questions

- **The sheet does not state which class each of the three examination-system profiles belongs to,
  and none of them maps cleanly.** Profile C (system administrator) has Class II knowledge and
  Class III potential reach; Profile A has neither knowledge of the system nor equipment, so it is
  below Class I as the lecture defines it. The task asks for a ranking by *access*, which is a
  different axis from the lecture's classes — whether the course wants the two axes reconciled is
  not stated.
- **No answer key is provided for 1(a)**; the pairing above is the only consistent assignment, but
  it is an inference from the lecture's vocabulary, not a published solution. *(Resolved
  2026-10-30: the official solution deck confirms the pairing exactly, see the section above.)*
- **The sheet gives no marks and no feedback format.** With no obligation to submit and no points
  required, it is not clear what the deliverable for the discussion session is.
- **Question 3(b) says "test that student accounts cannot modify grades" without saying how.**
  Whether the course intends manual testing, an access-control review, or a formal argument is not
  stated, and the assurance level implied is much lower than the evaluation slide's.
- **The exam is written and covers "everything from lectures and exercises"** per the course page,
  but this sheet's own instruction implies attendance is optional and nothing is submitted. What
  "exercises" contribute to the exam material is therefore not defined.
