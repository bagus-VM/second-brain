---
title: "Dolev-Yao Attacker Model"
tags: [concept, iot-security, cryptography, semester-1, course-iot-security]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[information-assurance]]", "[[threat-modeling]]"]
---

## One-line Summary
The Dolev-Yao attacker model (1983) is the *standard* adversary model for cryptographic protocol analysis: the attacker controls the entire network — can intercept, modify, replay, inject, and drop any message — but cannot break the cryptographic primitives; security proofs under Dolev-Yao guarantee the protocol is robust against any network-resident adversary, which is why the Mexis et al. paper evaluates their architecture against it.

## Core Intuition
When you design a security protocol, you need to *name your enemy*. The Dolev-Yao model is the most adversarial model in common use: it assumes the attacker can do *anything* an honest network participant can do, plus more. The only thing the attacker *cannot* do is break the math — they cannot, for example, decrypt a message without the key, forge a MAC without the key, or factor an RSA modulus.

The "anything on the network" part means:
- **Intercept**: read any message
- **Modify**: change any message in transit
- **Replay**: re-send a previously captured message
- **Inject**: create and send a new message
- **Drop**: prevent a message from reaching its destination
- **Eavesdrop**: passive observation

But cannot:
- **Decrypt without the key**
- **Forge a MAC without the key**
- **Factor RSA / solve ECDLP**
- **Find a hash collision in SHA-256**
- **Break AES by algebraic attack**

This is the right adversary for protocol design because the *real* network is exactly this hostile. The internet is untrusted; the wireless spectrum is untrusted; an IoT device's connection to its gateway traverses an unknown number of intermediate nodes. If your protocol is secure against Dolev-Yao, it is secure against any realistic network attacker.

The alternative — assuming the attacker can only do *some* things — gives weaker guarantees and is rarely worth the cost. The standard convention in security research: prove security against Dolev-Yao, then the protocol is "secure" in the cryptographic sense.

## Formal Definition / Statement

**Dolev-Yao attacker model (Dolev & Yao, 1983):**

The attacker is a probabilistic polynomial-time (PPT) Turing machine that:
1. Controls the entire communication network
2. Can perform any sequence of the following operations on any message in transit:
   - **Intercept** (read)
   - **Decrypt** (only if the attacker has the relevant key)
   - **Encrypt** (with any key the attacker has)
   - **Sign** (only if the attacker has the relevant private key)
   - **Verify signature**
   - **Concatenate, split** messages
   - **Send** any message the attacker can construct
3. Can intercept and replay previously sent messages
4. Can run any number of sessions in parallel (parallel-session attacks)

The attacker **cannot**:
- Break cryptographic primitives (no factoring RSA, no inverting AES, no SHA-256 collisions, etc.)
- Read the memory of a non-compromised device
- Access an honest party's private keys

**Security under Dolev-Yao:**

A protocol is "secure" if, for any PPT Dolev-Yao attacker:
- **Confidentiality**: the attacker cannot distinguish encryptions of two messages of their choice (IND-CPA)
- **Integrity**: the attacker cannot forge a message that will be accepted (EUF-CMA for signatures, existential unforgeability for MACs)
- **Authentication**: the attacker cannot impersonate an honest party
- **Availability**: the attacker can drop messages (DDoS), but this is typically out of scope for protocol security

**Application to Mexis et al. (2021):**

The paper evaluates the architecture against the Dolev-Yao model and claims robustness against attacks on CIA. The analysis is in Section 5 of the JETC paper. The architecture is secure because:
- Confidentiality: AES-128-CBC for data messages
- Integrity + Authentication: HMAC-SHA-256 for time messages, HMAC over data too
- Replay protection: nonces in time messages, timestamps in data messages
- Key management: PUF-derived keys, never transmitted

What the architecture does *not* protect against:
- Physical destruction of a subsystem (unmitigable)
- Side-channel attacks (out of scope)
- Compromised endpoints (Dolev-Yao assumes endpoints are honest)

## Key Properties / Complexity
- **Standard model**: every cryptographic protocol paper uses Dolev-Yao unless otherwise stated
- **Permutation-based**: formal proofs often use the "indistinguishability" framework
- **Computational soundness**: Dolev-Yao assumes perfect cryptography; real cryptography is only computationally secure. The "computational soundness" theorem (Abadi & Rogaway 2000) bridges the gap.
- **Limited by physical attacks**: a side-channel attack that leaks a key is *not* a Dolev-Yao break
- **Composes well**: if each component is Dolev-Yao secure, the composition usually is too (with care)
- **Symbolic vs computational**: Dolev-Yao is symbolic. Computational models (IND-CCA, EUF-CMA, etc.) are stronger but harder to use.

## Worked Example

**Dolev-Yao attack on a naive protocol:**
```
Protocol: Alice sends Bob her credit card number in cleartext over HTTP
Dolev-Yao attacker: intercepts, reads credit card, profit
Verdict: insecure (no confidentiality)
```

**Dolev-Yao attack on a slightly better protocol:**
```
Protocol: Alice sends Bob AES(K, credit_card)
But K is hard-coded in the firmware
Dolev-Yao attacker: extracts K from any device's firmware (the attacker has *one* compromised device), decrypts all messages
Verdict: insecure (key management failure)
```

**Dolev-Yao secure protocol:**
```
Protocol: TLS 1.3 with ECDHE key exchange + AES-GCM authenticated encryption
- ECDHE provides forward secrecy: compromising one session key does not reveal past sessions
- AES-GCM provides confidentiality + integrity in one primitive
- Server certificate (X.509) authenticates the server
- Client certificate (optional) authenticates the client
Dolev-Yao attacker: cannot decrypt, cannot forge, cannot impersonate (without the server's private key)
Verdict: secure
```

**Mexis et al. architecture under Dolev-Yao:**
```
Attacker can:
  - intercept all MQTT messages
  - replay old messages (but nonces prevent this)
  - inject new messages (but HMAC prevents this)
  - drop messages (DoS, out of scope)
Attacker cannot:
  - decrypt AES-128-CBC without the PUF-derived key
  - forge HMAC-SHA-256 without the key
  - impersonate a slave (would need its PUF key)
Verdict: CIA-robust under Dolev-Yao
```

## Common Pitfalls
- **Confusing Dolev-Yao with "any attacker"**: Dolev-Yao is powerful but bounded. Side-channel attacks, compromised endpoints, and physical destruction are *outside* the model.
- **Proving security only against a weaker model**: e.g., "secure against passive eavesdropper" is much weaker than Dolev-Yao. Most security analyses aim for Dolev-Yao or stronger.
- **Ignoring computational soundness**: symbolic Dolev-Yao proofs don't automatically translate to computational security. Use a computational proof (or rely on established bridges like Abadi-Rogaway).
- **Conflating Dolev-Yao with the threat model**: Dolev-Yao is a *cryptographic* model. A complete threat model also considers physical attacks, insider threats, supply chain compromise, etc.
- **Assuming Dolev-Yao secure = practically secure**: real cryptography has implementation bugs, side channels, and protocol misuse that Dolev-Yao doesn't model. A Dolev-Yao proof is a *necessary* condition for security, not a *sufficient* one.

## Connections
- [[information-assurance]] — CIA is what's protected under Dolev-Yao
- [[threat-modeling]] — Dolev-Yao is one threat model among many
- [[iot-attack-surfaces]] — the surface that Dolev-Yao attacks
- [[iot-attack-taxonomy]] — attacks that fit (and don't fit) the Dolev-Yao model
- [[iot-common-attacks]] — most are network-level, hence Dolev-Yao relevant
- [[paper-iot-lightweight-hardware-architecture]] — Mexis et al. evaluate against Dolev-Yao
- [[paper-iot-mexis-2021-poster]] — same
- [[iot-lecture-3]] — attack types introduced; Dolev-Yao is the formal model
- [[iot-lecture-4]] — secure design goals are CIA under Dolev-Yao
- [[iot-lecture-5]] — attack surface classes
- [[iot-lecture-6]] — cryptographic primitives that provide CIA under Dolev-Yao
- [[symmetric-encryption]] — confidentiality under Dolev-Yao
- [[message-authentication-code]] — integrity + authentication under Dolev-Yao
- [[digital-signatures]] — non-repudiation under Dolev-Yao

## Open Questions
- The Mexis et al. paper is silent on physical attacks. Should a follow-up extend the threat model to include side-channel and physical access?
- For very large IoT networks, is Dolev-Yao the right model, or does the "internal adversary" model (a compromised device) become the dominant concern?
- How does the model extend to quantum attackers? (Dolev-Yao + quantum adversary = "post-quantum Dolev-Yao", an active research area.)
