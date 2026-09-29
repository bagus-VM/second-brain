---
title: "IoT Security Landscape"
tags: [topic, iot-security, semester-1]
course: "IoT Security"
source_count: 5
status: current
last_updated: 2026-06-02
prerequisites: ["[[networking-fundamentals]]", "[[security-principles]]"]
---

## One-line Summary
A comprehensive overview of the IoT security domain spanning fundamentals, applications, [[information-assurance]], secure design practices, and attack surfaces across five core lecture areas.

## Core Intuition
IoT security is not a single discipline — it sits at the intersection of embedded systems, network security, software engineering, hardware trust, and operational policy. The landscape is defined by the tension between constrained devices (limited CPU, memory, power) and the expansive attack surface created when billions of such devices connect to the internet. Understanding the full picture requires mapping how each lecture area — from device fundamentals to attack surface taxonomy — contributes a piece of the puzzle.

## Formal Definition / Statement
The IoT Security Landscape encompasses five interdependent lecture domains:

1. **IoT Fundamentals** — The architecture of IoT systems: [[iot-device-fundamentals]], and communication protocols ([[iot-communication-protocols]]). Devices are classified by capability (constrained vs. unconstrained), and the [[iot-network-architecture]] (perception, network, application) provides the structural model.

2. **IoT Applications** — Real-world deployments that define threat models: smart homes, industrial IoT (IIoT), healthcare (IoMT), smart cities, agriculture, and wearables. Each domain introduces unique regulatory and safety requirements that shape security priorities (e.g., patient safety in IoMT, grid stability in energy).

3. **Information Assurance for IoT** — The [[cia-triad]] adapted for IoT: confidentiality (encryption on constrained devices), integrity (firmware signing, [[firmware-security]]), availability (resilience to DoS/jamming). Extends to authentication (device identity), non-repudiation (audit logs), and privacy (data minimization, [[privacy-by-design]] compliance). Risk assessment frameworks ([[risk-assessment-frameworks]]) guide prioritization.

4. **DevOps and Secure Design** — [[secure-development-lifecycle]] (SDL) applied to IoT: threat modeling during design, secure coding for embedded C/Rust, CI/CD pipelines with static analysis, firmware signing in build systems, and operational security post-deployment including [[ota-updates]] mechanisms and incident response.

5. **Attack Surfaces** — Systematic enumeration of where IoT systems can be attacked. Miessler's 15 attack surface classes (DefCon 2023) provide the canonical taxonomy, covering everything from physical interfaces and device memory to cloud APIs and ecosystem communications.

## Key Properties / Complexity

- **Scale**: Billions of devices, many unmanaged and never patched, create a massive aggregate attack surface.
- **Heterogeneity**: No single OS, protocol, or architecture dominates — security solutions must be adaptable.
- **Resource Constraints**: Many devices run on microcontrollers with kilobytes of RAM, ruling out traditional security tooling (no antivirus, limited TLS).
- **Long Lifecycles**: Industrial IoT devices may operate for 10–20 years, far exceeding typical software support windows.
- **Supply Chain Risk**: Components sourced globally with opaque firmware histories; hardware trojans and backdoors are real threats.
- **Convergence of IT/OT**: Operational technology networks (historically air-gapped) now connect to enterprise IT, exposing legacy protocols.
- **Regulatory Fragmentation**: EU Cyber Resilience Act, US IoT labeling, sector-specific mandates (HIPAA, NERC CIP) create compliance complexity.

## Connections

### Foundational Concepts
- [[iot-device-fundamentals]] — Hardware architectures, constrained vs. unconstrained devices, RTOS vs. Linux
- [[iot-communication-protocols]] — MQTT, CoAP, Zigbee, BLE, LoRaWAN, Thread/Matter
- [[iot-network-architecture]] — Three-tier model, fog/edge computing, gateway patterns
- [[iot-data-lifecycle]] — Collection, transmission, storage, processing, retention

### Application Domains
- [[smart-home-security]] — Consumer IoT threat models, voice assistants, hubs
- [[industrial-iot-security]] — SCADA, Modbus, OPC-UA, safety-critical systems
- [[healthcare-iot-security]] — IoMT devices, FDA guidance, patient safety
- [[smart-city-infrastructure]] — Traffic, utilities, surveillance, public safety

### Security Principles
- [[information-assurance]] — CIA triad, authentication, non-repudiation adapted for IoT
- [[risk-assessment-frameworks]] — NIST IR 8259, ENISA guidelines, IEC 62443
- [[privacy-by-design]] — Data minimization, consent, anonymization in sensor networks

### Design & Operations
- [[iot-lecture-4]] — Design goals and best practices for resilient IoT systems
- [[devops-security]] — Secure CI/CD for firmware, infrastructure as code
- [[operational-security-lifecycle]] — Post-deployment monitoring, patching, decommissioning

### Attack Knowledge
- [[iot-lecture-2]] — Taxonomy of attack types across all IoT layers
- [[iot-lecture-3]] — Miessler's 15 attack surface classes
- [[mirai-botnet]] — Case study in large-scale IoT compromise
- [[krack-attack]] — WPA2 key reinstallation attack affecting IoT Wi-Fi

### Hardware Trust
- [[iot-lecture-5]] — PUFs, TPMs, and security co-processors
- [[firmware-security]] — Secure boot, firmware signing, update integrity
- [[physical-unclonable-functions]] — Hardware-based device identity

## Open Questions
- How can security be standardized across the fragmented IoT ecosystem without stifling innovation?
- What lightweight cryptographic protocols will remain viable as quantum computing matures?
- Can zero-trust architectures be meaningfully applied to resource-constrained IoT networks?
- How should liability be assigned when an IoT device is compromised and causes physical harm?
- What role will AI-driven autonomous threat detection play in managing IoT fleet security at scale?
