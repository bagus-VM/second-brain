---
title: "AES (Advanced Encryption Standard)"
tags: [concept, iot-security, cryptography, semester-1, course-iot-security]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[symmetric-encryption]]"]
---

## One-line Summary
AES is the dominant symmetric block cipher, standardised as FIPS 197 in 2001 after winning the NIST competition; it operates on 128-bit blocks with 128/192/256-bit keys in 10/12/14 rounds of SubBytes-ShiftRows-MixColumns-AddRoundKey, is the workhorse for bulk data encryption in TLS, IoT link layers (Zigbee, BLE, LoRaWAN), and disk encryption, and is the reference against which lightweight alternatives (ASCON) are measured.

## Core Intuition
AES is so widely deployed that "encryption" almost always means AES in practice. The reason is that it is:
- **Fast**: ~10 GB/s in hardware (AES-NI on modern CPUs); 100s of MB/s in software on Cortex-M4
- **Secure**: no known practical attack against full AES-128 after 20+ years of cryptanalysis
- **Simple to implement**: 4 simple operations per round
- **Standardised**: FIPS 197, ISO/IEC 18033-3, mandatory in many US government contexts
- **Hardware-accelerated** on virtually every modern CPU and many MCUs (ESP32, STM32, NRF52 all have AES hardware)

The trade-off: AES is "heavyweight" by IoT standards. On the smallest 8-bit MCUs with no hardware acceleration, AES-128 in C is ~1 KB of code and ~100 cycles/byte — not impossible, but not free. This is why ASCON exists for the smallest devices.

For the lecture, AES is the example cipher for *all* of symmetric encryption. The properties of AES carry over to other ciphers with minor adjustments (block size, key size, round count, S-box).

## Formal Definition / Statement

**AES (FIPS 197, 2001):**
- **Block size**: 128 bits (always)
- **Key sizes**: 128, 192, or 256 bits
- **Rounds**: 10, 12, or 14 (for 128, 192, 256-bit keys respectively)
- **State**: 4×4 matrix of bytes (16 bytes total = 128 bits)
- **S-box**: 8-bit invertible, designed for resistance to linear and differential cryptanalysis
- **Round operations**:
  1. **SubBytes**: apply S-box to each byte
  2. **ShiftRows**: cyclic-shift each row of the state matrix
  3. **MixColumns**: matrix multiplication in GF(2^8) on each column
  4. **AddRoundKey**: XOR state with the round key
- **Key schedule**: expands the master key into Nb×(Nr+1) round keys

**AES-128 round structure:**
- 1 initial AddRoundKey
- 9 rounds of SubBytes → ShiftRows → MixColumns → AddRoundKey
- 1 final round: SubBytes → ShiftRows → AddRoundKey (no MixColumns)

**Modes of operation (block ciphers need them to encrypt more than one block):**
- **ECB** (Electronic Codebook) — never use; leaks plaintext patterns
- **CBC** (Cipher Block Chaining) — needs padding, requires random IV
- **CTR** (Counter) — turns block cipher into stream cipher
- **GCM** (Galois/Counter Mode) — CTR + GHASH for AEAD
- **CCM** (Counter with CBC-MAC) — used in Zigbee, BLE

**AES-128-GCM (the modern default):**
- Encryption: AES-CTR with 96-bit nonce, 32-bit counter
- Authentication: GHASH over (AD, ciphertext) using secret H = AES_K(0^128)
- Output: ciphertext (same length as plaintext) + 128-bit tag

**Security levels (NIST, 2023):**
- AES-128: 128-bit security (acceptable until 2030+)
- AES-192: 192-bit security
- AES-256: 256-bit security (post-quantum hedge — Grover halves to 128 effective bits)

## Key Properties / Complexity
- **Speed**: hardware ~10 GB/s (AES-NI), software ~500 MB/s on x86, ~100-200 cycles/byte on Cortex-M4
- **Code size**: ~1 KB C, smaller in assembly
- **RAM**: 16 bytes state + key schedule
- **Quantum**: AES-128 weakened to 64 effective bits by Grover's algorithm → use AES-256 for post-quantum
- **Side-channel**: vulnerable to power analysis without countermeasures; masked AES implementations exist
- **Hardware support**: AES-NI on x86, ARMv8 Crypto Extensions, dedicated peripherals on most modern MCUs

## Worked Example

**AES-128 encryption of a 16-byte block (simplified):**
```
state = plaintext (16 bytes)
state ⊕= round_key[0]                  # initial AddRoundKey
for round in 1..10:
    state = SubBytes(state)            # byte-wise S-box
    state = ShiftRows(state)           # row-wise cyclic shift
    if round < 10: state = MixColumns(state)  # GF(2^8) matrix mult
    state ⊕= round_key[round]
ciphertext = state
```

**AES-128-CBC encryption of a 256-byte firmware image:**
```
key = 128-bit
iv  = 128-bit random
c_0 = iv
for each 16-byte plaintext block p_i:
    p_i' = p_i ⊕ c_{i-1}              # CBC chain
    c_i = AES_Encrypt(key, p_i')
```

**AES-128-GCM authenticated encryption:**
```
key = 128-bit
nonce = 96-bit (MUST be unique per key)
ad = associated data
pt = plaintext
→ (ct, tag) = AES-GCM(key, nonce, ad, pt)
→ ct length = pt length
→ tag = 128 bits
```

## Common Pitfalls
- **Reusing a nonce in AES-GCM**: catastrophic. A reused nonce with the same key leaks the authentication subkey H = AES_K(0). Real-world bugs: 2017 "Forbidden Attack" on TLS.
- **Using ECB for multi-block data**: leaks plaintext patterns. The famous ECB-penguin image illustrates this. Use CBC with random IV, CTR with unique nonce, or (better) AES-GCM.
- **Predictable IV in CBC**: if IV is predictable and the attacker can submit chosen plaintexts, they can recover the plaintext (BEAST attack, 2011). Use random IV.
- **Padding oracle attack on CBC**: if error messages distinguish padding errors from MAC errors, the attacker can decrypt any ciphertext (Vaudenay's attack, 2002). Use encrypt-then-MAC, or AEAD.
- **Using AES-128 for post-quantum**: weakened by Grover. Use AES-256.
- **Implementing AES from scratch**: never do this. Use a vetted library (OpenSSL, mbedTLS, wolfSSL, libsodium). Side-channel and constant-time issues are hard to get right.

## Connections
- [[symmetric-encryption]] — the workhorse cipher
- [[asymmetric-encryption]] — alternative for key distribution
- [[hashing]] — companion primitive, used in HMAC and key derivation
- [[message-authentication-code]] — AES-CMAC is a MAC built from AES
- [[key-management-lifecycle]] — AES keys must come from a TRNG
- [[random-number-generator]] — AES-GCM nonces must be unique (CSPRNG is fine if you don't reuse)
- [[ascon]] — the NIST lightweight crypto winner, designed for devices too small for AES
- [[lightweight-cryptography]] — the design space for AES alternatives
- [[mqtt-security]] — TLS 1.3 uses AES-GCM for record encryption
- [[zigbee-security-model]] — AES-128-CCM* at the link layer
- [[ble-security]] — AES-CCM at the link layer
- [[ota-updates]] — firmware images are often encrypted with AES-GCM
- [[nist-iot-cybersecurity]] — NIST's role in standardising AES (FIPS 197)
- [[iot-lecture-6]] — source lecture, lists AES as the dominant symmetric cipher
- [[paper-iot-lightweight-hardware-architecture]] — Mexis et al. use AES-128-CBC
- [[paper-iot-mexis-2021-poster]] — same

## Open Questions
- Will AES be replaced by ASCON in IoT over the next decade, or will AES-NI and hardware support keep it dominant?
- For the very smallest devices (sub-cent cost, no MCU), is AES even implementable in software? (PRESENT might be the only option.)
- The 2023 NIST deprecation of 3DES — when will AES-128 be similarly deprecated in favour of AES-256? (Not soon — AES-128 is still considered secure.)
