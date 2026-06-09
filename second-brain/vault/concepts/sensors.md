---
title: "Sensors"
tags: [concept, iot-security, semester-1, iot-security]
course: "IoT Security"
source_count: 0
status: current
last_updated: 2026-06-09
prerequisites: ["[[internet-of-things]]"]
---

## One-line Summary
Sensors are IoT components that detect and measure physical phenomena — temperature, motion, pressure, light — converting real-world data into digital signals for processing.

## Core Intuition
If actuators are the "hands" of IoT, sensors are the "eyes and ears." A smart thermostat needs a temperature sensor. A self-driving car needs LIDAR, cameras, and accelerometers. An agricultural IoT system needs soil moisture sensors. The security concern is that sensors are the *trusted input* to the entire system — if an attacker can fool the sensor (spoofing), they control the system's perception of reality, which can trigger dangerous actuator responses.

## Formal Definition / Statement
A sensor is a device that detects changes in the physical environment and converts them into electrical signals that can be read by a processor.

### IoT Sensor Categories
| Category | Measures | Examples |
|----------|----------|----------|
| Environmental | Temperature, humidity, pressure, air quality | DHT22, BME280, MQ-135 |
| Motion/Acceleration | Movement, orientation, vibration | MPU-6050 accelerometer, PIR sensors |
| Optical | Light, colour, infrared, images | LIDAR, cameras, photodiodes |
| Chemical | Gas concentration, pH, water quality | MQ series gas sensors, pH probes |
| Biometric | Heart rate, fingerprint, iris | MAX30102 pulse oximeter, fingerprint scanners |
| Proximity/Distance | Object detection, range finding | Ultrasonic (HC-SR04), LIDAR, radar |
| Acoustic | Sound, vibration | MEMS microphones, piezoelectric sensors |

### Sensor in IoT Architecture
In the three-segment architecture:
1. **Sensing Layer** — Sensors gather environmental data (resource-constrained devices)
2. **Processing Layer** — Analyses sensor data and makes decisions
3. **Actuation Layer** — Executes actions based on sensor-driven decisions

Sensors are the *input* to the entire decision pipeline. Compromised sensors feed false data to the processing layer, which may trigger inappropriate actuator responses.

## Key Properties / Complexity

### Security Properties
- **Attack surface:** Sensors are physically exposed, especially in unattended deployments (fields, roads, buildings)
- **Spoofing:** Attackers can inject false signals (e.g., replaying recorded sensor data, shining a light at a LIDAR sensor)
- **Jamming:** Denial-of-service against sensors by flooding them with noise (e.g., ultrasonic jamming of microphone sensors)
- **Tampering:** Physical manipulation of sensor hardware to alter readings
- **Eavesdropping:** Sensor data may reveal sensitive information (e.g., occupancy patterns from motion sensors)

### Data Properties
- **Noisy:** All sensors have measurement error and environmental interference
- **Resource-constrained:** Many sensors run on battery power with limited computation
- **Continuous streams:** Sensors generate high-volume time-series data requiring efficient processing
- **Calibration:** Sensors drift over time and need periodic recalibration

### Sensor Fusion
Combining multiple sensor inputs improves reliability:
- Redundant sensors detect spoofing (if one sensor disagrees with others, it may be compromised)
- Different sensor types provide complementary information
- Voting mechanisms can reject outlier readings

## Worked Example
**Smart Home Intrusion Detection:**
1. PIR motion sensor detects movement in the living room
2. Window vibration sensor detects glass stress
3. Camera sensor captures an image
4. Processing layer correlates all three: motion + vibration + image = likely intrusion
5. Actuator response: alarm sounds, lights turn on, notification sent to homeowner

**Sensor Spoofing Attack:**
1. Attacker uses an infrared LED to blind the PIR motion sensor
2. Attacker uses ultrasonic noise to jam the vibration sensor
3. The processing layer receives no alerts — the intrusion goes undetected
4. Alternatively: attacker replays a recording of "no motion" to the sensor data channel

**Mitigation:**
- Multiple sensor types (cross-validation)
- Encrypted sensor-to-gateway communication
- Anomaly detection on sensor data streams
- Physical tamper-evident enclosures
- Regular calibration checks

## Common Pitfalls
- Trusting sensor data implicitly — sensors can be spoofed, jammed, or tampered with
- Using a single sensor for safety-critical decisions — redundancy is essential
- Ignoring physical attack surface — sensors are often deployed in uncontrolled environments
- Not encrypting sensor data in transit — eavesdropping on sensor data reveals patterns
- Assuming sensor accuracy equals sensor security — a sensor can be perfectly accurate yet completely spoofable
- Neglecting sensor lifecycle management — sensors degrade, drift, and need replacement

## Connections
- [[actuators]] — The complementary "doing" part of IoT; sensor data drives actuator commands
- [[internet-of-things]] — Sensors are one of the three core IoT components
- [[iot-architecture]] — Sensors sit in the sensing/edge layer of the three-segment architecture
- [[iot-attack-taxonomy]] — Eavesdropping, spoofing, and physical attacks target sensors
- [[information-assurance]] — Sensor compromise violates Integrity (false data) and potentially Safety
- [[iot-device-fundamentals]] — Sensor peripherals are part of the device attack surface
- [[industrial-iot-security]] — Industrial sensors (SCADA) control critical infrastructure
- [[penetration-testing-methodology]] — Sensor spoofing is a key test in IoT penetration testing
- [[zigbee-pairing-vulnerability]] — ZigBee sensors can be hijacked during insecure pairing

## Open Questions
- How do we detect sensor spoofing in real-time without redundant sensors?
- Should sensor data be authenticated at the hardware level (secure enclaves)?
- How do we handle sensor security in adversarial environments (military, autonomous vehicles)?
