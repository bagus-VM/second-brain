---
title: "IoT Security Overview"
tags: [concept, iot-security, semester-1, security]
course: "IoT Security"
source_count: 0
status: current
last_updated: 2026-07-02
prerequisites: []
---

## One-line Summary
IoT security spans the full lifecycle of connected devices — from threat modeling and secure design to identity management, communication protocols, compliance, and advanced threats including governmental attacks.

## Core Intuition
IoT devices are everywhere — sensors, cameras, medical devices, industrial controllers — and they're often the weakest link in security. Unlike traditional IT, IoT devices are resource-constrained, deployed in physically accessible locations, and expected to run for years without updates. Security must be designed in from the start, not bolted on after. The core strategy is [[defense-in-depth]]: multiple layers of protection so that no single failure is catastrophic.

## Formal Definition / Statement
**Scope of IoT Security (across all 8 lectures):**

1. **Threat Modeling**: Systematic identification of threats, attack surfaces, and risk ([[iot-attack-taxonomy]])
2. **Secure Design**: Building security into architecture from the ground up ([[security-by-design]])
3. **Privacy by Design**: Embedding data protection into system design ([[privacy-by-design]])
4. **Identity and Access Management**: Device identity, authentication, authorization ([[iot-identity-lifecycle]])
5. **Communication Security**: Securing data in transit across IoT protocols ([[iot-communication-protocols]])
6. **Compliance**: Meeting regulatory requirements ([[gdpr-compliance]])
7. **Advanced Threats**: Nation-state attacks, supply chain risks, AI-powered attacks ([[iot-lecture-8]])
8. **IoT 2.0 Ecosystem**: 5G, AI/ML, edge computing, blockchain integration ([[iot-lecture-8]])

## Key Properties / Complexity
- **Defense-in-depth**: Multiple security layers; no single point of failure ([[defense-in-depth]])
- **Resource constraints**: IoT devices have limited CPU, memory, and power
- **Long lifecycles**: Devices may run 10-20 years, far outlasting their security support
- **Physical exposure**: Devices often in publicly accessible locations
- **Scale**: Millions of devices, each a potential attack vector
- **Heterogeneity**: Diverse protocols, operating systems, and hardware

## Worked Example
**IoT Smart Home Attack Chain:**

1. **Reconnaissance**: Attacker scans for exposed IoT devices (Shodan)
2. **Initial Access**: Exploits default credentials on IP camera
3. **Lateral Movement**: Camera on same network as smart lock → pivot to lock
4. **Privilege Escalation**: Lock firmware has known vulnerability → root access
5. **Impact**: Physical security compromised (door unlocked remotely)

**Defence-in-depth countermeasures:**
- Network segmentation (camera on separate VLAN)
- Strong authentication (no default passwords)
- Firmware update mechanism (patch lock vulnerability)
- Intrusion detection (detect unusual device behavior)
- Physical tamper detection on devices

## Common Pitfalls
- **Security by obscurity**: Relying on secrecy rather than proven mechanisms
- **Ignoring physical security**: IoT devices can be physically tampered with
- **Default credentials**: Many breaches come from unchanged factory defaults
- **No update mechanism**: Devices that can't be patched become permanent vulnerabilities
- **Compliance ≠ security**: Meeting GDPR doesn't mean a system is secure

## Connections
- [[iot-lecture-1]] — introduction to IoT landscape and security challenges
- [[iot-lecture-8]] — advanced threats, governmental attacks, IoT 2.0 ecosystem
- [[iot-attack-taxonomy]] — systematic classification of IoT threats
- [[security-by-design]] — building security into architecture from the start
- [[privacy-by-design]] — embedding data protection into system design
- [[defense-in-depth]] — layered security strategy as the core approach
- [[gdpr-compliance]] — regulatory requirements for IoT data handling
- [[iot-identity-lifecycle]] — managing device identities from provisioning to decommissioning
- [[iot-communication-protocols]] — securing MQTT, CoAP, and other IoT protocols

## Open Questions
- (Overview page — no open questions; see individual lecture pages for topic-specific questions)
