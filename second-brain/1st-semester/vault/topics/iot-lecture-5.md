---
title: "IoT Security Hardware"
tags: [topic, iot-security, semester-1]
course: "IoT Security"
source_count: 5
status: current
last_updated: 2026-06-02
prerequisites: ["[[iot-lecture-1]]", "[[iot-lecture-4]]"]
---

## One-line Summary
Hardware-based security mechanisms for IoT devices, covering [[physical-unclonable-functions]] (PUFs) for device identity, Trusted Platform Modules (TPMs) for cryptographic operations, and security co-processors for offloading and isolating security-critical functions.

## Core Intuition
Software-only security is inherently fragile — keys stored in flash can be extracted, software can be modified, and credentials can be copied. Hardware security mechanisms anchor trust in physical properties of the device itself that cannot be easily replicated, modified, or extracted. PUFs exploit manufacturing variations that are unique to each chip and impossible to clone. TPMs provide a dedicated, tamper-resistant vault for cryptographic keys. Security co-processors isolate security-critical operations from the main application processor, limiting the blast radius of software compromise. Together, these technologies establish a hardware root of trust that underpins the entire IoT security stack.

## Formal Definition / Statement

### Physical Unclonable Functions (PUFs)

A PUF is a physical structure that exploits inherent, uncontrollable manufacturing variations in [[semiconductor]] devices to produce a unique, device-specific response to a given challenge. The response acts as a hardware fingerprint that is:
- **Unique**: Each chip produces a different response due to random manufacturing variations (dopant concentration, wire delays, oxide thickness).
- **Unclonable**: Even the manufacturer cannot create two chips with identical PUF responses because the variations are physically random.
- **Tamper-Evident**: Attempts to physically probe or modify the PUF structure alter its behavior, making attacks detectable.

#### PUF Types

**SRAM PUF**
- Exploits the power-up state of SRAM cells. Each SRAM cell has a slight bias toward 0 or 1 determined by [[transistor]] [[threshold-voltage]] differences. The pattern of 0s and 1s at power-up is unique per chip.
- Advantages: Available on most CMOS chips (no special fabrication), mature technology, well-studied reliability.
- Challenges: Bit errors due to temperature/voltage variation require fuzzy extraction (helper data algorithms).

**Ring Oscillator PUF (RO-PUF)**
- Uses pairs of identical ring oscillators. Manufacturing variations cause slight frequency differences between oscillator pairs. The relative frequencies produce a binary output.
- Advantages: Easy to implement in FPGAs and ASICs, straightforward measurement.
- Challenges: Sensitive to environmental conditions, requires many oscillator pairs for sufficient entropy.

**Arbiter PUF (APUF)**
- Two identical signal paths race against each other. An arbiter flip-flop determines which signal arrived first. Manufacturing variations in path delays create unique timing differences.
- Advantages: Exponential number of challenge-response pairs (CRPs) from a linear number of components.
- Challenges: Vulnerable to machine learning attacks that can model the delay paths and predict responses. Requires strong error correction.

**Butterfly PUF**
- Cross-coupled latches or flip-flops that settle into a unique state determined by manufacturing variations. Similar to SRAM PUF but can be implemented in reconfigurable logic.
- Advantages: Usable in FPGAs, stable over temperature ranges.
- Challenges: Requires careful design to avoid metastability issues.

**Coating PUF**
- A transparent dielectric coating with random particle distribution is applied over the chip surface. Sensors beneath the coating measure capacitance variations caused by the particle positions.
- Advantages: Directly protects the chip surface, tamper-evident by design.
- Challenges: Requires specialized fabrication, limited commercial adoption.

#### PUF Applications in IoT

1. **Device Authentication**: Challenge-Response Pairs (CRPs) enable device authentication without stored secrets. The verifier sends a challenge, and the device returns the PUF-derived response. Server-side stores expected CRPs or uses helper data for fuzzy extraction.

2. **Key Generation**: PUF responses are processed through fuzzy extractors (secure sketch + randomness extractor) to derive stable cryptographic keys without storing keys in non-volatile memory. The key exists only when the device is powered on.

3. **Anti-Counterfeiting**: PUF-based unique device identities can verify that a device is genuine. Supply chain participants can verify PUF responses against manufacturer records to detect cloned or counterfeit devices.

4. **Secure Boot Root of Trust**: PUF-derived keys can anchor the [[secure-boot-chain]], ensuring that boot verification keys are unique per device and not stored in extractable memory.

5. **IP Protection**: PUFs can be used to lock FPGA bitstreams or ASIC designs to specific hardware instances, preventing IP theft through design copying.

#### PUF Challenges

- **Reliability**: PUF responses can change due to temperature, voltage, aging, and noise. Error correction (fuzzy extractors, error-correcting codes) is required, which adds complexity and may leak information.
- **Entropy Quality**: Not all PUF types produce responses with sufficient entropy. Post-processing (hashing, randomness extraction) is typically required.
- **CRP Database Management**: For challenge-response PUFs, the verifier must store or regenerate expected CRPs, which creates a management challenge at scale.
- **Machine Learning Attacks**: Some PUF types (especially arbiter PUFs) are vulnerable to modeling attacks where ML models learn the challenge-response mapping from observed CRPs.
- **Environmental Sensitivity**: Field-deployed IoT devices experience wide temperature and voltage ranges that can cause PUF response drift beyond error correction capacity.

### Trusted Platform Modules (TPMs)

A [[trusted-platform-module]] is a dedicated security chip (or firmware implementation) that provides hardware-rooted cryptographic services. TPMs are standardized by the Trusted Computing Group ([[tcg-specifications]]).

#### TPM Architecture

**Hardware Components**
- **Cryptographic Engine**: Dedicated hardware for RSA, ECC, SHA-1/SHA-256/SHA-384, and random number generation. Operations execute inside the TPM, so keys never leave the chip.
- **Platform Configuration Registers (PCRs)**: Registers that store integrity measurements (hashes) of firmware, bootloader, OS, and application code. Extended (not overwritten) during boot to create a chain of trust.
- **Persistent Storage**: Non-volatile memory for storing the Endorsement Key (EK), Storage Root Key (SRK), and owner authorization data.
- **Volatile Storage**: Scratch space for session keys, transient keys, and operational data.
- **Random Number Generator (RNG)**: Hardware TRNG (True Random Number Generator) using thermal noise or other physical entropy sources. Provides high-quality randomness for key generation.

**Key Hierarchy**
- **Endorsement Key (EK)**: A unique RSA or ECC key burned into the TPM during manufacturing. The EK certificate (issued by the TPM manufacturer) proves the TPM is genuine. The EK never leaves the TPM and is used only for identity operations.
- **Storage Root Key (SRK)**: The root of the key hierarchy for storage. All other keys are wrapped (encrypted) under the SRK or a descendant key.
- **Attestation Identity Key (AIK)**: A key derived from or associated with the EK, used for remote attestation. Multiple AIKs can be created to avoid using the EK directly, providing privacy.
- **Platform Keys**: Keys created by the OS or applications, stored as blobs wrapped under the SRK, and loaded into the TPM only when needed.

#### TPM Functions for IoT

1. **Secure Boot Measurement**: During boot, each stage (BIOS/ROM → bootloader → OS → application) measures the next stage's hash into PCRs. The TPM extends PCR values: `PCR_new = Hash(PCR_old || new_measurement)`. This creates an unforgeable chain of boot integrity measurements.

2. **Remote Attestation**: A remote verifier can request a quote (signed PCR values) from the TPM. The TPM signs the PCR values with an AIK, proving the device's boot state. The verifier checks whether the PCR values match expected good values. This detects rootkits, modified firmware, or unauthorized boot configurations.

3. **Sealed Storage**: Data can be "sealed" to specific PCR values. Sealed data can only be unsealed (decrypted) when the PCRs match the expected values. This ensures that sensitive data (encryption keys, credentials) is accessible only when the system is in a known-good state.

4. **Key Storage and Protection**: Cryptographic keys are generated inside the TPM and never exposed in plaintext outside the chip. Keys are stored as encrypted blobs in device storage and loaded into the TPM only for use. This protects keys even if the device's main storage is fully compromised.

5. **Random Number Generation**: The TPM's hardware RNG provides cryptographically secure random numbers for key generation, nonce creation, and other cryptographic operations. Addresses the entropy problem common in constrained IoT devices.

6. **Dictionary Attack Protection**: The TPM tracks failed authentication attempts and implements exponential backoff, protecting against brute-force attacks on TPM-protected keys.

#### TPM Implementations for IoT

- **Discrete TPM (dTPM)**: A separate physical chip (e.g., Infineon OPTIGA, STMicroelectronics ST33, Nuvoton NPCT75x). Highest security level but adds cost ($0.50–$2.00), board space, and power consumption.
- **Firmware TPM (fTPM)**: TPM functionality implemented in firmware running on ARM TrustZone or similar TEE (Trusted Execution Environment). Lower cost (no additional chip) but relies on the TEE's isolation guarantees. Used in many ARM-based IoT platforms.
- **Integrated TPM**: TPM functionality built directly into the SoC (System on Chip). Lowest cost and power overhead but tied to specific [[silicon]].

#### TPM 2.0 for IoT

TPM 2.0 (current standard) offers improvements over TPM 1.2:
- **Algorithm Agility**: Supports multiple algorithms (RSA, ECC, SHA-256/384/512) and is designed to add post-quantum algorithms.
- **Enhanced Authorization**: Policy-based authorization allows complex access control rules beyond simple passwords.
- **Flexible Hierarchy**: Multiple hierarchies (platform, storage, endorsement, null) for different trust domains.
- **Better suited for constrained devices**: Reduced command set profiles (e.g., TPM 2.0 for embedded) minimize the implementation overhead.

### Security Co-Processors

Dedicated hardware blocks or separate chips that offload and isolate security-critical operations from the main application processor.

#### Types of Security Co-Processors

**Secure Elements (SE)**
- Tamper-resistant chips (often [[common-criteria]] EAL 4+ or EAL 5+ certified) designed for key storage and cryptographic operations.
- Examples: NXP A71CH, Infineon OPTIGA SLB 9670, Microchip ATECC608B.
- Provide secure key storage, ECC/RSA signing, TLS handshake acceleration, and secure boot support.
- Smaller and lower power than full TPMs, often communicating via I2C or SPI.
- Commonly used in smart cards, payment terminals, and consumer IoT.

**Hardware Security Modules (HSM)**
- High-assurance devices for cryptographic [[key-management-lifecycle]] and operations. Typically used on the server/cloud side rather than on individual IoT devices.
- [[fips-140-2]]/140-3 certified (Level 2–4).
- Examples: Thales Luna, AWS CloudHSM, YubiHSM.
- In IoT context, HSMs secure the cloud-side key management infrastructure that provisions and manages device keys.

**Trusted Execution Environments (TEE)**
- Hardware-isolated execution environments on the main SoC that protect code and data from the normal OS.
- ARM TrustZone: Splits the processor into Secure World and Normal World. Security-critical code (key management, biometric processing, secure boot) runs in Secure World, isolated from the potentially compromised Normal World OS.
- Intel SGX (Software Guard Extensions): Creates hardware-encrypted enclaves in memory. Used in edge computing IoT platforms.
- RISC-V MultiZone: Open-source TEE for RISC-V processors, relevant for emerging open-hardware IoT platforms.
- TEEs provide lower cost than discrete security chips but require careful implementation to avoid side-channel leakage between worlds.

**Cryptographic Accelerators**
- Hardware blocks that accelerate specific cryptographic operations (AES, SHA, ECC point multiplication) to reduce CPU load and power consumption.
- Not security co-processors in the isolation sense — they share the same security domain as the main CPU.
- Critical for constrained devices that cannot run cryptographic operations in software within timing or power budgets.
- Examples: ARM CryptoCell, ESP32 hardware AES/RSA acceleration, Nordic Semiconductor CryptoCell-310.

#### Security Co-Processor Applications

1. **TLS Offloading**: Performing the asymmetric cryptographic operations (ECDHE key exchange, certificate verification) during TLS handshakes, freeing the main CPU for application logic.

2. **Secure Boot Verification**: Verifying firmware signatures during boot, with the verification key stored in the security co-processor's tamper-resistant storage.

3. **Device Attestation**: Providing hardware-signed evidence of device identity and integrity to cloud services during provisioning or periodic check-ins.

4. **Key Provisioning**: During manufacturing, injecting unique device keys into the security co-processor's secure storage. Keys are generated externally (by a manufacturing HSM) or internally (by the co-processor's RNG).

5. **Secure Storage**: Protecting credentials, certificates, and configuration data in tamper-resistant storage that is inaccessible to the main CPU.

## Key Properties / Complexity

- **Cost vs. Security Trade-off**: Discrete TPMs and secure elements add $0.50–$2.00 to BOM (Bill of Materials). For high-volume, low-cost IoT devices, this is significant. Firmware-based solutions (fTPM, TEE) reduce cost but may reduce assurance.
- **Power Overhead**: Security co-processors consume power. For battery-powered IoT devices, the power budget for security operations must be carefully managed.
- **Supply Chain Trust**: Hardware security chips must be sourced from trusted manufacturers. Counterfeit or trojan-containing security chips would undermine the entire trust model.
- **Standardization Maturity**: TPM 2.0 is well-standardized for traditional computing but IoT-specific profiles are still evolving. PUF standardization (e.g., ISO/IEC 20897) is nascent.
- **Integration Complexity**: Adding hardware security requires PCB design changes, driver development, provisioning infrastructure, and key management lifecycle processes.
- **Quantum Threat Horizon**: Current PUF and TPM implementations rely on classical cryptography (RSA, ECC). Post-quantum migration paths must be considered for long-lived IoT devices.

## Connections

### Hardware Identity
- [[physical-unclonable-functions]] — Deep dive into PUF types, reliability, and security properties
- [[trusted-platform-module]] — TPM architecture, key hierarchy, and attestation protocols in detail

### Design Integration
- [[iot-lecture-4]] — Goal 5 (Hardware Protection) and how hardware security fits into the broader design framework
- [[firmware-security]] — How secure boot chains leverage TPMs and security co-processors
- [[secure-boot-chain]] — The boot measurement and verification process using TPM PCRs

### Attack Context
- [[iot-lecture-2]] — Physical attacks and cryptographic attacks that hardware security mitigates
- [[iot-lecture-3]] — Classes 2 (Device Memory), 3 (Physical Interfaces) addressed by hardware security
- [[side-channel-attacks]] — Power analysis, EM analysis, and fault injection countermeasures

### Provisioning and Lifecycle
- [[device-provisioning]] — How hardware security chips are provisioned during manufacturing
- [[key-management-lifecycle]] — Generation, storage, rotation, and revocation of hardware-protected keys
- [[operational-security-lifecycle]] — Long-term management of hardware-rooted trust

### Standards and Certification
- [[common-criteria]] — Evaluation assurance levels for secure elements and TPMs
- [[fips-140-2]] — Cryptographic module validation for HSMs and security processors
- [[tcg-specifications]] — Trusted Computing Group standards for TPMs and trusted platforms

### Broader IoT Security
- [[iot-lecture-1]] — Overview connecting hardware security to the full IoT security domain
- [[iot-lecture-4]] — Design principles that leverage hardware security mechanisms

## Open Questions
- Can PUFs provide sufficient reliability for devices operating in extreme environments (industrial, automotive, military)?
- How will post-quantum cryptography impact TPM designs, and what is the migration path for deployed IoT devices?
- Is the cost of discrete security hardware justified for consumer IoT devices with $5–$10 price points?
- How can hardware root of trust be maintained when device components are sourced from multiple global suppliers with varying trust levels?
- Can TEE-based security (TrustZone, SGX) provide equivalent assurance to discrete secure elements against sophisticated adversaries with physical access?
- How should hardware security mechanisms evolve to support decentralized IoT architectures (blockchain-based device identity, peer-to-peer attestation)?
