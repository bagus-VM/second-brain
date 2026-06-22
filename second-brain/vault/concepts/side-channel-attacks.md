---
title: "Side-Channel Attacks"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[iot-device-fundamentals]]", "[[physical-unclonable-functions]]"]
---
## One-line Summary
Side-channel attacks extract cryptographic keys and internal state from IoT devices by measuring physical phenomena — power consumption, electromagnetic emissions, timing, and sound — rather than breaking the math.

## Core Intuition
Cryptography is mathematically secure, but physical implementations leak information. A processor consuming different amounts of power when computing a 1 versus a 0 creates a measurable side channel. By analyzing thousands of power traces during cryptographic operations, an attacker can recover the secret key. IoT devices are especially vulnerable because they often lack side-channel countermeasures (they cost money and power) and because attackers can buy them for $5 and take them home to attack at leisure.

## Formal Definition / Statement
Side-channel attacks exploit information leaked through physical implementation characteristics rather than mathematical weaknesses in cryptographic algorithms.

**Power Analysis:**
- **SPA (Simple Power Analysis)**: Direct observation of power consumption traces during cryptographic operations. Different operations (multiplication vs. no operation) produce visibly different power patterns.
- **DPA (Differential Power Analysis)**: Statistical analysis of many power traces to extract correlations between power consumption and secret key bits. Requires thousands of traces but recovers keys automatically.
- **CPA (Correlation Power Analysis)**: Uses Pearson correlation between predicted power consumption (based on a key hypothesis) and actual measurements. Most common modern approach.

**Electromagnetic (EM) Analysis:**
- **EMA (Electromagnetic Analysis)**: Measures EM emanations from the device instead of power consumption. Can target specific chip regions (spatial selectivity).
- **Advantages**: Non-invasive, can target specific circuit blocks, works even when power analysis is filtered.

**Timing Attacks:**
- Measure execution time of cryptographic operations to infer secret data
- Example: RSA with square-and-multiply — if multiplication takes different time depending on key bit, timing reveals key
- Applicable to software implementations, especially on devices without constant-time code

**Fault Injection:**
- **Voltage glitching**: Brief voltage spikes during execution to skip instructions or corrupt data
- **Clock glitching**: Brief clock frequency changes to cause timing violations
- **Laser fault injection**: Precise laser pulses to flip specific bits in SRAM or logic
- **EM fault injection**: EM pulses to induce faults without physical access
- **Application**: Skip signature verification in secure boot, bypass authentication checks, induce key-dependent faults

**Acoustic Attacks:**
- Measure sound emitted by capacitors and inductors during cryptographic operations
- Can recover RSA keys from laptop/tablet at 30cm distance
- Less practical for embedded IoT but relevant for larger devices

**Cache Attacks:**
- Measure timing differences due to cache hits/misses during crypto operations
- Prime+Probe, Flush+Reload techniques
- Relevant for IoT devices running shared caches (multi-core MCUs, TEE environments)

## Key Properties / Complexity

- **IoT devices are easy targets**: Cheap, physically accessible, no tamper protection, no side-channel countermeasures
- **Equipment cost ranges from $0 (software timing) to $50,000+ (laser fault injection)**
- **DPA/CPA typically require 1,000-100,000 traces** — feasible within hours on a microcontroller
- **AES is vulnerable**: Table-based AES implementations leak key bits through cache access patterns and power consumption
- **RSA is vulnerable**: Modular exponentiation leaks key bits through timing and power
- **Countermeasures exist but cost resources**: Masking, shuffling, constant-time code, hardware noise generators
- **Physical access required**: Most side-channel attacks require the attacker to have the device (or be very close for EM/acoustic)

## Worked Example

**DPA attack on AES-128 in a smart card:**
1. Attacker has physical access to IoT device (e.g., smart meter)
2. Connects oscilloscope probe to VCC pin and ground
3. Sends 10,000 random plaintexts to the device, triggering AES encryption
4. Records power trace for each encryption (10,000 traces × 10,000 samples each)
5. For each key byte (16 bytes in AES-128), computes hypothetical power consumption for all 256 possible values
6. Computes Pearson correlation between hypothetical and actual power consumption
7. Key byte with highest correlation is the correct value
8. Repeat for all 16 bytes → full AES-128 key recovered

**Mitigation:**
- **Masking**: Randomize intermediate values during computation (split key shares)
- **Shuffling**: Randomize operation order to decorrelate power from key
- **Hardware countermeasures**: Power filtering, noise generation, constant-time hardware crypto

## Common Pitfalls

- Assuming "mathematically secure" means "physically secure"
- Not considering physical access in the threat model (especially for consumer IoT)
- Using software AES without side-channel countermeasures on a microcontroller
- Implementing RSA with variable-time modular exponentiation
- Relying on firmware-only security without hardware protections
- Assuming the device will be in a secure facility (consumer IoT is in the attacker's home)

## Connections

- [[iot-device-fundamentals]] — Constrained devices lack side-channel countermeasures
- [[physical-unclonable-functions]] — PUFs exploit physical properties; side channels attack them
- [[trusted-platform-module]] — TPMs designed with side-channel resistance
- [[secure-boot-chain]] — Fault injection can bypass secure boot verification
- [[key-management-lifecycle]] — Key extraction via side channels
- [[iot-lecture-5]] — Hardware security mechanisms and their physical attack surfaces
- [[iot-lecture-2]] — Physical attacks in the attack taxonomy

## Open Questions
- Can machine learning fully automate side-channel attacks, reducing the expertise required?
- How do post-quantum algorithms (lattice-based) compare to RSA/AES in side-channel vulnerability?
- What side-channel countermeasures are feasible for $1 IoT devices?
