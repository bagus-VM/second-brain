---
title: "Security by Design"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[cia-triad]]", "[[threat-modeling]]"]
---

## One-line Summary
Security by Design means integrating security from the very beginning of system design rather than adding it as an afterthought — a fundamental principle for IoT where retrofitting is often impossible.

## Core Intuition
It's 100x cheaper to fix a security flaw in design than after deployment. In IoT, where devices may be physically inaccessible, resource-constrained, or impossible to patch, getting security right from the start isn't just best practice — it's essential.

## Formal Definition / Statement
**Security by Design:** Integrating security from the very beginning of system design rather than adding it later. In IoT, this means:
- Security requirements are part of initial specifications
- [[threat-modeling|Threat modeling]] informs architectural decisions
- Security testing is integrated into every development phase
- The [[secure-development-lifecycle|SDLC]] includes security gates

**Lowest Common Denominator Approach:** If the security solution fits and works on a sensor or very small (pico) board, it can fit and work on all other devices and subsystems. Trade-off: effectiveness vs. cost.

## Key Properties / Complexity

### Secure Design Goals (from Lecture 4)
1. **Mitigate Automated Attack Risks** — Design to resist unsupervised attacks
2. **Secure Points of Integration** — Security at subsystem boundaries
3. **Protect Confidentiality and Integrity:**
   - Cryptography for data at rest and in motion
   - Data life cycle visibility
   - Secure [[ota-updates|OTA updates]]
4. **Design for Safety** — IoT systems must not cause harm
5. **Hardware Protection:**
   - Secure hardware components ([[physical-unclonable-functions|PUFs]], [[trusted-platform-module|TPM]])
   - Anti-tamper mechanisms
6. **Design for Availability:**
   - Cloud availability, load balancing, equipment failure protection
7. **Design for Resilience:**
   - Anti-jamming, device redundancy, gateway caching/clustering
   - Rate limiting, congestion control
   - Integrity-protected logging
8. **Design for Compliance:**
   - US IoT Cybersecurity Improvement Act 2020
   - ENISA baseline recommendations
   - US DHS guiding principles
   - US FDA medical device guidance

### Hardware Security Options
- **[[physical-unclonable-functions|PUFs]]** — Hardware primitives exploiting manufacturing variations
- **[[trusted-platform-module|TPM]]** — Dedicated security hardware for crypto operations
- **Security Co-processor** — Dedicated hardware for offloading security operations
- **Cryptographic Library** — Software-based crypto algorithms

## Worked Example
**Without Security by Design:** A smart lock ships with default credentials, no firmware update mechanism, and hardcoded encryption keys. After launch, a vulnerability is discovered — but there's no way to patch the lock. All units must be recalled.

**With Security by Design:** The same smart lock is designed with unique-per-device credentials, a secure OTA update mechanism, and key rotation capability. The same vulnerability is discovered — a firmware update is pushed automatically, fixing the issue for all devices.

## Common Pitfalls
- "We'll add security later" — retrofitting is expensive or impossible for deployed IoT
- Treating security as a feature rather than a quality attribute
- Designing security that's too heavy for resource-constrained devices
- Not considering the entire product lifecycle (deployment, operation, disposal)

## Connections
- [[threat-modeling]] — Informs what security to design in
- [[secure-development-lifecycle]] — Process for implementing security by design
- [[physical-unclonable-functions]] — Hardware security primitive
- [[trusted-platform-module]] — Hardware security module
- [[ota-updates]] — Enabling post-deployment security fixes
- [[resilience-iot]] — Designing for resilience
- [[operational-security-lifecycle]] — Security throughout the lifecycle
- [[iot-secure-design]] — Topic page on secure design

- [[iot-lecture-2]] — IoT Common Attacks — taxonomy
- [[iot-lecture-4]] — IoT Secure Design — best practices

## Open Questions
- How do we balance security by design with time-to-market pressure?
- What's the minimum viable security for a resource-constrained IoT device?
- How do we ensure supply chain security in the design phase?
