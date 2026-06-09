---
title: "OWASP IoT Top 10"
tags: [concept, iot-security, vulnerabilities, owasp, semester-1]
course: "IoT Security"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*The ten most critical IoT security vulnerabilities, providing a prioritized taxonomy for threat modeling and security testing.*

## Core Intuition
With billions of IoT devices deployed, you need a common language for 'what goes wrong most often.' The OWASP IoT Top 10 provides exactly that — a ranked list of the most impactful vulnerability categories, derived from real-world incidents and security research. It's the IoT equivalent of the famous OWASP Web Top 10, and it's what security auditors, penetration testers, and regulators reference when evaluating IoT products.

## Formal Definition / Statement
The OWASP IoT Top 10 (2018 edition, with updates) identifies the most critical IoT security vulnerabilities:

1. **I1: Weak, Guessable, or Hardcoded Passwords** — Default credentials, embedded passwords that can't be changed
2. **I2: Insecure Network Services** — Unnecessary open ports, vulnerable protocols (Telnet, FTP), unencrypted communications
3. **I3: Insecure Ecosystem Interfaces** — Weak security in web, mobile, cloud, and API interfaces
4. **I4: Lack of Secure Update Mechanism** — No OTA updates, unsigned firmware, no rollback protection
5. **I5: Use of Insecure or Outdated Components** — Known-vulnerable libraries, outdated OS, unpatched dependencies
6. **I6: Insufficient Privacy Protection** — Excessive data collection, insecure storage, no user data deletion
7. **I7: Insecure Data Transfer and Storage** — Plaintext protocols, unencrypted storage, weak key management
8. **I8: Lack of Device Management** — No asset management, no decommissioning process, no vulnerability monitoring
9. **I9: Insecure Default Settings** — Insecure default configurations, unnecessary features enabled by default
10. **I10: Lack of Physical Hardening** — Exposed debug ports (JTAG, UART), accessible firmware storage, no tamper detection

## Key Properties / Complexity
- Updated periodically; the 2018 version is most widely referenced
- Organized by impact, not frequency — I1 (weak passwords) is both most common and most impactful
- Provides a shared vocabulary for security assessments
- Maps to specific test cases in the OWASP IoT Testing Guide
- Referenced by ETSI EN 303 645, NISTIR 8259, and many national guidelines
- Applicable across all IoT verticals (consumer, industrial, healthcare)

## Worked Example
A security auditor evaluates a smart home hub using OWASP IoT Top 10:
- **I1**: Found 'admin:admin' default credentials that users aren't forced to change
- **I2**: Telnet (port 23) open and accessible from the LAN
- **I3**: Mobile app sends credentials in plaintext HTTP to the hub
- **I4**: No firmware update mechanism exists; vulnerabilities can't be patched
- **I5**: Running Linux kernel 3.10 with 47 known CVEs
- **I10**: JTAG header exposed on the PCB, allowing full memory dump

The auditor reports 6/10 categories affected. The product fails the assessment.

## Common Pitfalls
- **Not exhaustive**: The Top 10 covers the most common issues, not all possible vulnerabilities. Supply chain attacks and advanced persistent threats are not well represented.
- **Version drift**: The 2018 version predates many modern IoT attack vectors (e.g., API abuse in cloud-connected devices).
- **Overlap with web Top 10**: Some categories (I3 ecosystem interfaces) overlap with the general OWASP Web Top 10, causing confusion about which to apply.
- **Consumer bias**: The list skews toward consumer IoT. Industrial IoT vulnerabilities (e.g., protocol-specific attacks on Modbus) are not well covered.

## Connections
- [[penetration-testing-methodology]] — OWASP IoT Top 10 provides the target vulnerability categories for IoT pentests
- [[threat-modeling]] — Top 10 informs STRIDE threat categorization for IoT
- [[etsi-en-303-645]] — Many ETSI provisions directly address OWASP Top 10 categories
- [[nist-iot-cybersecurity]] — NIST baseline capabilities address several OWASP categories
- [[iot-attack-taxonomy]] — Broader taxonomy that includes OWASP categories plus additional vectors
- [[side-channel-attacks]] — I10 (physical hardening) addresses side-channel and physical extraction

## Open Questions
- How does this standard/framework apply to resource-constrained IoT devices with limited processing power?
- What are the practical tradeoffs between compliance and actual security improvement?
