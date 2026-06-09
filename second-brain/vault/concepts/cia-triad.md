---
title: "CIA Triad"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: []
---

## One-line Summary
The CIA Triad — Confidentiality, Integrity, Availability — is the foundational model of information security, extended in IoT to include Authentication, Non-repudiation, Resilience, and Safety.

## Core Intuition
Every security concern can be mapped to one of three questions: Is the data secret (Confidentiality)? Is the data correct (Integrity)? Is the data/system accessible (Availability)? In IoT, we extend this with: Who sent it (Authentication)? Can they deny it (Non-repudiation)? Can we keep going under attack (Resilience)? Will people get hurt (Safety)?

## Formal Definition / Statement
The CIA Triad defines the three core properties of information assurance:

1. **Confidentiality** — Keeping sensitive information secret and protected from disclosure
2. **Integrity** — Ensuring that information is not modified, accidentally or purposefully, without being detected
3. **Availability** — Ensuring that information and capabilities are available when needed

### IoT Extensions (Information Assurance)
4. **Authentication** — Ensuring that the source of data is from a known identity or endpoint (generally follows identification)
5. **Non-repudiation** — Ensuring that an individual or system cannot later deny having performed an action
6. **Resilience** — Maintaining state awareness and an accepted level of operational normalcy in response to disturbances, including threats of an unexpected and malicious nature
7. **Safety** — Not being in threat of undergoing or causing hurt, injury, or loss

## Key Properties / Complexity

### Interdependencies
- Increasing confidentiality (encryption) can decrease availability (if keys are lost)
- Integrity checks add overhead, potentially affecting availability
- Authentication adds latency, affecting real-time availability
- In IoT, these trade-offs are amplified by resource constraints

### IoT-Specific Challenges
- **Confidentiality:** Resource-constrained devices may not support strong encryption
- **Integrity:** Firmware and OTA updates must be integrity-protected
- **Availability:** IoT devices in critical infrastructure must resist DoS
- **Authentication:** Devices need to authenticate to networks before sending data
- **Safety:** IoT controls physical systems — a security breach can cause physical harm

## Worked Example
**Mirai Botnet attack on CIA:**
- **Availability:** DDoS attacks took down DNS infrastructure
- **Confidentiality:** Default passwords meant device credentials were effectively public
- **Integrity:** Compromised devices ran unauthorized software

**KRACK Attack on CIA:**
- **Confidentiality:** Key reinstallation could allow decryption of Wi-Fi traffic
- **Integrity:** Attacker could potentially inject packets

## Common Pitfalls
- Treating CIA as a checklist rather than a balancing act
- Forgetting the IoT extensions (authentication, non-repudiation, resilience, safety)
- Ignoring that safety is critical when IoT controls physical systems
- Assuming traditional IT security solutions map directly to resource-constrained IoT devices

## Connections
- [[information-assurance]] — Extended framework beyond CIA
- [[resilience-iot]] — Resilience as an extended security property
- [[security-by-design]] — Building CIA into systems from the start
- [[iot-attack-taxonomy]] — Attacks classified by which CIA property they violate
- [[mirai-botnet]] — Attack violating all three CIA properties
- [[krack-attack]] — Attack violating confidentiality and integrity
- [[denial-of-service]] — Attack on availability

## Open Questions
- How do we quantify the trade-offs between CIA properties in resource-constrained IoT?
- Should safety be considered a fourth pillar alongside CIA in IoT contexts?
