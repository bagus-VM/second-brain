---
title: "Trusted Computing Group (TCG) Specifications"
tags: [concept, iot-security, hardware-trust, standards, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
*TCG defines hardware-based security standards including TPM, DICE, and TRNG for establishing root of trust in computing devices.*

## Core Intuition
Software-only security has a fundamental problem: if the software is compromised, the security mechanisms it relies on are also compromised. TCG solves this by putting security primitives in hardware — a tamper-resistant chip that can store keys, attest to system state, and generate true random numbers. For IoT, TCG's DICE (Device Identifier Composition Engine) standard is particularly important because it provides hardware root of trust on resource-constrained microcontrollers that can't run a full TPM.

## Formal Definition / Statement
The Trusted Computing Group (TCG) is an industry consortium that develops security specifications. Key specifications include:

**TPM (Trusted Platform Module)** — ISO/IEC 11889
- Dedicated security chip (or firmware implementation) providing:
  - Secure key generation and storage (RSA, ECC)
  - Platform Configuration Registers (PCRs) for measured boot
  - Remote attestation (prove system state to a verifier)
  - True Random Number Generator (TRNG)
  - Sealed storage (data bound to specific platform state)

**DICE (Device Identifier Composition Engine)**
- Lightweight hardware root of trust for constrained devices
- Derives device identity from hardware unique ID + firmware measurement
- Layers: DICE Layer 0 (hardware) → Layer 1 (firmware) → Layer 2 (OS/app)
- Each layer derives new secrets based on measurement of the next
- Enables device attestation without a full TPM

**DICE Protection Environment (DPE)**
- Extension of DICE for multi-tenant and confidential computing
- Supports compartmentalized attestation

**TRNG (True Random Number Generator)**
- Hardware-based entropy source
- Required for cryptographic key generation

## Key Properties / Complexity
- TPM 2.0 is mandatory for Windows 11 certification
- DICE is designed for microcontrollers (ARM TrustZone, RISC-V)
- TPM provides tamper-resistant key storage; DICE derives keys from measurements
- Remote attestation enables zero-trust device onboarding
- PCRs extend (hash chain) — can't be forged without detecting tamper
- FIPS 140-2 Level 2+ validation common for TPM implementations
- TPM chips cost $1–3; DICE can be implemented in silicon with minimal die area

## Worked Example
An IoT gateway uses DICE for secure boot and attestation:
1. **Layer 0 (hardware)**: On power-up, the DICE hardware reads its unique device secret (UDS) and measures the bootloader hash
2. **Layer 1 (bootloader)**: Derives a Compound Device Identifier (CDI) = Hash(UDS || bootloader_measurement)
3. If the bootloader hasn't been tampered with, CDI is the expected value
4. The bootloader measures the OS and derives Layer 2 secrets
5. **Attestation**: The device sends its DICE certificate chain to the cloud service
6. The cloud verifies: 'This device's hardware identity is X, and it booted firmware with hash Y'
7. If Y matches the expected value, the device is granted network access

## Common Pitfalls
- **TPM is overkill for many IoT devices**: A $0.50 microcontroller can't justify a $2 TPM chip. DICE addresses this.
- **PCR state management**: Extending PCRs incorrectly can lock the device out of its own keys.
- **Firmware TPM (fTPM)**: Software TPM implementations (like AMD fTPM) have had vulnerabilities (faulTPM attack, 2023). Hardware TPM is more resistant.
- **DICE adoption**: Still emerging. Many IoT devices lack DICE support in their microcontrollers.
- **Supply chain**: TPMs must be provisioned during manufacturing. Getting unique, correctly provisioned TPMs at scale is a supply chain challenge.

## Connections
- [[physical-unclonable-functions]] — PUFs provide similar hardware identity guarantees
- [[secure-boot-chain]] — TCG measured boot and DICE are implementations of secure boot
- [[fips-140-2]] — TPMs are typically FIPS 140-2 Level 2+ validated
- [[common-criteria]] — TPMs often undergo CC evaluation at EAL4+
- [[device-provisioning]] — DICE certificates enable automated device onboarding
- [[key-management-lifecycle]] — TPM provides hardware-backed key storage and lifecycle management

## Open Questions
- How does this standard/framework apply to resource-constrained IoT devices with limited processing power?
- What are the practical tradeoffs between compliance and actual security improvement?
