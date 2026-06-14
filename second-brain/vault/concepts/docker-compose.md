---
title: "Docker Compose"
tags: [concept, reproducibility-engineering, semester-1, docker-compose, containerization, multi-service]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[reproducibility-engineering-lecture-6]]", "[[containerization-for-builds]]", "[[sqlite-architecture]]"]
---

## One-line Summary
Docker Compose is a tool for declaring and running multi-container Docker applications — a `compose.yaml` file specifies the services, their images, environment variables, port mappings, volumes, and dependencies, making it the standard for reproducible multi-service setups (e.g., a database server + a benchmark client).

## Core Intuition
A real application often involves multiple services: a database, a web server, a cache, a message queue, etc. Each service runs in its own Docker container. To start the whole application, you need to start all the containers in the right order with the right configuration.

**Docker Compose** lets you declare the entire application in a single `compose.yaml` file. The file specifies each service (image, environment, ports, volumes, dependencies). Running `docker compose up` starts everything; `docker compose down` stops everything. The same file works on any machine with Docker installed — perfect for reproducibility.

## Formal Definition / Statement

A `compose.yaml` file declares:
- **Services**: named containers, each with:
  - `image`: the Docker image to use (e.g., `postgres:16`)
  - `environment`: environment variables
  - `ports`: port mappings (host:container)
  - `volumes`: volume mounts
  - `depends_on`: dependencies on other services
  - `command`: override the default container command
  - `networks`: which networks to join
- **Volumes**: named volumes (persistent storage)
- **Networks`: virtual networks for inter-service communication

Example (PostgreSQL + pgbench from the lecture):
```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: benchdb
      POSTGRES_USER: lab
      POSTGRES_PASSWORD: labpw
    ports:
      - "5433:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
  bench:
    image: postgres:16
    depends_on:
      - db
    environment:
      PGPASSWORD: labpw
    command: bash -c "pgbench -i -h db -U lab benchdb && pgbench -h db -U lab -T 30 benchdb"
volumes:
  pgdata:
```

## Key Properties

### What Compose pins
- Image version (`postgres:16` — exact tag)
- Environment variables (database name, user, password)
- Port mappings (host:container)
- Volume mounts (where data is stored)
- Service dependencies (what must start first)
- Custom commands (override the image's default)

### What Compose does NOT pin
- The host OS
- The Docker version
- The underlying kernel
- The network configuration (beyond what's declared)
- Time, locale, and other environment variables not in the compose file

For full reproducibility beyond Compose, you need additional tools (Nix, Guix, Vagrant, full VM images).

### Common use cases
- **Local development**: `docker compose up` to start the full stack
- **CI/CD**: same compose file runs in CI
- **Research experiments**: archive the compose file with the experiment
- **Reproducible benchmarks**: PostgreSQL + pgbench, MySQL + sysbench, etc.

### `depends_on` caveats
The `depends_on` clause only waits for the *container* to start, not for the *service* to be ready. For databases that take time to initialise, you may need:
- A `healthcheck` declaration
- A wait loop in the dependent service's `command`
- An init script

This is a common reproducibility bug.

### Compose vs Kubernetes
- **Compose**: simple, single-host, ideal for development and small deployments
- **Kubernetes**: complex, multi-host, ideal for production at scale
- The same `compose.yaml` doesn't run on Kubernetes (different format), but tools like `kompose` convert between them

## Worked Example

A full reproducible setup for a database experiment:

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: benchdb
      POSTGRES_USER: lab
      POSTGRES_PASSWORD: labpw
    ports:
      - "5433:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U lab -d benchdb"]
      interval: 5s
      timeout: 5s
      retries: 5
  bench:
    image: postgres:16
    depends_on:
      db:
        condition: service_healthy
    environment:
      PGPASSWORD: labpw
    command: bash -c "pgbench -i -h db -U lab benchdb && pgbench -h db -U lab -T 30 benchdb"
volumes:
  pgdata:
```

To reproduce the experiment:
```bash
docker compose up
```

Anyone with Docker can run this. The result: a PostgreSQL server + a 30-second pgbench benchmark. The compose file is the reproducibility artifact.

## Common Pitfalls
- **`depends_on` doesn't wait for readiness**: use `condition: service_healthy` for services with healthchecks
- **Volumes persist across runs**: `docker compose down -v` deletes volumes; without `-v`, data persists
- **Hardcoded passwords in the compose file**: use `.env` files or secrets management
- **Port conflicts**: if host port 5433 is already in use, the container won't start. Choose an available port.
- **Image version drift**: `postgres:16` (no minor version) is a moving target. Use `postgres:16.1` for true reproducibility.
- **The compose file is the contract**: if you change it, you've changed the experiment. Version-control it.

## Connections
- [[reproducibility-engineering-lecture-6]] — the lecture
- [[containerization-for-builds]] — Docker for isolation
- [[reproducible-builds]] — same principles for builds
- [[sqlite-architecture]] — alternative DB architecture
- [[reprotest]] — for build reproducibility
- [[build-environment-isolation]] — preventing host-specific effects

## Open Questions
- How do you handle secrets in a reproducible compose file? (Use `.env` files; commit the structure but not the secrets.)
- What's the right balance between Docker Compose and full VM images? (Compose is simpler; VMs are more reproducible.)
- How do you version the compose file? (With the experiment, ideally with a DOI.)
- For very large experiments, can compose be combined with Kubernetes? (Yes — `kompose` converts.)
