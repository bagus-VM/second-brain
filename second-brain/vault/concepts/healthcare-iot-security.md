---
title: "Healthcare IoT Security"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[iot-device-fundamentals]]", "[[network-security-fundamentals]]"]
---
## One-line Summary
Healthcare IoT (IoMT) security covers connected medical devices — insulin pumps, pacemakers, patient monitors — where a security failure can directly harm or kill patients, regulated by FDA guidance and HIPAA.

## Core Intuition
Healthcare IoT is where cybersecurity becomes life safety. A compromised insulin pump can deliver a lethal dose. A hacked pacemaker can be stopped remotely. A ransomware attack on a hospital's connected devices can disable patient monitoring during surgery. Unlike a compromised smart bulb, a compromised medical device has immediate physical consequences. This elevates security from an IT concern to a patient safety imperative.

## Formal Definition / Statement
Internet of Medical Things (IoMT) encompasses connected medical devices that collect, transmit, or act upon health data. This includes:
- **Implantable devices**: Pacemakers, insulin pumps, neurostimulators, cochlear implants
- **Wearable devices**: Continuous glucose monitors, cardiac monitors, pulse oximeters
- **Point-of-care devices**: Infusion pumps, ventilators, patient monitors, imaging systems
- **Remote patient monitoring**: Blood pressure cuffs, weight scales, spirometers

**Regulatory Framework:**

**FDA Premarket Cybersecurity Guidance (2023):**
- Threat modeling required during device design
- Cybersecurity management plan throughout device lifecycle
- Vulnerability disclosure process (coordinated disclosure)
- Software Bill of Materials (SBOM) required
- Security testing (penetration testing, static analysis) documented
- OTA update capability for security patches

**HIPAA (Health Insurance Portability and Accountability Act):**
- Protects Protected Health Information (PHI)
- Requires encryption of PHI in transit and at rest
- Access controls, audit logging, risk assessment
- Business Associate Agreements (BAAs) for cloud providers
- Breach notification requirements (60 days)

**IEC 62443 for Medical:**
- Adapted for healthcare environments
- Network segmentation requirements
- Device authentication and authorization

**EU MDR (Medical Device Regulation) + Cyber Resilience Act:**
- CE marking requires cybersecurity assessment
- Post-market surveillance for vulnerabilities
- Incident reporting to authorities

## Key Properties / Complexity

- **Life safety priority**: Availability and integrity often outweigh confidentiality — a cardiac monitor must work even if its data isn't encrypted
- **Legacy device problem**: Hospitals run devices with 15-20 year lifespans running Windows XP or proprietary OS with no update mechanism
- **Clinical workflow tension**: Security measures that slow clinical workflows get bypassed (shared passwords, disabled screensavers, USB data transfer)
- **Regulatory burden**: FDA 510(k) clearance for security patches means updates are slow and expensive
- **Network segmentation critical**: Medical devices on the same network as billing systems creates cross-contamination risk
- **Supply chain risk**: Medical devices use third-party components (libraries, SDKs) with unknown vulnerabilities
- **Physical access**: Hospital devices are in semi-public areas; patients, visitors, and cleaning staff have physical access
- **Radio interference**: Wireless medical devices (Wi-Fi, BLE, proprietary RF) can be jammed or interfered with

## Worked Example

**Insulin pump attack chain:**
1. Researcher reverse-engineers insulin pump firmware (extracted via debug interface)
2. Discovers proprietary RF protocol uses no encryption, no authentication
3. Crafts replay attack: captures legitimate "deliver insulin" command
4. Replays command with modified dosage parameter
5. Pump delivers arbitrary insulin dose without patient confirmation
6. Potential outcome: lethal hypoglycemic episode

**Mitigation:**
- Mutual authentication between pump and controller (unique per-device keys)
- Encryption of all RF commands (AES-128 minimum)
- Dosage limits enforced in hardware (cannot exceed safe maximum regardless of command)
- Physical confirmation required for large dosage changes
- Anomaly detection (alert if unusual delivery pattern detected)

## Common Pitfalls

- Prioritizing patient convenience over security (disabling authentication for faster access)
- Not segmenting medical device networks from general hospital IT
- Using shared login credentials for clinical staff across multiple devices
- Ignoring FDA post-market cybersecurity requirements
- Not having a vulnerability disclosure policy (researchers find bugs but have no one to report to)
- Assuming medical devices are "air-gapped" when they're actually network-connected
- Not updating medical devices due to fear of FDA re-certification

## Connections

- [[industrial-iot-security]] — Both are safety-critical IoT domains
- [[privacy-by-design]] — HIPAA requires privacy-by-design for health data
- [[threat-modeling]] — FDA requires threat modeling for premarket submission
- [[secure-boot-chain]] — Medical devices need firmware integrity verification
- [[ota-updates]] — Critical for patching medical devices post-deployment
- [[risk-assessment-frameworks]] — Healthcare-specific risk assessment
- [[iot-compliance-frameworks]] — FDA, HIPAA, EU MDR compliance
- [[iot-lecture-1]] — Healthcare IoT in the application domain overview

## Open Questions
- How should FDA handle zero-day vulnerabilities in implanted devices that cannot be easily recalled?
- Can blockchain or other distributed systems provide tamper-proof audit logs for medical device access?
- How do we balance the right to security research with patient safety concerns when disclosing medical device vulnerabilities?
