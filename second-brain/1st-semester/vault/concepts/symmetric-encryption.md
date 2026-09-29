---
title: "Symmetric Encryption"
tags: [concept, iot-security, cryptography, semester-1, course-iot-security]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[information-assurance]]", "[[key-management-lifecycle]]"]
---

## One-line Summary
Symmetric encryption uses a single shared secret key to both encrypt and decrypt data — it is fast (1000× faster than asymmetric) and is the workhorse for bulk data protection in IoT, with AES as the dominant algorithm and lightweight variants (ASCON, ChaCha20) for constrained devices.

## Core Intuition
Two parties (Alice and Bob) want to communicate over an insecure channel. They share a secret key k out-of-band. Alice encrypts her plaintext m with k: c = E(k, m). The ciphertext c travels over the insecure channel. Bob decrypts: m = D(k, c). An eavesdropper sees c but cannot recover m without k.

The single shared key is both the strength and the weakness. **Strength**: symmetric algorithms are fast — AES-128 hits 10+ GB/s in hardware, and even software AES on a microcontroller can do tens of MB/s. **Weakness**: every pair of communicating parties needs its own key, so for n parties you need n(n-1)/2 keys. Distributing those keys securely is the *key management* problem, and it is why asymmetric crypto exists.

In IoT, symmetric encryption is used for:
- Bulk data protection (sensor readings, firmware images at rest)
- Link-layer encryption (Zigbee uses AES-128-CCM*, BLE uses AES-CCM, LoRaWAN uses AES-128)
- TLS record-layer encryption (AES-GCM, ChaCha20-Poly1305)
- Authenticated encryption (combining encryption + MAC in one primitive)

The two main families are **block ciphers** (AES, present, Ascon) and **stream ciphers** (ChaCha20, Grain). Block ciphers need a mode of operation (CBC, CTR, GCM) to encrypt more than one block at a time; the mode is where authenticated encryption lives (GCM, CCM, OCB, Poly1305).

## Formal Definition / Statement

A symmetric encryption scheme is a triple of algorithms:
- **KeyGen**(1^λ) → k (where λ is the security parameter)
- **Enc**(k, m) → c
- **Dec**(k, c) → m  (with Dec(k, Enc(k, m)) = m)

**Security**: IND-CPA (indistinguishability under chosen-plaintext attack) is the standard. The adversary chooses two plaintexts m₀, m₁, the challenger picks b ∈ {0, 1} uniformly and returns c = Enc(k, m_b). The adversary wins if they can guess b with probability significantly better than 1/2.

For authenticated encryption, IND-CCA (indistinguishability under chosen-ciphertext attack) plus INT-CTXT (integrity of ciphertexts) is the goal.

**Common ciphers (from the lecture):**

| Cipher | Type | Block / State | Key sizes | Notes |
|---|---|---|---|---|
| AES (FIPS 197) | Block, SPN | 128-bit block | 128, 192, 256 | Most widely used |
| DES | Block, Feistel | 64-bit block | 56 (effective) | Broken, deprecated |
| 3DES (Triple DES) | Block, Feistel | 64-bit block | 112 or 168 | Legacy, deprecated by NIST in 2023 |
| Blowfish | Block, Feistel | 64-bit block | 32–448 | Old, still in some embedded systems |
| Twofish | Block, SPN | 128-bit block | 128, 192, 256 | AES finalist, less common |
| CAST-128 | Block, Feistel | 64-bit block | 40–128 | Older, used in some PGP implementations |
| Camellia | Block, Feistel+SPN | 128-bit block | 128, 192, 256 | Used in TLS, Japanese standard |
| IDEA | Block, Lai-Massey | 64-bit block | 128 | Old, PGP-era |
| ChaCha20 | Stream, ARX | 512-bit state | 256 | Modern, fast in software |
| ASCON | Sponge, AEAD | 320-bit state | 128 | NIST lightweight crypto winner (2023) |

**Modes of operation (block ciphers):**
- **ECB** (Electronic Codebook) — never use; leaks plaintext patterns
- **CBC** (Cipher Block Chaining) — needs padding, vulnerable to padding oracles
- **CTR** (Counter) — turns block cipher into stream cipher, no padding needed
- **GCM** (Galois/Counter Mode) — CTR + GHASH for authentication; AES-GCM is the modern default
- **CCM** (Counter with CBC-MAC) — used in Zigbee, BLE, IEEE 802.15.4
- **OCB** (Offset Codebook) — patent issues, less common

**Authenticated encryption (AEAD):**
- **AES-GCM** — dominant, fast, parallelisable
- **AES-CCM** — smaller footprint than GCM, slower
- **ChaCha20-Poly1305** — software-friendly, used when AES hardware is unavailable
- **ASCON-128** — lightweight, the future for IoT

## Key Properties / Complexity
- **Speed**: hardware AES ~ 10 GB/s, software AES ~ 100 MB/s on Cortex-M4
- **Key distribution**: requires n(n-1)/2 keys for n parties — key management scales poorly
- **No non-repudiation**: both parties can encrypt, so neither can prove the other produced the ciphertext
- **Authenticated encryption is mandatory** in modern protocols (TLS 1.3, IoT protocols); unauthenticated encryption is a footgun
- **AES-128 is quantum-weakened** (Grover halves the key length to 64 effective bits); use AES-256 for post-quantum
- **Lightweight ciphers** (ASCON, PRESENT, GIFT) target < 2000 GE (gate equivalents) hardware footprint

## Worked Example

**AES-128-CBC encryption of a 16-byte block:**
- Key: 128 bits
- Plaintext block: 128 bits
- Operation: 10 rounds of SubBytes (S-box) → ShiftRows → MixColumns → AddRoundKey
- Output: 128-bit ciphertext

For multi-block messages, CBC chains each block: c_i = E(k, p_i ⊕ c_{i-1}), with c_0 = IV. The IV (initialisation vector) must be unique per key — predictable IVs break CBC catastrophically.

**AES-GCM encryption + authentication:**
- Key: 128 bits
- Nonce: 96 bits (MUST be unique per key)
- Plaintext: any length
- Associated data (AD): authenticated but not encrypted
- Output: ciphertext (same length as plaintext) + 128-bit tag

Receiver recomputes the tag over (key, nonce, AD, ciphertext) and accepts the message only if the tag matches. Any single bit flip invalidates the tag.

## Common Pitfalls
- **Reusing a nonce in AES-GCM or ChaCha20-Poly1305**: catastrophic. A reused nonce with the same key leaks the authentication subkey. This is the most common real-world crypto bug.
- **Using ECB for multi-block data**: leaks patterns. Use CBC with random IV, CTR with unique nonce, or (better) AES-GCM.
- **Confusing key sizes**: AES-128 vs AES-256 — only the round count and key schedule differ. AES-256 has 14 rounds vs 10 for AES-128.
- **DES is not secure**: 56-bit key is brute-forceable in hours on commodity hardware. Migrate everything to AES.
- **3DES is deprecated**: NIST deprecated 3DES for all new applications after 2023. Migrate to AES.
- **MD5 / SHA-1 are not secure for hashing**: collisions are known. Use SHA-256 or SHA-3.
- **Symmetric crypto solves confidentiality, not key distribution**: you still need a secure way to share the symmetric key (typically: asymmetric key exchange, then symmetric for data).

## Connections
- [[information-assurance]] — confidentiality is the service symmetric crypto provides
- [[asymmetric-encryption]] — alternative; solves key distribution but is slow
- [[digital-signatures]] — provides integrity, authentication, non-repudiation
- [[hashing]] — companion primitive, used in HMACs and key derivation
- [[message-authentication-code]] — symmetric equivalent of signatures, but no non-repudiation
- [[key-management-lifecycle]] — the operational challenge of distributing and rotating symmetric keys
- [[ascon]] — NIST lightweight crypto winner
- [[lightweight-cryptography]] — the design space for constrained devices
- [[random-number-generator|TRNGs]] — keys must come from a TRNG, not a PRNG
- [[message-authentication-code|ciphersuite / MAC]] — TLS combines symmetric + asymmetric + hashing in a named bundle
- [[ota-updates]] — firmware images are typically encrypted with AES-GCM or ChaCha20-Poly1305
- [[mqtt-security]] — TLS uses AES-GCM for record encryption
- [[zigbee-security-model]] — AES-128-CCM* at the link layer
- [[ble-security]] — AES-CCM at the link layer
- [[iot-lecture-6]] — source lecture
- [[nist-iot-cybersecurity]] — NIST's role in standardising algorithms

## Open Questions
- Will AES still be the IoT standard in 10 years, or will ASCON displace it? (NIST lightweight crypto standardisation favours ASCON; legacy systems will keep AES for decades.)
- For the smallest IoT devices (8-bit MCUs, no AES hardware), is ChaCha20 a better fit than software AES?
- Does the exam want you to memorise the AES round structure, or just the block/key sizes and that AES is the workhorse?
