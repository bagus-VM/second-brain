---
title: "Virtual Machines and Runtime Systems — Lecture 0 Overview (Organizational Matters)"
tags: [topic, virtual-machines, semester-2]
course: "Virtual Machines and Runtime Systems"
source_count: 1
status: current
last_updated: 2026-10-30
prerequisites: []
---

## One-line Summary
The seven-slide organizational deck: lecturer, rooms, the two exam dates, the lecture's full
contents map, the tutorial language policy (C/C++, maybe Rust), and the one course textbook.

## Core Map

```
s00.pdf — Organizational Matters (Dr. Armin Größlinger, WS 2026/27)
│
├── Lecturer: Armin Größlinger — lecture AND tutorials
│           IM 103, armin.groesslinger@uni-passau.de
├── Dates
│   ├── Lecture:  Tuesdays 16:00–17:30, (IM) SR 007
│   └── Tutorial: Wednesdays 12:15–13:45, (IM) HS 12
├── Examination: written
│   ├── 1st exam: Thursday, 11.02.2027, 14:00–15:30
│   ├── 2nd exam: Thursday, 01.04.2027, 14:00–15:30
│   ├── 90 minutes; rooms via Stud.IP
│   └── register in time via Campus Portal
├── Module: 6 ECTS — Master Informatik "Programmierung und Softwaresysteme"
│           / M.Sc. Computer Science (Focus "Programming and Software Systems")
├── Contents of the lecture
│   ├── Introduction to virtualization
│   ├── Runtime systems (C runtime, processes, thread scheduling,
│   │       memory management, runtime systems for high-level languages)
│   ├── Virtual machines (types: system VMs, process VMs, high-level
│   │       language VMs; implementation: interpreter, compiler, GC;
│   │       instrumentation; applications)
│   └── Containers ("light-weight virtualization"): Linux namespaces,
│           Kubernetes
├── Tutorials: C and C++, maybe Rust; quick C/C++ intro on October 21
│           (no tutorial session on October 14); The C Book online
└── Literature: J. Smith, R. Nair, Virtual Machines, Morgan Kaufmann, 2005
```

## What the Deck Actually Says

- **One person runs everything**: Armin Größlinger gives both the lecture and the tutorials
  (office IM 103, `armin.groesslinger@uni-passau.de`).
- **Exam registration is the student's job** — "Do not forget to register in time via Campus
  Portal!", with the examination office's semester-information page linked for registration
  periods.
- **The contents slide is the course's own table of contents**, and it ranges wider than the
  first two lectures suggest: after virtualization basics and the C runtime it goes on to
  memory management, runtime systems for *high-level* languages, the three VM types, their
  implementation techniques (interpreter, compiler, garbage collection), instrumentation, and
  finishes with containers — Linux namespaces and Kubernetes.
- **Tutorial language policy**: C and C++, "maybe Rust". A quick introduction to some aspects of
  C/C++ happened in the tutorial session of October 21; there was **no tutorial session on
  October 14**. Two free online references are named: *The C Book*
  (publications.gbdirect.co.uk/c_book) and cplusplus.com.
- **The textbook** is J. Smith & R. Nair, *Virtual Machines* (Morgan Kaufmann, 2005) — the
  classic systems-VM text, shown with its cover.

## Exam-Relevant Points

1. **Two exam dates, both Thursday 14:00–15:30**: **11.02.2027** and **01.04.2027**, 90 minutes
   each, rooms announced in Stud.IP.
2. **Registration via Campus Portal is mandatory and time-bound** — the one instruction the
   deck underlines.
3. **The contents slide is the scope map**: everything from abstraction/virtualization to
   containers and Kubernetes is fair game, which makes the later lectures' arrival in `raw/`
   worth tracking.
4. **6 ECTS**, Master's module "Programmierung und Softwaresysteme" / M.Sc. CS focus
   "Programming and Software Systems".

## Connections

- [[virtual-machines-and-runtime-systems-lecture-1]] — the first real lecture: the abstraction
  vs virtualization definitions this deck's contents slide promises.
- [[virtual-machines-and-runtime-systems-lecture-2]] — the C runtime system, the second block
  on the contents slide.
- [[virtual-machines-and-runtime-systems-exercise-1]], [[virtual-machines-and-runtime-systems-exercise-2]]
  — the tutorial side, running in C per the language policy.
- [[runtime-system]] — the concept page for the course's central object.

## Open Questions

- The deck names **no attendance policy and no grading split** (exam only vs tutorials counted)
  — nothing here settles how much the exercises weigh.
- "Maybe Rust" in the tutorials is never resolved in the material seen so far.
- Whether the 2nd exam requires failing the 1st, or is an ordinary resit, is not stated.
