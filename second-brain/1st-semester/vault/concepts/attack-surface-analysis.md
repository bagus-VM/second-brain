---
title: "Attack Surface Analysis"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[iot-attack-taxonomy]]", "[[threat-modeling]]"]
---

## One-line Summary
Daniel Miessler's 15 attack surface classes (DefCon 2023) provide a comprehensive framework for systematically analysing all the ways an IoT system can be attacked.

## Core Intuition
Instead of thinking about attacks ad-hoc, Miessler's framework categorises every possible entry point and weakness. If you systematically evaluate all 15 classes, you're far less likely to miss a critical vulnerability.

## Formal Definition / Statement
**15 IoT Attack Surface Classes** (Daniel Miessler, DefCon 2023):

1. **Access Control** — Authentication, session management, implicit trust, enrolment, decommissioning, lost access
2. **[[device-memory-attack-surface|Device Memory]]** — Clear text credentials, third-party credentials, encryption keys in memory
3. **[[physical-interface-attack-surface|Physical Interface Assessment]]** — Firmware extraction, user/admin CLI, privilege escalation, reset to insecure state
4. **[[web-interface-vulnerabilities|Device Web Interface]]** — SQL injection, XSS, username enumeration, weak passwords, account lockout, known credentials
5. **[[firmware-security|Device Firmware]]** — Hardcoded passwords, sensitive URL disclosure, encryption keys in firmware
6. **Device Network Services** — Information disclosure, user/admin CLI, injection, DoS
7. **Administrative Web Interface** — Same vulns as device web interface (SQL injection, XSS, etc.)
8. **Local Data Storage** — Unencrypted data, recoverable encryption keys, lack of integrity checks
9. **Cloud Web Interface** — Same web vulns (SQL injection, XSS, etc.)
10. **Third-Party Back-End APIs** — Unencrypted PII, device info leaks, location leaks
11. **[[ota-updates|Update Mechanism]]** — Unencrypted updates, unsigned updates, writable source location
12. **Mobile Application** — Implicit trust, known credentials, insecure data storage, lack of transport encryption
13. **Vendor Back-End API** — Inherent trust, weak auth, weak access control, injection
14. **[[ecosystem-communications-security|Ecosystem Communications]]** — Health checks, heartbeats, ecosystem commands, decommissioning, update pushes
15. **Network Traffic** — LAN traffic, LAN-to-Internet, non-standard protocols, short-range (Bluetooth, ZigBee, NFC)

## Key Properties / Complexity

### Why 15 Classes?
- IoT systems are complex ecosystems with many components
- Each component has a different attack profile
- Traditional IT attack surfaces don't cover physical, firmware, ecosystem-specific vectors

### Relationship to Attack Types (Lecture 3)
The 15 classes provide finer granularity than the 9 attack types from Lecture 3. For example:
- "Physical security attacks" (Lecture 3) → Classes 3 (Physical Interface), 8 (Local Storage)
- "Protocol attacks" (Lecture 3) → Class 15 (Network Traffic)
- "Spoofing" (Lecture 3) → Classes 1 (Access Control), 4/7/9 (Web Interfaces)

## Worked Example
**Evaluating a Smart Camera:**
| Class | Finding | Risk |
|-------|---------|------|
| Device Memory | Passwords stored in cleartext | High |
| Physical Interface | JTAG exposed on PCB | High |
| Firmware | Hardcoded admin password | Critical |
| Device Web Interface | No account lockout | Medium |
| Update Mechanism | Updates not signed | High |
| Mobile App | Credentials stored in plaintext | High |

This systematic evaluation across all 15 classes ensures nothing is missed.

## Common Pitfalls
- Only evaluating software attack surfaces and ignoring physical/firmware/ecosystem
- Treating the 15 classes as a checklist rather than a framework
- Not considering that classes interact (e.g., firmware extraction enables memory attacks)
- Ignoring third-party and vendor API attack surfaces

## Connections
- [[iot-attack-taxonomy]] — Broader attack categories
- [[device-memory-attack-surface]] — Class 2 deep dive
- [[physical-interface-attack-surface]] — Class 3 deep dive
- [[firmware-security]] — Class 5 deep dive
- [[web-interface-vulnerabilities]] — Classes 4, 7, 9 deep dive
- [[ota-updates]] — Class 11 deep dive
- [[ecosystem-communications-security]] — Class 14 deep dive
- [[iot-attack-surfaces]] — Topic page for comprehensive coverage

- [[iot-lecture-2]] — IoT Common Attacks — taxonomy
- [[iot-lecture-3]] — IoT Attack Surfaces — Miessler's 15 classes

## Open Questions
- How do the 15 classes map to specific compliance requirements?
- Can automated tools cover all 15 classes?
- How will new IoT technologies (5G, AI) create new attack surface classes?
