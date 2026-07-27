---
title: "SQLite Architecture"
tags: [concept, reproducibility-engineering, semester-1, sqlite, database, file-based]
course: "Reproducibility Engineering"
source_count: 1
status: current
last_updated: 2026-06-14
prerequisites: ["[[reproducibility-engineering-lecture-6]]"]
---

## One-line Summary
SQLite is a serverless, file-based, single-library database management system — the database *is* a cross-platform file, the entire DBMS is a single C library that links directly into the host application, and the source code is in the public domain (so reproducibility is built in).

## Core Intuition
Most databases are client/server systems: a separate server process manages the data, and clients connect over the network. **SQLite** is different — there is no server. The database is a single file (or in-memory), and the application links the SQLite library to read and write the file directly. The "architecture" is essentially: *application + SQLite library + database file*.

This design has massive reproducibility implications. The database *is* the file — copying the file is the entire reproducibility protocol. There's no server to install, no configuration to remember, no version skew between server and client. And the public domain licence means the exact source can be archived with the experiment.

## Key Concepts

### Serverless
- No separate database server process
- The application directly reads and writes the database file
- No client-server communication overhead
- No need to install, configure, or maintain a server

### Zero Configuration
- No setup required
- Creating a database is as simple as opening a file
- No server to start or stop
- No users to create or manage

### Single File
- The entire database resides in one cross-platform file
- Easy to copy, archive, email, or back up
- Works on any OS that has the SQLite library
- The file format is stable across versions

### Self-Contained
- The entire DBMS is a single C library
- The library links directly into the host application
- No external dependencies (other than standard C library)
- Easy to embed in any application

### Small
- Default build is < 1 MB of code
- Runtime memory use is just a few MB
- With tuning, library size and memory use can be much smaller
- Suitable for embedded systems and resource-constrained devices

### Transactional
- Fully ACID-compliant
- Multiple processes or threads can access safely
- Atomic commits (all-or-nothing)
- Crash-safe (data integrity preserved across crashes)

### SQL92-Compatible
- Supports most of the SQL92 (SQL2) standard
- Includes common extensions (CTEs, window functions, JSON support)
- Minor incompatibilities with PostgreSQL/MySQL are documented

### Well-Tested
- The SQLite development team takes code testing and verification very seriously
- 100% branch test coverage for the SQLite source code
- Regression tests run on millions of SQL statements
- Fuzz testing and stress testing

### Public Domain
- Source code is in the public domain
- "Free for everyone to use for any purpose"
- Can be modified, redistributed, sold, embedded — without restriction
- Major implications for reproducibility (the exact source can be archived with the experiment)

## Key Properties / Complexity

### The single-file database
A SQLite database is just a file. The file format is documented and stable. To back up a SQLite database, copy the file. To replicate a database to another machine, copy the file. To archive a database for long-term storage, copy the file.

Compare to PostgreSQL: to back up a database, you need to run `pg_dump` (or use physical replication), transfer the dump file, and restore it. Multiple components, multiple files, multiple steps. With SQLite, the entire backup protocol is `cp database.db backup.db`.

### Public domain and reproducibility
SQLite's public domain licence means:
- You can audit the source code: is the algorithm doing what the documentation claims?
- You can modify the source: add custom logging, fix bugs, port to a new platform
- You can ship the exact source with your experiment — version skew is impossible
- Compare to closed-source commercial DBs: you depend on the vendor's reproducibility story

For a research experiment using SQLite, you can archive the exact SQLite source code, the exact schema, the exact data, and the exact application code. Anyone with the same setup can reproduce your results.

### When SQLite is not appropriate
- **High-concurrency server workloads**: SQLite uses file-level locking; many concurrent writers will be serialised. For server-style workloads with many concurrent users, use PostgreSQL or MySQL.
- **Very large databases**: SQLite is fine for databases up to ~1 TB, but for petabyte-scale, use a server-based DBMS.
- **Network access**: SQLite is a file; clients need file system access. For clients on different machines, you need a network protocol (or run the same SQLite on each client).

### When SQLite is appropriate
- **Embedded systems**: smartphones, IoT devices, appliances
- **Application file format**: many applications use SQLite as their file format (Firefox, Chrome, macOS, Adobe Lightroom)
- **Small to medium websites**: low-traffic websites can use SQLite as their backend
- **Data analysis**: SQLite is excellent for one-person data analysis
- **Testing**: SQLite is fast to spin up and tear down, ideal for unit tests
- **Reproducible research**: SQLite's single-file, public-domain nature makes it ideal for archiving experiments

## Worked Example

A simple SQLite-based experiment:

```python
import sqlite3

# Open a database (creates the file if it doesn't exist)
conn = sqlite3.connect('experiment.db')
cursor = conn.cursor()

# Create a table
cursor.execute('CREATE TABLE measurements (id INTEGER PRIMARY KEY, value REAL)')

# Insert some data
for i in range(10):
    cursor.execute('INSERT INTO measurements (value) VALUES (?)', (i * 0.1,))

# Query
cursor.execute('SELECT * FROM measurements WHERE value > 0.5')
results = cursor.fetchall()

conn.commit()
conn.close()
```

After this script runs, `experiment.db` contains the entire database. To reproduce the experiment:
1. Copy `experiment.db` to another machine
2. Run the same script (or just query the database)
3. Get the same results

No server to set up. No configuration. The file *is* the experiment.

## Common Pitfalls
- **SQLite uses file-level locking for writers**: only one writer at a time. For high-concurrency workloads, use a different DBMS.
- **SQLite's SQL dialect has minor differences from PostgreSQL/MySQL**: e.g., SQLite has dynamic typing (no strict type enforcement), no native UUID type, no `BOOLEAN` type (uses 0/1 integers).
- **The "small" claim is for the default build**: with all features enabled, the library is larger. With minimum features, much smaller.
- **SQLite is not a "lightweight" database in the sense of "less powerful"**: it's a full SQL DBMS that happens to be small and embeddable.
- **The public domain licence is rare**: most open-source software is GPL, MIT, or Apache. Public domain means *no* licence at all — anyone can do anything.

## Connections
- [[reproducibility-engineering-lecture-6]] — the lecture
- [[containerization-for-builds]] — Docker for portable DB stacks
- [[reproducible-builds]] — same principles apply to SQLite
- postgresql-foreign-tables — alternative DB architecture
- public-domain-software — the licence category

## Open Questions
- For large-scale experiments (terabytes of data), is SQLite still the right choice? (Probably not — but the file-format approach is still useful for archival.)
- How does SQLite handle concurrent writers in practice? (File-level locking; can become a bottleneck for write-heavy workloads.)
- Are there alternatives to SQLite for embedded/reproducible databases? (DuckDB for analytics, LevelDB for key-value, etc.)

## Formal Definition / Statement

*To be filled.*
