---
title: "Scaling Database Systems - Exercise Kickoff and Tooling"
tags: [topic, scaling-database-systems, semester-2, exercise]
course: "Scaling Database Systems"
source_count: 4
status: current
last_updated: 2026-10-20
prerequisites: []
---

## One-line Summary
Everything the course has told you so far is logistics: when to show up, what to bring, how to run a container, how to hand in a milestone.

## Core Map

```
Scaling Database Systems (Chair of Scalable Database Systems, Passau)
├── Exercise groups - 3, same content, from 21/22 Oct 2026
│   ├── Wed 12:15-13:45 (ITZ) SR 004 | Thu 14:15-15:45 (ITZ) SR 001
│   ├── Thu 16:00-17:30 (ITZ) SR 004
│   └── sign-up 16 Oct -> 20 Oct 23:59, cap 30
├── Sheets (Stud.IP)
│   ├── sheet 1: Tue 20 Oct 18:00 -> DURING session 1
│   ├── sheet n>1: Fri 18:00 before -> BEFORE session
│   └── Stud.IP forum for questions outside sessions
├── Submissions -> Praktomat (praktomat.sdbs.fim.uni-passau.de)
│   ├── instance "Scaling Database Systems" / "Wintersemester 26/27"
│   ├── own account per instance, ZIM-name@ads.uni-passau.de, activation link
│   ├── deadline per exercise, auto check, no grades
│   └── Final Solution = most recent passing upload
├── Testing -> Docker
│   ├── local install (docs.docker.com/get-docker/) + hello-world
│   └── server "narrow-sea" (rootless Docker, per-user daemon)
│       ├── FIM account required, request by 19 Oct 2026
│       ├── university network only (VPN from home)
│       └── systemctl --user start docker on EVERY connect
└── The project -> miniHive
    ├── minimalistic version of Hive
    ├── command line + Python, no GUI in container
    └── >= 8 GiB main memory recommended
```

## What the Kickoff Sheets Say

The four ingested sheets are organisational and fit one process. The mechanics are recorded in full on the three concept pages; what follows is the workflow.

- **Sessions.** Three groups, same content, from 21/22 October 2026. You assign yourself to one group; sign-ups run from 16 October 2026 at 14:00 to 20 October 2026 at 23:59, each capped at 30. Bring your device.
- **Sheets.** The first sheet is published in Stud.IP on 20 October at 18:00 and is worked on *during* the first session. From the second sheet on, material appears at 18:00 on the Friday before and is worked on *before* the session. That inversion is the most consequential detail here: the rhythm changes after session one. Questions outside sessions go to the Stud.IP forum.
- **Submissions.** Praktomat handles all submissions, milestones included. No submission may be made public: no milestone code in the Stud.IP forum, no upload into a public GitHub repository. Plagiarism affects creator and copier.
- **Prerequisites.** The course builds miniHive, a minimalistic version of Hive, with extensive use of the command line and Python. Basic Bash usage, the concept and basic usage of Git, and basic usage of SSH are required; the sheet links free material for all three. At least 8 GiB of memory is recommended; support on your device is limited.
- **Docker server.** narrow-sea gives all participants an identical setup regardless of local OS. It needs a FIM account, separate from the ZIM account used for Stud.IP, and access is requested by 19 October 2026. The server is reachable only within the university network; from home you need a VPN. Docker runs rootless with a per-user daemon, and `systemctl --user start docker` must run on every connection. Hardware is shared: postpone, keep deadlines.
- **Praktomat.** Not integrated with university authentication, and each instance has its own accounts, so registration is required again even with an older instance. Only `ZIM-name@ads.uni-passau.de` addresses are accepted, and first login requires a disclaimer. Each exercise shows its deadline; after it, submission is impossible and email or paper hand-ins are not accepted. Submissions are checked automatically, never graded.

## Key Concepts at a Glance

| Page | One-line idea |
|------|---------------|
| [[minihive-project-structure]] | What the project is and what working on it costs |
| [[praktomat-submission-workflow]] | The submission state machine and the Final Solution rule |
| [[rootless-docker-server-access]] | The shared Docker host, how to get in, why it is rootless |
| [[scaling-database-systems]] | The course page: groups, sheets, deadlines |

## Before the First Session - Checklist

1. **Join a group** before 20 October 2026, 23:59.
2. **Create a FIM account** if you use narrow-sea, and mail the account name to `sds-tutorials@uni-passau.de`, subject "Docker Server Access", by 19 Oct 2026.
3. **Set up Docker**, locally or on narrow-sea, verify with hello-world.
4. **Install an OpenSSH client** (Windows OpenSSH feature; Linux/macOS `openssh`).
5. **Register on Praktomat** for the "Wintersemester 26/27" instance, activate via the emailed link, accept the disclaimer.
6. **Read the first sheet**, in Stud.IP from 20 October at 18:00; bring your device.
7. **Verify the tooling**: Bash, Git, SSH, and 8 GiB of memory.

## Exam-Relevant Points

The exam content is not in the ingested material. Nobody can say what will be asked, and nothing here predicts topics. Two things are established, and both are structural rather than topical:

- **The workflow is deadline-driven.** Every sheet is published on a fixed schedule, every exercise carries a hard cutoff with no alternative submission channel, and checking runs automatically rather than through a lecturer reading your work. Whichever milestones exist, the discipline is the same: work before the session, submit before the deadline, verify locally.
- **The tooling is a prerequisite, not a convenience.** Bash, Git, SSH, and Docker are stated as required skills, and the container has no GUI at all. Every milestone depends on that stack working before the first session, not during it.

Nothing else about the assessment is known: exam date, format, credit points, milestone list, and weighting are absent.

## Connections

- [[scaling-database-systems]] — the course page: schedule, groups, ingestion.
- [[minihive-project-structure]] — the artefact each milestone works on, and its constraints.
- [[praktomat-submission-workflow]] — where the work must arrive, how a passing submission survives.
- [[rootless-docker-server-access]] — where the test runs happen, why the environment is identical.
- [[containerization-for-builds]] — the practice the test container instantiates.
- [[docker-compose]] — how a multi-container environment would be described; use by the course is unstated.
- [[multi-stage-docker-build]] — relevant once a milestone image is assembled from layers.
- [[git-branching-and-merging]] — the version-control skill the sheet demands.
- [[git-commit-hygiene]] — commit discipline for the same reason.
- [[reproducible-builds]] — why a container is used: the artefact must run the same.
- [[client-server-db-architecture]] — a database concept the course name points at; not ingested.
- [[sqlite-architecture]] — another database concept the course may touch; the sheets are silent.

## Open Questions

- The technical content of the course has not been ingested. Everything above is logistics; no lecture claim is recorded.
- The content of the exercise sheets is unknown. Only their publication times and role are known.
- The milestone list, its boundaries, and their grading are not in the material.
- Whether the first sheet of 20 October was handled in the session of 21/22 October is unstated.
- The exam date, format, and credit points are unknown.
- Whether students work on milestones in groups, and how Git is coordinated, is not stated.
- Whether the course uses Docker Compose or other build tooling beyond the test container is unstated.
