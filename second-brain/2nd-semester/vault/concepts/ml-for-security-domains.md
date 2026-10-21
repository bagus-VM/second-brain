---
title: "ML for Security Domains: Network, Endpoint, Application, User and Process"
tags: [concept, ml-security, semester-2, security-domains]
course: "Machine Learning for Cybersecurity"
source_count: 1
status: current
last_updated: 2026-10-19
prerequisites: ["[[ml-task-taxonomy]]"]
---

## One-line Summary

L1 maps the same three tasks — regression, classification, clustering — onto five security domains, showing that the tasks transfer while the features, the labels and the difficulty do not.

## Core Intuition

Each domain asks a different question about a different object. Network protection asks whether this traffic is normal; endpoint protection whether this program or process is malicious; application security whether this request is an attack; user behaviour whether this person is behaving like themselves; process behaviour whether this transaction fits the business process. The object determines the data, which determines whether labels exist — which is why "classification" is easy on spam and near-impossible on user behaviour.

L1's framing sentence matters as much as the table: *machine learning is not a silver bullet for cybersecurity*.

## Formal Definition / Statement

| Domain | Scope on the slide | Regression | Classification | Clustering |
|---|---|---|---|---|
| **Network protection** | areas and protocols (Ethernet, wireless, SCADA, SDNs); IDS traditionally signature-based, some ML used for years; NTA analyses all traffic and each layer | predict packet parameters, compare with learned "normal" behaviour | attack classes: scanning, spoofing, DoS | forensic analysis |
| **Endpoint protection** | every endpoint has specifics, but common ML tasks; solutions differ by type (workstation, server, mobile, PLC, IoT); anti-virus observes executable features or process behaviour | predict the next system call | malware, spyware, ransomware | secure email gateways (separate legitimate attachments from outliers) |
| **Application security** | web apps, databases, ERP, SaaS, microservices; WAFs and static/dynamic code analysis | anomalies in HTTP requests (XXE, SSRF, auth bypass) | known injections (SQLi, XSS, RCE) | user activity, for DDoS and mass exploitation |
| **User behaviour** | SIEM solves many tasks if configured properly, but not all; domain, application, SaaS, social and messenger accounts all need monitoring | anomalies in user actions (login at an unusual time) | group users for peer-group analysis | separate groups of users, detect outliers |
| **Process behaviour** | requires knowing the business process; banking/retail fraud vs. a plant floor in manufacturing demand different domain knowledge | predict the next user action, detect credit-card fraud | known types of fraud | compare business processes, detect outliers |

## Key Properties

- **The task column is constant, the difficulty is not.** Regression appears in all five domains, yet only user behaviour is described as an unsupervised problem.
- **User behaviour is the domain without labels.** L1: "as a rule, there is no labelled dataset as well as any idea of what to look for". Malware detection, by contrast, focuses on common attacks and permits training a classifier.
- **Application security is explicitly not universal.** "It is almost impossible to build a universal ML model to deal with all threats effectively" — solve some tasks, not all.
- **Process behaviour is where features are the bottleneck.** Features differ in every process, so how you represent data to the algorithm is essential.
- **SIEM is necessary but insufficient.** It handles a lot when configured properly; the account surface has outgrown rule configuration. All of it also depends on data access: direct APIs and swift log extraction.

## Worked Example

In **application security** the classes are known and named (SQLi, XSS, RCE) and payloads are plentiful, so a supervised classifier is obvious. In **network protection** the classes are also known (scan, spoof, DoS) but traffic is high-volume and opaque, so features come from packet metadata and the regression variant often fits better. In **user behaviour** there are no classes to learn, so classification survives only as peer-group analysis and the detection job falls to clustering. Same three words on the slide; three engineering problems.

## Common Pitfalls

- **Assuming the domain dictates the task.** All three tasks appear in every domain; the domain dictates the data.
- **Treating anomaly detection as threat detection.** L1: correlation does not imply causation; outliers may come from chance, new applications or workforce changes, producing false positives that need manual investigation. ML's contribution is to evaluate risk *beyond* the outlier, using history.
- **Expecting one model per organisation.** Application security alone spans web apps, databases, ERP, SaaS and microservices.
- **Ignoring endpoint heterogeneity.** A model for workstations does not transfer to a PLC or an IoT device.
- **Skipping business-process knowledge.** Without it, "anomalous" is undefined.

## Connections

- [[ml-task-taxonomy]] — the six families; this page is the domain axis.
- [[security-terminology-and-risk-model]] — each domain protects a different asset class.
- [[attacker-classification]] — user-behaviour monitoring is the control that matters against insiders.
- [[ml-learning-paradigms]] — why user behaviour is unsupervised by necessity.

## Open Questions

- No metrics appear, so the five domains cannot be compared for maturity.
- "Process behaviour" and "user behaviour" overlap in the credit-card example, which appears under both.
