---
title: "Network Security Fundamentals"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[networking-fundamentals]]"]
---
## One-line Summary
Network security fundamentals — firewalls, IDS/IPS, VPNs, and segmentation — are the defensive tools applied to IoT networks to detect, prevent, and contain attacks.

## Core Intuition
IoT devices are inherently difficult to secure at the device level: limited resources, no user interface, no IT staff. Network security compensates by adding defenses around the devices. A firewall blocks unauthorized connections. An IDS detects anomalous traffic. A VPN encrypts communication. Segmentation limits blast radius. You may not be able to install antivirus on a sensor, but you can control what network traffic reaches it.

## Formal Definition / Statement
Network security encompasses mechanisms that protect networked systems from unauthorized access, misuse, and attack:

**Firewalls:**
- **Packet filtering**: Allow/deny based on source/dest IP, port, protocol. Stateless (each packet evaluated independently) or stateful (tracks connection state).
- **Application-layer firewalls**: Inspect packet content (e.g., CoAP method, MQTT topic). Can block specific MQTT publish topics or CoAP resource paths.
- **Next-Generation Firewalls (NGFW)**: Combine packet filtering, application inspection, IDS/IPS, and threat intelligence.
- **IoT-specific**: Protocol-aware firewalls that understand MQTT, CoAP, Zigbee application-layer semantics.

**Intrusion Detection/Prevention Systems (IDS/IPS):**
- **Signature-based**: Match traffic patterns against known attack signatures. Fast but cannot detect zero-day attacks.
- **Anomaly-based**: Build baseline of normal traffic, alert on deviations. Can detect novel attacks but generates false positives.
- **IoT-specific**: Detect anomalous device behavior (sensor sending data at unusual rates, device communicating with unexpected endpoints).

**VPN (Virtual Private Network):**
- **IPsec**: Network-layer encryption, strong authentication. Common for site-to-site connections.
- **TLS VPN**: Application-layer encryption, easier to deploy. Common for remote access.
- **WireGuard**: Modern, lightweight VPN. Suitable for IoT gateways.
- **IoT use case**: Encrypt all device-to-cloud traffic through a VPN tunnel, hiding IoT traffic from local network observers.

**Network Segmentation:**
- **VLANs**: Virtual LANs separate broadcast domains. IoT devices on a separate VLAN cannot directly access enterprise workstations.
- **Microsegmentation**: Fine-grained policies per device or group. Each IoT device can only communicate with its approved endpoints.
- **DMZ (Demilitarized Zone)**: Intermediate zone between untrusted (internet) and trusted (internal) networks. IoT gateways can be placed in DMZs.
- **Air gap**: Complete physical isolation. Rare for IoT but used in critical industrial systems.

**Additional Mechanisms:**
- **Network Access Control (NAC)**: 802.1X port authentication. Devices must authenticate before accessing the network.
- **DNS Security (DNSSEC)**: Prevents DNS spoofing that could redirect IoT devices to malicious servers.
- **DHCP Snooping**: Prevents rogue DHCP servers from redirecting IoT device traffic.

## Key Properties / Complexity

- **IoT devices cannot run host-based firewalls** — network-level defenses are the primary control
- **Segmentation is the single most impactful** network security measure for IoT
- **Anomaly detection for IoT** requires understanding normal device behavior (many devices have very predictable communication patterns)
- **VPN overhead** may be too high for constrained devices — use gateway-level VPN instead
- **Firewall rules must be protocol-aware**: blocking port 1883 entirely breaks MQTT; you need to allow specific topics and clients
- **NAC/802.1X** is challenging for headless IoT devices without user interfaces for certificate management
- **Encrypted traffic** limits inspection capabilities — IDS cannot inspect TLS-encrypted MQTT payloads without TLS termination

## Worked Example

**IoT network segmentation for a smart building:**
```
Internet ←→ Firewall ←→ Core Switch
                            ├── VLAN 10: Corporate IT (workstations, printers)
                            ├── VLAN 20: IoT Devices (sensors, cameras, thermostats)
                            ├── VLAN 30: Building Automation (HVAC, lighting, access control)
                            └── VLAN 40: Management (SSH, SNMP to IoT devices)
```

Firewall rules:
- VLAN 20 → Internet: Allow MQTT/TLS to cloud broker (port 8883), block all else
- VLAN 20 → VLAN 10: Block all (IoT cannot reach corporate network)
- VLAN 30 → VLAN 20: Block all (building automation isolated from IoT)
- VLAN 40 → VLAN 20: Allow SSH/SNMP from management stations only
- VLAN 20 → VLAN 20: Block (prevent lateral movement between IoT devices)

## Common Pitfalls

- Flat network with IoT devices on the same VLAN as enterprise systems
- Firewall rules that are too permissive ("allow all outbound" defeats the purpose)
- Not monitoring IoT network traffic for anomalies
- Using WPA2-PSK with a shared password for all IoT devices on Wi-Fi
- Not implementing NAC — any device can plug into the network
- Assuming VPN alone is sufficient without segmentation
- Not logging firewall events for IoT network segments

## Connections

- [[networking-fundamentals]] — Network layers and protocols that security mechanisms protect
- [[iot-network-architecture]] — Where to place firewalls, IDS, VPNs in the IoT architecture
- [[zero-trust-architecture]] — Evolution beyond perimeter-based network security
- [[iot-firewalling]] — IoT-specific firewalling and segmentation strategies
- [[industrial-iot-security]] — OT network security (IEC 62443 zones and conduits)
- [[smart-home-security]] — Home network segmentation for IoT
- [[iot-lecture-4]] — Secure design goals including network protection
- [[krack-attack]] — Wi-Fi security weakness requiring network-level mitigation

## Open Questions
- Can SDN (Software-Defined Networking) enable dynamic, context-aware IoT network security?
- How should network security adapt to IoT devices that roam between networks (mobile health devices, connected vehicles)?
- What is the right balance between inspection depth and performance for IoT network traffic?
