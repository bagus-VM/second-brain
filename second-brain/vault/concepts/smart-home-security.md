---
title: "Smart Home Security"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 0
status: draft
last_updated: 2026-06-04
prerequisites: ["[[iot-device-fundamentals]]", "[[iot-communication-protocols]]"]
---

## One-line Summary
Smart home security covers consumer IoT threat models — voice assistants, smart locks, cameras, and hubs — where privacy invasion, physical access bypass, and botnet enrollment are the primary risks.

## Core Intuition
Smart homes are the most personal IoT environment: devices listen to conversations, watch through cameras, track occupancy, and control physical access (locks, garage doors). A compromised smart home isn't just a data breach — it's a privacy nightmare and a physical security risk. Consumer IoT devices are also the most cost-constrained, meaning security is often the first thing cut. The Mirai botnet proved that millions of insecure consumer IoT devices can be weaponized at scale.

## Formal Definition / Statement
Smart home IoT encompasses connected devices in residential environments:

**Device Categories:**
- **Voice Assistants**: Amazon Echo, Google Home, Apple HomePod — always-on microphones, cloud processing, third-party skill ecosystems
- **Smart Locks**: BLE/Wi-Fi/Z-Wave door locks with remote unlock capability
- **Security Cameras**: IP cameras (indoor/outdoor), video doorbells, baby monitors
- **Smart Hubs/Bridges**: Central controllers (Samsung SmartThings, Philips Hue Bridge, Apple HomePod as Thread border router)
- **Thermostats**: HVAC control with occupancy sensing and remote access
- **Appliances**: Smart TVs, refrigerators, washing machines with network connectivity
- **Lighting/Plugs**: Smart bulbs, outlets, switches

**Threat Model:**
- **Privacy invasion**: Eavesdropping via cameras/microphones, occupancy pattern inference, behavioral profiling
- **Physical access bypass**: Smart lock compromise grants physical entry to the home
- **Botnet enrollment**: Default-credential devices recruited into DDoS botnets (Mirai)
- **Lateral movement**: Compromised smart bulb as pivot to home network (work laptop, NAS)
- **Voice command injection**: Ultrasonic or inaudible commands to voice assistants (DolphinAttack)
- **Supply chain attacks**: Compromised firmware updates from manufacturer or third-party integrations

**Hub Architecture:**
- Local hub (SmartThings, Hubitat) processes rules locally, reducing cloud dependency
- Cloud-dependent hubs (Ring, Nest) require internet for most functionality
- Matter/Thread hubs provide local control with cross-vendor interoperability

## Key Properties / Complexity

- **Cost pressure**: Consumer IoT margins are thin; security features add cost (secure element = +$0.50-2.00 per device)
- **No IT department**: Consumers are not security professionals; devices must be secure by default
- **Ecosystem complexity**: A typical smart home has 10-30 devices from 5-10 different manufacturers using 3-5 different protocols
- **Always-on devices**: Voice assistants and cameras are high-value surveillance targets
- **Long deployment**: Consumer devices may remain in homes for 5-10 years after manufacturer stops updates
- **Third-party integrations**: IFTTT, Alexa Skills, Google Actions create transitive trust relationships
- **Physical proximity**: Many attacks require being within Wi-Fi/BLE range (nearby apartment, parking lot)

## Worked Example

**Ring doorbell compromise chain:**
1. Attacker finds Ring doorbell with default or reused password
2. Uses credential stuffing (passwords leaked from other breaches)
3. Gains access to Ring account — can view all cameras, unlock connected locks
4. Accesses historical video footage revealing occupancy patterns
5. Uses two-way audio to communicate with/terrify occupants
6. Lateral movement: Ring app has access to home Wi-Fi credentials

**Secure smart home configuration:**
1. Separate VLAN for IoT devices (isolated from work/personal devices)
2. Unique strong passwords for every device and service
3. Two-factor authentication on all cloud accounts
4. Local-only control where possible (Hubitat, Home Assistant)
5. Regular firmware updates enabled
6. Voice assistant mute button used when not actively needed
7. Camera feeds processed locally, not sent to cloud

## Common Pitfalls

- Connecting all IoT devices to the main home Wi-Fi network (flat network)
- Using the same password across all smart home devices and services
- Not enabling 2FA on cloud accounts controlling smart locks and cameras
- Buying the cheapest devices with no update support
- Not considering that smart TVs and voice assistants are always listening
- Trusting cloud-only devices that stop working when the manufacturer shuts down servers
- Not realizing that a compromised smart plug can be used to pivot to the entire home network

## Connections

- [[iot-communication-protocols]] — BLE, Zigbee, Thread/Matter, Wi-Fi in smart homes
- [[ble-security]] — BLE pairing for smart locks and sensors
- [[zigbee-security-model]] — Zigbee in smart home mesh networks
- [[smart-city-infrastructure]] — Smart homes as part of larger smart city
- [[privacy-by-design]] — Privacy concerns unique to home IoT
- [[device-provisioning]] — Consumer-friendly device setup and security
- [[iot-network-architecture]] — Home network architecture and segmentation
- [[mirai-botnet]] — Consumer IoT devices as botnet targets
- [[iot-lecture-1]] — Smart home in the application domain overview
- [[iot-lecture-2]] — Attacks targeting consumer IoT

## Open Questions
- Will Matter/Thread provide sufficient default security for non-technical consumers?
- How can smart home devices remain functional after the manufacturer exits the market?
- What liability should manufacturers bear when compromised smart home devices are used in botnets?
