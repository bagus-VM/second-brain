---
title: "Random Number Generation (TRNG, PRNG, DRBG)"
tags: [concept, iot-security, cryptography, semester-1, course-iot-security]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[information-assurance]]", "[[key-management-lifecycle]]"]
---

## One-line Summary
Cryptographic keys, nonces, and IVs must come from unpredictable, high-entropy sources — True Random Number Generators (TRNGs) sample physical processes (memory start-up, thermal noise, photoelectric effect, DRAM decay) and are unpredictable but biased, while Pseudo-Random Number Generators (PRNGs) are deterministic algorithms seeded by entropy; the lecture covers the taxonomy (DRBGs vs NDRNGs, TRNGs vs PRNGs) and post-processing (von Neumann correction, entropy distillation) needed to turn biased TRNG output into uniform random bits.

## Core Intuition
Every cryptographic primitive eventually needs randomness: AES keys, RSA primes, ECDSA nonces, TLS nonces, session keys, IVs, salts. If the randomness is weak, every cryptographic guarantee above it collapses. This is why the NSA reportedly subverted the Dual_EC_DRBG — they didn't need to break the math, they just needed the random numbers to be predictable.

The taxonomy in the lecture distinguishes:

- **DRBG** (Deterministic Random-Bit Generator) = any RNG whose output is determined by its initial state and inputs. **All PRNGs are DRBGs.**
- **NDRNG** (Non-Deterministic Random Number Generator) = RNG that uses a non-deterministic entropy source (physical process). **TRNGs are NDRNGs.**
- **PRNG** (Pseudo-Random Number Generator) = a DRBG whose output "looks random" — passes statistical tests. The output is fully determined by the seed; same seed → same output.
- **TRNG** (True Random Number Generator) = a NDRNG that uses a physical process. The output is fundamentally unpredictable (in principle), but is usually **biased** — not uniformly random.

**The key insight for IoT**: the lecture emphasises that **memory-based TRNGs are practical and cheap**. The start-up values of SRAM, the decay characteristics of DRAM, the rowhammer disturbance, the read/write latency of cells — all of these are physical properties of memory that already exists in the system. No extra silicon. The TRNG is "free" in the sense that the memory is already on the chip.

The catch: these physical TRNGs are *unpredictable* but *biased*. You need **post-processing** to extract uniform random bits:

- **Von Neumann correction**: take pairs of bits, discard 00 and 11, map 01 to 0 and 10 to 1. Output is uniform regardless of input bias. Cost: throws away on average half the bits.
- **Parity-based**: XOR consecutive bits. Works under weak bias assumptions.
- **Hash-based**: pass through a cryptographic hash (SHA-256), which compresses the entropy and outputs uniform bits. Used in modern TRNG designs.
- **Cryptographic extractors** (e.g., based on the leftover hash lemma): provably extract min-entropy into uniform bits.

This is the **entropy distillation** step, and it is where the "random" in "random number" actually happens.

## Formal Definition / Statement

**Taxonomy (from the lecture):**

| Type | Source | Determinism | Example |
|---|---|---|---|
| DRBG | Algorithm + state | Deterministic | NIST SP 800-90A (Hash_DRBG, HMAC_DRBG, CTR_DRBG) |
| NDRNG | Physical process | Non-deterministic | Thermal noise, photoelectric, memory start-up |
| PRNG | Algorithm + seed | Deterministic | Linear congruential, Mersenne Twister, ChaCha20-based CSPRNG |
| TRNG | Physical process | Non-deterministic | Same as NDRNG |

**Properties of a secure DRBG:**
- **Backward secrecy**: compromise of current state does not reveal past outputs
- **Forward secrecy**: compromise of current state does not reveal future outputs (only true if continuously reseeded)
- **Resilience to compromise**: ability to recover from state compromise after reseeding

NIST SP 800-90A specifies three DRBGs:
- **Hash_DRBG**: hash-based
- **HMAC_DRBG**: HMAC-based, the recommended one
- **CTR_DRBG**: block-cipher-based (AES)

**Memory-based TRNGs (the practical IoT list from the lecture):**

| Construction | Source of randomness |
|---|---|
| SRAM start-up values | Power-up cell bias |
| DRAM start-up values | Power-up cell bias (same as SRAM) |
| DRAM decay | Time-dependent charge loss after power-off |
| DRAM data remanence | Residual charge after overwriting |
| DRAM rowhammer | Disturbance in adjacent cells under repeated access |
| DRAM read/write latency | Cell-dependent response to short-latency operations |
| Flash program disturbance | Bit errors in unaccessed cells during neighbour writes |

All of these satisfy: unique per chip, persistent, hard to imitate. They are all "free" — they exploit hardware that already exists on the IoT device.

**TRNG quality metrics:**
- **Entropy per bit**: how much information each bit carries (1.0 for uniform random, 0 for deterministic)
- **Min-entropy**: H_∞(X) = -log₂(max Pr[X = x]) — worst-case unpredictability
- **NIST SP 800-90B**: statistical test suite for entropy sources
- **Dieharder, NIST STS**: test suites for RNG output

**Debiasing methods:**
- **Von Neumann (1936)**: simplest, throws away half the bits
- **Peres**: extends Von Neumann, ~3× more efficient
- **Hash-based (SHA-256)**: most modern, ~80% efficient
- **Linear-feedback shift register (LFSR) XOR trees**: hardware-friendly

## Key Properties / Complexity
- **TRNGs are unpredictable but biased**: post-processing is mandatory
- **PRNGs are deterministic**: same seed → same output. NEVER use a PRNG for cryptographic key generation.
- **DRBGs are the right primitive for general use**: NIST SP 800-90A specifies them
- **Memory-based TRNGs are the IoT default**: free, no extra silicon
- **Entropy distillation is non-negotiable**: NIST SP 800-90C requires it
- **Min-entropy target**: 256 bits of min-entropy for a 256-bit AES key
- **The lecture's "memory as TRNG" insight**: by far the most important practical lesson for IoT — you don't need dedicated hardware for randomness

## Worked Example

**NIST SP 800-90A HMAC_DRBG (used in many IoT protocols):**
```
State: (Key K, Value V)
Instantiate(entropy_input, nonce, personalization_string):
  K = 0x00 * outlen
  V = 0x01 * outlen
  K, V = HMAC_DRBG_Update(entropy_input || nonce || personalization_string, K, V)
  return (K, V)

Generate(requested_bits):
  temp = empty
  while len(temp) < requested_bits:
    V = HMAC(K, V)
    temp = temp || V
  return (leftmost requested_bits of temp, new state)
```

This is *deterministic* — same initial (K, V) and same inputs always produce the same output. The unpredictability comes entirely from the entropy input at instantiation. Reseed periodically to maintain forward secrecy.

**Von Neumann debiasing (Python):**
```python
def von_neumann(bits):
    output = []
    for i in range(0, len(bits) - 1, 2):
        b0, b1 = bits[i], bits[i+1]
        if b0 == 0 and b1 == 1:
            output.append(0)
        elif b0 == 1 and b1 == 0:
            output.append(1)
        # else discard pair
    return output
```

If the input is biased Pr[0] = p, Pr[1] = 1-p, then Pr[output=0] = Pr[01] / (Pr[01] + Pr[10]) = p(1-p) / (p(1-p) + (1-p)p) = 1/2. The output is exactly uniform regardless of p.

**SRAM PUF as TRNG (the lecture's most important example):**
```
1. Power off the SRAM
2. Power on
3. Each cell settles to either 0 or 1 based on manufacturing variation
4. The 0/1 pattern is the entropy source
5. Post-process via von Neumann or SHA-256 to get uniform bits
```

This is the cheapest TRNG possible: every microcontroller has SRAM, and the power-up state is naturally random.

## Common Pitfalls
- **PRNG used for key generation**: catastrophic. The seed is the only entropy, and the seed is often predictable (time, PID, low-entropy noise).
- **TRNG output used without debiasing**: biased key material is partially predictable. An adversary who knows the bias can reduce the effective key size.
- **Insufficient entropy at boot**: Linux kernel famously had the "low entropy at boot" problem. Modern systems use `getrandom()` or `/dev/urandom` after seeding.
- **Same seed across devices**: factory-default seeds (zero, time) are predictable. Use a per-device seed from a TRNG.
- **Mixing TRNG with PRNG and assuming the output is strong**: NIST requires the entropy source to be sampled at full rate. Mixing dilutes entropy.
- **Math.random() (JavaScript) and rand() (C)** are NOT cryptographic. Use crypto.getRandomValues() or arc4random_uniform().

## Connections
- [[information-assurance]] — entropy underpins every cryptographic service
- [[key-management-lifecycle]] — keys are random; randomness quality is key quality
- [[physical-unclonable-functions]] — PUFs are sometimes used as TRNGs (the start-up value is a random bit)
- [[trusted-platform-module]] — TPMs include a hardware TRNG
- [[ascon]] — ASCON's security depends on a strong nonce; a weak RNG breaks ASCON
- [[lightweight-cryptography]] — lightweight protocols need lightweight entropy sources
- [[symmetric-encryption]] — AES keys come from the RNG
- [[asymmetric-encryption]] — RSA primes, ECDSA nonces come from the RNG
- [[digital-signatures]] — ECDSA nonces MUST be high-entropy (PS3 bug)
- [[hashing]] — salts come from the RNG
- [[iot-lecture-6]] — source lecture
- [[iot-lecture-5]] — covered PUFs and TPMs as hardware primitives

## Open Questions
- The lecture lists seven memory-based TRNG constructions. Are all seven equally practical, or is one dominant in commercial IoT?
- How do you certify the entropy of a TRNG? (NIST SP 800-90B process, statistical tests, modelling the physical source.)
- For an IoT device with no dedicated hardware TRNG, can a memory-based PUF (PUFMem) be certified for cryptographic use?
