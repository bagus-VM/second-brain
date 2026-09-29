---
title: "IoT Security - Lecture 8: Compliance, IoT 2.0, and Advanced Threats"
tags: [topic, iot-security, semester-1, compliance, iot-2.0]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-07-01
prerequisites: [iot-identity-lifecycle, privacy-by-design, defense-in-depth]
---

## One-line Summary
IoT security requires ongoing compliance monitoring, periodic risk assessments, and defence-in-depth against increasingly sophisticated threats including governmental-level attacks and the emerging IoT 2.0 ecosystem.

## Core Intuition
Deploying IoT security is not a one-time event — it's a continuous program of monitoring, testing, and remediation. As IoT evolves into IoT 2.0 (integrating 5G/6G, AI/ML, edge computing, blockchain), the attack surface expands and threats become more sophisticated (governmental-level attacks with vast resources). Defence-in-depth is not optional — it's the only viable strategy.

## IoT Compliance Monitoring Program

### Executive Oversight
- **Policies, procedures, documentation**: formal security framework
- **Training and education**:
  - IoT data security
  - IoT privacy
  - Safety procedures for IoT systems
  - IoT-specific security tools (scanners)
  - Cybersecurity tools
  - Data security
  - Defense in depth
  - Privacy
  - IoT, networks, and cloud
  - Threats/attacks
  - Certifications
- **Testing**: regular security testing

### Internal Compliance Monitoring
Continuous cycle:
1. Install/update sensors
2. Automated search for flaws
3. Collect results
4. Triage
5. Bug fixes
6. Progress reports
7. System design updates
8. System implementation

### Periodic Risk Assessments

**Black-box testing** (no internal knowledge):
- Physical security evaluation
- Firmware/software update process analysis
- Interface analysis
- Wireless security evaluation
- Configuration security evaluation
- Mobile application evaluation
- Cloud security analysis (web service security)

**White-box assessments** (full internal knowledge):
- Staff interviews
- Reverse-engineering
- Hardware component analysis
- Code analysis
- System design and configuration documentation reviews
- [[attack-tree]] and [[fault-tree]] analysis

**Fuzz testing**:
- Power-on/power-off sequences/state changes
- Protocol tag/length/value fields
- Header processing
- Data-validation attacks
- Integrate with analyser

**Remediation planning**: examine existing compliance standards, support for IoT

## Governmental-Level Attacks

### Characteristics
- Performed by government/state-level or tech-giant-level agencies
- **Practically impossible to avoid** due to extremely high level of:
  - Resources
  - Time
  - Effort
- Becoming more frequent
- Will significantly affect IoT
- **[[resilience-iot]] and prevention measures required**

### Implications
- No single defense is sufficient
- Defence-in-depth is mandatory
- Assume breach, design for resilience
- Regular updates and patching critical

## IoT 2.0

### Definition
A concept connecting IoT to other innovative technologies:
- **5G/6G**: faster, lower-latency connectivity
- **Machine learning and AI**: intelligent decision-making at edge
- **Edge computing**: processing closer to data source
- **Industry 4.0/5.0**: smart manufacturing
- **Blockchain**: decentralized trust, smart contracts
- **Post-CMOS technologies**: new hardware paradigms
- **User-friendliness, sustainability, interoperability, scalability, security**

### Architecture Evolution

**Conventional IoT Architecture:**
- Traditional layered model
- Device → Gateway → Cloud
- Centralized processing

**Recent Layered IoT Architectures:**
- More layers, more abstraction
- Edge/fog computing layers
- AI/ML integration layers
- Blockchain layers for trust

### Key Challenges
- **Scalability**: billions of devices
- **Interoperability**: diverse protocols, standards
- **Security**: expanded attack surface
- **Privacy**: more data collection points

## Device Compromise Attack Example
(Zhou et al. 2021)

Shows how a single compromised device can cascade through the network, emphasizing need for:
- Device authentication
- Network segmentation
- Continuous monitoring
- Rapid incident response

## Defence-in-Depth Approach
Multiple layers of security:
1. **Physical security**: tamper resistance
2. **Device security**: secure boot, firmware signing
3. **Network security**: encryption, segmentation
4. **Application security**: input validation, secure coding
5. **Cloud security**: access control, monitoring
6. **Data security**: encryption at rest and in transit
7. **Operational security**: patching, monitoring, incident response

No single layer is sufficient — attacker must breach all layers to succeed.

## Key Properties
- **Continuous monitoring**: security is not a one-time deployment
- **Multiple assessment types**: black-box, white-box, fuzz testing
- **Governmental threats**: require resilience, not just prevention
- **IoT 2.0**: expanded ecosystem with new technologies and new risks
- **Defence-in-depth**: multiple layers, no single point of failure

## Common Pitfalls
- Thinking security is "done" after initial deployment — it's continuous
- Relying on single defense mechanism — attacker only needs to breach one layer
- Underestimating governmental-level attackers — they have vast resources
- Ignoring compliance monitoring — regulations require ongoing proof
- Treating IoT 2.0 as just "more devices" — it's fundamentally new architectures and threat models
- Confusing black-box (no internal knowledge) with white-box (full knowledge) testing

## Connections
- [[iot-identity-lifecycle]] — identity management is part of compliance
- [[privacy-by-design]] — privacy is a compliance requirement
- [[defense-in-depth]] — core strategy against sophisticated attacks
- [[attack-tree]] — white-box assessments include attack tree analysis
- [[fault-tree]] — white-box assessments include fault tree analysis
- [[threat-modeling]] — risk assessments are a continuous threat modeling practice
- [[resilience-iot]] — governmental attacks demand resilience, not just prevention
- [[security-by-design]] — defence-in-depth and compliance are security-by-design principles
- [[secure-development-lifecycle]] — compliance monitoring integrates with the SDLC
- [[operational-security-lifecycle]] — internal monitoring maps to define/implement/operate/dispose
- [[iot-compliance-frameworks]] — compliance monitoring targets framework requirements
- [[iot-2.0]] — IoT 2.0 concept page (deeper treatment of IoT 2.0)
- [[mirai-botnet]] — canonical example of large-scale device compromise cascading
- [[zero-trust-architecture]] — no single trust domain; defence-in-depth aligns with zero trust
- [[iot-security-overview]] — broader course context
- [[pki]] — PKI is part of IoT identity and compliance
- [[gdpr-compliance]] — GDPR requires ongoing compliance monitoring
- [[information-assurance]] — compliance monitoring is a form of information assurance

## Open Questions
- How do small IoT manufacturers implement formal compliance programs?
- What specific resilience measures work against governmental-level attacks?
- How does blockchain actually improve IoT 2.0 security (beyond the hype)?
- What are the practical limits of fuzz testing for IoT protocols?
