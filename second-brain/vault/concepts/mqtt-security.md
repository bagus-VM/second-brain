---
title: "MQTT Security"
tags: [concept, iot-security, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: ["[[iot-communication-protocols]]"]
---
## One-line Summary
MQTT security covers TLS encryption, authentication methods, access control lists, and broker hardening for the publish/subscribe messaging protocol used by most IoT cloud platforms.

## Core Intuition
MQTT has no built-in security — it relies entirely on external mechanisms. The broker is the single point of trust: it authenticates clients, enforces topic-level access controls, and (optionally) encrypts transport. A misconfigured broker is an open door — and many are. Public MQTT brokers without authentication are trivially exploitable: anyone can subscribe to all topics and publish commands to any device.

## Formal Definition / Statement
MQTT (Message Queuing Telemetry Transport) is a lightweight publish/subscribe messaging protocol over TCP (default port 1883, TLS port 8883). Current version: MQTT 5.0 (2019).

**Security Mechanisms:**

**Transport Security:**
- TLS 1.2+ for encrypted transport (MQTT over TLS, port 8883)
- Mutual TLS (mTLS): both broker and client present X.509 certificates
- WebSocket transport (MQTT over WSS) for browser-based clients

**Authentication:**
- Username/password in CONNECT packet (cleartext without TLS!)
- Client certificates (X.509) — strongest option, requires PKI infrastructure
- OAuth 2.0 tokens (MQTT 5.0 enhanced authentication)
- Token-based authentication (JWT, API keys) via custom broker plugins

**Authorization (Access Control):**
- Topic-level ACLs: define which clients can PUBLISH or SUBSCRIBE to which topics
- Pattern-based ACLs: `sensors/{clientid}/#` — client can only access its own topics
- Role-based access control (RBAC): group clients by role with different topic permissions
- Wildcard restrictions: limit use of `#` (all topics) and `+` (single-level) wildcards

**MQTT 5.0 Security Enhancements:**
- Enhanced Authentication (SASL-based, pluggable auth mechanisms)
- Reason codes on all acknowledgments (better error handling)
- Topic aliases (reduce overhead, potential for confusion attacks if not managed)
- User properties (custom metadata for security context)
- Session expiry (automatic cleanup of abandoned sessions)

## Key Properties / Complexity

- **Broker is the trust anchor**: All security enforcement happens at the broker; if compromised, all connected devices are exposed
- **Topic design is security design**: Topic hierarchy must encode authorization boundaries (e.g., `/org/device/data` for multi-tenant isolation)
- **Retained messages** can leak data: a retained message on a topic is delivered to every new subscriber, including attackers
- **Will messages** (Last Will and Testament) can be abused to trigger actions on disconnect
- **QoS levels affect security**: QoS 2 (exactly-once) creates more state at the broker, increasing DoS surface
- **Shared subscriptions** (MQTT 5.0) introduce load balancing but complicate authorization
- **Clean session vs persistent sessions**: Persistent sessions store messages for offline clients — larger attack surface if client credentials are compromised

## Worked Example

**Exploiting an open MQTT broker:**
```bash
# Connect to open broker (no auth)
mosquitto_sub -h vulnerable-broker.com -t '#' -v

# Receive all published data:
# home/sensor/temperature 22.5
# home/sensor/humidity 45
# home/lock/status unlocked
# industrial/plc/pressure 150.2

# Inject false data:
mosquitto_pub -h vulnerable-broker.com -t 'home/thermostat/set' -m '40'

# Trigger actuator:
mosquitto_pub -h vulnerable-broker.com -t 'home/lock/command' -m 'unlock'
```

**Hardened MQTT deployment:**
```mosquitto.conf
# TLS required
port 8883
cafile /etc/mosquitto/ca.crt
certfile /etc/mosquitto/server.crt
keyfile /etc/mosquitto/server.key
require_certificate true
use_identity_as_username true

# ACL file
acl_file /etc/mosquitto/acl

# Connection limits
max_connections 1000
max_inflight_messages 20
```

## Common Pitfalls

- Using MQTT without TLS — credentials and data in cleartext
- Using the `#` wildcard in production subscriptions (receives ALL traffic)
- Not implementing topic-level ACLs — any authenticated user can publish anywhere
- Hardcoding broker credentials in firmware (extractable via firmware analysis)
- Not limiting connection rates — broker can be DoS'd with connection floods
- Ignoring retained messages — sensitive data persists in the broker
- Using MQTT 3.1.1 instead of 5.0 for new deployments (missing security features)

## Connections

- [[iot-communication-protocols]] — MQTT in the protocol landscape
- [[coap-security]] — Compare CoAP and MQTT security models
- [[zigbee-security-model]] — Zigbee uses different trust model (Trust Center)
- [[key-management-lifecycle]] — Certificate management for mTLS
- [[network-security-fundamentals]] — TLS fundamentals
- [[iot-network-architecture]] — MQTT broker placement in the architecture
- [[iot-lecture-2]] — MQTT exploitation in the protocol attacks taxonomy
- [[device-provisioning]] — Certificate provisioning for MQTT clients

## Open Questions
- How should MQTT brokers handle certificate revocation at IoT scale (millions of devices)?
- Can MQTT 5.0's enhanced authentication replace client certificates for constrained devices?
- What is the right topic hierarchy design for multi-tenant IoT platforms?
