---
title: "IoT 2.0"
tags: [concept, iot-security, semester-1, course-iot-security]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[internet-of-things]]", "[[iot-lecture-1]]"]
---

## One-line Summary
IoT 2.0 is the next generation of the Internet of Things, integrating 5G/6G, machine learning, edge computing, Industry 4.0, and blockchain into interconnected systems of systems (SoS) — the framing adopted in [[iot-lecture-1]] and formally defined in the Zhou et al. 2021 IEEE Access survey (see [[paper-zhou-iot-2-0]]).

## Core Intuition
The original IoT was about connecting devices: sensors, actuators, microcontrollers, gateways, clouds. The vision was "anything that can be connected will be connected."

IoT 2.0 is the recognition that the original vision is *being realised*, and the result is qualitatively different. With ~17 billion devices today (projected 30+ billion by 2030), the IoT is now:

- **Heterogeneous at scale**: billions of devices, thousands of vendors, hundreds of protocols
- **AI-driven**: machine learning runs on the edge, in the fog, and in the cloud, making decisions in real time
- **Mission-critical**: autonomous vehicles, remote surgery, smart grids — failure has physical consequences
- **Network-of-networks**: smart cities, smart homes, smart vehicles, smart grids all communicate with each other (systems of systems)
- **Constrained**: the smallest devices are coin-cell-powered sensors with 32 KB of flash

The Anagnostopoulos lecture series uses "IoT 2.0" as the motivating framing. The Zhou et al. survey is the academic formalisation.

The key implication for security: as IoT becomes more capable and more critical, security failures become more dangerous. Stuxnet showed that industrial IoT attacks can destroy centrifuges. Mirai showed that consumer IoT can be weaponised at internet scale. KRACK showed that even WPA2 has fundamental flaws. IoT 2.0 needs *holistic* security — not just securing individual devices, but securing the systems of systems.

## Formal Definition / Statement

**IoT 2.0 (per the Zhou et al. survey and Anagnostopoulos lectures):**

A new generation of IoT characterised by:
- **Integration with 5G/6G**: ultra-low latency, ultra-reliable communication
- **ML/AI embedded**: distributed intelligence across edge, fog, cloud
- **Edge computing**: data processed near the source, not centralised
- **Industry 4.0 / IIoT**: industrial automation as a primary use case
- **Blockchain integration**: for trust and decentralised identity
- **Tactile Internet**: human-machine interaction with haptic feedback, ~1 ms latency
- **Cyber-physical systems**: physical consequences to digital events

**Seven dimensions (from Zhou et al.):**
1. Machine learning intelligence
2. Mission-critical communication
3. IoT scalability
4. Energy harvesting-based sustainability
5. IoT interoperability
6. User-friendly IoT
7. IoT security (cross-cutting)

**Architectural evolution:**
- Conventional 6-layer: physical, perception, network, middleware/cloud, application, business
- Recent 3-layer (with edge): end device, fog/edge, cloud
- Recent 6-layer: end device, communication, fog/edge, network core, cloud, application
- 8-layer (proposed): end device, communication, fog/edge, data storage, collaboration/process, cloud, application, security (cross-cutting)

**Examples of IoT 2.0 systems:**
- Smart home coordinating with smart car and satellite navigation
- Forest fire emergency response: satellite IoT detects fire → on-site IoT confirms → highway infrastructure notifies vehicles → fire department deploys autonomous systems
- Industrial IoT (IIoT) with predictive maintenance, autonomous robots, digital twins
- Smart grid with distributed energy resources, demand-response, blockchain-based energy trading

**IoT 2.0 security challenges:**
- Massive attack surface (billions of devices)
- Constrained devices (cannot run heavy crypto)
- Heterogeneous protocols (no one-size-fits-all security)
- Real-time requirements (cannot afford multi-second crypto)
- Long device lifetimes (security must age well over 10+ years)
- Physical exposure (sensors in open fields, smart meters in basements)

## Key Properties / Complexity
- **Scale**: billions of devices
- **Heterogeneity**: many vendors, many protocols, many use cases
- **Constraints**: small devices, limited power, limited compute
- **Real-time**: many use cases require low latency
- **Long-lived**: devices deployed for years, security must age well
- **Physically exposed**: deployed in open environments, accessible to attackers
- **Safety-critical**: failures have physical consequences (autonomous vehicles, medical devices, industrial control)

## Worked Example

**Forest fire emergency response (from Lecture 1):**
1. **Space segment IoT** (satellite with thermal imaging) detects anomalous heat signatures in a forest
2. **On-site agricultural IoT** sensors confirm: temperature rise, smoke, wind direction
3. **Highway infrastructure IoT** (smart traffic signs, connected traffic lights) receives alert
4. **Connected vehicles** in the affected area receive rerouting instructions
5. **Fire department dispatch** receives location and severity data
6. **Autonomous UAVs** are deployed for initial reconnaissance
7. **Residents' cellphones** receive evacuation alerts

This is a *system of systems* — at least 6 different IoT domains (space, agriculture, transportation, emergency, public safety, consumer) coordinating in real time. Each component has its own security requirements. A failure in any one could cascade.

## Common Pitfalls
- **Treating IoT 2.0 as just "more IoT"**: the qualitative change matters. ML-driven decision making, real-time constraints, and cross-domain integration are *new* problems.
- **Ignoring the long lifetime**: an IoT device deployed today may be in service for 10+ years. AES-128 is considered secure until 2030+, but the device may be operating until 2040. Plan for cryptographic agility.
- **Underestimating physical exposure**: IoT devices in the field can be physically tampered with. Hardware security (PUFs, TPMs, tamper-evident packaging) is essential.
- **Assuming interoperability exists**: it doesn't. The Zhou et al. paper identifies interoperability as a *major blocker* for IoT 2.0. Standards work is ongoing.

## Connections
- [[internet-of-things]] — the parent concept
- [[iot-lecture-1]] — IoT 2.0 introduced as a framing
- [[paper-zhou-iot-2-0]] — the formal survey that defines the seven dimensions
- [[iot-architecture]] — the 6-layer → 8-layer evolution
- [[machine-learning-basics]] — one of the seven dimensions
- [[iot-applications]] — the application breadth
- [[iot-security-landscape]] — the security context
- [[iot-attack-surfaces]] — the expanded attack surface
- [[industrial-iot-security]] — IIoT as a primary IoT 2.0 use case
- [[smart-home-security]] — the user-facing side of IoT 2.0
- [[healthcare-iot-security]] — the life-critical side
- [[paper-iot-lightweight-hardware-architecture]] — Mexis et al. architecture for IoT 2.0 security
- [[paper-iot-mexis-2021-poster]] — the demo companion
- [[lightweight-cryptography]] — ASCON, NIST response to IoT 2.0 security at scale

## Open Questions
- Will IoT 2.0 become a self-fulfilling vision (real products ship with these features) or remain a research framing?
- How will post-quantum migration work for billions of IoT devices? (This is the biggest open security problem.)
- Will blockchain-based identity and trust actually scale to IoT, or is it overhyped?
- Will the 8-layer architecture (or some variant) become a standard, or will vendors continue to ship bespoke stacks?