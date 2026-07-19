---
title: "RepEng In-Class Exercise 6 — Database Architectures"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-10
---

# In-Class Exercise Sheet 6 — Database Architectures & SQLite

---

## Exercise 1 — Database System Architectures

### (a) Client/Server Architecture:
- **User Application** → **DB Client Library** → **Network** → **RDBMS Server**
- Components: client host(s), network, user application, DB client library, RDBMS server, DB file(s)

### (b) Embedded (SQLite) Architecture:
- **User Application** → **SQLite Library** → **SQLite file(s)**
- Components: user application, SQLite library, SQLite file(s)
- No network, no separate server — the database engine runs in-process

---

## Exercise 2 — SQLite Features for Reproducibility

- **Serverless:** No separate server process. The library accesses storage files directly. → *Reproducibility:* No server configuration to replicate. Just share the file.

- **Zero-configuration:** No setup needed. Creating an instance is as easy as opening a file. → *Reproducibility:* Eliminates a major source of environment-specific failures.

- **Single-file database:** Entire DB in one cross-platform file. → *Reproducibility:* Share one file and the entire database is shared. No fragmentation across filesystem.

- **Self-contained:** Single library contains the entire system, integrates into host application. → *Reproducibility:* Minimal dependency chain. One library, one file.

- **Compact:** <1MB code, few MB memory. → *Reproducibility:* Fits inside a Docker container easily.

- **ACID transactions:** Safe concurrent access. → *Reproducibility:* Deterministic transaction behavior.

- **SQL92 compatible:** Supports most SQL92 features. → *Reproducibility:* Standard SQL means portable queries.

- **Extensively tested:** The SQLite team takes testing very seriously. → *Reproducibility:* Known, reliable behavior.

---

## Exercise 3 — SQLite Public Domain

SQLite is **public domain** — no license restrictions at all.

**Consequences for reproducibility:**
- Can be freely included in any project (commercial, academic, open-source) without licensing concerns
- Can be bundled inside Docker containers or reproduction packages without worrying about license compliance
- No license incompatibilities with other components
- Can modify and redistribute without attribution requirements (though attribution is good practice)

---

## Exercise 4 — SQLite Limitations

SQLite is NOT a good choice when you need:

- **High write concurrency** — SQLite uses file-level locking; only one writer at a time
- **Very large databases** (hundreds of GB to TB) — designed for embedded/small-scale use
- **Network access** — no client/server architecture; only local file access
- **High user counts** — not designed for many simultaneous connections
- **Fine-grained access control** — no user/role management (relies on filesystem permissions)

---

## Exercise 5 — Docker Compose File

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
    command: >
      bash -c "
      pgbench -h db -U lab -i benchdb &&
      pgbench -h db -U lab -c 10 -t 1000 benchdb
      "

volumes:
  pgdata:
```

**Word bank answers:**
- `image: postgres:16` (both services)
- `POSTGRES_DB: benchdb`
- `POSTGRES_USER: lab`
- `POSTGRES_PASSWORD: labpw`
- `ports: "5433:5432"` (host:container)
- `volumes: pgdata:/var/lib/postgresql/data`
- `depends_on: db`
- `PGPASSWORD: labpw`

---

## Exercises 6 & 7 — SQL Views and Foreign Tables

### Exercise 6:
- Creating a view does NOT copy data — it stores the query definition. → True
- Views can simplify complex joins for end users. → True
- Views are always updatable. → False (depends on complexity)
- `CREATE VIEW AS SELECT ...` materializes nothing until queried. → True

### Exercise 7:
When querying a large CSV as a foreign table:
- `SELECT * FROM measurements;` — **Must scan entire file** (returns all rows)
- `SELECT * FROM measurements WHERE run_id = 42;` — **Must scan entire file** (CSV has no index; must check every row)
- `SELECT COUNT(*) FROM measurements;` — **Must scan entire file** (must count all rows)

**Answer:** All three queries require scanning the entire file because CSV is a flat, unindexed format. There's no way to skip rows or use an index.


---

## Related Resources

### 📖 Lecture 6: Database System Architectures and Reproducibility
- Lecture topic: [[reproducibility-engineering-lecture-6]]

**Key concepts covered:**
- [[containerization-for-builds]]
- [[reproducible-builds]]
- [[sqlite-architecture]]
- [[docker-compose]]
- [[foreign-tables-postgresql]]
- [[client-server-db-architecture]]
