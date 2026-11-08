---
title: "IoT Firewalling"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[iot-architecture]]", "[[iot-connectivity-protocols]]"]
---

## One-line Summary
IoT firewalling filters network traffic directed at resource-constrained IoT devices that cannot run their own firewalls — a necessary security measure because IoT devices have limited computation and memory capabilities.

## Core Intuition
Your smart sensor can't run a firewall — it doesn't have the CPU or RAM. So the network must protect it. IoT firewalling moves the security perimeter from the device to the network, filtering traffic before it reaches vulnerable devices.

## Formal Definition / Statement
**IoT Firewalling:** A best security practice where network-level filtering is applied to protect IoT devices that have limited computation and memory capabilities. Firewalling is necessary in IoT networks to filter packets directed to devices, since the devices themselves cannot implement adequate filtering.

## Key Properties / Complexity

### Why IoT Needs Special Firewalling
- **Resource constraints:** Devices can't run traditional firewall software
- **Diverse protocols:** Must filter ZigBee, BLE, LoRaWAN, not just TCP/IP
- **Default deny:** Should block all unnecessary traffic by default
- **Device-aware:** Should understand device behaviour patterns (anomaly detection)

### Approaches
1. **Network-level firewalls** — Gateway-based filtering for IoT traffic
2. **Micro-segmentation** — Isolate IoT devices in separate network segments
3. **Protocol-aware filtering** — Understand IoT-specific protocols
4. **Behavioural analysis** — Detect anomalies in device communication patterns
5. **Cloud-based IoT firewalls** — Centralized policy management

### Implementation Considerations
- Must not add significant latency (real-time IoT)
- Must handle diverse protocols (not just IP)
- Must scale to thousands of devices
- Must be centrally manageable

## Worked Example
**Smart Home IoT Firewall:**
1. All IoT devices connected to dedicated IoT VLAN
2. Gateway firewall rules:
   - Allow: IoT devices → cloud API (specific ports only)
   - Block: IoT devices → internet (except cloud API)
   - Block: IoT devices → each other (unless explicitly allowed)
   - Block: External → IoT devices (except through gateway)
3. Anomaly detection: camera suddenly starts sending data to unknown IP → alert + block

## Common Pitfalls
- Putting IoT devices on the same network as computers and phones
- Allowing IoT devices unrestricted internet access
- Not monitoring IoT network traffic for anomalies
- Assuming the router's built-in firewall is sufficient for IoT

## Connections
- [[iot-architecture]] — Firewalling protects architectural layers
- [[iot-connectivity-protocols]] — Must handle diverse protocols
- [[attack-surface-analysis]] — Network services and traffic are attack surfaces
- [[ecosystem-communications-security]] — Securing inter-component communications
- [[security-by-design]] — Firewalling is a secure design goal
- [[mirai-botnet]] — Unprotected IoT devices were recruited into Mirai

## Open Questions
- How do we firewall IoT devices using non-IP protocols?
- Can AI/ML improve IoT traffic anomaly detection?
- What's the right granularity for IoT network segmentation?
