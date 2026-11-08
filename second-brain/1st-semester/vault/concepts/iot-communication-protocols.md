---
title: "IoT Communication Protocols"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[networking-fundamentals]]"]
---
## One-line Summary
IoT communication protocols — MQTT, CoAP, Zigbee, BLE, LoRaWAN, and Thread/Matter — are the languages IoT devices use to talk, and each has distinct security models, strengths, and weaknesses.

## Core Intuition
Choosing a communication protocol is choosing a security posture. MQTT assumes a trusted broker. CoAP runs over UDP and needs DTLS for security. Zigbee uses a trust centre with shared keys. BLE has multiple pairing modes with different security levels. There is no universally "secure" protocol — each makes trade-offs between power consumption, range, bandwidth, and security guarantees.

## Formal Definition / Statement
IoT communication protocols operate at different layers of the network stack and serve different use cases:

**Application-layer protocols (over IP):**
- **MQTT (Message Queuing Telemetry Transport)**: Publish/subscribe messaging over TCP. Lightweight, broker-mediated. Standard port 1883 (unencrypted) / 8883 (TLS). Security: TLS + username/password or client certificates.
- **CoAP (Constrained Application Protocol)**: RESTful request/response over UDP. Designed for constrained devices. Standard port 5683. Security: DTLS (Datagram TLS). Lightweight alternative: OSCORE for end-to-end security.

**Link-layer / mesh protocols (non-IP):**
- **Zigbee (IEEE 802.15.4)**: Low-power mesh networking. Security via AES-128-CCM with network key managed by a Trust Centre. Zigbee 3.0 uses install codes for device joining.
- **BLE (Bluetooth Low Energy)**: Point-to-point or mesh. Multiple pairing modes: Just Works, Passkey Entry, Numeric Comparison, OOB. AES-CCM encryption. BLE 5.0+ supports LE Secure Connections (ECDH-based).
- **LoRaWAN**: Long-range, low-power WAN. Class A/B/C devices. Security: AES-128 with AppSKey (application) and NwkSKey (network) session keys. OTAA (Over-The-Air Activation) for key exchange.
- **Thread/Matter**: IPv6-based mesh (IEEE 802.15.4). Thread provides the network layer; Matter provides the application layer. Security: DTLS, ECC-based commissioning, certificate-based device identity.

## Key Properties / Complexity

| Protocol | Transport | Range | Bandwidth | Crypto | Key Management |
|---|---|---|---|---|---|
| MQTT | TCP | LAN/WAN | Moderate | TLS 1.2+ | Broker-managed |
| CoAP | UDP | LAN | Low | DTLS / OSCORE | PSK / RPK / X.509 |
| Zigbee | 802.15.4 | 10-100m | 250kbps | AES-128-CCM | Trust Centre |
| BLE | 2.4GHz | 10-50m | 1-2Mbps | AES-CCM | Pairing/bonding |
| LoRaWAN | LoRa | 2-15km | 0.3-50kbps | AES-128 | OTAA / ABP |
| Thread | 802.15.4 | 10-100m | 250kbps | DTLS + ECC | Commissioner |

- **MQTT** has no native security — it relies entirely on TLS at the transport layer and ACLs at the broker
- **CoAP** with OSCORE provides end-to-end security that survives proxy traversal, unlike DTLS which terminates at each hop
- **Zigbee's** well-known Trust Centre Link Key (ZigBeeAlliance09) is a major vulnerability if install codes are not used
- **BLE** Just Works mode is vulnerable to MITM because it skips authentication
- **LoRaWAN** ABP (Activation By Personalization) uses hardcoded session keys that never rotate
- **Thread/Matter** are the newest and have the strongest default security posture

## Worked Example

**MQTT security failure scenario:**
1. IoT sensor publishes temperature to `home/sensor/temp` on public broker (no auth)
2. Attacker subscribes to `#` (wildcard) — receives all sensor data from all topics
3. Attacker publishes to `home/thermostat/set` — sets temperature to unsafe value
4. No TLS → all data visible in cleartext to any network observer
5. No ACLs → any connected client can publish/subscribe to any topic

**Secure MQTT deployment:**
1. Broker requires TLS (port 8883) with client certificates
2. Each device has unique X.509 certificate provisioned during manufacturing
3. Broker ACLs restrict: sensor can only PUBLISH to its own topic prefix
4. Thermostat can only SUBSCRIBE to its command topic
5. Wildcard subscriptions require admin role

## Common Pitfalls

- Using MQTT without TLS — all data including credentials sent in cleartext
- Relying on BLE "Just Works" pairing for security-critical applications
- Using LoRaWAN ABP with static keys that never rotate
- Assuming Zigbee's AES-128 encryption is secure when the well-known link key is used
- Not realising CoAP over DTLS terminates encryption at proxies (use OSCORE for e2e)
- Treating Thread/Matter as secure by default without verifying commissioning configuration

## Connections

- [[mqtt-security]] — Deep dive into MQTT hardening
- [[coap-security]] — DTLS, OSCORE, and CoAP-specific attack mitigations
- [[ble-security]] — BLE pairing modes, encryption, known vulnerabilities
- [[zigbee-security-model]] — Trust Centre, network key, AES-128-CCM details
- [[iot-device-fundamentals]] — Device capability determines feasible protocols
- [[iot-network-architecture]] — Protocol choice affects network topology
- [[krack-attack]] — WPA2 attack affecting Wi-Fi-based IoT protocols
- [[iot-lecture-2]] — Protocol attacks taxonomy

## Open Questions
- Will Matter's stronger default security displace Zigbee in consumer IoT?
- Can OSCORE scale to large deployments with thousands of constrained devices?
- How will post-quantum cryptography be integrated into resource-constrained protocols like LoRaWAN?
