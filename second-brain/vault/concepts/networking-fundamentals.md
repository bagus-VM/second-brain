---
title: "Networking Fundamentals"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
Networking fundamentals — the OSI model, TCP/IP, addressing, and routing — are the prerequisite knowledge needed to understand how IoT devices communicate and where that communication can be attacked.

## Core Intuition
Every IoT security vulnerability exists somewhere in the network stack. A weak password is an application-layer problem. Cleartext MQTT is a transport-layer problem. A spoofed MAC address is a link-layer problem. Without understanding the layers, you cannot identify where a vulnerability lives, what it affects, or how to fix it. The OSI model is the map; TCP/IP is the terrain.

## Formal Definition / Statement
The OSI (Open Systems Interconnection) model defines seven layers of network communication:

**Layer 1 — Physical**: Electrical signals, radio waves, optical pulses. IoT relevance: wireless protocols (Wi-Fi, BLE, Zigbee, LoRa) operate here. Jamming and physical layer attacks target this layer.

**Layer 2 — Data Link**: Frames, MAC addresses, switching. IoT relevance: MAC address spoofing, ARP attacks, BLE/Zigbee link-layer encryption. Ethernet (802.3), Wi-Fi (802.11), BLE (802.15.1), Zigbee (802.15.4).

**Layer 3 — Network**: IP addressing, routing. IoT relevance: IPv4/IPv6, 6LoWPAN (IPv6 over low-power networks), routing attacks, IP spoofing. RPL (Routing Protocol for Low-Power and Lossy Networks).

**Layer 4 — Transport**: TCP (reliable, connection-oriented) and UDP (unreliable, connectionless). IoT relevance: MQTT over TCP, CoAP over UDP, TLS/DTLS encryption here. Port scanning targets this layer.

**Layer 5-6 — Session/Presentation**: Session management, data formatting. IoT relevance: TLS handshake (session establishment), data serialization (JSON, CBOR, Protocol Buffers).

**Layer 7 — Application**: Application protocols. IoT relevance: MQTT, CoAP, HTTP, Zigbee ZCL, BLE GATT. Most IoT-specific attacks target this layer.

**TCP/IP Stack (practical model):**
- **Link Layer**: Ethernet, Wi-Fi, BLE, Zigbee
- **Internet Layer**: IPv4, IPv6, ICMP
- **Transport Layer**: TCP, UDP
- **Application Layer**: HTTP, MQTT, CoAP, DNS, DHCP

**Addressing:**
- **MAC address**: Layer 2, hardware-unique (48-bit for Ethernet, 48-bit for BLE)
- **IP address**: Layer 3, logical (IPv4: 32-bit, IPv6: 128-bit)
- **Port**: Layer 4, identifies service (MQTT: 1883, CoAP: 5683, HTTP: 80)
- **6LoWPAN**: Compresses IPv6 for constrained networks (IEEE 802.15.4)

**Routing:**
- Static routing: manually configured paths
- Dynamic routing: OSPF, BGP, RPL (for low-power networks)
- NAT: translates private to public IP addresses

## Key Properties / Complexity

- **IoT uses both TCP and UDP**: MQTT/TCP for reliable messaging, CoAP/UDP for lightweight communication — each has different security implications
- **6LoWPAN compresses IPv6 headers** to fit in 802.15.4 frames — security headers may be stripped or compressed
- **RPL routing protocol** for low-power networks has known attacks (wormhole, sinkhole, selective forwarding)
- **IoT devices often lack standard network stack hardening**: no SYN cookies, no ICMP rate limiting, no port randomization
- **NAT traversal** is a challenge for IoT devices behind home routers — UPnP/PCP can be exploited
- **DNS is a critical dependency**: IoT devices resolving cloud endpoints via DNS are vulnerable to DNS spoofing/cache poisoning
- **Multicast and broadcast** used by discovery protocols (mDNS, SSDP) can be exploited for amplification attacks

## Worked Example

**Network-level attack on IoT:**
1. Attacker on same Wi-Fi network as IoT devices
2. ARP spoofing: attacker sends gratuitous ARP replies claiming to be the gateway
3. IoT devices update ARP tables, route traffic through attacker
4. Attacker performs MITM on cleartext MQTT traffic (port 1883)
5. Attacker captures sensor data and injects false commands
6. Even with TLS, attacker can see which devices communicate (metadata)

**Defence:**
1. Static ARP entries for critical devices (not scalable but effective for gateways)
2. 802.1X port-based authentication on switches
3. DHCP snooping and dynamic ARP inspection on managed switches
4. TLS for all MQTT traffic (prevents cleartext interception)
5. VPN tunnel for IoT device-to-cloud communication

## Common Pitfalls

- Not understanding that BLE/Zigbee operate at Layer 2, not Layer 3 — different security model than IP
- Assuming TLS protects against all network attacks (it doesn't protect against DNS spoofing)
- Using static IP addresses on IoT devices without proper DHCP reservation
- Not considering 6LoWPAN header compression's impact on security
- Ignoring Layer 2 attacks (ARP spoofing, MAC flooding) on IoT networks
- Not monitoring IoT network traffic for anomalies

## Connections

- [[network-security-fundamentals]] — Security mechanisms applied to the networking layers
- [[iot-network-architecture]] — How networking layers map to IoT architecture tiers
- [[iot-communication-protocols]] — Protocols operate at different OSI layers
- [[ble-security]] — Layer 2 security for BLE
- [[zigbee-security-model]] — Layer 2 security for Zigbee
- [[coap-security]] — Layer 4 (UDP) + Layer 7 security for CoAP
- [[mqtt-security]] — Layer 4 (TCP) + Layer 7 security for MQTT
- [[iot-lecture-1]] — Networking as a prerequisite for IoT security

## Open Questions
- How does the transition from IPv4 to IPv6 affect IoT security posture?
- Can RPL be hardened against routing attacks without excessive overhead for constrained devices?
- What is the right network architecture for IoT devices that need both local and cloud connectivity?
