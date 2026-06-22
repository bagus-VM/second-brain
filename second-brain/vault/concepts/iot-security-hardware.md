---
title: "IoT Security Hardware"
tags: [concept, iot-security, hardware, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
*Hardware security components and architectures that provide root of trust, secure storage, and tamper resistance for IoT devices.*

## Core Intuition
Software-only security has a ceiling. If an attacker can read your flash memory, modify your bootloader, or probe your bus, no amount of software encryption saves you. Hardware security creates a foundation that software builds upon — a tamper-resistant chip that stores keys in a way that even physical access can't extract them. For IoT, the challenge is fitting meaningful hardware security into a $0.50 microcontroller.

## Formal Definition / Statement
IoT security hardware spans a spectrum from basic to advanced:

**Secure Elements (SE):**
- Dedicated tamper-resistant chips (e.g., ATECC608A, SE050, ST33)
- Store cryptographic keys in protected hardware
- Perform crypto operations internally (keys never leave the chip)
- Common certifications: CC EAL5+, FIPS 140-2 Level 2+
- Cost: $0.30–$2.00 per unit

**Trusted Platform Module (TPM):**
- Standardized security chip (ISO/IEC 11889)
- PCR-based measured boot, remote attestation
- RSA/ECC key generation and storage
- More feature-rich than SE but higher cost and power

**Trusted Execution Environment (TEE):**
- Hardware-isolated execution environment on the main processor
- ARM TrustZone: splits processor into Secure World and Non-Secure World
- RISC-V Physical Memory Protection (PMP): hardware-enforced memory isolation
- Runs trusted code in isolation from the main OS

**Physical Unclonable Functions (PUF):**
- Exploit manufacturing variations to create unique device fingerprints
- No stored secret — the 'key' is derived from physical properties
- Variations: SRAM PUF, Ring Oscillator PUF, Arbiter PUF
- Applications: device authentication, key generation

**Hardware Security Modules (HSM):**
- Enterprise-grade crypto processing and key management
- Used in IoT gateways, cloud HSMs for fleet management
- Typically FIPS 140-2 Level 3+

**Debug Interface Control:**
- One-time programmable (OTP) fuses to disable JTAG/SWD
- Secure debug: require authentication to access debug ports
- Production vs development configurations

## Key Properties / Complexity
- Secure elements add $0.30–$2.00 to BOM cost
- TrustZone adds zero hardware cost (built into ARM Cortex-M33/M55) but requires secure firmware
- PUFs have no stored secret to extract — fundamentally different from key-based security
- TPM power consumption: 25–100mW (significant for battery-powered IoT)
- SE power consumption: <5mW during crypto operations
- Hardware security is only as good as the provisioning process

## Worked Example
Comparing security hardware options for an IoT product:

**Option A: Bare MCU ($0.50)**
- No hardware security. Keys in flash (extractable). Debug ports open.
- Suitable for: non-critical, short-lifecycle, indoor-only devices

**Option B: MCU + Secure Element ($0.80)**
- ATECC608A stores device certificate and TLS keys
- Keys never leave the SE — even firmware can't extract them
- Suitable for: consumer IoT, smart home, wearables

**Option C: MCU with TrustZone ($0.50)**
- ARM Cortex-M33 with TrustZone-M
- Secure World handles key management, secure boot, crypto
- Non-Secure World runs application code
- Suitable for: cost-sensitive products needing good security

**Option D: MCU + SE + TPM ($2.50)**
- Full hardware security stack
- TPM for remote attestation, SE for key storage, TrustZone for isolation
- Suitable for: industrial IoT, medical devices, critical infrastructure

## Common Pitfalls
- **Provisioning is critical**: Hardware security is useless if keys are provisioned insecurely
- **Supply chain trust**: How do you verify the secure element itself isn't compromised?
- **Over-specification**: Using a TPM for a $5 sensor is cost-prohibitive
- **Driver support**: Not all RTOS/BSPs have good support for all SE/TEE options
- **PUF reliability**: PUF responses can vary with temperature and aging; fuzzy extraction is needed
- **Debug access**: Leaving debug ports open in production negates hardware security benefits

## Connections
- [[physical-unclonable-functions]] — Detailed treatment of PUF technology
- [[tcg-specifications]] — TPM and DICE specifications
- [[iot-device-fundamentals]] — Hardware architecture context for security hardware
- [[secure-boot-chain]] — Hardware root of trust enables secure boot
- [[key-management-lifecycle]] — Hardware security underpins key management
- [[side-channel-attacks]] — Hardware security must resist side-channel attacks

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
