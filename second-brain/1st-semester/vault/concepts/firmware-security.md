---
title: "Firmware Security"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[attack-surface-analysis]]", "[[ota-updates]]"]
---

## One-line Summary
Firmware security covers vulnerabilities in IoT device firmware — including hardcoded passwords, sensitive URL disclosure, and embedded encryption keys — that can be exploited through firmware extraction and reverse engineering.

## Core Intuition
Firmware is the software that runs on your IoT device. If an attacker can extract it (via physical access or network exploits), they can reverse engineer it to find hardcoded secrets, hidden commands, and vulnerabilities. Many IoT vendors ship firmware with glaring security issues.

## Formal Definition / Statement
**Device Firmware Attack Surface (Miessler Class 5):**
1. **Hardcoded passwords** — Passwords embedded directly in firmware code
2. **Sensitive URL disclosure** — Internal API endpoints, admin URLs exposed in firmware
3. **Encryption keys** — Cryptographic keys hardcoded in firmware

## Key Properties / Complexity

### Firmware Extraction Methods
- **Physical:** JTAG, SPI flash dump, UART bootloader
- **Logical:** Update mechanism exploitation, vendor website, man-in-the-middle
- **Side-channel:** Power analysis, electromagnetic analysis (advanced)

### Common Firmware Vulnerabilities
- Default/hardcoded credentials (admin/admin, root/password)
- Embedded API keys for cloud services
- Private keys for TLS or code signing
- Debug backdoors left from development
- Unpatched third-party libraries (known CVEs)
- Lack of ASLR, stack canaries, and other binary protections

### Firmware Security Measures
- **Secure boot** — Verify firmware signature before execution
- **Signed updates** — Only accept firmware signed by the vendor
- **Encrypted firmware** — Obfuscate firmware to deter extraction
- **Key storage** — Use [[trusted-platform-module|TPM]] or [[physical-unclonable-functions|PUFs]] instead of hardcoded keys
- **Stripping** — Remove debug symbols and unused code before shipping

## Worked Example
**Firmware Extraction and Analysis:**
1. Download firmware update from vendor website (HTTP)
2. Extract filesystem (binwalk)
3. Search for strings: `grep -r "password" firmware/`
4. Find: `admin_password = "s3cr3t123"` hardcoded in config
5. Find: AWS API key embedded for cloud communication
6. Find: Private TLS key used by all devices of this model
7. Use credentials to access device web interface and cloud API
8. All devices of this model are now compromised

## Common Pitfalls
- Storing secrets in firmware (use secure hardware instead)
- Not signing firmware updates
- Shipping debug code in production firmware
- Not stripping symbols and debug information
- Using the same firmware for all devices (no per-device unique keys)

## Connections
[[digital-signatures]] — firmware images are verified using RSA/ECDSA/Ed25519 signatures before boot
- [[attack-surface-analysis]] — Miessler class 5
- [[ota-updates]] — Secure update mechanism protects firmware
- [[device-memory-attack-surface]] — Firmware often contains memory-mapped secrets
- [[physical-interface-attack-surface]] — Physical access enables firmware extraction
- [[security-by-design]] — Firmware security must be designed in
- [[web-interface-vulnerabilities]] — Firmware often hosts the web interface
- [[mirai-botnet]] — Default credentials in firmware enabled Mirai

- [[iot-lecture-1]] — IoT Security Landscape — course overview
- [[iot-lecture-3]] — IoT Attack Surfaces — Miessler's 15 classes
- [[iot-lecture-4]] — IoT Secure Design — best practices
- [[iot-lecture-5]] — IoT Security Hardware — PUFs, TPMs, secure boot

## Open Questions
- Should firmware be open-source for security auditing?
- How do we handle firmware security for devices with 10+ year lifespans?
- Can automated firmware analysis tools replace manual security review?
