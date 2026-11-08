---
title: "IoT Compliance Frameworks"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[security-by-design]]", "[[operational-security-lifecycle]]"]
---

## One-line Summary
IoT compliance frameworks — including the US IoT Cybersecurity Improvement Act, ENISA recommendations, DHS principles, and FDA guidance — establish regulatory requirements and best practices for IoT security.

## Core Intuition
Self-regulation hasn't worked in IoT security. Governments and agencies have stepped in with frameworks that define minimum security requirements. Understanding these is essential because compliance is increasingly a prerequisite for market access.

## Formal Definition / Statement
Key IoT compliance frameworks:

1. **US IoT Cybersecurity Improvement Act of 2020** — Federal law requiring minimum security standards for IoT devices used by US federal agencies. Covers vulnerability management, patch management, and configuration management.

2. **ENISA Baseline Security Recommendations** — European Union Agency for Cybersecurity guidelines providing baseline security recommendations for IoT. Covers secure development, deployment, and operation.

3. **US DHS Guiding Principles for Secure IoT** — Department of Homeland Security principles for securing IoT across critical infrastructure sectors.

4. **US FDA Guidance on IoT Medical Devices** — Food and Drug Administration specific guidance for cybersecurity in medical IoT devices, including pre-market and post-market requirements.

## Key Properties / Complexity

### Common Requirements Across Frameworks
- Secure development practices
- Vulnerability disclosure and management
- Authentication and access control
- Data protection (encryption at rest and in transit)
- Patch/update mechanisms
- Logging and monitoring

### Design for Compliance
Compliance should be designed in from the start — it's a secure design goal (Lecture 4). Retrofitting compliance is expensive and may require architectural changes.

### Challenges
- **Fragmentation:** Different countries, different rules
- **Evolution:** Regulations are still evolving
- **Enforcement:** Varies by jurisdiction and sector
- **Overlap:** Multiple frameworks may apply to a single device

## Worked Example
**Medical IoT Device Compliance:**
1. Design phase: FDA pre-market guidance informs threat model
2. Development: ENISA baseline security recommendations applied
3. US government deployment: IoT Cybersecurity Improvement Act requirements verified
4. Post-market: FDA post-market surveillance requirements for vulnerability monitoring
5. European market: ENISA recommendations for ongoing operation

## Common Pitfalls
- Treating compliance as a checkbox exercise rather than a security practice
- Not tracking regulatory changes across jurisdictions
- Assuming compliance equals security — frameworks set minimums, not optimal security
- Ignoring sector-specific requirements (medical, automotive, industrial)

## Connections
- [[security-by-design]] — Compliance is a design goal
- [[operational-security-lifecycle]] — Compliance requirements span the lifecycle
- [[iot-compliance-frameworks]] — connects to [[resilience-iot]] for operational requirements
- [[ota-updates]] — Required for compliance with patch management requirements

## Open Questions
- Will there be a global IoT security standard?
- How do we balance innovation with regulatory compliance?
- What happens when devices outlive the manufacturer's compliance?
