---
title: "Information Assurance"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[cia-triad]]"]
---

## One-line Summary
Information Assurance extends the CIA Triad with Authentication, Non-repudiation, Resilience, and Safety to form a comprehensive framework for evaluating security in IoT systems.

## Core Intuition
CIA alone isn't enough for IoT. When devices control physical things (cars, medical devices, power grids), we also need to know who sent a command (Authentication), prevent denial of actions (Non-repudiation), survive attacks (Resilience), and prevent harm (Safety).

## Formal Definition / Statement
Information Assurance encompasses seven properties:
1. **Confidentiality** — Protection from unauthorized disclosure
2. **Integrity** — Detection of unauthorized modification
3. **Availability** — Access when needed
4. **Authentication** — Verified identity of data source
5. **Non-repudiation** — Inability to deny having performed an action
6. **Resilience** — Maintaining operational normalcy under disturbance
7. **Safety** — Protection from hurt, injury, or loss

## Key Properties / Complexity

### Authentication in IoT
- Devices must authenticate to the network before collecting or sending data
- Software running on devices must be authorized and authenticated
- Challenge: resource-constrained devices can't always run heavy auth protocols

### Non-repudiation in IoT
- Critical for audit trails in industrial IoT
- Requires cryptographic signatures, which need key management infrastructure
- Challenge: maintaining time-synchronized logs across distributed devices

### Resilience in IoT
Four pillars: **Anticipate → Withstand → Recover → Evolve**
- Anticipate: Proactively identify and prepare for threats
- Withstand: Maintain operations during a threat event
- Recover: Restore normal operations after disruption
- Evolve: Learn and improve from incidents

Implementation: device redundancy, gateway caching/clustering, rate limiting, congestion control, integrity-protected logging, flexible policy management

### Safety in IoT
- Unique to IoT/cyber-physical systems
- A security breach can cause physical harm (car crashes, medical device failures, power grid explosions)
- Safety analysis uses [[fault-tree|fault trees]] and hazard analysis

## Worked Example
**Industrial IoT Safety Failure:** A compromised sensor in a chemical plant reports false temperature readings (Integrity violation). The processing system doesn't detect the tampering (Authentication failure). The cooling system is not activated, leading to overheating (Safety violation). The attacker denies sending the false data (Non-repudiation failure).

## Common Pitfalls
- Treating Information Assurance as just "CIA plus some extras" — the extensions are critical in IoT
- Ignoring safety when IoT controls physical systems
- Not designing for resilience from the start
- Confusing authentication with authorization

## Connections
- [[cia-triad]] — Foundation of Information Assurance
- [[resilience-iot]] — Deep dive into the resilience pillar
- [[threat-modeling]] — Using IA properties to categorize threats
- [[iot-attack-taxonomy]] — Attacks classified by IA property violated
- [[security-by-design]] — Building all IA properties into design
- [[operational-security-lifecycle]] — Maintaining IA throughout operations

- [[iot-lecture-1]] — IoT Security Landscape — course overview
- [[iot-lecture-2]] — IoT Common Attacks — taxonomy
- [[iot-lecture-4]] — IoT Secure Design — best practices

## Open Questions
- How do we measure resilience quantitatively?
- Should safety certification be mandatory for all IoT devices?
- How do the seven properties scale across a system of systems?
