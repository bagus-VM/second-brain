---
title: "Device Memory Attack Surface"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[attack-surface-analysis]]"]
---

## One-line Summary
The device memory attack surface class covers sensitive data stored in IoT device memory — including cleartext usernames, passwords, third-party credentials, and encryption keys — that can be extracted through physical or logical attacks.

## Core Intuition
IoT devices store secrets in memory. If that memory is accessible — through physical access, firmware extraction, or a memory dump vulnerability — all those secrets are exposed. This is often the easiest way to compromise a device.

## Formal Definition / Statement
**Device Memory Attack Surface (Miessler Class 2):**
Sensitive data that may be found in IoT device memory:
1. **Clear text username** — Usernames stored without encryption
2. **Clear text passwords** — Passwords stored without encryption
3. **Third-party credentials** — Credentials for external services stored insecurely
4. **Encryption keys** — Cryptographic keys stored in accessible memory

## Key Properties / Complexity

### Why It's Critical
- Memory is often directly accessible via physical interfaces ([[physical-interface-attack-surface|JTAG, UART]])
- Firmware extraction can reveal memory contents
- Many devices have no memory protection mechanisms
- Compromised memory often gives access to cloud APIs, other devices, and user data

### Mitigation Strategies
- **Encrypt sensitive data in memory** — Don't store plaintext
- **Use hardware security modules** ([[trusted-platform-module|TPM]], [[physical-unclonable-functions|PUFs]]) for key storage
- **Disable debug interfaces** in production (JTAG, SWD)
- **Memory protection units (MPUs)** — Restrict access to sensitive memory regions
- **Secure key storage** — Dedicated secure memory regions

## Worked Example
**Memory Dump Attack:**
1. Attacker gains physical access to IoT device
2. Connects to JTAG debug interface
3. Reads out flash memory contents
4. Finds: Wi-Fi password in cleartext, cloud API key, admin credentials
5. Uses credentials to access cloud platform
6. Gains control over all devices linked to that account

## Common Pitfalls
- Storing credentials in plaintext "because it's a constrained device"
- Not disabling debug interfaces in production units
- Assuming physical access is unlikely (IoT devices are often in uncontrolled environments)
- Using hardcoded keys that are the same across all devices of a model

## Connections
- [[attack-surface-analysis]] — Part of Miessler's 15 classes
- [[physical-interface-attack-surface]] — Physical access enables memory extraction
- [[firmware-security]] — Firmware often contains memory contents
- [[device-memory-attack-surface]] → [[trusted-platform-module]] — TPM protects key material
- [[physical-unclonable-functions]] — PUFs eliminate stored key vulnerabilities
- [[mirai-botnet]] — Default/hardcoded credentials in memory

## Open Questions
- What is the cost-performance trade-off for memory encryption in constrained devices?
- Can memory attestation detect tampering in real-time?
