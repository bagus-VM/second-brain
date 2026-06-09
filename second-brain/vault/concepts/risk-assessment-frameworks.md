---
title: "Risk Assessment Frameworks for IoT"
tags: [concept, iot-security, risk-management, standards, semester-1]
course: "IoT Security"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: []
---

## One-line Summary
*Structured methodologies for identifying, analyzing, and evaluating security risks specific to IoT systems and devices.*

## Core Intuition
You can't secure everything equally — you need to prioritize. Risk assessment frameworks provide the structure to identify what could go wrong, how likely it is, how bad it would be, and where to invest limited security resources. For IoT, this means considering not just data breaches but physical safety, supply chain risks, and the unique constraints of constrained devices. The framework you choose determines what risks you see and what you miss.

## Formal Definition / Statement
Several frameworks apply to IoT risk assessment:

**NIST Cybersecurity Framework (CSF) 2.0**
- Five functions: Identify, Protect, Detect, Respond, Recover (+ Govern)
- Risk assessment is part of the 'Identify' function
- Provides a common language for communicating risk
- Voluntary but widely adopted

**NISTIR 8259 (IoT-specific)**
- IoT device cybersecurity baseline
- Risk-informed: capabilities should match the device's risk profile
- Focuses on manufacturer responsibilities

**ENISA IoT Risk Assessment**
- European Union Agency for Cybersecurity guidance
- Asset-threat-vulnerability model specific to IoT
- Considers physical, network, application, and lifecycle threats

**IEC 62443-3-2**
- Industrial IoT-specific risk assessment
- Zone and conduit model for network segmentation
- Defines target Security Levels based on risk

**ISO 27005**
- General information security risk management
- Can be applied to IoT with appropriate threat catalogs

**OCTAVE (Operationally Critical Threat, Asset, and Vulnerability Evaluation)**
- Carnegie Mellon / CERT
- Asset-centric approach, considers organizational context

**Process:**
1. Asset identification (what needs protection)
2. Threat identification (what could attack it)
3. Vulnerability identification (what weaknesses exist)
4. Impact analysis (consequences of successful attack)
5. Likelihood analysis (probability of attack)
6. Risk determination (risk = impact × likelihood)
7. Risk treatment (accept, mitigate, transfer, avoid)

## Key Properties / Complexity
- Risk = Likelihood × Impact (most frameworks use this formula)
- IoT-specific considerations: physical access, long lifecycles, constrained resources, supply chain
- Quantitative methods assign monetary values; qualitative methods use high/medium/low
- Risk assessment should be iterative, not one-time
- Threat catalogs for IoT are less mature than for IT systems
- Safety-critical IoT (medical, industrial) requires higher rigor than consumer IoT

## Worked Example
A hospital assesses risk for a new IoT infusion pump:
1. **Assets**: Patient health data, pump control commands, firmware, network credentials
2. **Threats**: Unauthorized pump control (patient safety), data exfiltration (HIPAA), ransomware (availability)
3. **Vulnerabilities**: Default credentials, unencrypted BLE communication, no firmware integrity check
4. **Impact**: Critical — unauthorized pump control could cause patient harm or death
5. **Likelihood**: Medium — BLE requires proximity, but hospital networks are accessible to insiders
6. **Risk**: Critical × Medium = High Risk — requires immediate mitigation
7. **Treatment**: Implement mutual authentication, encrypt BLE, add firmware signing, deploy network segmentation (IEC 62443 zones)
8. **Residual risk**: After mitigation, risk is reduced to Low — accepted by the hospital CISO

## Common Pitfalls
- **Checkbox mentality**: Treating risk assessment as a compliance exercise rather than a genuine security activity.
- **Ignoring IoT-specific threats**: Applying generic IT risk frameworks without considering physical access, firmware tampering, or supply chain risks.
- **Static assessment**: Performing risk assessment once at deployment and never updating it as threats evolve.
- **Over-reliance on likelihood**: Rare but catastrophic events (nation-state attacks on critical infrastructure) may be underestimated.
- **Supply chain blind spot**: Most frameworks don't adequately address risks from third-party components, libraries, and manufacturing.

## Connections
- [[common-criteria]] — CC evaluation results inform risk acceptance decisions
- [[iec-62443]] — 3-2 provides the standard risk assessment methodology for industrial IoT
- [[nist-iot-cybersecurity]] — NISTIR 8259 risk-informed approach to device capabilities
- [[etsi-en-303-645]] — ETSI provisions are risk-mitigation controls
- [[threat-modeling]] — Threat modeling (STRIDE, DREAD) is a component of risk assessment
- [[owasp-iot-top-10]] — Top 10 informs threat identification in the risk assessment process

## Open Questions
- How does this standard/framework apply to resource-constrained IoT devices with limited processing power?
- What are the practical tradeoffs between compliance and actual security improvement?
