---
title: "Asymmetric Encryption"
tags: [concept, iot-security, cryptography, semester-1, course-iot-security]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[information-assurance]]", "[[symmetric-encryption]]"]
---

## One-line Summary
Asymmetric encryption uses a public/private key pair — the public key encrypts, the private key decrypts — solving the key distribution problem at the cost of being ~1000× slower than symmetric crypto; the two main families are integer-factorisation (RSA) and elliptic-curve discrete-logarithm (ECC), with both being quantum-vulnerable and replaced by post-quantum algorithms in the 2020s.

## Core Intuition
The asymmetry comes from *one-way functions with a trapdoor*. There is a mathematical operation that is easy to do one way and infeasible to reverse — *unless* you have a special piece of information (the private key) that makes the reverse easy.

For **RSA**, the one-way function is *multiplying two large primes*. Multiplying is fast; factoring the product back into the primes is believed to be hard (no polynomial-time algorithm is known on a classical computer). The trapdoor is knowledge of the prime factors, which lets you compute the private key from the public key.

For **ECC (Elliptic Curve Cryptography)**, the one-way function is *scalar multiplication on an elliptic curve*. Given a base point G and a scalar k, computing P = kG is fast. Given P and G, recovering k is the **elliptic curve discrete logarithm problem (ECDLP)** — believed to be hard on classical computers. The trapdoor is knowledge of k.

In both cases, the public key is derived from the private key (modulus N = p·q for RSA; point P = kG for ECC), but the reverse direction is computationally infeasible. The user publishes the public key; only they can decrypt with their private key.

**The killer feature**: key distribution is solved. To send Alice an encrypted message, you look up her public key (which can be in a public directory) and encrypt with it. Only Alice's private key can decrypt. No shared secret required beforehand.

**The killer drawback**: speed. RSA operations are 100-1000× slower than AES. ECC is faster than RSA but still 10-100× slower than AES. So in practice, **almost all protocols use hybrid encryption**: asymmetric to exchange a fresh symmetric key, then symmetric for bulk data. TLS does exactly this (RSA or ECDHE for key exchange, AES-GCM for data).

## Formal Definition / Statement

A public-key (asymmetric) encryption scheme is a triple:
- **KeyGen**(1^λ) → (pk, sk) (public + private key pair)
- **Enc**(pk, m) → c
- **Dec**(sk, c) → m  (with Dec(sk, Enc(pk, m)) = m)

**Security**: IND-CCA (indistinguishability under chosen-ciphertext attack).

**RSA (Rivest-Shamir-Adleman, 1977):**
- **Key generation**:
  - Choose two large random primes p, q
  - Compute N = p·q (modulus, typically 2048 or 4096 bits)
  - Compute φ(N) = (p-1)(q-1)
  - Choose e (public exponent, typically e = 65537 = 2^16+1)
  - Compute d = e^(-1) mod φ(N) (private exponent)
  - pk = (N, e), sk = (N, d) [p, q, φ(N) discarded]
- **Encrypt**: c = m^e mod N
- **Decrypt**: m = c^d mod N
- **Security assumption**: integer factorisation is hard (no known polynomial-time algorithm on classical hardware)
- **Padding schemes** (raw RSA is deterministic and malleable, so you must pad):
  - PKCS#1 v1.5 — older, has known implementation bugs (Bleichenbacher)
  - OAEP (Optimal Asymmetric Encryption Padding) — modern, IND-CCA secure

**ECC (Elliptic Curve Cryptography, mid-1980s):**
- **Key generation**:
  - Choose an elliptic curve E over a prime field F_p (e.g., NIST P-256, Curve25519)
  - Choose a base point G on E of prime order n
  - Choose random scalar k ∈ [1, n-1]
  - pk = kG (a point on E), sk = k
- **Encrypt / decrypt**: depends on the scheme — ECIES (Elliptic Curve Integrated Encryption Scheme) is the standard. Uses ECDH for key agreement + AES for bulk data.
- **Security assumption**: elliptic curve discrete logarithm problem (ECDLP) is hard

**Common curves:**
| Curve | Field size | Security | Notes |
|---|---|---|---|
| NIST P-192 | 192-bit | ~96 bits | Deprecated |
| NIST P-224 | 224-bit | ~112 bits | |
| NIST P-256 (secp256r1) | 256-bit | ~128 bits | Widely deployed, TLS, Bitcoin |
| NIST P-384 (secp384r1) | 384-bit | ~192 bits | High-security |
| NIST P-521 (secp521r1) | 521-bit | ~256 bits | Top-tier |
| Curve25519 (X25519) | 255-bit | ~128 bits | Faster, cleaner, used in TLS 1.3, Signal |
| Ed25519 | 255-bit | ~128 bits | Signature curve, used in SSH, TLS 1.3 |
| secp256k1 | 256-bit | ~128 bits | Bitcoin, Ethereum |

**Key size equivalence (approximate, classical security):**
| Symmetric | RSA | ECC |
|---|---|---|
| 128 bits | 3072 bits | 256 bits |
| 192 bits | 7680 bits | 384 bits |
| 256 bits | 15360 bits | 512 bits |

This is why ECC dominates in IoT: equivalent security with much smaller keys, signatures, and ciphertexts.

## Key Properties / Complexity
- **Solves key distribution**: public key can be published
- **~1000× slower than symmetric** (RSA), ~10-100× slower (ECC)
- **Enables digital signatures**: only the private key holder can sign
- **Enables non-repudiation**: signatures are publicly verifiable but only the private key holder can produce them
- **RSA-2048 ≈ ECC-224 in security**, RSA-3072 ≈ ECC-256
- **Quantum-broken**: Shor's algorithm factors integers and computes ECDLP in polynomial time. Both RSA and ECC are dead against a sufficiently large quantum computer. NIST standardised post-quantum algorithms (Kyber, Dilithium) in 2024.
- **Large key sizes**: RSA-2048 keys are 256 bytes; ECC-256 keys are 32 bytes (private) or 65 bytes (public, uncompressed)

## Worked Example

**RSA-2048 encryption of a 256-byte message:**
- m padded to 256 bytes using OAEP → padded
- c = padded^65537 mod N (modular exponentiation, slow on software)
- c is 256 bytes (same length as modulus)

Decryption: padded = c^d mod N, then unpad. The modular exponentiation with a 2048-bit exponent is the slow part — milliseconds on a small MCU.

**Hybrid encryption (TLS-style):**
1. Client generates random 32-byte AES key K
2. Client encrypts K with server's RSA public key: c = RSA-OAEP(pk_server, K)
3. Server decrypts: K = RSA-OAEP-decrypt(sk_server, c)
4. Both sides use K for AES-GCM bulk encryption

This gives you the key distribution of RSA with the speed of AES. The 1000× RSA cost is amortised over a long AES session.

**ECDSA signature (used in TLS, Bitcoin):**
1. Choose random nonce k (MUST be unique per signature, or the private key leaks — this is the PlayStation 3 bug)
2. Compute (r, s) where r = (kG)_x mod n, s = k^(-1)(H(m) + d·r) mod n
3. Signature is (r, s)
4. Verify: u1 = H(m)·s^(-1) mod n, u2 = r·s^(-1) mod n, R = u1·G + u2·pk. Accept if R_x = r mod n.

## Common Pitfalls
- **Reusing a nonce in ECDSA**: catastrophic. Recovers the private key. This is the most famous crypto bug in history (Sony PlayStation 3).
- **Using textbook RSA without padding**: deterministic, malleable, vulnerable to many attacks. Always use OAEP (encryption) or PSS (signatures).
- **Confusing RSA key sizes**: RSA-2048 is ~equivalent to ECC-224, NOT ECC-256. ECC key sizes are smaller because of the underlying math.
- **Forgetting that RSA-2048 is quantum-broken**: against a CRQC (cryptographically relevant quantum computer), RSA-2048 is broken. Migrate to post-quantum (Kyber for key exchange, Dilithium for signatures).
- **Slow private-key operations on small MCUs**: RSA-2048 decryption takes ~100ms on a Cortex-M4. ECC-256 ECDSA sign takes ~50ms. IoT key sizes should be chosen with the device's compute budget in mind.
- **Hard-coding private keys in firmware**: never do this. Use a TPM, secure element, or PUF-based key generation.

## Connections
- [[information-assurance]] — confidentiality, authentication, non-repudiation
- [[symmetric-encryption]] — alternative, fast but needs shared secret
- [[digital-signatures]] — the other major asymmetric primitive
- [[key-management-lifecycle]] — operational challenge
- [[hashing]] — used in signatures (hash-then-sign)
- [[message-authentication-code]] — symmetric alternative for integrity
- [[physical-unclonable-functions]] — can generate private keys without storing them
- [[trusted-platform-module]] — stores private keys in hardware
- [[ota-updates]] — signatures verify firmware authenticity
- [[mqtt-security]] — TLS uses ECDHE for key exchange, RSA or ECDSA for server authentication
- [[iot-lecture-6]] — source lecture

## Open Questions
- Will post-quantum migration (Kyber, Dilithium) be a smooth transition, or will it be a multi-decade mess like the DES→AES migration?
- For an IoT device with no TLS support, can elliptic-curve key exchange (ECDH) be implemented to establish a shared secret with a server? (Yes — Curve25519 is fast and small.)
