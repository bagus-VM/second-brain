---
title: "Denial of Service (DoS) in IoT"
tags: [concept, iot-security, attacks, semester-1]
course: "IoT Security"
source_count: 1
status: current
last_updated: 2026-06-22
prerequisites: []
---
## One-line Summary
*Attacks that make IoT devices or services unavailable to legitimate users, ranging from simple resource exhaustion to large-scale distributed botnets.*

## Core Intuition
IoT devices are particularly vulnerable to DoS because they have limited resources. A Raspberry Pi can handle a flood of requests; a microcontroller with 32KB of RAM cannot. Worse, compromised IoT devices are increasingly used as weapons in DDoS attacks against others. The Mirai botnet showed that millions of insecure IoT devices can generate traffic volumes that overwhelm even well-provisioned targets.

## Formal Definition / Statement
Denial of Service (DoS) attacks against IoT:

**Against the IoT Device:**
- **Resource exhaustion**: Flood the device with requests until it runs out of memory, CPU, or battery
- **Connection flooding**: Exhaust the device's limited connection table (e.g., SYN flood on a constrained TCP stack)
- **Protocol abuse**: Send malformed packets that crash the device's protocol parser
- **Jamming**: Radio frequency interference that blocks wireless communication (Wi-Fi, BLE, Zigbee)
- **Battery drain**: Repeatedly wake a sleeping device to exhaust its battery
- **Bricking**: Corrupt firmware to render the device permanently unusable

**Against IoT Infrastructure:**
- **Amplification attacks**: Use IoT devices to amplify traffic (e.g., CoAP amplification: small request → large response)
- **Botnet DDoS**: Compromised IoT devices coordinated to flood a target (Mirai generated 1.2 Tbps)
- **DNS tunnelling abuse**: Use IoT devices as DNS relay for DDoS amplification
- **API flooding**: Overwhelm the cloud backend with requests from thousands of devices

**Against IoT Ecosystem:**
- **Service disruption**: Take down the management platform so devices can't be controlled
- **Update mechanism abuse**: Flood the update server to prevent legitimate devices from updating
- **Certificate revocation flooding**: Mass-revoke certificates to disrupt fleet operations

## Key Properties / Complexity
- IoT devices typically handle 10-100 concurrent connections; enterprise servers handle millions
- Battery-powered devices are vulnerable to energy-depletion attacks
- Wireless jamming requires proximity but is extremely effective
- CoAP amplification factor can be 10-30x (small request, large response)
- Mirai-class botnets can generate Tbps-level traffic
- DoS on safety-critical IoT (medical, industrial) can cause physical harm

## Worked Example
DoS attack and defence for an IoT fleet:

**Attack**: Attacker targets a smart building's HVAC control system
1. Scan: Find 200 HVAC controllers on the building's Wi-Fi network
2. Resource exhaustion: Send rapid CoAP GET requests to each controller
3. Each controller allocates memory for the response, runs out of RAM
4. Controllers stop responding to legitimate temperature readings
5. Building management system loses visibility into HVAC status
6. Temperature rises to dangerous levels server room

**Defence:**
1. **Rate limiting**: Each controller accepts max 10 requests/second per source IP
2. **Network segmentation**: HVAC controllers on isolated VLAN, accessible only from management subnet
3. **CoAP rate limiting**: Response size limited to prevent amplification
4. **Watchdog timer**: Hardware watchdog reboots controller if it hangs for >30 seconds
5. **Intrusion detection**: Alert on unusual traffic patterns (sudden spike in CoAP requests)
6. **Graceful degradation**: Controllers continue local operation even when network is saturated

## Common Pitfalls
- **DoS is easy, defence is hard**: DoS attacks require minimal sophistication; defending against them is complex
- **DDoS from IoT is growing**: As more insecure IoT devices are deployed, botnet capacity grows
- **False positives**: Rate limiting can block legitimate traffic during peak usage
- **Physical layer jamming**: No software defence against RF jamming — requires physical security
- **Cost of defence**: DDoS mitigation services are expensive for small IoT vendors
- **Cascading failures**: DoS on one component can cascade through interconnected systems

## Connections
- [[iot-common-attacks]] — DoS is one of the most common IoT attack categories
- [[mirai-botnet]] — The canonical example of IoT-enabled DDoS
- [[iot-secure-design]] — Secure design includes DoS resilience
- [[network-security-fundamentals]] — Network-level DoS mitigation techniques
- [[availability]] — DoS directly targets the availability component of the CIA triad
- [[coap-security]] — CoAP protocol is particularly susceptible to amplification attacks

## Open Questions
- How does this concept apply in practice with real-world constraints?
- What are the deeper implications that aren't immediately obvious?
