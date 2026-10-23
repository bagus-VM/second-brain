---
title: "Mining Software Repositories — Lecture 0 Overview (Organization, Schedule, and Course Map)"
tags: [topic, mining-software-repositories, semester-2, course-organization]
course: "Mining Software Repositories"
source_count: 1
status: current
last_updated: 2026-10-22
prerequisites: []
---

## One-line Summary
The organizational deck fixes the frame for the whole course: two lecturers, a Monday lecture
and a Wednesday exercise slot, two preliminary exam dates, an exercise format that changes with
the number of participants, an explicit list of learning goals and prerequisites, and a
three-column map of the content the semester will cover.

## Core Map

```
Lecture 0 — Organization
│
├── People and schedule
│   ├── Prof. Dr. Steffen Herbold, Lukas Schulte
│   ├── Lecture: Monday 10:15-11:45, Building HK 28 – SR 010
│   ├── Exercises: Wednesday 10:15-11:45, Building HK 14b – SR 017
│   └── Everything via Stud.IP (slides, sheets, announcements, literature hints)
│
├── Examination
│   ├── Exam date 1: Wednesday, Feb 10th, 14:00-16:00
│   ├── Exam date 2: Monday, Mar 22nd, 10:00-12:00
│   ├── "The exam dates are preliminary."
│   └── Registration deadline set by the central document of the
│       examinations office — no participation without timely registration
│
├── Exercise rules
│   ├── Weekly, slot chosen freely, alone or in groups
│   ├── Few participants -> individual feedback plus a "Testat"
│   └── Many participants -> everything discussed as a group
│
├── Learning goals
│   ├── Role of MSR for tools and evidence-based software engineering
│   ├── Collecting repository data and enriching it
│   └── Designing MSR studies and tools, and applying all of it
│
├── Prerequisites
│   ├── Machine learning, data science, statistics
│   ├── Software engineering incl. version control, issue tracking, QA
│   ├── Python, pandas, matplotlib, scikit-learn, databases
│   └── -> [[evidence-based-software-engineering]] [[mining-software-repositories]]
│
└── Contents of the lecture (three columns)
    ├── MSR data collection
    │   ├── Data sources and collecting raw data -> [[software-repositories]]
    │   ├── Enriching data with heuristics and manual validation
    │   │       -> [[repository-link-enrichment]]
    │   ├── Visualizing code and its history
    │   └── Software metrics -> [[software-metrics]]
    ├── Empirical methods
    │   ├── Research paradigms -> [[msr-research-paradigms]]
    │   ├── Sampling -> [[msr-sampling]]
    │   ├── Basic statistics and experiment designs
    │   │       -> [[msr-statistical-methods]]
    │   └── Basics of qualitative analysis -> [[grounded-theory]]
    └── Applications of MSR
        ├── Developer social networks -> [[developer-social-networks]]
        ├── Studying social aspects of software engineering
        ├── Understanding defects -> [[defect-prediction]]
        └── Threats to validity -> [[threats-to-validity]]
```

## Key Concepts at a Glance

| Page | Core idea |
|------|-----------|
| [[mining-software-repositories]] | The pipeline the course is built on: repository data, collection, analysis, and the resulting insight or tool |
| [[evidence-based-software-engineering]] | The learning goal's justification — decisions in software engineering should rest on collected evidence, as in medicine |
| [[software-repositories]] | The first content column: a large catalogue of data sources, chosen problem-first rather than convenience-first |
| [[repository-link-enrichment]] | The second half of collection: linking commits, issues, and pull requests, where most MSR noise enters |
| [[software-metrics]] | Turning raw observations into rule-governed numbers that describe a product or a process |
| [[msr-sampling]] | How a study decides which data it looks at and how far its claims travel |
| [[defect-prediction]] | The application side's defect layer: learning from historic defect data to flag likely defective artifacts |
| [[threats-to-validity]] | The closing topic: the structured assessment of how far a result can be trusted |

## Lecture Structure

1. **Administration** — instructors and contact addresses, the lecture slot and room, the exercise
   slot and room, and the pointer to the examinations office page for the registration deadline.
2. **Exam dates** — two candidate dates, both flagged as preliminary, with the warning that
   failing to register in time means not being allowed to take the exam.
3. **Exercise** — a weekly application of lecture concepts; the format adapts to attendance: with
   few participants each group gets individual feedback and a "Testat", with many participants
   everything is discussed as a group from the students' own solutions.
4. **What exercises are and are not** — a two-column slide separating what they provide (feedback,
   hints, learning) from what they are not (a guarantee of a good grade, a programming tutorial, a
   second lecture, a place for administrative questions).
5. **Communication and materials** — Stud.IP carries slides, sheets, announcements and literature
   hints; students must be enrolled in both the lecture and the exercise.
6. **Learning goals and prerequisites** — three goals, and prerequisites spanning machine learning,
   data science, software engineering, programming, and databases.
7. **Contents of the lecture** — the three-column map reproduced above, closing with "Questions?".

## Exam-Relevant Points

1. **The three learning goals are the exam scope.** Knowing MSR's role for tools and
   evidence-based software engineering, understanding collection and enrichment, and being able to
   design studies and tools map one-to-one onto the three content columns.
2. **Two exam dates, both preliminary.** The slides warn about this explicitly, so any date
   printed here may move; the registration deadline is the binding constraint, and failing it
   removes the right to sit the exam.
3. **The exercise is optional in the sense that not doing it does not fail you** — but it is also
   not optional in the sense that you can expect a good grade without solving it.
4. **The prerequisites tell you what the course assumes**: statistics, machine learning, software
   engineering practice, and Python with pandas, matplotlib, and scikit-learn.
5. **The content map is the syllabus.** Collection, enrichment, social aspects, defects, methods,
   and validity are the assessed arc, in that order.

## Connections

- [[mining-software-repositories]] — the course page this organization deck opens.
- [[mining-software-repositories-lecture-1]] — the introduction that defines the field the map
  describes.
- [[mining-software-repositories-exercise-1]] — the first sheet, due 21.10.2026.
- [[mining-software-repositories-exercise-2]] — the second sheet, due 28.10.2026.
- [[evidence-based-software-engineering]] — the learning goal that the introduction expands.
- [[threats-to-validity]] — the last item in the content map and the closing lecture.
- [[msr-research-paradigms]] — the paradigm frame that the methods column presumes.

## Open Questions

- **Credit points, exam format, and weighting are never stated.** The slides give two date/time
  windows and nothing about the type of exam or how the exercise contributes to the grade.
- **The registration deadline itself is not given**; it lives in an external central document
  that is only linked, and the deck's exam dates are labelled preliminary.
- **"Exercises: What they are and are not" promises individual feedback for practical solutions,
  but never says whether that feedback is graded** or whether a "Testat" is required.
- Whether the room and time slots remain stable for the whole semester is not stated.
