---
title: "IoT Applications"
tags: [concept, iot-security, semester-1, course-iot-security]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[internet-of-things]]", "[[iot-2-0]]", "[[iot-lecture-2]]"]
---

## One-line Summary
IoT applications span a wide range of domains — smart home, smart city, industrial automation, healthcare, agriculture, transportation, energy, space — each with its own security requirements, threat model, and deployment constraints; the Anagnostopoulos lecture series uses several concrete scenarios (forest fire emergency response, Internet of Lights, smart home coordination) to make the abstract security concepts concrete.

## Core Intuition
The IoT is not a single thing — it is many industries, each with its own devices, protocols, regulatory requirements, and risk profiles. A smart home camera and a wind turbine sensor and a hospital patient monitor have almost nothing in common except the "things connected to the internet" framing.

The IoT Security course works through several application scenarios to make the abstract security concepts (CIA triad, attack surface, threat modelling) concrete. The Zhou et al. 2021 survey (see [[paper-zhou-iot-2-0]]) maps the application space as:

- **Space IoT**: satellite-based sensing, communications
- **Maritime IoT**: ship tracking, ocean monitoring
- **Agriculture & Aquaculture IoT**: soil moisture, livestock tracking, fish farming
- **Smart Cities**: traffic, lighting, waste, pollution
- **Energy / Power / Sustainability IoT**: smart grid, renewable energy
- **Industry & Manufacturing IoT (IIoT)**: factory automation, predictive maintenance
- **Smart Home**: consumer devices, security, entertainment
- **Healthcare IoT**: patient monitoring, medication adherence, telemedicine
- **Transportation IoT**: connected vehicles, fleet management, autonomous driving
- **Retail IoT**: inventory, customer analytics, supply chain
- **Wearables IoT**: fitness, health, AR/VR

Each domain has its own security requirements. A smart meter in a basement has different threats than a satellite in orbit. A medical device in a hospital has different regulatory requirements than a consumer fitness tracker.

## Formal Definition / Statement

**Application scenarios from the lectures:**

### Smart Home Coordination (L2)
- Smart car, satellite navigation, smart fridge, smart oven, smart TV, video recorder
- Use case: arrive home → garage opens, lights turn on, oven starts dinner, TV records the show you didn't catch
- Security risk: if car is stolen, attacker can also access home (car key fob relays to garage door)

### Forest Fire Emergency Response (L1, L2)
- Space segment IoT detects fire via thermal imaging
- On-site agricultural IoT confirms (temperature, smoke, wind)
- Highway infrastructure IoT reroutes traffic
- Connected vehicles receive alerts
- Fire department dispatches autonomous UAVs
- Resident cellphones receive evacuation alerts
- Security risk: false alerts cause panic; spoofed alerts could direct people *toward* danger

### Internet of Lights (L2)
- All smart lights in a space connected by digital networks
- Can communicate with each other, servers, gateways, sensors
- Use cases: building automation, energy savings, security
- **LiFi** (Light Fidelity): wireless communication using light, not radio
- Security: light can't penetrate walls, so inherently more secure than Wi-Fi in some scenarios

### Internet of Sounds (IoS, L2)
- Emerging research field at intersection of IoT and Sound and Music Computing
- Smart speakers, voice assistants, acoustic sensing
- Security: voice spoofing, ultrasonic attacks (inaudible commands)

### Smart Grid (covered in many lectures)
- Distributed energy resources (solar panels, batteries)
- Smart meters (consumption reporting)
- Demand-response (utility signals appliance to reduce load)
- Security risk: cascading failures, false billing, grid destabilisation

### Industrial IoT (IIoT)
- Factory automation with sensors and actuators
- Predictive maintenance (ML-driven)
- Digital twins (virtual model of physical system)
- Security: Stuxnet showed industrial attacks can destroy physical equipment

### Healthcare IoT
- Patient monitoring (heart rate, blood pressure, oxygen)
- Medication adherence (smart pill bottles)
- Telemedicine (remote consultation)
- Implanted medical devices (pacemakers, insulin pumps)
- Security: life-critical; FDA and EU MDR regulatory requirements

## Key Properties / Complexity
- **Diverse**: each domain has its own protocols, regulations, and threat models
- **Interconnected**: smart home + smart car + smart city means a single attack can cascade
- **Critical**: failures in industrial, healthcare, or transportation IoT can kill people
- **Long-lived**: industrial IoT devices may be in service for 20+ years
- **Regulated**: medical, financial, and critical infrastructure IoT are heavily regulated
- **Constrained**: many application scenarios involve small, low-power devices

## Worked Example

**Smart home attack scenario (L1 example):**
1. Attacker steals the user's smart car
2. Car has a digital key fob that is paired with the smart home
3. Car automatically opens the smart garage door
4. Attacker now has physical access to the home
5. Attacker can pivot to other smart home devices (cameras, locks, alarms)

This is a *cascading IoT attack* — exploiting the trust relationship between the car and the home. The security challenge: the car and the home use different vendors, different protocols, but share trust. There's no single "smart home security" team; it's distributed across vendors.

**Forest fire response — the security analysis:**
- Space IoT data must be authenticated (spoofed satellite data could trigger false evacuations)
- On-site sensors must be tamper-resistant (physical access to an agricultural sensor is easy)
- Highway infrastructure must validate commands (a malicious vehicle could trigger false traffic alerts)
- Evacuation alerts must be authentic (fake alerts could direct people into the fire)
- All of this must work in real time, with no centralised authority

The IoT 2.0 vision requires *systems of systems* security, not just point solutions.

## Common Pitfalls
- **Assuming "IoT security" is one thing**: it isn't. Smart home security and industrial IoT security have different threat models, different regulations, and different security budgets.
- **Underestimating the cascade risk**: an attack on a low-criticality device (a smart speaker) can pivot to a high-criticality device (a smart lock) via the home network.
- **Ignoring the long lifetime**: an industrial IoT device deployed today may be running in 2040. Plan for cryptographic agility.
- **Treating "security" as a software problem**: in IoT, hardware security (PUFs, TPMs, secure boot) is often more important than software security.
- **Forgetting the regulatory context**: medical, financial, and critical infrastructure IoT have specific regulatory requirements (FDA, EU MDR, NERC CIP, etc.) that the security design must satisfy.

## Connections
- [[internet-of-things]] — the parent concept
- [[iot-2-0]] — the framing for many of these applications
- [[iot-lecture-1]] — initial introduction to the diversity
- [[iot-lecture-2]] — vulnerability-attack-countermeasure cycle
- [[iot-architecture]] — the layered architecture
- [[iot-security-landscape]] — the security context
- [[iot-attack-surfaces]] — the expanded surface
- [[smart-home-security]] — consumer IoT
- [[industrial-iot-security]] — IIoT
- [[healthcare-iot-security]] — medical IoT
- [[paper-zhou-iot-2-0]] — the survey that maps the application space
- [[paper-iot-lightweight-hardware-architecture]] — Mexis et al. architecture for IoT 2.0 security

## Open Questions
- Which IoT application domain will be the first to have a major, publicised security failure? (My guess: smart home — too many devices, too little security investment.)
- How will regulation catch up to the IoT 2.0 reality? (The EU Cyber Resilience Act is a start, but enforcement is the question.)
- Will vertical-specific IoT platforms win (e.g., a healthcare-IoT-only cloud), or will general-purpose IoT platforms (AWS IoT, Azure IoT) dominate?
- How will consumer trust in IoT evolve after the next big breach? (Mirai didn't kill consumer IoT; will the next one?)
