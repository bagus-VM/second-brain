---
title: "Advanced IT Security — Exercise 2: Cryptography, the Adversary, and Hash Functions"
tags: [topic, advanced-it-security, semester-2, exercise, cryptography]
course: "Advanced IT Security"
source_count: 3
status: current
last_updated: 2026-11-07
prerequisites: ["[[advanced-it-security-lecture-1]]"]
---

## One-line Summary
The first cryptography sheet: name the three-way terminology split, compare the old and the new paradigm and say why a TTP appears, separate unconditional from conditional security, notice that encryption does not stop an attacker from *deleting* messages — and then work the three hash properties until pre-image, second pre-image and collision can be told apart on sight, ending on why a bare hash value authenticates nobody.

## Core Map

```
Advanced IT Security — Exercise Sheet 2 (discussion 05.11.2026, supervisor Emiliia Gelóczi)
│
├── Question 1 — Cryptography and the Adversary
│   ├── (a) cryptography vs cryptanalysis vs cryptology
│   ├── (b) old vs new paradigm; why a trusted third party is needed
│   ├── (c) unconditional vs conditional security — the fundamental difference
│   └── (d) can the attacker still delete or block? which property suffers?
│       → [[unconditional-vs-conditional-security]]
│
└── Question 2 — Cryptographic Hash Functions
    ├── (a) ease of computation and compression, in your own words
    ├── (b) the three security properties in mathematical notation
    ├── (c) match three search problems to those properties
    ├── (d) n = 32 bits: how many hash values?
    └── (e) MDC vs MAC, and why a hash value alone cannot authenticate
        → [[cryptographic-hash-functions]] · [[mdc-vs-mac]]
```

## Key Concepts at a Glance

| Page | What the sheet exercises |
|------|--------------------------|
| [[cryptographic-hash-functions]] | 2(a)–(d): the definition, the three resistance properties, their differences, and the digest-size arithmetic |
| [[mdc-vs-mac]] | 2(e): the keyed/unkeyed split, and the reason a plain hash cannot attest a sender |
| [[unconditional-vs-conditional-security]] | 1(c): the resource model of the adversary as the fundamental difference |
| [[advanced-it-security-lecture-1]] | The deck behind every question on this sheet — it covers exactly this ground and nothing beyond it |

## The Sheet

Printed facts: *"Exercise Sheet 2"*, winter term 2026/27, **date of discussion 05. November 2026**, supervisor **Emiliia Gelóczi**.

As with sheet 1, the course's own rules apply: handing in is not mandatory, there are no credit
points, attendance is not mandatory but recommended — and the sheet's material is examinable
because the exam covers "everything from the lectures and everything from the exercises".

Two questions, four and five parts. Question 1 is the *introductory* half of lecture 1; question 2
is the deck's payload. There is **no prohibition on outside help** in this sheet (unlike the two
Mining Software Repositories sheets), so full answers follow.

## Question 1 — Cryptography and the Adversary

### 1(a) Cryptography, cryptanalysis, cryptology

| Term | Definition (the lecture's own wording) |
|---|---|
| **Cryptology** | The union of the two: the field that contains both building and breaking. |
| **Cryptography** | The science and study of secret writing — today defined as the study of mathematical techniques related to aspects of information security, such as confidentiality, data integrity, entity authentication and data origin authentication. |
| **Cryptanalysis** | The science and study of methods of *breaking* ciphers. |

So the nesting is cryptology ⊃ {cryptography, cryptanalysis}, and the two members are adversaries
of each other by construction: one builds the system, the other tries to defeat it. Note the modern
widening of "cryptography" — it is no longer only about secrecy of content, but about the
techniques behind integrity and authentication as well.

### 1(b) Old paradigm, new paradigm, and why a TTP

| | Old paradigm | New paradigm |
|---|---|---|
| Parties | A and B **trust each other** | A and B are, e.g., customer and merchant — they **do not** trust each other |
| Channel | insecure; A and B construct a secure logical channel over it | the same insecure channel |
| Intruder | an **outsider** who can read, delete and insert messages | the same outsider **plus** the insider: "we want protection against insider fraud as much as protection against outsiders" |
| Extra machinery | none required | **trusted third parties** to settle disputes |

**Why a TTP becomes necessary.** In the old paradigm, the only dispute is with an outsider, and both
honest parties already share a goal. As soon as the parties themselves may cheat — a merchant who
denies receiving an order, a customer who denies placing one — no protocol between just those two
can resolve the disagreement, because each one's claim is exactly what is in question. A third party
that both sides already trust is the only place an arbiter can come from. The slide states it
directly: *trusted third parties help settle disputes*. The same absence of mutual trust is what
makes key establishment and certification a third-party problem (agenda item 6), and it is the
reason cryptography is described as an *enabling technology* for commerce rather than a fix for it.

### 1(c) Unconditional and conditional security

| | Unconditional | Conditional |
|---|---|---|
| Adversary's computing power | **unbounded** | bounded (a realistic adversary) |
| Guarantee | the system is secure even against unbounded power | breakable in principle, but only with more computing power than a realistic adversary has |
| Measured with | **information theory** | **complexity theory** |
| Durability | an impossibility argument — no future machine changes it | an estimate about the state of the art — a better algorithm or a bigger machine changes it |

**The fundamental difference is the *resource model of the adversary*, not the size of the key and
not "theoretical vs practical".** Everything else follows from it: because the adversary is
unbounded in the first case, only a *structural* argument (there is nothing in the ciphertext to
learn) can work, and that is what information theory measures. Because the adversary is bounded in
the second case, the security is a *cost statement* — "no known attack below X operations" — which
is a claim about today's algorithms and machines, and is the kind of claim every real system uses.
[[unconditional-vs-conditional-security]] carries the worked 32-bit-hash example.

### 1(d) Can the attacker still delete or block the messages?

**Yes — encryption does nothing about it.** Encryption provides the *data confidentiality* service:
it hides the content of messages. The lecture's own intruder model is explicit that the intruder can
*read, delete and insert*; encryption addresses the "read" and leaves "delete" untouched.

The property that suffers is **availability** — the messages do not arrive at all, and no ciphertext
can be verified as missing. Two refinements worth stating because they distinguish a good answer:

- Deletion and insertion also undermine **data origin authentication / integrity of the channel**:
  without authentication, the receiver cannot tell that a message was dropped or that another was
  injected in its place. What is *not* affected is the confidentiality of the messages that do
  arrive.
- Availability is the one of the three classical goals that no cryptographic primitive provides on
  its own; countering deletion is done by redundancy, retransmission, sequence numbers and
  acknowledgements — engineering, with cryptographic authentication used to *detect* tampering
  rather than to prevent suppression. This is the same "which property is affected" move as
  exercise 1's CIA classification task.

## Question 2 — Cryptographic Hash Functions

### 2(a) Ease of computation and compression

- **Ease of computation**: given the function `h` and an input `x`, computing `h(x)` is easy — the
  digest costs about as much as reading the data. A hash function that is expensive to evaluate is
  useless for the jobs (integrity checking, password storage, signatures) it exists for.
- **Compression**: the function maps inputs of *arbitrary* length to results of *fixed* length. This
  is what makes a digest storable and comparable in constant space — and it is also what makes
  collisions unavoidable, since infinitely many inputs share finitely many outputs. Cryptographic
  hashing is the discipline of making those collisions hard to *find*.

### 2(b) The three security properties, in notation

| Property | Statement |
|---|---|
| **Pre-image resistance** (one-way) | for any given `y`, it is computationally infeasible to find `x` such that `h(x) = y` |
| **Second pre-image resistance** | given `x`, it is computationally infeasible to find `x' ≠ x` such that `h(x) = h(x')` |
| **Collision resistance** | it is computationally infeasible to find `x` and `x'`, `x ≠ x'`, such that `h(x) = h(x')` |

**The differences, stated as the free variable:** pre-image resistance fixes the *output* and lets
the adversary search all inputs; second pre-image resistance fixes one *input* and lets the adversary
search for a different input with the same output; collision resistance fixes nothing, so the
adversary may choose both inputs. More freedom makes the problem easier, so collision resistance
implies second pre-image resistance (a collision-finder is a second-pre-image finder for the `x` you
happened to be given) but **not** pre-image resistance. The slide's three Notes are exactly this:
Note 1 (collision ⇒ 2nd pre-image), Note 2 (in practice CRHFs are pre-image resistant as well), Note
3 (pathological examples are collision resistant but not pre-image resistant).

### 2(c) Matching the situations

| Situation | Property |
|---|---|
| a) Given a hash value `y`, find a message `m` such that `h(m) = y` | **Pre-image resistance** |
| b) Given a message `m`, find another message `m' ≠ m` such that `h(m) = h(m')` | **Second pre-image resistance** |
| c) Find any two different messages `m ≠ m'` such that `h(m) = h(m')` | **Collision resistance** |

The giveaway in each case: (a) mentions no input at all, (b) hands you the input, (c) hands you
nothing.

### 2(d) How many hash values can a 32-bit function produce?

`n = 32` bits means `2^32` distinct digests: **2^32 = 4 294 967 296**. The count is computed, not
quoted:

```
2^32                = 4294967296          = 4,294,967,296
birthday bound 2^16 = 65536              (rule of thumb: 50 % collision chance)
exact   sqrt(2·2^32·ln2) ≈ 77163        (same question, computed)
```

The useful second half of the answer: with only 32 bits, finding a collision is expected after
roughly `2^16` tries (the birthday bound) — about 65 000 evaluations, or under a second on a
laptop — while finding a *pre-image* needs about `2^32` tries. That gap is why digest sizes are
chosen against the birthday bound (hence 256 bits, not 64), and it is also why a 32-bit digest can
never be a cryptographic commitment.

### 2(e) MDC vs MAC, and why a hash value alone cannot authenticate the sender

- **MDC (manipulation/modification detection code, message integrity code)** — *unkeyed*. Used to
  detect changes to a document: apply `h` to `x`, keep `h(x)` in a secure place, recompute and
  compare later. Its security rests entirely on the reference value being out of the attacker's
  reach — which is a distribution problem, not a cryptographic one.
- **MAC (message authentication code)** — *keyed*, a function `h(x, k)` of an arbitrary-length input
  and a fixed-length secret key. It assures **both the source of a message and its integrity**,
  because producing a valid tag requires the key.
- **Why a plain hash value is not enough to authenticate the sender:** a hash contains no secret, so
  anyone can compute it. An attacker who intercepts the pair can write their own pair:

```
attacker sees      m,  h(m)
attacker sends     m', h(m')          // their own message and its correct digest
receiver checks    h(m') == h(m')     // passes — and proves nothing about who sent it
```

The receiver has no way to prefer the original pair, because both pairs are equally self-consistent.
Authentication requires something the attacker *cannot* reproduce: a shared secret (MAC) or the
sender's private key (digital signature). This is exactly the slide's service taxonomy — integrity
(hash) and data-origin authentication (MAC/signature) are two different services — and it is also
why the MDC's reference value must arrive through a channel the attacker does not control.

## The Official Solutions, and the Three Tasks the Sheet PDF Did Not Show

`Ubung/Exercise_2_with_solutions.pdf` (15 pages, arrived 2026-11-07) contains the sheet's questions
*with* the model answers. It changes three things about this page.

**1. Every answer above is confirmed.** The deck's wording matches the reasoning given here point by
point: cryptography/cryptanalysis/cryptology; the old paradigm's mutually trusting parties versus the
new paradigm's TTP; unconditional security analysed with information theory and conditional security
with complexity theory; the three properties distinguished by which variable is fixed; 2³² =
4,294,967,296; MDC unkeyed versus MAC keyed, and the modified-message attack showing why a bare hash
authenticates nobody.

**2. It opens with a repetition block that this page did not have.** Three true/false statements with
answers:

| Statement | Answer | The deck's reason |
|---|---|---|
| If a message is encrypted, its integrity and availability are automatically guaranteed | **False** | encryption protects confidentiality; it neither detects modification nor prevents blocking, deletion or delay |
| An insider attacker can also perform an active attack | **True** | the classifications are independent — e.g. an administrator who changes a grade is insider *and* active |
| A system with appropriate safeguards has no remaining security risks | **False** | safeguards reduce risk; what remains is **residual risk** — backups can fail, be corrupted, or be unreachable during the incident |

The third one is the only place in the ingested material where "residual risk" is defined, so it is
worth keeping even though it belongs to lecture 0's vocabulary.

**3. It adds three tasks the sheet PDF did not print at all.** All three are worked below, because
they are the only *numerical* exercises the course has produced so far.

### Task A — Find a collision for h(x) = x mod 13

| Part | Task | Answer |
|---|---|---|
| a | hashes of 17, 25, 39, 42, 52 | 4, 12, 0, 3, 0 |
| b | two different inputs with the same hash | 39 and 52 (both 0) — or 13 and 26 |
| c | given h(x) = 5, one possible input | 5 (also 18, 31, …) |
| d | given x = 17, another input with the same hash | 30 (17 mod 13 = 4, 30 mod 13 = 4) |
| e | which part is which property | b = collision finding, c = pre-image finding, d = second-pre-image finding |

**Why it is not cryptographically secure**, in the deck's terms: it is easy to compute and produces a
fixed-size output, but *inverting it is arithmetic* — given y, the inputs are y + 13k for every integer
k, so pre-image resistance is zero; collisions are equally free (any two inputs 13 apart), so
collision resistance is zero as well. The output space has only 13 values, so the birthday bound of
2^(n/2) is meaningless at this size. Ease of computation and compression are two of the five properties
— the other three are what it lacks.

### Task B — Hash or MAC?

| Scenario | Decision | Why |
|---|---|---|
| A downloaded file is compared against a SHA-256 hash from a trusted source | **Hash** | the reference value arrives through a channel the attacker does not control, so an MDC is sufficient |
| Alice sends Bob a message; Bob wants to verify it came from someone holding their shared key and was not modified | **MAC** | origin authentication requires a secret; only the key holder can produce the tag |
| A company publishes a document and its hash on the same untrusted website | **Neither** | an attacker who controls the site replaces both halves consistently — the pair proves nothing |
| Two users want to communicate confidentially over a public network | **Neither** | confidentiality needs encryption, not a hash or a MAC |

### Task C — True or false

| Statement | Answer | Why |
|---|---|---|
| Two different messages can produce the same hash value | **True** | compression into a fixed-size output makes collisions unavoidable when the input domain is larger |
| A collision-resistant hash function guarantees that collisions do not exist | **False** | collision resistance means finding them is computationally infeasible, not that they are impossible |
| A MAC can help authenticate a message's origin | **True** | a valid tag is evidence that someone possessing the shared key generated it |
| Encryption automatically protects against denial-of-service attacks | **False** | an attacker may still block or delete encrypted traffic |
| Pre-image resistance and second pre-image resistance describe the same problem | **False** | second pre-image starts from a particular input; pre-image starts from a target hash value |

Note the deck's own numbering defect: **question 2 has two parts labelled "(d)"** — the digest-count
question and the MDC/MAC question. They are reproduced here as 2(d) and 2(e) to match this page's
earlier structure, which follows the sheet's ordering.

## Connections

- [[advanced-it-security-lecture-1]] — the deck that covers this sheet question for question.
- [[advanced-it-security-lecture-0]] / [[advanced-it-security-lecture-0b]] — the vocabulary layer underneath (services, properties, attackers).
- [[advanced-it-security-exercise-1]] — the previous sheet; same "answer the property that was asked about" discipline, applied to CIA classification.
- [[cryptographic-hash-functions]] — Question 2 in full.
- [[mdc-vs-mac]] — Question 2(e) in full.
- [[unconditional-vs-conditional-security]] — Question 1(c) in full.
- [[integrity-definition-landscape]] — the definitional fight over "integrity" from lecture 0; Question 1(d) is its operational consequence.
- `raw/lectures/Advanced IT Security/Ubung/Advanced_IT_Sec_Exercise_2.pdf` — the sheet itself.

## Open Questions

- **The official solution deck arrived on 2026-11-07 and confirms every answer above**
  (`Ubung/Exercise_2_with_solutions.pdf`); it also adds the three tasks worked in the section above.
  One open point remains: the deck answers 2(b) in prose sentences rather than in the notation the
  sheet asked for ("using mathematical notation"), so the notation on this page is still this page's
  own construction, not the model answer's.
- **Question 1(d) does not name the property it wants** — "which security property would be
  affected" is answerable as availability alone, or as availability plus the loss of
  origin-authentication. The lecture's intruder model (read/delete/insert) supports the second
  reading; the sheet does not say which is expected.
- **The sheet gives no marks, no hand-in requirement and no feedback format**, as with sheet 1 — the
  discussion session on 05.11.2026 is the only feedback channel.
- **2(d) asks only for the count**, not for the birthday-bound consequence; whether the exam expects
  the consequence unprompted is not stated in the sheet.
