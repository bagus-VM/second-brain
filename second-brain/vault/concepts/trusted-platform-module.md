---
title: "Trusted Platform Module (TPM)"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[security-by-design]]"]
---

## One-line Summary
A Trusted Platform Module (TPM) is a dedicated security hardware chip (or firmware implementation) providing cryptographic operations, secure key storage, and platform integrity measurement for IoT devices.

## Core Intuition
Think of a TPM as a tiny, tamper-resistant vault inside your device that handles all the sensitive cryptographic operations. Keys never leave the TPM, so even if the main system is compromised, the attacker can't extract the secrets.

## Formal Definition / Statement
**Trusted Platform Module (TPM):** Dedicated security hardware for cryptographic operations and secure key storage. Provides:
- **Cryptographic key generation and storage** — Keys generated and stored inside the TPM
- **Platform integrity measurement** — Boot process is measured and attested
- **Random number generation** — Hardware TRNG for cryptographic use
- **Sealed storage** — Data encrypted to specific platform state
- **Remote attestation** — Prove to a remote party that the platform is in a known good state

## Key Properties / Complexity

### Capabilities
- RSA, ECC, SHA cryptographic operations
- Secure key hierarchy (storage root key → child keys)
- PCR (Platform Configuration Registers) for integrity measurement
- Endorsement key for device identity
- Anti-hammering (locks out after too many failed attempts)

### TPM in IoT
- Suitable for higher-end IoT devices (gateways, industrial controllers)
- May be too expensive/power-hungry for very constrained sensors
- Alternative: firmware TPM (fTPM) — software implementation with hardware root of trust
- Complementary with [[physical-unclonable-functions|PUFs]] — PUFs for identity, TPMs for crypto operations

### Limitations
- Adds cost ($1-5 per chip)
- Adds power consumption
- Requires software integration (TSS — TPM Software Stack)
- TPM 1.2 had some known vulnerabilities; TPM 2.0 is current standard

## Worked Example
**TPM-based Secure Boot in IoT Gateway:**
1. On power-on, TPM measures the boot firmware hash into PCR[0]
2. Each subsequent boot stage is measured into PCRs
3. TPM compares PCR values against known-good values
4. If values match → boot continues
5. If values don't match → boot halts (firmware tampered)
6. Remote server can verify boot integrity via remote attestation

## Common Pitfalls
- Assuming TPM makes a system "secure" — it's a building block, not a complete solution
- Not protecting the TPM-to-application interface
- Using TPM 1.2 when TPM 2.0 has significant security improvements
- Ignoring that firmware TPM (fTPM) has weaker security guarantees than discrete TPM

## Connections
[[digital-signatures]] — TPMs perform signing operations and store signing keys in tamper-resistant hardware
- [[security-by-design]] — TPM is a hardware security design choice
- [[physical-unclonable-functions]] — Complementary hardware security primitive
- [[iot-security-hardware]] — Topic page on hardware security
- [[firmware-security]] — TPM protects firmware integrity
- [[device-memory-attack-surface]] — TPM protects key material from memory attacks

- [[iot-lecture-5]] — IoT Security Hardware — PUFs, TPMs, secure boot

## Open Questions
- How do we manage TPM lifecycle across billions of IoT devices?
- Is firmware TPM (fTPM) sufficient for IoT, or do we need discrete TPMs?
- How does TPM integrate with IoT-specific protocols and architectures?
