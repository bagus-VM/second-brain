---
title: "Resilience in IoT"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[cia-triad]]", "[[security-by-design]]"]
---

## One-line Summary
Resilience in IoT means maintaining state awareness and an accepted level of operational normalcy in response to disturbances, including unexpected and malicious threats — implemented through anticipate, withstand, recover, and evolve.

## Core Intuition
Prevention alone isn't enough — attackers will get through. Resilience assumes breaches happen and focuses on maintaining operations despite them. In IoT, where devices control physical systems, resilience can be the difference between a minor disruption and a catastrophe.

## Formal Definition / Statement
**Resilience:** Maintaining state awareness and an accepted level of operational normalcy in response to disturbances, including threats of an unexpected and malicious nature.

### Four Pillars
1. **Anticipate** — Proactively identify and prepare for potential threats
2. **Withstand** — Maintain operations during a threat event
3. **Recover** — Restore normal operations after a disruption
4. **Evolve** — Learn and improve from incidents

## Key Properties / Complexity

### Design for Resilience (Lecture 4)
- **Protecting against jamming attacks** — Frequency hopping, redundant communication
- **Device redundancy** — Backup devices for critical functions
- **Gateway caching** — Local data caching when cloud is unreachable
- **Digital configurations** — Ability to restore device configurations
- **Gateway clustering** — Multiple gateways for fault tolerance
- **Rate limiting** — Preventing resource exhaustion
- **Congestion control** — Managing network traffic under attack
- **Flexible policy and security management** — Administrator controls
- **Logging mechanisms** — Integrity-protected logs fed to cloud for safe storage

### Relationship to CIA
- Resilience extends **Availability** — not just "is it available?" but "can it stay available under attack?"
- Also supports **Integrity** — logging and monitoring detect integrity violations

## Worked Example
**Resilient Smart Grid:**
1. **Anticipate:** Threat intelligence indicates increased attacks on power grid IoT
2. **Withstand:** DDoS attack on grid sensors → gateway caching provides last-known data, rate limiting prevents resource exhaustion, redundant sensors continue operating
3. **Recover:** Attack subsides → cached data reconciled with live data, compromised sensors isolated and re-flashed
4. **Evolve:** Post-incident analysis → new detection rules added, sensor firmware updated with anti-DDoS measures

## Common Pitfalls
- Confusing resilience with availability — resilience is about maintaining operations under attack, not just uptime
- Not testing resilience — you don't know if you're resilient until you test under stress
- Designing resilience only for cyber threats — natural disasters, hardware failures, and human errors also matter
- Ignoring the "evolve" pillar — incidents without learning are wasted

## Connections
- [[cia-triad]] — Resilience extends the Availability property
- [[information-assurance]] — Resilience is one of the seven IA properties
- [[security-by-design]] — Resilience must be designed in
- [[operational-security-lifecycle]] — Resilience is an operational concern
- [[iot-secure-design]] — Topic page on secure design goals
- [[ota-updates]] — Enables recovery through patching

## Open Questions
- How do we measure resilience quantitatively?
- What level of resilience is "good enough" for non-critical IoT?
- How do we test resilience without disrupting production systems?
