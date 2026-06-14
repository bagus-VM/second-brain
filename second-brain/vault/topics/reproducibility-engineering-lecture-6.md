---
title: "Lecture 6: Database System Architectures and Reproducibility"
tags: [topic, reproducibility-engineering, semester-1, database-architecture, sqlite, docker-compose]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[reproducibility-engineering-lecture-5]]", "[[containerization-for-builds]]", "[[reproducible-builds]]"]
sources: ["raw/lectures/reproducibility_engineering/Vorlesung/SoSe_2026_RepEng_IC_6___Architectures.pdf"]
---

## One-line Summary
Database systems have three main deployment architectures (file-based like [[sqlite-architecture|SQLite]], client/server like PostgreSQL, embedded like SQLite library) — each with different reproducibility tradeoffs; the lecture walks through SQLite's distinctive features (serverless, single-file, ACID, public domain source), Docker Compose for multi-service reproducible database stacks, and PostgreSQL foreign tables for capturing system information during experiments.

## Core Intuition
How you *deploy* a database system affects its reproducibility. A file-based system like [[sqlite-architecture|SQLite]] is trivially reproducible — copy the file. A client/server system like PostgreSQL involves more moving parts — the server process, the network, configuration files, the client library. A bug in *any* of these can make a "reproducible" experiment non-reproducible.

The lecture walks through three common DB architectures and their reproducibility implications, then introduces Docker Compose as the standard way to package a multi-service database stack for reproducibility. The case study: capturing system information during a database experiment using PostgreSQL foreign tables — a practical example of integrating experiment metadata capture into a database workflow.

## Key Concepts

### Three database system architectures
- **File-based / library / serverless**: SQLite — the database is a single file, accessed by linking the SQLite library into the application. No server process.
- **Client/server**: PostgreSQL, MySQL, Oracle — a separate server process manages the database; clients connect over the network.
- **Embedded**: SQLite library, BerkeleyDB — the database engine is linked into the application, but it's a full database system (not just a file format).

### SQLite's distinctive features
- **Serverless**: no separate server process
- **Zero configuration**: no setup; create a database by opening a file
- **Single-file**: the entire database is one cross-platform file
- **Self-contained**: the entire DBMS is one library, linked into the host application
- **Small**: default build is < 1 MB code, a few MB memory
- **Transactional**: fully ACID-compliant, safe for multi-process/multi-thread access
- **SQL92-compatible**: supports most standard SQL
- **Well-tested**: the SQLite team takes code testing and verification very seriously
- **Public domain**: the source code is free for any purpose — major implications for reproducibility

### Docker Compose for reproducible database stacks
A `compose.yaml` file declares multiple services (e.g., a database server and a benchmark client) and their relationships. Each service is a Docker container; the Compose file ensures consistent versions, configuration, and network setup across runs and across machines.

For example, a PostgreSQL + pgbench setup:
```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: benchdb
      POSTGRES_USER: lab
      POSTGRES_PASSWORD: labpw
    ports: ["5433:5432"]
    volumes: [pgdata:/var/lib/postgresql/data]
  bench:
    image: postgres:16
    depends_on: [db]
    environment:
      PGPASSWORD: labpw
    command: bash -c "pgbench -i -h db -U lab benchdb && pgbench -h db -U lab -T 30 benchdb"
volumes:
  pgdata:
```

This Compose file is the *reproducibility artifact*: anyone with Docker can run `docker compose up` and get the same database setup.

### PostgreSQL foreign tables for experiment metadata
PostgreSQL's `file_fdw` extension lets you query external files (e.g., `/proc/meminfo`) as if they were database tables. This is useful for capturing system information during a database experiment:
```sql
CREATE FOREIGN TABLE experiment_meminfo (
  key text,
  value text
)
SERVER local_files
OPTIONS (filename '/proc/meminfo', format 'csv', delimiter ':');
```

A subtle point: PostgreSQL *does not* verify the file exists or is readable at `CREATE FOREIGN TABLE` time. The verification happens only at query time. This is sound for reproducibility (we want to record what was actually there, not what was supposed to be there), but it can surprise new users.

## Key Properties

### Why SQLite is reproducible-friendly
- The database *is* the file: copying the file is the entire reproducibility protocol
- No server configuration to remember
- No version-skew between server and client
- Public domain source code means you can inspect and modify it
- The single-file format is the *archival format* — no need for export/import

### Why public-domain source code matters for reproducibility
- You can audit the implementation: is the algorithm doing what the documentation claims?
- You can modify it: add custom logging, fix bugs, port to a new platform
- You can ship the exact source with your experiment — version skew is impossible
- Compare to closed-source commercial DBs: you depend on the vendor's reproducibility story

### Server vs serverless — the reproducibility tradeoff
- **Serverless** (SQLite): easier to reproduce, but limited in scale and concurrency
- **Server-based** (PostgreSQL): more powerful, but more components to coordinate
- For experiment reproducibility, SQLite is often the better choice unless you need server-side features
- For production, server-based is usually necessary

### Docker Compose — the reproducibility standard
- The `compose.yaml` file is the reproducibility artifact
- It pins image versions, environment variables, port mappings, volumes, dependencies
- The same Compose file on any machine with Docker produces the same setup
- Limitations: it doesn't pin the host OS, the Docker version, or the underlying kernel

## Worked Example: PostgreSQL + pgbench

From the exercise sheet, the Docker Compose setup runs a PostgreSQL server and a benchmark client:

1. **`db` service**: PostgreSQL 16, listening on port 5432 (exposed as host port 5433). Database `benchdb`, user `lab`, password `labpw`. Data persisted in a `pgdata` volume.
2. **`bench` service**: same PostgreSQL image, but overrides the default `command` to run `pgbench` instead of starting a server. Depends on the `db` service. Reads `PGPASSWORD` from the environment.
3. **`pgbench` workflow**: first initialises the benchmark tables (`pgbench -i`), then runs a 30-second benchmark (`pgbench -T 30`).
4. **Reproducibility**: anyone with Docker can run `docker compose up` to get the exact same setup. The compose file pins image versions (postgres:16) and all configuration.

## Common Pitfalls

- **Docker Compose doesn't pin everything**: the host OS, Docker version, and underlying kernel are not specified. For full reproducibility, you need additional tools (Nix, Guix, Vagrant).
- **The `depends_on` clause doesn't wait for readiness**: it only waits for the container to *start*, not for the service to be ready. For PostgreSQL, you may need a healthcheck or a wait loop.
- **Volumes persist data across runs**: `docker compose down` does not delete volumes. For a fresh experiment, you must `docker compose down -v`.
- **PostgreSQL foreign tables don't validate file existence**: `CREATE FOREIGN TABLE` succeeds even if the file doesn't exist. Validation happens at query time. This is by design (the file might appear later) but can be surprising.
- **SQLite is not suitable for high-concurrency server workloads**: SQLite uses file-level locking; many concurrent writers will be serialised. For server-style workloads, use PostgreSQL or MySQL.
- **The lecture's title is "Architectures" but the focus is on reproducibility**: the connection between DB architecture and reproducibility is the central theme. Don't focus on the DB theory alone.

## Connections
- [[reproducibility-engineering-lecture-5]] — reproducible builds; L06 extends to database reproducibility
- [[containerization-for-builds]] — Docker is the underlying tool for Docker Compose
- [[reproducible-builds]] — the same principles apply to database systems
- [[sqlite-architecture]] — the canonical file-based DB
- [[docker-compose]] — the standard for multi-service reproducible setups
- [[foreign-tables-postgresql]] — the lecture's example for experiment metadata capture
- [[client-server-db-architecture]] — the contrast to SQLite
- public-domain-software — why SQLite's license matters for reproducibility
- [[software-analyse-lecture-7]] — both courses discuss context-sensitivity / configuration management

## Open Questions
- Are there established benchmarks for database reproducibility (analogous to the "reproducibility builds" benchmarks)?
- How do you reproduce a database experiment that uses a commercial closed-source DBMS? (You can't — this is the "reproducibility crisis" applied to databases.)
- What is the best practice for capturing and archiving experiment metadata? Foreign tables are one option; experiment-tracking tools (MLflow, Sacred) are another.
- For large-scale database experiments (terabytes of data), how do you balance reproducibility with storage costs?
