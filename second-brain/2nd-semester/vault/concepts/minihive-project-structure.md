---
title: "The miniHive Project"
tags: [concept, scaling-database-systems, semester-2]
course: "Scaling Database Systems"
source_count: 3
status: current
last_updated: 2026-10-20
prerequisites: ["[[scaling-database-systems]]"]
---

## One-line Summary
miniHive is the term project of Scaling Database Systems: a minimalistic version of Hive, built on the command line in Python and tested inside a Docker container.

## Core Intuition

The project exists to make the course's subject matter physical. A theoretical field is learned
one way, from slides; a course whose deliverable is a running program is learned another, by
breaking it. So the course does the obvious, and pedagogically expensive, thing: it hands you a
miniature of the real thing and makes you build it.

What "the real thing" is, the ingested sheets do not say. The prerequisites sheet names the project
and its toolchain, and stops there.

Two properties carry most of the weight. First, **the deliverable is a working program, not a
written answer.** The sheet states that the work makes "extensive use of the command line
(terminal) and Python". A build that only works in an IDE with a mouse does not pass. Second,
**the environment is identical for everyone.** A Docker container is provided to test the
implementation, and the course provides a shared server precisely so that all participants have
the same setup regardless of their local operating system. Whether grading of a milestone depends
on whose laptop produced it is not stated in the sheets — but the identical-environment property is
exactly what would make such a dependency harmless.

The consequence students underestimate: the *interface* of this project is a terminal. The sheet
states it as a warning rather than a feature — the miniHive container has no graphical user
interface. Bash competence is not a nicety; it is a requirement, because there is no alternative
path through the container.

## Formal Definition / Statement

What the ingested prerequisites sheet states, precisely and completely:

- **The artefact.** "In this course, you will build miniHive, a minimalistic version of Hive."
- **The substrate.** "You will make extensive use of the command line (terminal) and Python."
- **The test environment.** "Further, there will be a Docker container for you to test your
  implementation."
- **Required skills for the first session.** A working Docker setup, plus (a) basic Bash command
  line usage in Linux, (b) concept and basic usage of Git, (c) basic usage of SSH.
- **The Bash clause.** "This is important, the miniHive container does not have a graphical user
  interface!"
- **Hardware recommendation.** "We recommend at least 8 GiB of main memory for running the
  miniHive Docker container." Without that, the course server may be used instead.
- **Reference material.** A Bash video playlist, the Udacity *Version Control with Git* course,
  and the Passau FIM page on SSH.
- **Support boundary.** Because every machine differs in environment, installed applications,
  and hardware, support for problems on your own device is limited. Questions go to the Stud.IP
  course forum; check whether the question has already been answered, and give details such as
  operating system and the failed command.
- **Submission and disclosure rules.** Milestones are submitted through Praktomat. No submission
  may be made public: no posting milestone code into the Stud.IP forum, no upload into a public
  GitHub repository. Plagiarism affects the creator and the one who copies it.

That is the entirety of what the source says about the project. Every statement above is
quotable from the sheet.

## Key Properties

- **Minimalistic by construction.** The target is a stripped-down Hive, not Hive. A minimal
  project is one where the student can hold the whole system in their head — the point of the
  exercise, and why the name is *mini*Hive.
- **Terminal-first.** No GUI in the container. The command line is the interface, and Bash skill
  is a requirement, not a nicety.
- **Python-based.** Python is the implementation language alongside the shell.
- **Container-tested.** Every implementation is tested in a Docker container, local or shared.
- **Memory-demanding.** At least 8 GiB of main memory is recommended. With less, the container
  may not run, and the course server becomes the practical option.
- **Version-controlled.** Git is a required skill. Milestones arrive in sequence, so the
  implementation's history is part of its life.
- **Remotely reachable.** SSH is required, which matters for the shared-server path.
- **Non-public by obligation.** Submissions stay private; disclosure of milestone code is
  prohibited, and the sanction is symmetric: plagiarism affects creator and copier.

## Worked Example

A first contact with the project, using only what the sheets establish.

**Step 1 — decide where the container runs.** The student has 16 GiB of RAM on a Linux laptop, so
the 8 GiB recommendation is met: Docker is installed locally per
<https://docs.docker.com/get-docker/>, followed by the hello-world image as a sanity check, as
the sheet instructs. A student with 4 GiB of RAM requests the course server instead, described
in [[rootless-docker-server-access]].

**Step 2 — get the tooling into shape.** The container has no GUI, so the student confirms a
Bash shell is what they type into all term, works through the Bash playlist and the Udacity Git
course, and confirms `git` behaves.

**Step 3 — work on the project.** The student writes the miniHive implementation in Python,
driving it from the terminal inside the container, with the version history in Git under the
discipline in [[git-commit-hygiene]] and [[git-branching-and-merging]].

**Step 4 — test.** The implementation runs inside the container. If the container misbehaves, the
student asks in the Stud.IP forum, giving operating system and failed command, after checking
whether the question is already answered. Support on one's own device is limited, so a
reproducible description matters.

**Step 5 — hand in.** The milestone goes to Praktomat with the exact filename the exercise
specifies, as described in [[praktomat-submission-workflow]]. The code stays private: no public
repository, no code in the forum. If someone posted their solution publicly and the student
copied it, the sanction lands on both.

Notice what this example contains and what it does not: it describes *how to work on* miniHive
and the constraints on that, and nothing about what miniHive is made of internally.

## Common Pitfalls

- **Treating Bash as optional because Python is the "real" language.** The sheet's emphasis —
  an exclamation mark in the source — exists because students underestimate this. The container
  has no GUI, so a GUI-based workflow cannot be transferred.
- **Skipping the hello-world check.** Both the prerequisites sheet and the Docker server sheet
  instruct you to run the hello-world image — the cheapest check that daemon, storage driver, and
  image pull path work.
- **Underestimating the memory requirement.** Ignoring 8 GiB yields a container that starts
  slowly, thrashes, or dies — which then looks like a bug in your code.
- **Posting milestone code in the Stud.IP forum, or pushing to a public GitHub repository.** The
  exercise sheet names both as prohibited. The forum is for questions, not delivery.
- **Assuming plagiarism sanctions hit only the copier.** The sheet says plagiarism affects the
  creator and the one who copies it. Public posting is a bad trade even for the poster.
- **Blaming the environment instead of the code.** Stating operating system and the failed
  command separates an environment problem from a logic problem.
- **Delaying the setup until the week of the first session.** The kickoff sheet lists Docker
  setup before the first session as a to-do. With a server application due by 19 October, the
  local path is the one you control.
- **Assuming the container is a convenience.** It is a grading condition: the same
  implementation is evaluated under the same conditions.

## Connections

- [[scaling-database-systems]] — the course that owns the project.
- [[praktomat-submission-workflow]] — the channel through which milestones are delivered.
- [[rootless-docker-server-access]] — the shared alternative to a local container.
- [[containerization-for-builds]] — the practice the test container instantiates.
- [[multi-stage-docker-build]] — how a test image with several layers is assembled.
- [[docker-compose]] — how a multi-service test environment would be described.
- [[git-commit-hygiene]] — the version-control discipline the Git requirement implies.
- [[git-branching-and-merging]] — branching strategy for a milestone-driven project.
- [[reproducible-builds]] — why a container is the reference environment.
- [[client-server-db-architecture]] — the shape a Hive-like system has; not ingested yet.
- [[sqlite-architecture]] — a concrete engine architecture, useful contrast later.
- [[object-relational-databases]] — background for a Hive-like system.

## Open Questions

- **miniHive's internal architecture unknown.** The sheet names the project and its toolchain
  and says nothing about what miniHive contains: no components, no interfaces, no storage or
  execution model, no configuration surface, no command or query surface. Nothing about Hive's
  own design — architecture, metastore, storage layer, execution model — appears in the ingested
  material either. That belongs to the lecture material, not yet ingested.
- **Milestone breakdown unknown.** How many milestones exist, what each delivers, what
  the acceptance criteria are, and how they relate are not stated anywhere.
- **Container-to-milestone relationship unknown.** Whether each
  milestone ships its own image, whether one image is reused, and what the container contains are
  all open.
- **Grading of the project unknown.** No weights, no rubric, no statement of how milestone
  results enter the final grade. The exercises sheet only says Praktomat is used for all
  submissions, milestones among them.
- **Group work on miniHive unknown.** The exercise groups cover the same
  content, each capped at 30; that is scheduling, not collaboration on the code.
- **Expected Git usage unknown.** Git is a required skill, but the sheet does not say
  whether a branch per milestone is expected, whether the repository is shared, or whether the
  history is inspected.
- **The 8 GiB memory recommendation is unexplained.** The sheet says "We recommend at least 8 GiB
  of main memory for running the miniHive Docker container", but whether that is a hard
  requirement, an observation, or a safety margin is not stated.
