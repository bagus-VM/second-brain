---
title: "ASCON (NIST Lightweight Crypto Winner)"
tags: [concept, iot-security, cryptography, lightweight, semester-1, course-iot-security]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[symmetric-encryption]]", "[[lightweight-cryptography]]", "[[iot-lecture-6]]"]
---

## One-line Summary
ASCON is the algorithm family selected by NIST in February 2023 as the winner of the lightweight cryptography standardisation process (2015–2023) — a single 320-bit permutation that provides authenticated encryption (ASCON-128), hashing (ASCON-Hash), and extendable-output functions in one small, side-channel-resistant, energy-efficient design suitable for the most resource-constrained IoT devices.

## Core Intuition
Most modern crypto was designed for desktop and server hardware — AES on Intel/AMD, RSA on cryptographic accelerators, SHA-256 in SIMD instructions. When you try to run these on a coin-cell-powered IoT sensor with 32 KB of flash and 4 KB of RAM, you hit walls:

- **Code size**: AES-128 in C is ~1 KB; ChaCha20 is ~500 bytes; ASCON is **< 200 bytes** for the core permutation
- **RAM footprint**: AES needs the entire 16-byte block in RAM; ASCON works on a 40-byte state
- **Energy per operation**: critical for battery-powered devices; ASCON's 5-bit S-box is much cheaper than AES's 8-bit S-box
- **Side-channel resistance**: ASCON is designed to be constant-time and easy to mask

NIST recognised this gap in 2015 and ran a decade-long standardisation process. From a pool of 57 initial submissions, NIST narrowed to 10 round-2 candidates, announced 5 finalists in 2021, and selected **ASCON** in February 2023.

ASCON's design is built around a single **320-bit permutation** (the *p-state* with a 64-bit S-box) that is used in different ways to provide:
- Authenticated encryption with associated data (AEAD): ASCON-128, ASCON-128a
- Hashing: ASCON-Hash, ASCON-Hasha
- Extendable-output functions (XOF): ASCON-XOF, ASCON-Xofa
- Post-quantum variant: ASCON-80pq

The advantage of one permutation doing many jobs: small code, small state, well-understood security analysis. Same hardware serves encryption, hashing, and key derivation.

**The Passau connection**: ASCON was developed by Christoph Dobraunig, Maria Eichlseder, and Florian Mendel at TU Graz (Austria), with contributions from many international collaborators. The University of Passau (where this lecture series is from) is one of the leading IoT security groups in Europe — the lecture's heavy emphasis on ASCON reflects the group's research focus on this algorithm.

## Formal Definition / Statement

**ASCON permutation:**
- State: 320 bits (five 64-bit words)
- Number of rounds: 1, 6, or 12 depending on the mode
- Round structure: add constant → S-box layer → linear diffusion layer
- S-box: 5-bit (cheaper than AES's 8-bit S-box in hardware)

**ASCON-128 (the primary AEAD):**
- **Key**: 128 bits
- **Nonce**: 128 bits (must be unique per key)
- **Associated data** (AD): any length
- **Plaintext**: any length
- **Output**: ciphertext (same length as plaintext) + 128-bit tag
- **Rounds**: 12 (initialisation + finalisation), 6 (associated data + plaintext)

**Initialisation:**
```
state = IV ‖ key ‖ nonce (320 bits)
state = p^a (apply permutation a times, a=12)
```

**Process associated data:**
```
For each AD block:
  state = state ⊕ AD_block ‖ padding
  state = p^b (b=6)
state = state ⊕ (0^320-bit ‖ 1)
```

**Process plaintext (encryption):**
```
For each plaintext block:
  c_i = p_i ⊕ state[0..|p_i|]
  state = (c_i ‖ 0*) ‖ state[|c_i|..]
  state = p^b
```

**Finalisation:**
```
state = state ⊕ (0^320-bit ‖ key)
state = p^a
state = state ⊕ key
tag = state[0..128]
```

**ASCON-Hash:**
- Output: 256-bit digest (or variable with XOF)
- Structure: sponge construction, capacity = 256 bits, rate = 64 bits
- Absorb: XOR message blocks into rate, then apply p
- Squeeze: read rate, apply p, repeat

**ASCON-80pq (post-quantum variant):**
- Same structure as ASCON-128 but with a 160-bit key
- Doubles the key size to resist Grover's quantum search (which halves effective key length)
- Use when quantum adversaries are a concern

## Key Properties / Complexity

| Property | ASCON-128 | AES-128-GCM | ChaCha20-Poly1305 |
|---|---|---|---|
| Key size | 128 | 128 | 256 |
| Nonce size | 128 | 96 | 96 |
| Tag size | 128 | 128 | 128 |
| Ciphertext expansion | 0 (same as plaintext) | 0 | 0 |
| AEAD | Yes | Yes | Yes |
| Software code size | ~200 bytes | ~1 KB | ~500 bytes |
| Hardware area | ~2.5 kGE | ~10 kGE | ~5 kGE |
| Software speed (Cortex-M4) | ~50-100 cycles/byte | ~100-200 cycles/byte | ~100-200 cycles/byte |
| Side-channel resistance | Designed for masking | Needs care | Designed for constant-time |

- **Single permutation, multiple uses**: AEAD, hash, XOF all share the p-state
- **No table lookups**: immune to cache-timing attacks
- **No integer additions**: immune to certain side channels
- **5-bit S-box optimised for masking**: efficient side-channel countermeasures
- **Online**: encrypt/decrypt as the data streams in, no pre-computation
- **Inverse-free**: no need for a separate decryption permutation
- **Single-pass**: one pass over the data, not two (CBC-MAC + encrypt style)

## Worked Example

**ASCON-128 authenticated encryption of a 32-byte sensor reading:**
```
key = 128-bit device secret (e.g., derived from PUF)
nonce = 128-bit counter (monotonically increasing)
ad = "sensor_id=0x42" (10 bytes, authenticated but not encrypted)
plaintext = 32 bytes of temperature readings

(ciphertext, tag) = ASCON-128(key, nonce, ad, plaintext)
send: (nonce, ad, ciphertext, tag)
```

Receiver: re-derives the same key, increments nonce, recomputes (ciphertext', tag') and accepts if tag' == tag.

**ASCON-Hash for firmware fingerprinting:**
```
firmware_image = 256 KB binary
digest = ASCON-Hash(firmware_image)  # 256-bit output
sign(digest) with ECDSA  # 64-byte signature
```

ASCON-Hash can be used as a drop-in for SHA-256, with smaller code and better side-channel resistance on small MCUs.

## Common Pitfalls
- **Reusing a nonce in ASCON**: catastrophic, same as AES-GCM. Monotonically increasing counters are the standard mitigation.
- **Assuming ASCON is post-quantum**: ASCON-128 is *symmetric*, so Grover's algorithm halves the effective key length. ASCON-80pq exists for this reason, but ASCON-128 is not safe against a CRQC.
- **Confusing ASCON-128 with AES-128 in security level**: both are 128-bit security against classical attacks, but AES-128 is hardware-accelerated on most modern CPUs; ASCON-128 is the choice for *constrained* devices.
- **Treating ASCON as experimental**: it's NIST-standardised (SP 800-232 expected) and ready for production deployment.
- **Side-channel implementation without masking**: ASCON's 5-bit S-box is masking-friendly, but the implementation must be carefully written to maintain that property. A naive implementation can leak via power analysis.

## Connections
- [[iot-lecture-6]] — source lecture (full slide on ASCON features)
- [[lightweight-cryptography]] — the NIST process that produced ASCON
- [[symmetric-encryption]] — ASCON is symmetric; provides confidentiality + authentication
- [[message-authentication-code]] — ASCON-128 is an AEAD (authenticated encryption with associated data), combining encryption and MAC
- [[hashing]] — ASCON-Hash is a drop-in SHA-256 alternative
- [[nist-iot-cybersecurity]] — NIST's role in standardising ASCON
- [[random-number-generator|TRNGs]] — ASCON needs high-entropy nonces
- [[key-management-lifecycle]] — ASCON-128 keys are typically derived via HKDF from a master secret
- [[ota-updates]] — firmware could be encrypted with ASCON-128 instead of AES-GCM
- [[mqtt-security]] — TLS 1.3 with ASCON cipher suites is being proposed for IoT
- [[paper-iot-lightweight-hardware-architecture]] — Mexis et al. 2021 paper, in the same research family
- [[paper-zhou-iot-2-0]] — Zhou et al. 2021 IoT 2.0 survey, mentions lightweight crypto as an IoT 2.0 enabler
- [[physical-unclonable-functions]] — PUFs can derive ASCON keys without storing them

## Open Questions
- Will ASCON-80pq see adoption, or will post-quantum migration go directly to Kyber + Dilithium (the NIST PQC winners)?
- The lecture lists 12 specific features of ASCON. Does the exam expect the full list, or just the headline ones (AEAD + hash, lightweight, side-channel resistance)?
- For an 8-bit AVR microcontroller with 2 KB of flash, can ASCON-128 fit? (Probably not as C; needs assembly tuning. AES-128 in hardware-accelerated form might still be preferred.)
