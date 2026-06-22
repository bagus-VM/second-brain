---
title: "Security Principles"
tags: [concept, iot-security, fundamentals, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
*The foundational principles that guide all security design decisions: defense in depth, least privilege, fail secure, and separation of duties.*

## Core Intuition
Before you learn any specific technology or standard, you need to internalize the principles that underlie all of them. These principles are timeless — they applied to castle defense in medieval times and they apply to IoT device security today. When you're designing a system and face a tradeoff, these principles tell you which way to lean. They're the equivalent of 'first principles' in physics.

## Formal Definition / Statement
Core security principles applicable to IoT:

1. **Defense in Depth** — Multiple layers of security controls. If one layer fails, others provide protection. Example: encrypted communication + authenticated access + firmware integrity + network segmentation.

2. **Principle of Least Privilege (PoLP)** — Every component, user, and process should have only the minimum access rights needed to perform its function. Example: a temperature sensor doesn't need access to the camera feed.

3. **Fail Secure (Fail Safe)** — When a system fails, it should default to a secure state. Example: if an IoT lock loses connectivity, it should remain locked (not unlock).

4. **Separation of Duties** — Critical operations require multiple parties to authorize. Example: firmware updates require both a signing key AND an authorized deployment server.

5. **Economy of Mechanism** — Keep security mechanisms as simple as possible. Complex systems have more vulnerabilities. Example: use TLS rather than inventing a custom encryption protocol.

6. **Complete Mediation** — Every access to every resource must be checked for authorization. Don't cache authentication decisions.

7. **Open Design** — Security should not depend on the secrecy of the design (Kerckhoffs's principle). Only keys should be secret, not algorithms.

8. **Psychological Acceptability** — Security mechanisms should not make the system harder to use than without them. If security is too burdensome, users will bypass it.

9. **Least Common Mechanism** — Minimize shared resources between users/processes to prevent information leakage.

10. **Security by Default** — Systems should be secure out of the box. Insecure features should require explicit opt-in.

## Key Properties / Complexity
- These principles originated from Saltzer and Schroeder (1975) and have been refined over decades
- No single principle is sufficient; they work together
- IoT-specific tensions: defense in depth vs resource constraints, fail secure vs fail safe (safety systems)
- Principles are design guidance, not implementation specifications
- Tradeoffs exist: complete mediation has performance cost, separation of duties adds complexity
- Regulatory frameworks (IEC 62443, ETSI) encode these principles as specific requirements

## Worked Example
Designing a smart door lock using security principles:
- **Defense in depth**: BLE authentication + physical key backup + tamper alarm + firmware signing
- **Least privilege**: The lock's BLE service can only lock/unlock, not access Wi-Fi credentials or user data
- **Fail secure**: If the lock loses power or connectivity, the deadbolt stays locked
- **Separation of duties**: Firmware updates require both manufacturer signing key AND user confirmation on the app
- **Economy of mechanism**: Use standard BLE pairing with Secure Connections, not a custom protocol
- **Security by default**: Lock ships with auto-lock enabled, BLE discoverability disabled, and a unique pairing code
- **Psychological acceptability**: Users can unlock with a tap on their phone — security doesn't add friction to normal use

## Common Pitfalls
- **Principle conflicts**: Fail secure vs fail safe — a nuclear plant should fail safe (shut down safely), not fail secure (keep running).
- **Over-application**: Applying least privilege too strictly can make systems unusable. A smart home hub needs access to multiple device types.
- **Principle ≠ implementation**: Knowing the principles doesn't mean you can implement them correctly. 'Use defense in depth' doesn't tell you which layers to add.
- **Context-dependent**: The right balance of principles depends on the threat model. A toy camera needs different tradeoffs than a medical device.

## Connections
- [[principle-of-least-privilege]] — Detailed treatment of PoLP specifically
- [[zero-trust-architecture]] — Zero trust is an implementation of defense in depth + complete mediation
- [[threat-modeling]] — Threat models determine which principles to prioritize
- [[iot-device-fundamentals]] — Resource constraints affect which principles are practical
- [[privacy-by-design]] — Privacy principles parallel and complement security principles
- [[iec-62443]] — Industrial security standard that encodes these principles into requirements

## Open Questions
- How does this standard/framework apply to resource-constrained IoT devices with limited processing power?
- What are the practical tradeoffs between compliance and actual security improvement?
