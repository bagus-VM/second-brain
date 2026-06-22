---
title: "IoT Network Architecture"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[networking-fundamentals]]", "[[iot-device-fundamentals]]"]
---
## One-line Summary
IoT network architecture is the three-tier model — perception (devices), network (connectivity), and application (cloud/services) — that defines how data flows and where security boundaries must exist.

## Core Intuition
Every IoT security decision depends on understanding where a component sits in the architecture. A sensor at the edge has different constraints than a cloud API. A gateway bridges two worlds and must enforce security at the boundary. If you do not understand the architecture, you cannot identify where to place firewalls, where to encrypt, or where to authenticate.

## Formal Definition / Statement
The standard IoT architecture is a three-tier model:

**Tier 1 — Perception Layer (Edge/Device Layer)**
- Physical devices: sensors, actuators, embedded systems
- Constrained resources: limited CPU, memory, power
- Protocols: BLE, Zigbee, LoRaWAN, 802.15.4
- Security concerns: physical tampering, sensor spoofing, firmware extraction, weak credentials
- Key devices: MCUs, sensors, RFID tags, cameras

**Tier 2 — Network Layer (Connectivity/Transport Layer)**
- Transmits data from perception to application layer
- Includes gateways, routers, switches, and access points
- Protocols: Wi-Fi, Ethernet, cellular (4G/5G), LPWAN, satellite
- Security concerns: eavesdropping, MITM, DDoS, protocol exploitation, lateral movement
- Key component: **Gateways** — bridge constrained device protocols (Zigbee, BLE) to IP networks

**Tier 3 — Application Layer (Cloud/Service Layer)**
- Data processing, storage, analytics, user interfaces
- Cloud platforms: AWS IoT, Azure IoT Hub, Google Cloud IoT
- APIs, dashboards, machine learning inference
- Security concerns: API abuse, data breaches, unauthorized access, insecure cloud configuration

**Extended architectures:**
- **Fog Computing**: Processing at the network edge (gateways, routers) to reduce latency and bandwidth. Security challenge: fog nodes are more accessible than cloud data centers.
- **Edge Computing**: Processing on the device itself or a nearby edge server. Security challenge: limited physical security, constrained management.
- **Gateway Patterns**: Protocol translation (Zigbee-to-IP), local data aggregation, local rule execution, security enforcement point.

## Key Properties / Complexity

- **Attack surface scales with tiers**: Each tier adds protocols, interfaces, and trust boundaries
- **Gateways are high-value targets**: Compromise one gateway, compromise all devices behind it
- **Fog/edge reduces data exposure** (data processed locally) but increases physical attack surface
- **North-south traffic** (device-to-cloud) is typically well-secured; **east-west traffic** (device-to-device, gateway-to-gateway) is often overlooked
- **Network segmentation** is critical: IoT devices should be on separate VLANs/subnets from enterprise IT
- **Protocol translation** at gateways creates opportunities for inspection but also introduces new vulnerabilities (parser bugs, protocol downgrade)
- **Multi-tenancy**: Cloud platforms serving multiple customers must isolate device data and control channels

## Worked Example

**Smart building architecture:**
```
[IoT Sensors] --Zigbee/BLE--> [Floor Gateway] --MQTT/TLS--> [Building Cloud]
     |                              |
[HVAC actuators]              [Local Rules Engine]
[Occupancy sensors]           [Fog Processing]
[Smart locks]
```

1. Zigbee sensors report temperature/occupancy to floor gateway
2. Gateway translates Zigbee to MQTT, applies local rules (e.g., if occupancy=0, dim lights)
3. Gateway forwards aggregated data to cloud via TLS
4. Cloud runs analytics, provides dashboard, sends commands back

**Security boundaries:**
- Between sensors and gateway: Zigbee AES-128-CCM with install codes
- Gateway itself: hardened Linux, iptables firewall, no unnecessary services
- Between gateway and cloud: mutual TLS with client certificates
- Cloud: IAM policies, encrypted storage, audit logging
- Between building network and corporate IT: VLAN isolation, firewall

## Common Pitfalls

- Flat network with IoT devices on the same subnet as workstations and servers
- Gateway with default credentials and unnecessary open ports
- No encryption between perception and network layers (cleartext Zigbee/BLE)
- Trusting the gateway implicitly — if compromised, all downstream devices are exposed
- Not monitoring east-west traffic within the IoT network segment
- Over-reliance on cloud processing without local failover (cloud outage = no automation)

## Connections

- [[iot-device-fundamentals]] — Perception layer device types and constraints
- [[iot-communication-protocols]] — Protocols used at each tier
- [[iot-data-lifecycle]] — Data flows through all three tiers
- [[network-security-fundamentals]] — Firewalls, IDS, VPN at the network layer
- [[zero-trust-architecture]] — Microsegmenting the IoT network
- [[smart-home-security]] — Consumer IoT architecture example
- [[industrial-iot-security]] — ICS/SCADA architecture differences
- [[iot-firewalling]] — Network segmentation and traffic filtering for IoT
- [[iot-lecture-1]] — IoT Security Landscape overview

## Open Questions
- How do satellite IoT (LEO) constellations change the three-tier model?
- Can mesh networks eliminate the gateway as a single point of failure without sacrificing security?
- What is the right balance between edge processing (more physical attack surface) and cloud processing (more network exposure)?
