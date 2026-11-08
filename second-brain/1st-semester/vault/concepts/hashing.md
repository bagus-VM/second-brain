---
title: "Cryptographic Hashing"
tags: [concept, iot-security, cryptography, semester-1, course-iot-security]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[information-assurance]]"]
---

## One-line Summary
A cryptographic hash H maps arbitrary-length input to a fixed-length digest with three security properties — pre-image resistance, second pre-image resistance, collision resistance — and is the building block for digital signatures, MACs (HMAC), key derivation, password storage, and data fingerprinting; SHA-256 and SHA-3 are the modern standards, MD5 and SHA-1 are broken and deprecated.

## Core Intuition
A cryptographic hash is a "fingerprint function" for digital data. Take any input — a 1-byte message, a 4 GB firmware image, the entire Bible — and you get a fixed-size output, typically 256 bits. The output is the *digest*. Two different inputs should, with overwhelming probability, give two different digests. And you should not be able to reverse the function: given a digest, finding an input that hashes to it should be computationally infeasible.

This combination of properties makes the hash function the workhorse of modern cryptography:

- **Integrity**: hash the message, send the hash separately, recompute on receive, compare. If the hashes match, the message wasn't modified.
- **Digital signatures**: instead of signing the (potentially huge) message, sign its 256-bit hash. Verification does the same.
- **HMACs**: hash-based message authentication codes use a key combined with the message through two hash passes.
- **Key derivation**: turn a low-entropy password into a high-entropy key via iterated hashing.
- **Password storage**: store H(password || salt) instead of the password. The server never sees the password in the clear.
- **Merkle trees**: blockchains, git, IPFS, certificate transparency — all use hash trees.

**Three security properties** to fix:

1. **Pre-image resistance**: given y, hard to find m with H(m) = y. (Pre-image: the input.)
2. **Second pre-image resistance**: given m₁, hard to find m₂ ≠ m₁ with H(m₁) = H(m₂).
3. **Collision resistance**: hard to find *any* m₁ ≠ m₂ with H(m₁) = H(m₂). This is the strongest property and the hardest to achieve — by the birthday paradox, a hash with n-bit output has collisions after ~√(2^n) = 2^(n/2) hashes. SHA-256 has 256-bit output, so collision-finding takes ~2^128 work, which is infeasible. MD5 has 128-bit output, so collisions should take ~2^64 work — but clever attacks find them in seconds.

## Formal Definition / Statement

A cryptographic hash function H: {0,1}* → {0,1}^n satisfies:

1. **Deterministic**: H(m) is always the same for the same m
2. **Fast to compute** for any m
3. **Pre-image resistance**: given y, finding m with H(m) = y is infeasible
4. **Second pre-image resistance**: given m₁, finding m₂ ≠ m₁ with H(m₁) = H(m₂) is infeasible
5. **Collision resistance**: finding any m₁ ≠ m₂ with H(m₁) = H(m₂) is infeasible
6. **Avalanche effect**: changing 1 bit of m changes ~50% of the bits of H(m)

**Common hash functions (from the lecture context + standard knowledge):**

| Hash | Output | Status | Notes |
|---|---|---|---|
| MD5 | 128 bits | **Broken** (collisions) | Never use |
| SHA-1 | 160 bits | **Broken** (collisions, 2017 SHAttered) | Deprecated by NIST 2011 |
| SHA-256 (SHA-2 family) | 256 bits | Secure | Most widely deployed |
| SHA-384, SHA-512 | 384, 512 bits | Secure | High-security variants |
| SHA-3 (Keccak) | 224, 256, 384, 512 bits | Secure | Different design (sponge), SHA-2 backup |
| BLAKE2 | 256, 512 bits | Secure | Faster than SHA-256, used in some modern systems |
| BLAKE3 | 256 bits (XOF) | Secure, modern | Very fast, parallelisable |

**How SHA-256 works (Merkle–Damgård construction):**
1. Pad the message to a multiple of 512 bits
2. Initialise 8 32-bit state variables (h₀ through h₇) with fixed constants
3. Process each 512-bit block:
   - Expand the block into 64 32-bit words
   - 64 rounds of bitwise operations: Ch, Maj, Σ, σ, with K constants
   - Update the state
4. Concatenate the final state to get the 256-bit digest

**SHA-3 (Keccak) uses a different construction: the sponge.**
- Capacity c = 2·output length (e.g., c = 512 for SHA3-256)
- Rate r = 1600 - c (e.g., r = 1088 for SHA3-256)
- Absorb phase: XOR input blocks into the r-bit rate portion of the state, then apply the Keccak-f permutation
- Squeeze phase: read r bits from the rate portion

## Key Properties / Complexity
- **Fixed output size** regardless of input
- **Deterministic** (same input → same output, always)
- **Avalanche effect**: tiny input change → totally different output
- **Collision resistance**: ~2^(n/2) work to find a collision for n-bit hash
- **Pre-image resistance**: ~2^n work to find a pre-image
- **Speed**: SHA-256 ~500 MB/s software on modern CPU, ~10 GB/s hardware
- **Quantum-weakened by Grover**: hash with n-bit output has ~n/2 effective bits. So SHA-256 → 128-bit quantum security. SHA-512 is the post-quantum hedge.
- **HMAC construction**: H(k ⊕ opad ‖ H(k ⊕ ipad ‖ m)) — uses the hash twice with different pads

## Worked Example

**Password storage:**
```
user registers with password "correct horse battery staple"
  server generates random salt s (16 bytes)
  server stores: s, h = SHA-256(s || "correct horse battery staple")
user logs in with password "correct horse battery staple"
  server reads salt s, computes h' = SHA-256(s || password)
  server compares h' to stored h
  if match: authentication succeeds
```

The salt prevents rainbow table attacks: two users with the same password get different hashes. The hash prevents the server from learning the password (server stores only the hash).

**SHA-256 collision attack on MD5 (the famous example):**
- In 2004, Wang et al. demonstrated MD5 collisions in ~1 hour on a desktop
- In 2008, researchers forged an X.509 certificate using an MD5 collision
- Result: MD5 was definitively broken for any integrity-critical use
- This drove the migration to SHA-2 and the development of SHA-3

**HMAC-SHA256 (used in the Mexis et al. paper for IoT authentication):**
```
k = 32-byte shared secret
ipad = 0x36 repeated 64 times
opad = 0x5c repeated 64 times
HMAC(k, m) = SHA-256((k ⊕ opad) ‖ SHA-256((k ⊕ ipad) ‖ m))
```

This construction is provably secure as a MAC if the underlying hash is a secure PRF, and it does not require any extension of the hash function's attack surface.

## Common Pitfalls
- **MD5 or SHA-1 for integrity or signatures**: broken. Use SHA-256 minimum.
- **Hashing passwords without salt**: rainbow tables defeat the hash instantly. Always salt.
- **Hashing passwords with a single SHA pass**: too fast. Brute force at billions of guesses per second. Use a slow KDF: bcrypt, scrypt, Argon2, or PBKDF2 with high iteration count.
- **Storing the salt and the hash together**: that's fine, the salt is not secret. The salt's job is to make rainbow tables impractical, not to be secret.
- **Confusing hashing with encryption**: hashing is one-way, encryption is reversible. You cannot "decrypt" a hash. The word "decrypt" in marketing for password "recovery" tools means brute force.
- **Using a hash to compare two values for equality**: timing attacks can leak the matching prefix. Use a constant-time compare (`subtle.ConstantTimeCompare` in Go, `crypto.timingSafeEqual` in Node, `hmac.compareDigest` in Python).

## Connections
- [[information-assurance]] — integrity is what hashing provides
- [[symmetric-encryption]] — often combined with hashing (encrypt-then-MAC, AEAD)
- [[asymmetric-encryption]] — combined with hashing in signatures (hash-then-sign)
- [[digital-signatures]] — RSA-PSS, ECDSA, Ed25519 all hash the message first
- [[message-authentication-code]] — HMAC is the standard hash-based MAC
- [[key-management-lifecycle]] — hashing is used in key derivation (HKDF, PBKDF2)
- [[random-number-generator|TRNGs]] — salts must be random (TRNG or CSPRNG)
- [[ota-updates]] — firmware hashes are signed
- [[mqtt-security]] — TLS uses HMAC-SHA256 for record authentication (older suites)
- [[iot-lecture-6]] — source lecture
- [[nist-iot-cybersecurity]] — NIST's role in standardising hash functions

## Open Questions
- Will SHA-3 ever displace SHA-2 in practice, or will SHA-2 remain dominant for inertia reasons?
- For ultra-constrained IoT devices, is there a use case for truncated hashes (e.g., SHA-256/128 = first 128 bits) to save bandwidth? (Yes, in some protocols.)
