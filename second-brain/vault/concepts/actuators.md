---
title: "Actuators"
tags: [concept, iot-security, semester-1, iot-security]
course: "IoT Security"
source_count: 0
status: current
last_updated: 2026-06-09
prerequisites: ["[[internet-of-things]]"]
---

## One-line Summary
Actuators are IoT components that perform physical actions in response to commands — motors, valves, displays, locks — representing the "doing" part of the sense-process-act cycle.

## Core Intuition
If sensors are the "eyes and ears" of IoT, actuators are the "hands and feet." A temperature sensor detects heat; an actuator opens a valve to release coolant. A motion sensor detects movement; an actuator unlocks a door. The critical security insight is that compromised actuators can cause *physical harm* — not just data breaches. An attacker who controls a car's braking actuator or a pacemaker's pacing actuator can kill.

## Formal Definition / Statement
In the IoT three-segment architecture:
1. **Sensing Layer** — sensors and data aggregators (input)
2. **Processing Layer** — servers that analyse data and make decisions (logic)
3. **Actuation Layer** — actuators and agents that perform physical actions (output)

An actuator converts an electrical signal into a physical action. It is the interface between the digital world (commands) and the physical world (movement, flow, heat, light).

### Types of Actuators
| Type | Physical Action | IoT Examples |
|------|----------------|--------------|
| Electric motors | Rotation, linear motion | Robotic arms, drone rotors, garage doors |
| Hydraulic/Pneumatic | Force via fluid pressure | Industrial presses, braking systems |
| Solenoids | Linear push/pull | Door locks, valve controls |
| Thermal | Heat/cold generation | Smart thermostats, heated seats |
| Optical | Light emission | LED displays, smart lighting |
| Acoustic | Sound generation | Alarms, speakers |

## Key Properties / Complexity

### Security Implications
- **Physical impact:** Unlike data breaches, actuator compromise causes real-world damage
- **Safety-critical:** Medical devices, vehicles, industrial control systems — actuator failures can be fatal
- **Command injection:** If an attacker can send commands to actuators, they control the physical system
- **Feedback loops:** Many actuator systems use sensor feedback; compromised sensors can cause actuator misuse

### Attack Vectors
- **Network compromise:** Intercepting or injecting commands to actuators over the network
- **Firmware manipulation:** Modifying actuator control logic in firmware
- **Sensor spoofing:** Feeding false sensor data to trigger inappropriate actuator responses
- **Physical access:** Direct manipulation of actuator wiring or interfaces

### Mitigations
- Command authentication and integrity verification
- Actuator rate limiting and bounds checking
- Hardware interlocks and fail-safe defaults
- Redundant sensor inputs for safety-critical decisions

## Worked Example
**Smart Home HVAC System:**
1. Temperature sensor reads 30°C (above setpoint of 22°C)
2. Processing unit sends "activate cooling" command to HVAC actuator
3. Actuator opens cooling valve and starts fan motor

**Attack scenario:**
1. Attacker spoofs temperature sensor to read 50°C
2. Processing unit sends "maximum cooling" command
3. Actuator runs at maximum capacity, potentially damaging the system
4. Or: attacker intercepts the command channel and sends "disable cooling" during a heat wave

**Mitigation:**
- Sensor data authenticated with [[digital-signatures]]
- Actuator commands signed and encrypted
- Hardware thermal fuse limits actuator output regardless of commands
- Redundant sensors from different manufacturers

## Common Pitfalls
- Treating actuator security as a software-only problem — physical safety interlocks are essential
- Assuming actuators are "just output devices" — they are the highest-risk component because they cause physical effects
- Ignoring the sensor-actuator feedback loop — compromised sensors indirectly compromise actuators
- Not designing fail-safe defaults — actuators should enter a safe state when communication is lost
- Underestimating the attack surface of legacy industrial actuators with no authentication

## Connections
- [[sensors]] — The complementary "sensing" part of IoT; sensors and actuators form the physical interface
- [[internet-of-things]] — Actuators are one of the three core IoT components
- [[iot-architecture]] — Actuators sit in the actuation layer of the three-segment architecture
- [[iot-attack-taxonomy]] — Physical security attacks and DoS can target actuators
- [[information-assurance]] — Actuator compromise violates Safety (beyond CIA)
- [[industrial-iot-security]] — Industrial IoT has the most dangerous actuators (SCADA, ICS)
- [[iot-device-fundamentals]] — Actuator peripherals are part of the device attack surface
- [[penetration-testing-methodology]] — Impact demonstration often involves controlling actuators

## Open Questions
- How do we certify actuator safety in systems with machine-learning-based control?
- Should actuators have independent security processors separate from the main controller?
- How do we handle actuator security in autonomous systems where no human is in the loop?
