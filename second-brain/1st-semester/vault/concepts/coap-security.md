---
title: "CoAP Security"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[iot-communication-protocols]]"]
---
## One-line Summary
CoAP (Constrained Application Protocol) security covers DTLS for transport encryption, OSCORE for end-to-end application security, and the unique challenges of securing a UDP-based REST protocol on resource-constrained devices.

## Core Intuition
CoAP is HTTP for constrained devices — it uses the same REST verbs (GET, POST, PUT, DELETE) but over UDP instead of TCP. This saves power and bandwidth but loses TCP's reliability and ordered delivery. Security comes in two flavors: DTLS (like TLS but for UDP) protects the transport hop-by-hop, while OSCORE protects messages end-to-end through proxies. The choice between them has major architectural implications.

## Formal Definition / Statement
CoAP (RFC 7252) is an application-layer protocol for constrained devices operating over UDP (default port 5683, secured port 5684).

**DTLS (Datagram Transport Layer Security):**
- Provides confidentiality, integrity, and authentication for UDP transport
- Three modes:
  - **Pre-Shared Keys (PSK)**: Symmetric keys pre-configured on client and server. Lowest overhead. Suitable for constrained devices.
  - **Raw Public Keys (RPK)**: Asymmetric keys without certificate infrastructure. Moderate overhead. No CA dependency.
  - **X.509 Certificates**: Full PKI with certificate chains. Highest overhead. Best for enterprise deployments.
- DTLS 1.2 (RFC 6347) current standard; DTLS 1.3 (RFC 9147) adds reduced handshake latency
- **Limitation**: DTLS terminates at each hop — if traffic passes through a CoAP proxy, the proxy decrypts and re-encrypts, breaking end-to-end security

**OSCORE (Object Security for Constrained RESTful Environments, RFC 8613):**
- Provides end-to-end security for CoAP messages that survives proxy traversal
- Protects the CoAP payload and selected header fields using AEAD (AES-CCM or AES-GCM)
- Uses a Security Context with Sender ID, Recipient ID, and Master Secret
- Lightweight: adds ~20 bytes overhead per message
- Supports replay protection via sequence numbers
- Can be combined with DTLS for layered security (transport + application)

**CoAP-Specific Threats:**
- **IP spoofing**: UDP source addresses are trivially spoofable; CoAP responses can be redirected
- **Amplification attacks**: Small CoAP requests can generate large responses (especially with block-wise transfers), enabling DDoS amplification
- **Cross-protocol attacks**: CoAP-to-CoAP or CoAP-to-HTTP proxy vulnerabilities
- **Resource exhaustion**: Constrained devices have limited connections; flooding with CON (confirmable) messages drains resources

## Key Properties / Complexity

- **DTLS handshake cost**: Full DTLS handshake requires 2 round trips (DTLS 1.2) or 1 RTT (DTLS 1.3) — significant on high-latency LPWAN links
- **PSK is most practical** for constrained IoT but requires secure key distribution
- **OSCORE message size overhead** is ~20 bytes — acceptable for most payloads but significant for very small sensor readings
- **CoAP block-wise transfer** (RFC 7959) allows large payloads but creates amplification attack surface
- **Observe (RFC 7641)** subscriptions create long-lived state — DoS potential if subscriptions are not rate-limited
- **CoAP over TCP (RFC 8323)** exists for environments where UDP is problematic, enabling standard TLS instead of DTLS
- **Group OSCORE** extends OSCORE for multicast CoAP, relevant for IoT command-and-control

## Worked Example

**CoAP amplification attack:**
1. Attacker spoofs victim's IP as source, sends small CoAP GET to `/sensors/data` on thousands of CoAP servers
2. Each server responds with large sensor data payload (amplification factor 10-50x)
3. Victim receives flood of unsolicited CoAP responses
4. Mitigation: CoAP servers validate source IP via Echo option (RFC 9175)

**OSCORE end-to-end protection:**
1. Sensor generates temperature reading
2. OSCORE encrypts payload with AES-CCM-128/64 using shared Master Secret
3. Adds Sender Sequence Number for replay protection
4. Message traverses CoAP proxy — proxy forwards without decrypting payload
5. Cloud server decrypts with matching Security Context
6. Even a compromised proxy cannot read or modify the sensor data

## Common Pitfalls

- Using CoAP without DTLS or OSCORE — all data including credentials in cleartext over UDP
- Not implementing the CoAP Echo option, leaving servers open to amplification attacks
- Confusing DTLS (hop-by-hop) with OSCORE (end-to-end) — they solve different problems
- Not handling DTLS session resumption — full handshake on every reconnection is expensive
- Ignoring CoAP's UDP nature — no built-in congestion control, packet ordering, or reliability
- Using self-signed certificates without proper validation — trivial MITM

## Connections

- [[iot-communication-protocols]] — CoAP in the protocol landscape
- [[mqtt-security]] — Compare CoAP and MQTT security models
- [[network-security-fundamentals]] — DTLS as transport security
- [[key-management-lifecycle]] — PSK distribution and rotation for CoAP
- [[iot-device-fundamentals]] — Resource constraints drive CoAP design choices
- [[iot-lecture-2]] — CoAP exploitation in the protocol attacks taxonomy

## Open Questions
- Will DTLS 1.3 adoption accelerate with its reduced handshake latency?
- Can OSCORE be practically deployed in large-scale mesh networks with thousands of devices?
- How should CoAP servers handle the growing problem of open relays used for DDoS amplification?
