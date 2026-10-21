---
title: "AI Engineering Lab (Block Seminar)"
tags: [course, semester-2, ai-engineering]
semester: "SoSe 2026"
exam_date: "report-based"
credits: "TBD"
language: "English"
source_count: 2
status: current
last_updated: 2026-10-19
prerequisites: []
---

## One-line Summary
A build-an-agent-harness lab: Group 11 built **StudyMate**, an autonomous study agent that compiles lecture material into an Obsidian knowledge base, with persistent memory, subagents, permissions, and production observability.

## What the Deliverable Actually Is

Not an exam. A working harness plus an IEEE-format report and an oral defence. The group's artifacts live in this vault:

- Report sources and builders: `vault/topics/Ai Engineering Lab/report/` — `build_report_ieee.py`, `report_spec.json`, figure generators, `StudyMate_report_IEEE_plain2.pdf`
- Study material produced during the project: `oral-exam-study-guide.md` (1506 lines), `Plain Language Study Notes.md`, `memory-architecture.md`, `call-graph.md`
- Code: `projects/group-11/` — `src/study_agent/` (engine, memory with embeddings + rerank + retrieval + store, tools, MCP client, subagents), `tests/` (~40 test modules), `observability/` (Prometheus rules, Langfuse dashboard provisioning)

## Architecture (from the repo README and report figures)

- **Agent loop:** ReAct-style reason/act cycle over an LLM client with a mock backend for tests
- **Memory:** facts, procedures, threads; embedding-based retrieval with reranking; compaction when context fills
- **Tools:** file operations, terminal, MCP (stdio + external sessions), vault linter
- **Delegation:** subagents with their own context, permission events, and trace spans
- **Observability:** spans for LLM calls, tool calls, subagent runs, permission decisions; dashboards provisioned programmatically into Langfuse + Prometheus/Grafana

## Why It Belongs in This Vault

StudyMate is the same idea as this vault, implemented as software: raw sources in, atomic cross-linked notes out, memory that persists, gaps surfaced instead of hidden. The report's "beyond minimums" section is the honest part — what was built past the brief and what was deliberately not pursued.

## Open Questions

- Group report is a group artifact; the individual IEEE report is a separate file. Keep them distinct when citing.
- The repo's `daily_reports/` holds 37 daily logs across three authors — useful evidence for the report, not yet synthesized into vault pages.
