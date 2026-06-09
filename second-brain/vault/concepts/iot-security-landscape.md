---
title: "IoT Security Landscape"
tags: [concept, iot-security, overview, semester-1]
course: "IoT Security"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*A comprehensive overview of the IoT security domain spanning device fundamentals, communication protocols, applications, information assurance, and attack surfaces.*

## Core Intuition
IoT security isn't a single discipline — it's the intersection of embedded systems, network security, software engineering, hardware trust, and operational policy. The landscape is defined by the tension between constrained devices (limited CPU, memory, power) and the expansive attack surface created when billions of such devices connect to the internet.

## Formal Definition / Statement
The IoT Security Landscape encompasses five interdependent domains:

1. **IoT Fundamentals** — Device architectures ([[iot-device-fundamentals]]), communication protocols ([[iot-communication-protocols]]), and network architecture ([[iot-network-architecture]]). Devices classified by capability (constrained vs unconstrained).

2. **IoT Applications** — Real-world deployments defining threat models: smart homes, industrial IoT, healthcare (IoMT), smart cities, agriculture, wearables. Each domain introduces unique regulatory and safety requirements.

3. **Information Assurance for IoT** — The [[cia-triad]] adapted for IoT: confidentiality (encryption on constrained devices), integrity ([[firmware-security]]), availability (resilience to DoS). Extends to authentication, non-repudiation, and privacy ([[privacy-by-design]]).

4. **DevOps and Secure Design** — [[secure-development-lifecycle]] applied to IoT: threat modeling, secure coding, CI/CD with static analysis, firmware signing, [[ota-updates]], incident response.

5. **Attack Surfaces** — Systematic enumeration of attack vectors. Miessler's 15 attack surface classes cover physical interfaces, device memory, cloud APIs, and ecosystem communications.

## Key Properties / Complexity
- Scale: billions of devices, many unmanaged and never patched
- Heterogeneity: no single OS, protocol, or architecture dominates
- Resource constraints: kilobytes of RAM rule out traditional security tooling
- Long lifecycles: industrial devices may operate 10–20 years
- Supply chain risk: opaque firmware histories, hardware trojans
- IT/OT convergence: historically air-gapped OT networks now connect to enterprise IT
- Regulatory fragmentation: EU CRA, US IoT labeling, sector-specific mandates

## Worked Example
Mapping the landscape for a healthcare IoT deployment:
- **Fundamentals**: BLE-connected patient monitors, MQTT to gateway, Wi-Fi to cloud
- **Application**: IoMT domain — patient safety critical, HIPAA regulated
- **Assurance**: Encrypted BLE, signed firmware, availability for patient monitoring
- **Secure Design**: FDA pre-market guidance, IEC 62443 for network segmentation
- **Attack Surface**: Physical (hospital access), network (shared hospital Wi-Fi), cloud (patient data API)

## Common Pitfalls
- **Scope creep**: The landscape is vast; trying to address everything at once leads to addressing nothing well
- **Moving target**: New protocols, devices, and attacks emerge constantly
- **Disciplinary silos**: Hardware, network, and software teams often don't communicate about security
- **Compliance ≠ security**: Meeting regulatory requirements doesn't guarantee security

## Connections
- [[iot-device-fundamentals]], [[iot-communication-protocols]], [[iot-network-architecture]] — Foundation layer
- [[iot-common-attacks]], [[iot-attack-taxonomy]] — Threat landscape
- [[iot-secure-design]], [[iot-compliance-frameworks]] — Defense landscape
- [[information-assurance]], [[cia-triad]] — Security principles adapted for IoT
- [[risk-assessment-frameworks]] — Prioritizing within the landscape

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
