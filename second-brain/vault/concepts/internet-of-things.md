---
title: "Internet of Things (IoT)"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: []
---

## One-line Summary
The Internet of Things is a network of physical devices embedded with sensors, software, and connectivity that collect and exchange data, potentially acting without direct human intervention.

## Core Intuition
Imagine every physical object around you — your car, fridge, lights, factory machines, farm sensors — all connected and communicating. The IoT extends the internet from screens and phones to the entire physical world, creating a "systems of systems" of unprecedented scale and complexity.

## Formal Definition / Statement
**IBM definition:** A network of physical devices, vehicles, appliances, and other objects embedded with sensors, software, and network connectivity, allowing them to collect and share data.

**Wikipedia:** Devices that connect and exchange data over the Internet or other communications networks.

**Anagnostopoulos (most comprehensive):** A network where data are exchanged, processed, and utilised by sensors, actuators, and other electronic devices, potentially leading to actions without direct human intervention, supervision, or control.

## Key Properties / Complexity

### IoT Components
1. **Sensors and Data Aggregators** — Resource-constrained devices (single-board computers, microprocessors) that gather environmental information
2. **Actuators and Agents** — Devices performing tasks based on commands from the processing segment; COTS hardware or dedicated limited-functionality hardware
3. **Processing Segment** — High-end devices (infrastructure servers) that decide actions based on data and predefined rules

### IoT Segments/Domains (IEEE World Forum)
- Space, Maritime, Agriculture & Aquaculture
- Smart Cities, Energy/Power/Sustainability
- Industry and Manufacturing

### Scale
- ~17 billion connected devices today
- Projected ~30 billion by 2030

### Security vs. Cost Balance
The relationship between security investment, cost of damages, ease of use, user experience, and risk assessment leads to determining an "acceptable level of security."

## Worked Example
**Smart car scenario:** A smart car automatically opens the smart garage door when it approaches home. If the car is stolen, the attacker now has access to the home — a cascading security failure across IoT subsystems that were designed independently but connected implicitly.

**Unsupervised field deployment:** IoT devices deployed in open fields (agriculture, environment monitoring) are totally unsupervised and physically accessible — creating a wide physical attack surface.

## Common Pitfalls
- Treating IoT as just "smartphones but smaller" — the diversity of devices, protocols, and constraints is far greater
- Ignoring the physical attack surface — IoT devices are often in uncontrolled environments
- Assuming connectivity homogeneity — IoT uses Wi-Fi, LoRaWAN, Bluetooth, CAN, ZigBee, Serial, Analog I/O, and more
- Underestimating cascading failures in interconnected systems of systems

## Connections
- [[iot-architecture]] — How IoT components are structured
- [[iot-connectivity-protocols]] — The diverse connectivity solutions
- [[iot-2.0]] — Next-generation IoT with 5G/6G, AI, blockchain
- [[security-by-design]] — Security must be built in from the start
- [[iot-security-landscape]] — Overview of the entire IoT security domain
- [[attack-surface-analysis]] — Understanding the attack surface of IoT systems
- [[resilience-iot]] — Maintaining operations under threat

## Open Questions
- How do we standardise security across such heterogeneous ecosystems?
- What is the "acceptable level of security" for critical infrastructure IoT?
- How will the projected doubling of devices by 2030 affect the threat landscape?
