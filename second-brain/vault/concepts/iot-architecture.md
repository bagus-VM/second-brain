---
title: "IoT Architecture"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[internet-of-things]]"]
---

## One-line Summary
IoT architecture consists of three main segments — sensors/data aggregators, actuators/agents, and processing infrastructure — connected by diverse protocols, forming a system of systems.

## Core Intuition
Think of IoT as a three-layer cake: at the bottom, tiny devices sense the world; in the middle, actuators do things; at the top, powerful servers make decisions. The security challenge is that each layer has different capabilities, constraints, and attack surfaces.

## Formal Definition / Statement
IoT architecture comprises three functional segments:
1. **Sensing/Edge Layer** — Sensors and data aggregators (resource-constrained: SBCs, microprocessors) gathering environmental data
2. **Actuation Layer** — Actuators and agents performing physical actions based on processing-layer commands; often COTS or dedicated hardware with limited functionality
3. **Processing/Cloud Layer** — High-end infrastructure servers that analyse data and make decisions based on predefined rules

These segments are connected via diverse connectivity solutions (Wi-Fi, LoRaWAN, Bluetooth, Ethernet, Serial, CAN, ZigBee) and span multiple domains (Space, Maritime, Agriculture, Smart Cities, Energy, Industry).

## Key Properties / Complexity

### Heterogeneity
- Massive diversity in hardware, software, and protocols
- No single standard governs all IoT deployments
- Leads to incompatibility and integration challenges

### Resource Constraints
- Edge devices have limited computation, memory, and power
- Security solutions must be lightweight enough for constrained devices
- "Lowest common denominator approach": if security works on the smallest device, it works everywhere

### Scale
- Billions of devices forming systems of systems
- Networks of networks with varying trust boundaries

### Connectivity Diversity
- Short-range: Bluetooth, ZigBee, NFC
- Long-range: LoRaWAN, cellular
- Wired: Ethernet, CAN bus, Serial
- Each protocol has its own security model (or lack thereof)

## Worked Example
**Emergency Response (Forest Fire):**
1. Space segment IoT detects fire via satellite
2. On-location agricultural IoT confirms
3. Highway infrastructure notifies vehicles
4. Fire department deploys autonomous systems (UAVs, fire trucks)
5. Cellphones receive alerts

This involves satellite → on-site IoT → highway infrastructure → vehicles → UAVs → cellphones — each with different protocols, trust models, and security requirements.

## Common Pitfalls
- Designing security for each layer in isolation — cross-layer attacks exploit the boundaries
- Assuming the processing layer is always reachable — edge computing and intermittent connectivity are common
- Ignoring that COTS components may have unknown supply chain risks

## Connections
- [[internet-of-things]] — Core IoT definition
- [[iot-connectivity-protocols]] — Protocols connecting the architecture
- [[iot-attack-taxonomy]] — Attacks mapped to architectural layers
- [[attack-surface-analysis]] — Miessler's 15 attack surface classes
- [[iot-firewalling]] — Filtering traffic between architectural layers
- [[ecosystem-communications-security]] — Securing inter-component communication

## Open Questions
- How should security responsibilities be distributed across resource-heterogeneous layers?
- What is the optimal boundary between edge processing and cloud processing for security?
