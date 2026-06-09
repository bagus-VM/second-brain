---
title: "Threat Modeling"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-04
prerequisites: ["[[internet-of-things]]", "[[cia-triad]]", "[[iot-network-architecture]]", "[[security-principles]]"]
---

## One-line Summary
Threat modeling — using frameworks like STRIDE, DREAD, and attack trees — systematically identifies what can go wrong in an IoT system before it's built, so defenses can be designed in rather than bolted on.

## Core Intuition
You cannot defend against threats you haven't identified. Threat modeling is the structured process of asking "what could an attacker do?" before writing code or designing hardware. For IoT, this is especially critical because devices are hard to update after deployment, physically exposed, and have long lifecycles. A threat model done at design time prevents vulnerabilities that would be expensive or impossible to fix later.

## Formal Definition / Statement
Threat modeling is a systematic process for identifying, quantifying, and addressing security threats to a system. Key frameworks:

**STRIDE (Microsoft):**
- **S**poofing: Impersonating a user or device (mitigated by authentication)
- **T**ampering: Modifying data or code (mitigated by integrity checks, signing)
- **R**epudiation: Denying actions performed (mitigated by audit logging)
- **I**nformation Disclosure: Exposing confidential data (mitigated by encryption)
- **D**enial of Service: Making systems unavailable (mitigated by rate limiting, redundancy)
- **E**levation of Privilege: Gaining unauthorized access levels (mitigated by least privilege)

Applied to IoT: STRIDE is applied to each component (device, gateway, cloud, mobile app) and each data flow between components.

**DREAD (Risk Rating):**
- **D**amage: How bad is the impact?
- **R**eproducibility: How easy is it to reproduce?
- **E**xploitability: How much skill/effort to exploit?
- **A**ffected Users: How many users impacted?
- **D**iscoverability: How easy to find the vulnerability?

Each factor scored 1-10, averaged for overall risk rating. Used to prioritize mitigations.

**Attack Trees:**
- Root node: attacker's goal (e.g., "unlock smart lock")
- Child nodes: alternative methods to achieve the goal (AND/OR branches)
- Leaf nodes: specific, actionable attack steps
- Used to visualize attack paths and identify critical choke points

**PASTA (Process for Attack Simulation and Threat Analysis):**
1. Define objectives (business context)
2. Define technical scope (architecture)
3. Application decomposition (data flows)
4. Threat analysis (who attacks and why)
5. Weakness/vulnerability analysis
6. Attack modeling (attack trees/scenarios)
7. Risk and impact analysis

**LINDDUN (Privacy Threat Modeling):**
- **L**inking: Connecting data to individuals
- **I**dentifying: Determining identity from data
- **N**on-repudiation: Proving someone did something
- **D**etecting: Detecting user behavior
- **D**ata Disclosure: Exposing collected data
- **U**nawareness: Users not informed about data collection
- **N**on-compliance: Violating privacy regulations

## Key Properties / Complexity

- **Threat modeling should happen early** — during design, not after deployment
- **IoT threat models must consider physical attacks** (not just network/application)
- **STRIDE per element**: Apply STRIDE to every component and every data flow in the architecture diagram
- **Attack trees scale with system complexity** — a smart home with 30 devices has a large tree
- **DREAD is subjective** — different analysts may score differently; use calibrated scales
- **Privacy threats require separate modeling** — STRIDE focuses on security, LINDDUN on privacy
- **Iterative process**: Threat models must be updated as the system evolves

### IoT-Specific Challenges
- **Diverse assets:** Devices, gateways, cloud, mobile apps, APIs
- **Diverse threats:** Physical, network, protocol, software, supply chain
- **Diverse environments:** Home, industrial, medical, agricultural
- **Resource constraints:** Can't protect everything equally — must prioritize

### Evaluation Factors
- Attacker capabilities (technical ability, stealth, cost)
- Attack behaviours and probabilities
- Impact (individual + aggregated)
- Benefits to attacker
- Detriments to attacker (risk, cost, effort)

## Worked Example

**STRIDE analysis for MQTT-based sensor network:**

| Component | Threat | Risk | Mitigation |
|---|---|---|---|
| Sensor → Broker | Spoofing: Rogue sensor publishes fake data | High | Client certificates (mTLS) |
| Sensor → Broker | Tampering: MITM modifies temperature reading | High | TLS encryption |
| Broker | Repudiation: Sensor denies sending data | Medium | Audit logging with timestamps |
| Sensor → Broker | Info Disclosure: Cleartext sensor data | High | TLS encryption |
| Broker | DoS: Connection flood from rogue devices | High | Rate limiting, connection quotas |
| Broker → Cloud | Elevation: Sensor gains publish access to admin topics | High | Topic-level ACLs |

**Attack tree for "unlock smart lock":**
```
UNLOCK SMART LOCK
├── OR: Exploit smart lock directly
│   ├── AND: BLE MITM attack
│   │   ├── Within BLE range (10m)
│   │   └── Lock uses Just Works pairing
│   ├── AND: Firmware vulnerability
│   │   ├── Extract firmware (JTAG/UART)
│   │   └── Find buffer overflow in BLE stack
│   └── AND: Default credentials
│       └── Try default PIN (0000, 1234)
├── OR: Compromise controlling device
│   ├── Steal owner's phone
│   ├── Compromise smart home hub
│   └── Brute-force cloud account
└── OR: Physical attack
    ├── Lock picking (not cyber)
    └── Shim/bypass mechanical override
```

## Common Pitfalls

- Threat modeling after deployment instead of during design
- Only considering network attacks, ignoring physical and supply chain threats
- Treating threat modeling as a one-time activity (it should be iterative)
- Using DREAD scores without calibration (subjective and inconsistent)
- Not involving developers, operations, and business stakeholders in the process
- Creating overly complex models that nobody reads or acts upon
- Ignoring privacy threats (STRIDE alone is insufficient for IoT)
- Generating threat lists without prioritizing them

## Connections

- [[attack-tree]] — Structured diagram of attacker paths
- [[fault-tree]] — Structured diagram of failure paths
- [[attack-surface-analysis]] — Miessler's 15 attack surface classes as input to threat models
- [[penetration-testing-methodology]] — Pentesting validates threat model assumptions
- [[risk-assessment-frameworks]] — Risk assessment quantifies and prioritizes identified threats
- [[security-principles]] — Principles that guide mitigation strategies
- [[security-by-design]] — Threat modeling is a core security-by-design activity
- [[iot-lecture-3]] — Attack surfaces identified through threat modeling
- [[iot-lecture-4]] — Design goals address identified threats
- [[privacy-by-design]] — LINDDUN for privacy threat modeling
- [[iot-attack-taxonomy]] — Catalogue of threats to model against
- [[operational-security-lifecycle]] — Threat modelling in the Define phase
- [[iot-secure-design]] — Topic page on secure design practices

## Open Questions
- Can AI-assisted threat modeling tools reliably generate threat models for novel IoT architectures?
- How should threat models handle unknown unknowns — attacks that haven't been discovered yet?
- What is the right level of detail for an IoT threat model (too detailed = unused, too high-level = useless)?
- How do we threat-model systems with billions of heterogeneous devices?
