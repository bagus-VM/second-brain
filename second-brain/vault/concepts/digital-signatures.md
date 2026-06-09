---
title: "Digital Signatures"
tags: [concept, iot-security, semester-1, cryptography]
course: "IoT Security"
source_count: 0
status: current
last_updated: 2026-06-08
prerequisites:
  - cia-triad
  - trusted-platform-module
---

## One-line Summary
*A digital signature is a cryptographic mechanism that proves a message was created by a specific sender and has not been altered in transit.*

## Core Intuition
Imagine you write a letter and seal it with a wax stamp unique to you. Anyone can verify the seal is yours, but no one can forge it without your stamp. A digital signature does the same thing for electronic data: it binds a piece of data to the identity of its creator, providing both **authentication** (who sent it) and **integrity** (it wasn't tampered with). Unlike a physical signature, a digital signature changes completely if even a single bit of the message changes — making forgery computationally infeasible.

In IoT, digital signatures are everywhere: firmware updates are signed so devices can verify they're loading legitimate code (not malware), device identities are signed by certificate authorities, and commands between devices can be signed to prevent spoofing.

## Formal Definition / Statement
A digital signature scheme consists of three algorithms:

1. **Key Generation** (KeyGen): Generate a public-private key pair (pk, sk).
2. **Signing** (Sign): Given a message *m* and the private key *sk*, produce a signature *σ = Sign(sk, m)*.
3. **Verification** (Verify): Given a message *m*, signature *σ*, and public key *pk*, return true or false: *Verify(pk, m, σ) ∈ {true, false}*.

**Security requirements:**
- **Correctness:** Valid signatures always verify: *Verify(pk, m, Sign(sk, m)) = true*
- **Unforgeability:** Without the private key *sk*, no computationally bounded adversary can produce a valid signature for any new message (Existential Unforgeability under Chosen-Message Attack — EUF-CMA)
- **Non-repudiation:** The signer cannot deny having signed the message (unlike symmetric MACs where both parties share the key)

## How It Works — Step by Step

### Signing
1. Compute a **cryptographic hash** of the message: *h = Hash(m)* (e.g., SHA-256)
2. **Encrypt the hash** with the signer's private key: *σ = Encrypt(sk, h)*
3. Send the message *m* along with the signature *σ*

### Verification
1. Receive message *m* and signature *σ*
2. Compute the hash: *h = Hash(m)*
3. **Decrypt the signature** using the signer's public key: *h' = Decrypt(pk, σ)*
4. Compare: if *h = h'*, the signature is valid

**Why hash first?** Signing the full message would be slow (asymmetric crypto is expensive). Hashing reduces the data to a fixed-size digest (256 bits for SHA-256) regardless of message length.

## Common Algorithms

| Algorithm | Key Size | Signature Size | Based On | Notes |
|-----------|----------|----------------|----------|-------|
| RSA (PKCS#1 v1.5 / PSS) | 2048–4096 bit | Same as key size | Integer factorization | Widely deployed, larger signatures |
| ECDSA (P-256, P-384) | 256–384 bit | ~64–96 bytes | Elliptic curve DLP | Smaller keys, preferred for constrained devices |
| Ed25519 | 256 bit | 64 bytes | Twisted Edwards curve | Fast, deterministic (no random nonce needed) |

**In IoT context:** The lectures reference **RSA-2048**, **ECDSA-P256**, and **Ed25519** for firmware signing. ECDSA and Ed25519 are preferred for resource-constrained devices due to smaller key and signature sizes.

## Key Properties
- **Provides:** Authentication, Integrity, Non-repudiation
- **Does NOT provide:** Confidentiality (the message is sent in plaintext; combine with encryption for secrecy)
- **Asymmetric:** Requires public/private key pair (unlike MACs which use a shared secret)
- **Computationally expensive:** ~1000x slower than symmetric operations — this is why messages are hashed first
- **Non-repudiation:** Unique to digital signatures (not available in MACs). The signer cannot later claim they didn't sign.

## Worked Example — Firmware Update Signature

An IoT device manufacturer wants to push a firmware update:

1. **Manufacturer signs the firmware:**
   - Hash the firmware image: *h = SHA-256(firmware.bin)*
   - Sign with manufacturer's private key: *σ = ECDSA-Sign(sk_manufacturer, h)*
   - Publish: firmware.bin + σ + certificate chain

2. **Device receives and verifies:**
   - Extract public key from certificate, verify certificate chain against root of trust
   - Hash the received firmware: *h' = SHA-256(firmware.bin)*
   - Verify: *ECDSA-Verify(pk_manufacturer, h', σ)*
   - If valid → install firmware. If invalid → reject and rollback to previous version.

This prevents: (a) an attacker pushing malicious firmware, (b) a MITM modifying the firmware in transit, (c) rollback attacks (when combined with version numbers).

## Common Pitfalls
- **Confusing digital signatures with MACs:** MACs use a shared symmetric key (both parties can sign) — no non-repudiation. Digital signatures use asymmetric keys — only the private key holder can sign.
- **Signing without hashing:** Technically possible but insecure (RSA textbook signatures are vulnerable to existential forgery) and impractical (signing the full message is slow).
- **Random nonce reuse in ECDSA:** If the same nonce *k* is used for two different messages with the same private key, the private key can be trivially recovered. This is how the PlayStation 3 ECDSA key was extracted.
- **Signature ≠ Encryption:** "Signing is encrypting with the private key" is a useful mental model for RSA but technically misleading for ECDSA/Ed25519 where the math is different.
- **Forgetting certificate verification:** A valid signature means nothing if you don't verify who owns the public key. Always verify the certificate chain.

## Connections
[[iot-security-exam-format]] — Digital signatures given as example security solution exam question
[[firmware-security]] — Firmware images must be cryptographically signed (RSA-2048, ECDSA-P256, Ed25519)
[[iot-secure-design]] — Goal 3: Firmware integrity via cryptographic signing
[[trusted-platform-module]] — TPMs perform signing operations and store signing keys securely
[[ota-updates]] — Signed firmware updates with anti-rollback
[[cia-triad]] — Digital signatures protect Integrity and provide Authentication
[[information-assurance]] — Non-repudiation is one of the extended security properties
[[physical-unclonable-functions]] — PUFs can generate device-specific keys used for signing

## Open Questions
- [ ] Does the exam expect the RSA-specific "sign = encrypt with private key" explanation, or the general hash-then-sign model?
- [ ] Are we expected to know the math behind ECDSA or Ed25519, or just the conceptual workflow?
- [ ] Are certificate chains and PKI in scope for the exam?
