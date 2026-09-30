---
title: "IoT Security Exam Format"
tags: [exam, semester-1, iot-security]
course: "IoT Security"
source: "Email from Dr. Nikolas (2026-06-08)"
status: current
last_updated: 2026-06-08
prerequisites:
  - iot-security-landscape
  - cia-triad
  - iot-common-attacks
  - threat-modeling
---

## One-line Summary
*Written exam (60–90 min) with three question types: definitions, use-case scenarios, and security solutions.*

## Exam Structure

**Format:** Written, 60–90 minutes
**Instructor:** Dr. Nikolas

### Question Type 1 — Definitions
Define core IoT security concepts.

Examples given by the instructor:
- "Define what the IoT is."
- "Define what confidentiality is."

**Key rule:** You do NOT need to reproduce the exact wording from the slides. You must provide a *valid* definition. Example acceptable answer for confidentiality:
> "Confidentiality is the property relevant to ensuring that secret information is only available to parties that should legitimately be able to access it."

**Implication:** Rote memorization of slide definitions is unnecessary. What matters is that you *understand* the concept well enough to articulate it precisely in your own words.

### Question Type 2 — Use Case Scenarios
You are given an IoT scenario (smart car, smart home, smart agricultural field, etc.) and asked to:

1. Identify **two assets** (devices, networks, etc.)
2. Provide **two threats**
3. Provide **two attacks**
4. Provide **two countermeasures**
5. Explain which **security property** (CIA+) each relates to
6. Comment on **cost** and **expertise needed**

This is a structured analysis question — they want to see you can walk through the full threat modeling pipeline for a concrete scenario.

**Study strategy:** Practice with any IoT scenario. The template is always the same:
`scenario → assets → threats → attacks → countermeasures → CIA mapping → cost/expertise`

### Question Type 3 — Security Solutions
Explain how a specific security mechanism works.

Example: "Explain how a digital signature works."

**Study strategy:** For each security solution in the course, be able to explain *how it works*, not just *what it does*. Understand the mechanism, the steps, the math if applicable.

## Worked Example — Use Case Scenario

**Scenario:** Smart Home

| Step | Answer |
|------|--------|
| Asset 1 | Smart thermostat (IoT device controlling HVAC) |
| Asset 2 | Home Wi-Fi network (connects all smart devices) |
| Threat 1 | Unauthorized access to thermostat (privacy invasion, physical safety) |
| Threat 2 | Network eavesdropping on unencrypted traffic |
| Attack 1 | Default credential exploitation (cf. [[mirai-botnet]]) |
| Attack 2 | Man-in-the-middle on Wi-Fi (cf. [[krack-attack]]) |
| Countermeasure 1 | Mandatory password change on first setup |
| Countermeasure 2 | WPA3 enforcement + TLS for device communication |
| CIA mapping | Confidentiality (eavesdropping), Availability (DoS via thermostat lockout) |
| Cost | Low for password enforcement; moderate for WPA3/TLS rollout |
| Expertise | Low for password policy; medium for network-level encryption |

## Common Pitfalls
- Don't just name the concept — explain *how it works* when asked about security solutions.
- Use case scenarios require structured answers. Random threats without CIA mapping loses points.
- "Countermeasure" ≠ "turn it off." Think about practical, deployable mitigations.

## Connections
[[cia-triad]] — every use case answer must map back to CIA properties
[[iot-common-attacks]] — source material for attack types
[[threat-modeling]] — the structured process behind use case scenarios
[[iot-attack-taxonomy]] — 9 categories to draw from
[[iot-secure-design]] — design principles relevant to countermeasures
[[mirai-botnet]] — classic example for use case attack answers
[[krack-attack]] — classic example for network-level attacks
[[digital-signatures]] — confirmed example security solution exam question

## Open Questions
- [ ] Which specific security solutions are in scope? (Digital signatures confirmed; others TBD)
- [ ] Are there past exam papers available for practice?
- [ ] Does the "use case scenario" section allow choosing which scenario to answer, or is it assigned?


---

## Related Resources

### 📖 IoT Security Landscape
- Lecture topic: [[iot-lecture-1]]

**Key concepts covered:**
- [[networking-fundamentals]]
- [[security-principles]]
- [[information-assurance]]
- [[iot-device-fundamentals]]
- [[iot-communication-protocols]]
- [[iot-network-architecture]]
- [[cia-triad]]
- [[firmware-security]]
- [[privacy-by-design]]
- [[risk-assessment-frameworks]]
- [[secure-development-lifecycle]]
- [[ota-updates]]
- [[iot-data-lifecycle]]
- [[smart-home-security]]
- [[industrial-iot-security]]
- [[healthcare-iot-security]]
- [[smart-city-infrastructure]]
- [[devops-security]]
- [[operational-security-lifecycle]]
- [[mirai-botnet]]
- [[krack-attack]]
- [[physical-unclonable-functions]]

### 📖 IoT Common Attacks
- Lecture topic: [[iot-lecture-2]]

**Key concepts covered:**
- [[networking-fundamentals]]
- [[mqtt-security]]
- [[coap-security]]
- [[zigbee-security-model]]
- [[ble-security]]
- [[mirai-botnet]]
- [[krack-attack]]
- [[zigbee-pairing-vulnerability]]
- [[attack-surface-analysis]]
- [[security-by-design]]
- [[information-assurance]]
- [[network-security-fundamentals]]

### 📖 IoT Attack Surfaces
- Lecture topic: [[iot-lecture-3]]

**Key concepts covered:**
- [[attack-surface-analysis]]
- [[mirai-botnet]]
- [[owasp-iot-top-10]]
- [[web-interface-vulnerabilities]]
- [[physical-interface-attack-surface]]
- [[threat-modeling]]
- [[penetration-testing-methodology]]
- [[firmware-security]]
- [[zigbee-pairing-vulnerability]]
- [[nist-iot-cybersecurity]]

### 📖 IoT Secure Design
- Lecture topic: [[iot-lecture-4]]

**Key concepts covered:**
- [[resilience-iot]]
- [[iot-compliance-frameworks]]
- [[iot-firewalling]]
- [[ota-updates]]
- [[iec-62443]]
- [[security-by-design]]
- [[devops-security]]
- [[operational-security-lifecycle]]
- [[digital-signatures]]
- [[firmware-security]]
- [[web-interface-vulnerabilities]]
- [[mirai-botnet]]
- [[krack-attack]]
- [[nist-iot-cybersecurity]]
- [[etsi-en-303-645]]
- [[threat-modeling]]
- [[principle-of-least-privilege]]
- [[zero-trust-architecture]]
- [[information-assurance]]

### 📖 IoT Security Hardware
- Lecture topic: [[iot-lecture-5]]

**Key concepts covered:**
- [[physical-unclonable-functions]]
- [[semiconductor]]
- [[transistor]]
- [[threshold-voltage]]
- [[secure-boot-chain]]
- [[trusted-platform-module]]
- [[tcg-specifications]]
- [[silicon]]
- [[common-criteria]]
- [[key-management-lifecycle]]
- [[fips-140-2]]
- [[firmware-security]]
- [[side-channel-attacks]]
- [[device-provisioning]]
- [[operational-security-lifecycle]]

### 📖 Cryptography and Lightweight Security Primitives for IoT
- Lecture topic: [[iot-lecture-6]]

**Key concepts covered:**
- [[information-assurance]]
- [[physical-unclonable-functions]]
- [[trusted-platform-module]]
- [[random-number-generator]]
- [[lightweight-cryptography]]
- [[ascon]]
- [[cia-triad]]
- [[authentication]]
- [[non-repudiation]]
- [[resilience-iot]]
- [[digital-signatures]]
- [[ota-updates]]
- [[firmware-security]]
- [[secure-boot-chain]]
- [[nist-iot-cybersecurity]]
- [[key-management-lifecycle]]
- [[iot-secure-design]]
- [[mqtt-security]]
- [[zigbee-security-model]]
- [[ble-security]]

### 📖 Identity Life Cycle and Privacy in IoT
- Lecture topic: [[iot-lecture-7]]

**Key concepts covered:**
- [[trusted-platform-module]]
- [[iot-architecture]]
- [[iot-compliance-frameworks]]
- [[privacy-by-design]]
- [[secure-boot-chain]]
- [[asymmetric-encryption]]
- [[iot-2-0]]
- [[iot-data-lifecycle]]
- [[iot-secure-design]]
- [[nist-iot-cybersecurity]]
- [[authentication]]
- [[key-management-lifecycle]]

### 📖 IoT Security - Lecture 8: Compliance, IoT 2.0, and Advanced Threats
- Lecture topic: [[iot-lecture-8]]

**Key concepts covered:**
- [[attack-tree]]
- [[fault-tree]]
- [[resilience-iot]]
- [[iot-identity-lifecycle]]
- [[privacy-by-design]]
- [[defense-in-depth]]
- [[threat-modeling]]
- [[security-by-design]]
- [[secure-development-lifecycle]]
- [[operational-security-lifecycle]]
- [[iot-compliance-frameworks]]
- [[iot-2.0]]
- [[mirai-botnet]]
- [[zero-trust-architecture]]
- [[iot-security-overview]]
- [[pki]]
- [[gdpr-compliance]]
- [[information-assurance]]

### 📖 DRAM-PUF Based IoT Security Protocol
- Lecture topic: [[iot-lecture-9]]

**Key concepts covered:**
- [[physical-unclonable-functions]]
- [[trusted-platform-module]]
- [[device-provisioning]]
