---
title: "MDC vs MAC"
tags: [concept, advanced-it-security, semester-2, cryptography]
course: "Advanced IT Security"
source_count: 2
status: current
last_updated: 2026-11-04
prerequisites: ["[[cryptographic-hash-functions]]"]
---

## One-line Summary
An MDC is an *unkeyed* digest and can only detect that something changed; a MAC is a *keyed* digest and can additionally attest *who* produced it — which is why an ordinary hash value, travelling with its own message, authenticates nothing.

## Core Intuition
A digest is a fingerprint of the data, and a fingerprint proves identity only if the person holding it is not the person being identified. An unkeyed hash has no secret in it: an attacker who rewrites `m` to `m'` simply recomputes `h(m')` and sends the pair. Nothing in the pair lets the receiver prefer the original. Adding a key changes the adversary's job from "compute" to "compute without knowing the secret" — and that is the difference between detecting an accident and detecting an attack.

## Formal Definition / Statement
The lecture's functional classification (slide 13) splits hash functions by whether they are keyed:

| | MDC (manipulation / modification detection code, message integrity code) | MAC (message authentication code) |
|---|---|---|
| Key | **unkeyed** — `h(x)` | **keyed** — `h(x, k)` |
| Detects | changes to a document | the source of a message **and** its integrity |
| Sub-kinds | **OWHF** (pre-image + 2nd pre-image resistant) and **CRHF** (2nd pre-image + collision resistant) | — |
| Trust requirement | the reference digest must be obtained through a channel the attacker does not control | the shared key `k` must be secret to the legitimate parties |

A keyed hash function is formally `h(x, k)`: arbitrary-length input `x`, fixed-length key `k`, fixed-length output.

## Key Properties
- **Unkeyed ⇒ no origin authentication.** Every party can compute `h`; therefore any party can recompute it after modifying the message. The pair `(m, h(m))` is self-consistent for *any* `m` the attacker chooses.
- **An MDC can still detect attacks, but only with an out-of-band reference.** Store `h(x)` in a secure place and compare later: any change is caught. That is the lecture's own formulation (slide 11) and its whole security rests on the reference value being untouchable by the attacker — which is a *distribution* problem, not a cryptographic one.
- **A MAC moves the requirement from a secure channel to a shared secret.** Both parties hold `k`; the attacker does not. Verification of `h(x', k) = tag` therefore fails for a modified `x'` unless the attacker guesses `k` or forges a tag.
- **The MAC does not make the message confidential.** Integrity/origin and confidentiality are separate services (slide 10); a MAC over plaintext leaves the plaintext readable.
- **In the cryptographic-services taxonomy**, the three goals are distinct: data confidentiality (encryption hides content), data integrity (hash functions detect changes), data origin authentication (digital signatures and MACs verify source and integrity). "Data origin authentication" is the goal only the keyed/digital-signature side can meet.

## Worked Example
Exercise sheet 2, Question 2(e) — the exam-shaped version, with the three-way answer:

1. **MDC** = unkeyed hash used to detect changes to a document. Anyone can compute it, so it detects *changes* only in the presence of a trusted reference value.
2. **MAC** = keyed hash (`h(x, k)`) used to assure both the source of a message and its integrity, because producing a valid tag requires the key.
3. **Why an ordinary cryptographic hash value alone cannot authenticate the sender:** the hash contains no secret, so an active attacker who intercepts `(m, h(m))` can replace the pair with `(m', h(m'))` of their own making, and the receiver has no way to tell the two pairs apart. Authentication needs something the attacker cannot reproduce — a key, or a signature over the message with the sender's private key.

The concrete attack in three lines:

```
attacker intercepts   m,   h(m)
attacker sends        m',  h(m')        // m' is the attacker's own message
receiver verifies     h(m') == h(m')    // true — and proves nothing about the sender
```

## Common Pitfalls
- **Believing a digest "travels safely" with its message.** If both come over the same untrusted channel, the digest is decoration; the attack above is two lines of work.
- **Calling MD5/SHA-1 "MACs".** They are unkeyed MDCs; a MAC needs a key and a construction around them (HMAC).
- **Assuming a MAC gives non-repudiation.** Both parties know `k`, so either could have produced the tag; only a digital signature (private key, one holder) supports a dispute with a third party — which is exactly the "new paradigm"/TTP material from slide 7.
- **Forgetting that the reference value must be protected.** Comparing against a hash stored in the same writable place the attacker reached is not integrity.
- **Treating MDC and MAC as interchangeable in the exercise's vocabulary.** The sheet's 2(e) asks for the difference; the key is the whole answer.

## Connections
- [[cryptographic-hash-functions]] — the MDC/MAC taxonomy is half of this page; the OWHF/CRHF split and the three resistance properties live there.
- [[integrity-definition-landscape]] — lecture 0's claim that integrity concerns unauthorised modification (ISO 7498-2) vs Clark–Wilson's stricter "no modification by authorised users either"; a MAC's guarantee is the narrow, history-based kind.
- [[unconditional-vs-conditional-security]] — a MAC's security is conditional, on the key remaining secret and the tag unforgeable within a work bound.
- [[advanced-it-security-lecture-1]] — slides 13 and 10 are the source of the table and the service taxonomy.
- [[advanced-it-security-exercise-2]] — Question 2(e).
- [[gsm-security-political-constraints]] — the LEA/key-escrow material from the same deck as a reminder that key distribution and key recovery are organisational problems wrapped around these primitives.

## Open Questions
- **The deck writes "see later" next to MACs** (slide 13) — the constructions (HMAC and friends) are not in the ingested 16 slides, so this page's MAC treatment is definitional only.
- **Whether the course wants the textbook "MDC detects accidental corruption, MAC detects deliberate modification" framing** is not stated; the slide's own criterion is the keyed/unkeyed split, and this page follows the slide.
