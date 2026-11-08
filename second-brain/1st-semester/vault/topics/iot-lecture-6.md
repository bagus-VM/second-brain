---
title: "Cryptography and Lightweight Security Primitives for IoT"
tags: [topic, iot-security, semester-1, course-iot-security, cryptography]
course: "IoT Security"
source_count: 2
status: current
last_updated: 2026-06-14
prerequisites: ["[[iot-lecture-3]]", "[[iot-lecture-5]]", "[[information-assurance]]"]
sources: ["raw/lectures/iot_security/IoTsec6_2026.pdf"]
---

## One-line Summary
Cryptography gives IoT devices the four basic security services — confidentiality (encryption), integrity (hashing/MAC), authentication (signatures/MAC), non-repudiation (asymmetric signatures) — using either symmetric algorithms (one shared key) or asymmetric algorithms (public/private key pair); the lecture then introduces the hardware security primitives ([[physical-unclonable-functions]], [[trusted-platform-module]], TRNGs) and the NIST lightweight crypto standardisation that produced ASCON.

## Core Intuition

The first half of the lecture maps the four extended CIA properties to the cryptographic mechanisms that provide them:

| Security service | Cryptographic mechanism |
|---|---|
| Confidentiality | **Encryption** (symmetric or asymmetric) |
| Integrity | **Digital signature** or **Message Authentication Code (MAC)** |
| Authentication | **Digital signature** or **MAC** |
| Non-repudiation | **Digital signature** (asymmetric only) |

Two facts to fix in mind before anything else:

1. **Symmetric crypto uses one shared secret key**. It is fast, but the key has to be distributed securely to every party, and it cannot provide non-repudiation (because both parties could have produced the MAC, the signer can deny it).
2. **Asymmetric crypto uses a public/private key pair**. It is ~1000× slower, but solves key distribution (publish the public key freely) and uniquely provides non-repudiation (only the holder of the private key can sign).

The second half of the lecture zooms into the practical primitives an IoT device actually has on the chip:

- **Memory-based [[physical-unclonable-functions]]** — the start-up values of SRAM, the decay characteristics of DRAM, the rowhammer disturbance in DRAM, the read/write latency of cells. All of these exploit the fact that the silicon itself is the security anchor, and the "key" is a property of the physical hardware that cannot be cloned.
- **[[trusted-platform-module]]s** — a dedicated cryptoprocessor that holds keys and performs crypto operations in tamper-resistant hardware. Costs money, area, and power, so it is only used in high-end IoT.
- **[[random-number-generator|TRNGs]]** — needed because every cryptographic key, nonce, and IV is drawn from a high-entropy source. Deterministic / software-only RNGs (PRNGs, DRBGs) are not safe for key generation; only physics-based or memory-based TRNGs are.
- **[[lightweight-cryptography]]** and **[[ascon]]** — the NIST-driven response to the fact that AES, SHA-2, RSA, and ECDSA are too heavy for the smallest IoT devices. ASCON won the NIST lightweight crypto competition in 2023 and is now the recommended algorithm for constrained IoT.

## Formal Definition / Statement

### Types of basic security applications (the lecture's own taxonomy)

1. **Encryption / Decryption** — provides **confidentiality**
   - Symmetric: AES, Blowfish, DES, 3DES, Twofish, CAST-128, Camellia, IDEA
   - Asymmetric: RSA, Elliptic Curve Cryptography (ECC)
2. **Hashing** — provides **integrity** (and is a building block for signatures, MACs, key derivation)
3. **Digital signatures** — provide **integrity**, **authentication**, and **non-repudiation**
   - Symmetric variant: Message Authentication Code (MAC) — integrity + data-origin authentication only, no non-repudiation
   - Asymmetric variants: RSA (with PKCS#1 or PSS padding), DSA, ECDSA
4. **Random number generation** — provides the entropy for keys, nonces, IVs

### Symmetric vs Asymmetric — the table to memorise

| Property | Symmetric | Asymmetric |
|---|---|---|
| Keys | 1 shared secret | Public + private pair |
| Speed | Fast (MB/s–GB/s) | Slow (KB/s–MB/s) |
| Key distribution | Hard (must share out-of-band) | Easy (publish public key) |
| Non-repudiation | No | Yes |
| Examples | AES, 3DES, ChaCha20 | RSA, ECDSA, Ed25519 |
| Key sizes (today) | 128-bit AES, 256-bit ChaCha20 | 2048+ bit RSA, 256-bit EC |
| Typical use | Bulk data encryption | Key exchange, signatures, certificates |

### Hashing

A cryptographic hash H: {0,1}* → {0,1}^n with three properties:

- **Pre-image resistance**: given y, hard to find m with H(m) = y
- **Second pre-image resistance**: given m₁, hard to find m₂ ≠ m₁ with H(m₁) = H(m₂)
- **Collision resistance**: hard to find any m₁ ≠ m₂ with H(m₁) = H(m₂)

Examples: SHA-1 (broken), SHA-256, SHA-3 (Keccak), BLAKE2. MD5 and SHA-1 are deprecated — they have known collisions.

### Digital signatures (the four-step construction)

1. **Key generation**: (pk, sk) ← KeyGen(1^λ)
2. **Sign**: σ ← Sign(sk, m)
3. **Verify**: Verify(pk, m, σ) → {accept, reject}
4. **Security**: existentially unforgeable under chosen-message attack (EUF-CMA)

### MACs (symmetric "signatures")

MAC_k(m) = tag. Both sender and receiver share k. Properties:

- **Integrity**: any modification of m invalidates the tag (with overwhelming probability)
- **Data-origin authentication**: only a party holding k could have produced the tag
- **No non-repudiation**: the verifier could have produced the same tag, so the signer can deny

Examples:
- **HMAC-SHA1** / **HMAC-SHA256** — hash-based, most common
- **CMAC** — block-cipher based, uses AES or 3DES
- **GMAC** — the authentication component of GCM mode of AES (GCM = Galois/Counter Mode, gives authenticated encryption)

### Random number generators

| Type | Source | Use |
|---|---|---|
| **TRNG** (True RNG / NDRNG) | Physical process: thermal noise, photoelectric effect, radioactive decay, memory start-up values, rowhammer disturbance | Cryptographic key generation, nonces |
| **PRNG** (Pseudo RNG / DRBG) | Deterministic algorithm seeded by entropy; expands seed into a stream of bits | Non-key uses (e.g., padding, salts) |

A TRNG output is **unpredictable but usually biased** — you need **entropy distillation** (von Neumann correction, hash-based post-processing, parity-based methods) to get unbiased random bits suitable for cryptographic use.

### Memory-based PUFs (the practical IoT flavour)

The lecture lists seven concrete memory-based PUF constructions:

1. **SRAM PUF** — power-up values of SRAM cells
2. **DRAM PUF (start-up values)** — same as SRAM PUF, in DRAM
3. **DRAM PUF (decay-based)** — how DRAM cells lose charge over time after power-off
4. **DRAM PUF (data remanence)** — the residual charge after overwriting
5. **DRAM PUF (rowhammer disturbance)** — bit flips in neighbouring rows from repeated access
6. **DRAM PUF (reduced read/write latency)** — incomplete operations produce cell-dependent values
7. **Flash PUF (program disturbance)** — bit disturbances in unaccessed cells when neighbours are written

All seven satisfy the PUF trifecta: instance-unique, persistent over time, hard to imitate. The "memory-based" qualifier means the primitive lives inside a component the system already has — no extra silicon.

### TPMs

A Trusted Platform Module is a dedicated, tamper-resistant microcontroller that:

- Stores cryptographic keys in hardware
- Performs signing, encryption, decryption, key generation in isolation from the main CPU
- Implements a platform integrity measurement (PCRs, measured boot)
- Communicates with the main CPU over a serial bus (I²C, SPI, LPC)

**Version 2.0** (the current standard) is the version to know. TPM 2.0 supports multiple algorithms (RSA, ECC, SHA-256, HMAC) and is what Windows 11 requires on every new PC.

**Cost**: dedicated hardware means more money, board area, and power. This is why TPMs are found in gateways, high-end IoT, and laptops, but rarely in coin-cell-powered sensors.

### ASCON — the NIST lightweight crypto winner

Selected by NIST in February 2023 from a finalist pool announced in 2021. Properties (from the lecture):

- Authenticated encryption + hashing with one lightweight permutation
- Provably secure mode with keyed finalisation
- Software and hardware implementable
- Small state, simple permutation — designed for constrained devices
- **Key size = tag size = security level**: 128 bits recommended
- Minimal overhead: ciphertext length = plaintext length
- Single-pass, online (encrypt/decrypt on the fly), nonce-based, inverse-free
- Timing resistance: no table lookups, no integer additions
- Side-channel resistance: S-box optimised for masking

This is the algorithm to know for IoT exams — the same professor's research group (Passau) has published on ASCON.

## Key Properties / Complexity

### Cryptographic fundamentals table (memorise this)

| Security service | Cryptographic mechanism |
|---|---|
| Confidentiality | Encryption (symmetric or asymmetric) |
| Integrity | Digital signature OR MAC |
| Authentication | Digital signature OR MAC |
| Non-repudiation | Digital signature (asymmetric only) |

### Why MACs cannot give non-repudiation

A MAC is computed using a key k that **both** the sender and the receiver know. So the receiver could have produced the tag themselves. The sender can therefore plausibly deny having sent the message: "anyone with the key could have produced that tag." A digital signature uses the sender's *private* key, which only the sender holds, so the receiver provably could not have produced it.

### The "lightweight" property of ASCON

ASCON is built around a 320-bit permutation (called the *p-state*) with a 64-bit S-box. It is *one* algorithm family with multiple modes:

- **ASCON-128 / ASCON-128a** — authenticated encryption
- **ASCON-80pq** — post-quantum variant
- **ASCON-Hash / ASCON-Hasha** — hash function
- **ASCON-XOF / ASCON-Xofa** — extendable-output function

Compare to AES: AES-128 has a 128-bit block, requires 10/12/14 rounds depending on key size, and has a larger S-box and state. ASCON's design is intentionally narrower for hardware simplicity.

### When to use what (exam-level guidance)

- **Symmetric encryption** (AES-128-GCM): bulk data, in-session, both sides share a key negotiated earlier
- **Asymmetric encryption** (RSA, ECIES): rare in practice; mostly used to encrypt a *symmetric key* for hybrid schemes
- **MAC** (HMAC-SHA256, CMAC): when both sides are trusted and you only need integrity + authentication
- **Digital signature** (ECDSA, Ed25519, RSA-PSS): firmware signing, certificate signing, anywhere non-repudiation matters
- **Hash** (SHA-256, SHA-3): data fingerprinting, password storage (with salt + slow KDF), Merkle trees
- **TRNG** (memory-based, ring-oscillator): key generation, nonces
- **PRNG** (DRBG, ChaCha20-based): everything else

## Worked Example

### End-to-end signed firmware update (combines L3 + L5 + L6 concepts)

```
Manufacturer:                   Device:
  privKey = KeyGen()              store pubKey (in TPM, in cert)
  digest = SHA-256(firmware)      
  sig = ECDSA-Sign(privKey, digest)
  send (firmware, sig)  ─────►   digest' = SHA-256(firmware)
                                   ok = ECDSA-Verify(pubKey, digest', sig)
                                   if ok: install firmware
                                   if not: reject
```

This binds three cryptographic primitives (hashing for efficiency, asymmetric crypto for the signature, a TPM to hold the device's trust anchor) into a single security guarantee. An attacker who modifies the firmware in transit cannot produce a valid signature.

### ASCON-128 authenticated encryption

```
key  = 128 bits
nonce = 128 bits
associated data = ad (e.g., packet header, authenticated but not encrypted)
plaintext = pt
→ ASCON-128(key, nonce, ad, pt) → (ciphertext, tag)
→ ciphertext length == plaintext length, tag = 128 bits
```

The receiver has the same key and nonce, recomputes the tag over the ciphertext + AD, and accepts the message only if the recomputed tag matches. Any single bit flip in the ciphertext, key, nonce, or AD invalidates the tag → integrity + authentication in one primitive.

### Von Neumann entropy extraction (TRNG post-processing)

```
pairs of bits (b0, b1) from biased TRNG:
  if b0 == b1: discard pair
  if b0 == 0 and b1 == 1: output 0
  if b0 == 1 and b1 == 0: output 1
```

This produces a uniform random bit stream regardless of the TRNG's bias, at the cost of throwing away on average half the input bits. It is the simplest debiasing method.

## Common Pitfalls

- **"MAC = digital signature"**: false. A MAC is a symmetric primitive; only a digital signature (asymmetric) gives non-repudiation.
- **Using a hash for "encryption"**: hashing is one-way. You cannot recover the message from a hash. Encryption is reversible (with the key).
- **PRNG used for key generation**: deterministic algorithms seeded with low entropy produce guessable keys. Use a TRNG for keys; PRNGs are fine for non-secret randomness.
- **"AES is unbreakable"**: AES-128 is secure against classical brute force, but vulnerable to future quantum algorithms (Grover's algorithm halves the effective key length → AES-256 preferred for post-quantum). Same for RSA (Shor's algorithm breaks it entirely).
- **TPM solves everything**: a TPM protects the keys it stores, but it cannot prevent an attacker who has physical access from reflashing the firmware. TPMs are part of a layered defence, not a silver bullet.
- **TRNGs are uniformly random**: false — they are *unpredictable* but typically *biased*. Always post-process.
- **Reusing a nonce in ASCON / AES-GCM**: catastrophic. A reused nonce with the same key in many AEAD constructions leaks the plaintext or the authentication key. This is the most common real-world cryptographic bug.
- **Confusing key sizes**: RSA-2048 is approximately as strong as ECC-224, not ECC-256. ECC key sizes are smaller because of the underlying math (discrete log on elliptic curves is harder than integer factoring per bit).
- **Forgetting that PUFs need helper data**: PUF responses are noisy. A fuzzy extractor (helper data algorithm) is required to derive a stable key. Without it, the same challenge will give slightly different responses on different reads.

## Connections
- [[iot-lecture-1]] — IoT definitions, the inherent diversity that makes security hard
- [[iot-lecture-2]] — IoT application scenarios, the vulnerability-attack-countermeasure cycle
- [[iot-lecture-3]] — CIA triad, attack types, SDLC; this lecture adds the cryptographic toolbox that realises CIA
- [[iot-lecture-4]] — DevOps, secure design goals, operational security life cycle; crypto primitives slot into "design for confidentiality and integrity"
- [[iot-lecture-5]] — attack surface analysis, the same hardware primitives (PUFs, TPMs) appear here as defences
- [[information-assurance]] — CIA + extensions; this lecture names the *cryptographic* mechanisms behind each
- [[cia-triad]] — confidentiality, integrity, availability
- [[authentication]] — one of the four cryptographic services
- [[non-repudiation]] — only achievable with asymmetric signatures
- [[resilience-iot]] — design for resilience; cryptography is a building block
- [[digital-signatures]] — exists already; the algorithmic and use-case detail
- [[physical-unclonable-functions]] — hardware security primitive; new subtypes introduced in L6
- [[trusted-platform-module]] — TPM 2.0; cost-benefit for IoT
- [[random-number-generator|TRNGs]] — the entropy source for cryptographic key generation
- [[lightweight-cryptography]] — NIST process, ASCON selection
- [[ascon]] — the algorithm; features, modes, post-quantum variant
- [[ota-updates]] — signature verification is the gatekeeper for firmware updates
- [[firmware-security]] — signed firmware, anti-rollback
- [[secure-boot-chain]] — TPM-measured boot
- [[nist-iot-cybersecurity]] — NIST IR 8114 context, the lightweight-cryptography programme
- [[key-management-lifecycle]] — the operational side of using these primitives
- [[iot-secure-design]] — secure design goal: "Apply cryptography to secure data at rest and in motion"
- [[mqtt-security]] — MQTT uses TLS (AES, HMAC, ECDHE) for transport security
- [[zigbee-security-model]] — Zigbee uses AES-128-CCM* (CCM mode with MIC) for link-layer security
- [[ble-security]] — BLE uses AES-CCM for link-layer encryption and authentication

## Open Questions
- Will ASCON-80pq hold up against cryptanalytic advances? (Selected in 2023, so it has recent scrutiny — but post-quantum security analysis is ongoing.)
- The lecture claims PUF responses are "robust" and "persistent over time" — is that true across the full operating temperature range, or only within the lab-tested range?
- For an IoT device with no TPM, can a memory-based PUF + secure boot substitute? (Most papers say yes; the practical engineering question is the helper data scheme.)
- Does the exam care about specific NIST publication numbers (FIPS 197 for AES, FIPS 186-4 for DSA, SP 800-90A for DRBGs) or only the algorithm names?
