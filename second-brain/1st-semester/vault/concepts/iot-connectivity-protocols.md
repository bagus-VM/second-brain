---
title: "IoT Connectivity Protocols"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-02
prerequisites: ["[[internet-of-things]]", "[[iot-architecture]]"]
---

## One-line Summary
IoT uses a huge diversity of connectivity solutions — Wi-Fi, LoRaWAN, Bluetooth, Ethernet, Serial, CAN, ZigBee — each with different security models, leading to incompatibility and standardization challenges.

## Core Intuition
Unlike traditional IT (which mostly uses Ethernet/TCP-IP), IoT devices communicate over dozens of different protocols depending on their power, range, and use case. Each protocol brings its own security assumptions — or lack thereof.

## Formal Definition / Statement
IoT connectivity protocols are the communication standards used to exchange data between IoT devices, gateways, and processing infrastructure. They span from short-range (NFC, Bluetooth, ZigBee) to long-range (LoRaWAN, cellular) to wired (Ethernet, CAN bus, Serial).

## Key Properties / Complexity

### Protocol Overview
| Protocol | Range | Power | Use Case | Security Model |
|----------|-------|-------|----------|----------------|
| Wi-Fi | ~100m | High | Home/office IoT | WPA2/WPA3 |
| Bluetooth/BLE | ~10-100m | Low | Wearables, sensors | Pairing-based |
| ZigBee | ~100m | Very low | Home automation, sensors | AES-128, but pairing vulnerable |
| LoRaWAN | ~15km | Very low | Agriculture, smart cities | AES-128, key management challenges |
| CAN Bus | Wired | N/A | Automotive, industrial | No native security |
| Ethernet | Wired | N/A | Industrial, infrastructure | Standard IT security |
| Serial/UART | Wired | N/A | Debug, legacy | No native security |
| NFC | ~10cm | Very low | Payment, access | Limited, proximity-based |

### Security Challenges
- **No universal standard** — each protocol has its own security mechanisms (or none)
- **Legacy protocols** (CAN, Serial) were designed without security in mind
- **Resource constraints** prevent running full TLS/IPsec on many devices
- **ZigBee pairing vulnerability** — protocol designed for easy setup lacked security configuration; network keys can be sniffed during pairing
- **KRACK attack on WPA2** — even widely-trusted Wi-Fi security can be broken at the protocol level

## Worked Example
**ZigBee Pairing Attack:** During device pairing, ZigBee transmits network keys that can be intercepted by nearby attackers because the protocol prioritized ease of setup over security. This is a protocol-level design flaw, not an implementation bug.

**CAN Bus in Automotive:** The CAN bus protocol has no authentication or encryption. Any device on the bus can send arbitrary commands. This has been exploited in car hacking demonstrations to control braking and steering.

## Common Pitfalls
- Assuming all wireless protocols have equivalent security
- Ignoring that protocol selection is a security decision
- Treating wired protocols as inherently secure (CAN bus has zero native security)
- Not considering that protocol diversity makes unified security policy enforcement difficult

## Connections
- [[zigbee-pairing-vulnerability]] — Specific protocol attack on ZigBee
- [[krack-attack]] — Protocol-level attack on WPA2/Wi-Fi
- [[iot-architecture]] — Protocols connect architectural layers
- [[iot-firewalling]] — Filtering traffic across different protocols
- [[ecosystem-communications-security]] — Securing communications between ecosystem components
- [[attack-surface-analysis]] — Network traffic as an attack surface class

## Open Questions
- Can a unified security framework cover all IoT protocols?
- How do we retrofit security into legacy protocols like CAN bus?
- Will Matter/Thread standardization improve IoT protocol security?
