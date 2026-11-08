---
title: "Lightweight Cryptography"
tags: [concept, iot-security, cryptography, lightweight, semester-1, course-iot-security]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[symmetric-encryption]]", "[[ascon]]", "[[iot-lecture-6]]"]
---

## One-line Summary
Lightweight cryptography is the design space of cryptographic primitives that fit on the most resource-constrained IoT devices (sub-2000 GE hardware, < 1 KB code, low energy per operation) — the NIST standardisation process (2015–2023) selected ASCON as the winner, but the broader family includes PRESENT, GIFT, SIMON, SPECK, ChaCha20, and many others; lightweight crypto is a *requirement* for IoT, not an optimisation.

## Core Intuition
The lecture quotes NIST IR 8114 directly:

> "There are several emerging areas in which highly constrained devices are interconnected, working in concert to accomplish some task. Examples of these areas include: automotive systems, sensor networks, healthcare, distributed control systems, the Internet of Things (IoT), cyber-physical systems, and the smart grid. Security and privacy can be very important in all of these areas. Because the majority of modern cryptographic algorithms were designed for desktop/server environments, many of these algorithms cannot be implemented in the constrained devices used by these applications. When current NIST-approved algorithms can be engineered to fit into the limited resources of constrained environments, their performance may not be acceptable. For these reasons, NIST started a lightweight cryptography project to investigate the issues and then develop a strategy for the standardization of lightweight cryptographic algorithms."

This is the official statement of the problem. The standard answer is **ASCON**, but the *category* of lightweight crypto is broader and worth understanding as a design space.

**The constraints** in IoT (from the lecture and standard knowledge):
- **Code size**: < 2 KB ROM for the algorithm
- **RAM**: < 1 KB for state
- **Hardware area**: < 2000 GE (gate equivalents) for ASIC implementation
- **Energy**: < 100 µJ per authenticated encryption operation
- **Latency**: variable, but should be sub-millisecond on the target device
- **Throughput**: variable, but often < 1 MB/s on the smallest devices
- **Side-channel resistance**: increasingly required for security

**Why AES, SHA-256, RSA, ECDSA don't fit**:
- AES-128 in software: ~1 KB code, ~200 bytes state, ~50-200 cycles/byte on Cortex-M4 — fits on most modern MCUs, but struggles on 8-bit AVR
- SHA-256: similar
- RSA-2048: ~50-100 ms per signature on Cortex-M4, requires large key storage
- ECDSA-P256: ~50-100 ms per signature, smaller keys (32 bytes), better fit
- All of these have hardware acceleration on modern 32-bit MCUs — but the smallest IoT devices are 8-bit AVRs with no hardware crypto

**The lightweight crypto response**:
- Symmetric ciphers: PRESENT, GIFT, SIMON, SPECK, SKINNY, ASCON
- Hash functions: PHOTON, SPONGENT, ASCON-Hash
- AEAD: ASCON (the winner)
- MACs: Chaskey, SipHash (lightweight MACs)
- Public-key: mostly ECC variants (Ed25519 is small), but no post-quantum public-key crypto fits yet

The trade-off: lightweight algorithms have *less security margin* than AES-256/SHA-512. They are designed to be secure against known attacks but with smaller constants. For most IoT, this is the right trade-off — the device has no other choice.

## Formal Definition / Statement

**NIST lightweight cryptography standardisation process:**

| Year | Event |
|---|---|
| 2015 | NIST announces lightweight crypto project |
| 2017 | NIST IR 8114 published: "Report on Lightweight Cryptography" |
| 2018-2019 | 57 initial submissions |
| 2019 | 56 candidates accepted into round 1 (one withdrawn) |
| 2019 | 32 candidates advance to round 2 |
| 2021 | 10 finalists announced |
| 2021 | 5 finalists selected: ASCON, Elephant, GIFT-COFB, Grain-128AEAD, ISAP, Photon-Beetle, Romulus, Sparkle, Xoodyak, (10 total) |
| February 2023 | ASCON selected as winner |
| 2024-2025 | NIST SP 800-232 (ASCON standard) finalised |

**ASCON family (the winner):**
- ASCON-128 (AEAD, 128-bit key)
- ASCON-128a (AEAD, 128-bit key, faster on 64-bit)
- ASCON-80pq (AEAD, 160-bit key, post-quantum)
- ASCON-Hash, ASCON-Hasha
- ASCON-XOF, ASCON-Xofa

**Other notable lightweight algorithms:**

| Algorithm | Type | Key/State/Output | Notes |
|---|---|---|---|
| PRESENT | Block cipher | 80/128-bit key, 64-bit block | ISO/IEC 29192-2, used in RFID |
| GIFT | Block cipher | 128-bit key, 64/128-bit block | Replaces PRESENT in many designs |
| SIMON/SPECK | Block cipher | Various | NSA designs, controversial origin |
| SKINNY | Block cipher | Various | NIST round 2 candidate |
| ChaCha20 | Stream cipher | 256-bit key, 96-bit nonce | Used in TLS 1.3, WireGuard |
| Poly1305 | MAC | 256-bit key, 128-bit tag | Often paired with ChaCha20 |
| Chaskey | MAC | 128-bit key, 128-bit tag | Lightweight ARX MAC |
| SipHash | MAC | 128-bit key, 64-bit tag | Used in hash tables (DoS resistance) |
| PHOTON | Hash | Various | Lightweight hash, sponge-based |
| SPONGENT | Hash | Various | Lightweight hash, sponge-based |

**Design metrics:**
- **GE (Gate Equivalents)**: 2-input NAND gate as a unit. Lightweight = < 2000 GE.
- **Code size**: bytes of ROM. Lightweight = < 2 KB.
- **RAM**: bytes. Lightweight = < 100 bytes.
- **Energy**: µJ per operation. Measured on a specific target (e.g., 0.13 µm CMOS).
- **Throughput**: bits/second at a given clock frequency.
- **Latency**: clock cycles to first ciphertext byte.

## Key Properties / Complexity
- **Hardware area**: < 2000 GE typical target (PRESENT is ~1570 GE, ASCON is ~2.5 kGE)
- **Code size**: < 2 KB typical target
- **RAM**: < 100 bytes typical target
- **Energy**: < 100 µJ per AEAD operation typical target
- **Security**: 128-bit classical security is the typical goal
- **Side-channel resistance**: many lightweight designs (ASCON, GIFT) are designed for masking efficiency
- **Throughput**: highly variable — 10 kbps for the smallest devices, 100 Mbps for larger
- **Trade-off**: lightweight algorithms have smaller security margin than AES-256. The compactness comes from narrower primitives, fewer rounds, smaller state — all of which reduce the gap between attack complexity and brute-force complexity.

## Worked Example

**PRESENT (the classic lightweight block cipher, ISO/IEC 29192-2):**
- 80-bit or 128-bit key
- 64-bit block
- 31 rounds
- Each round: addRoundKey → S-box (4-bit) → permutation → addRoundKey
- Hardware: ~1570 GE (smaller than AES)
- Code: ~1 KB
- Use case: RFID tags, smart cards, sensor nodes

**ASCON-128 on a Cortex-M4 (no hardware acceleration):**
- ~50-100 cycles/byte
- ~10-20 µJ per byte on a typical low-power MCU
- RAM: 40 bytes
- Code: ~500 bytes (C) or ~200 bytes (assembly)
- Throughput at 10 MHz: ~100-200 kbps

**ChaCha20-Poly1305 on a Cortex-M4:**
- ~100-200 cycles/byte
- ~30-50 µJ per byte
- RAM: ~100 bytes
- Code: ~500 bytes
- Throughput at 10 MHz: ~50-100 kbps

ASCON beats ChaCha20 on most metrics for the smallest devices.

## Common Pitfalls
- **"Lightweight = less secure"**: the goal is to be as secure as AES for the *use case*, not to be universally stronger. PRESENT-80 has 80-bit security, which is sufficient for RFID but less than AES-128.
- **Ignoring side channels**: many lightweight algorithms are designed for *constant-time* implementation. A naive C port can leak keys via power analysis.
- **Comparing GE counts without context**: 1570 GE for PRESENT is impressive, but if your ASIC has 1 MGE available, the difference between 2 kGE and 10 kGE doesn't matter.
- **Over-rotation of algorithms**: don't change algorithms on every product generation. Migrate to ASCON and stay there for a decade.
- **Forgetting the energy budget**: on a coin-cell-powered sensor, every microjoule matters. ASCON's energy advantage over AES-128 is significant.

## Connections
- [[ascon]] — the NIST winner; the canonical IoT crypto choice
- [[symmetric-encryption]] — the broader family
- [[asymmetric-encryption]] — lightweight ECC (Ed25519, X25519) is the public-key choice for IoT
- [[hashing]] — ASCON-Hash replaces SHA-256 in lightweight settings
- [[message-authentication-code]] — Chaskey, SipHash are lightweight MACs
- [[nist-iot-cybersecurity]] — NIST's role in standardising lightweight crypto
- [[iot-lecture-6]] — source lecture (covers NIST IR 8114 quote and ASCON selection)
- [[iot-lecture-1]] — IoT diversity is what makes lightweight crypto necessary
- [[paper-zhou-iot-2-0|IoT 2.0]] — IoT 2.0 needs lightweight crypto at scale
- [[physical-unclonable-functions]] — combine with lightweight crypto for hardware-rooted trust
- [[ota-updates]] — lightweight crypto for firmware updates on constrained devices
- [[paper-iot-lightweight-hardware-architecture]] — Mexis et al. 2021 paper, the architecture for lightweight hardware security
- [[paper-zhou-iot-2-0]] — Zhou et al. 2021 survey, discusses lightweight crypto as IoT 2.0 enabler

## Open Questions
- For the smallest IoT devices (8-bit, < 16 KB flash), is ASCON the right choice or is a simpler algorithm like PRESENT still preferred?
- How will post-quantum crypto migrate to the lightweight setting? (Kyber is too heavy for most IoT; PQ candidates for lightweight IoT are still being researched.)
- The lecture's quote is from NIST IR 8114 (2017). Will NIST publish an updated report in the post-ASCON era?
