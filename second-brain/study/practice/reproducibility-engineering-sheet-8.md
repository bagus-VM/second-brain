---
title: "Exercise Sheet 8: Tidy Data with DuckDB"
tags: [practice, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-08
---

# Exercise Sheet 8: Tidy Data with DuckDB

## Exercises

### Q1 DuckDB Setup

DuckDB is an embedded column-oriented OLAP database. Set up a Docker container to run DuckDB and load a CSV file.

<details>
<summary>Solution</summary>

DuckDB runs as an embedded process, meaning there is no separate server. The simplest way to use it in a reproducible environment is a Docker container:

```bash
docker run --rm -it -v $(pwd):/data duckdb/duckdb:latest
```

This mounts your working directory into the container at `/data`. Once inside the DuckDB shell, load a CSV:

```sql
INSTALL csv;
LOAD csv;
CREATE TABLE tb AS SELECT * FROM read_csv_auto('/data/tb.csv');
```

DuckDB auto-detects column types with `read_csv_auto`. For reproducibility, you can also specify the schema explicitly to avoid type inference drift across versions:

```sql
CREATE TABLE tb AS SELECT * FROM read_csv('/data/tb.csv',
    header=true,
    columns={
        'country': 'VARCHAR',
        'year': 'INTEGER',
        'cases': 'INTEGER',
        'population': 'INTEGER'
    }
);
```

</details>

### Q2 Tidy Data Principles

State the three tidy data principles from Wickham.

<details>
<summary>Solution</summary>

Wickham's tidy data principles:

1. **Each variable forms a column.** A variable is something you measure or record, like "cases" or "population". If a column header contains values (like years 1999, 2000), those are not variable names and the data is untidy.
2. **Each observation forms a row.** An observation is one unit of analysis, like one country in one year. All values for that observation belong in a single row.
3. **Each value forms a cell.** Every cell contains exactly one value. No cell should hold a compound string like "745/19987071" that encodes two values.

These principles make data easier to manipulate, analyze, and feed into statistical tools. Most tools expect tidy data as input.

</details>

### Q3 Identifying Untidy Data

Consider the WHO tuberculosis dataset where columns are `country`, `year`, and pairs of columns like `m014`, `m1524`, `m2534`, `f014`, `f1524`, etc. Is this tidy? Why or why not?

<details>
<summary>Solution</summary>

**No, this is not tidy.** The column names `m014`, `m1524`, `m2534`, `f014`, `f1524` encode two variables: sex (`m`/`f`) and age group (`014`, `1524`, `2534`). The column headers contain values, not variable names.

To tidy this, you need to unpivot these columns into two new columns: `sex` and `age_group`, with a third column holding the count. The tidy form has columns `country`, `year`, `sex`, `age_group`, `cases`.

</details>

### Q4 Pivoting Columns to Rows (UNPIVOT)

Given the untidy WHO data from Q3, use DuckDB's `UNPIVOT` to convert the sex-age columns into rows.

<details>
<summary>Solution</summary>

```sql
SELECT * FROM who_tb
UNPIVOT (
    cases FOR sex_age IN ("m014", "m1524", "m2534", "f014", "f1524", "f2534")
);
```

This produces one row per country-year-sex_age combination, with a `cases` column holding the counts. The `sex_age` column still encodes two variables in one string, so you would split it next (see Q6).

</details>

### Q5 Pivoting Columns to Rows Without UNPIVOT

Perform the same unpivot operation without using DuckDB's `UNPIVOT` keyword.

<details>
<summary>Solution</summary>

Without `UNPIVOT`, use `UNION ALL` to stack each column into rows:

```sql
SELECT country, year, 'm014' AS sex_age, m014 AS cases FROM who_tb
UNION ALL
SELECT country, year, 'm1524' AS sex_age, m1524 AS cases FROM who_tb
UNION ALL
SELECT country, year, 'm2534' AS sex_age, m2534 AS cases FROM who_tb
UNION ALL
SELECT country, year, 'f014' AS sex_age, f014 AS cases FROM who_tb
UNION ALL
SELECT country, year, 'f1524' AS sex_age, f1524 AS cases FROM who_tb
UNION ALL
SELECT country, year, 'f2534' AS sex_age, f2534 AS cases FROM who_tb;
```

Each `UNION ALL` branch selects one of the original columns and assigns its name to a new `sex_age` column. This is the manual approach that `UNPIVOT` automates.

</details>

### Q6 Pivoting Rows to Columns (PIVOT)

Given tidy data with columns `country`, `year`, `sex`, `cases`, pivot the `sex` values into separate columns.

<details>
<summary>Solution</summary>

```sql
SELECT * FROM tidy_tb
PIVOT (
    SUM(cases) FOR sex IN ('m', 'f')
);
```

This produces columns `country`, `year`, `m`, `f` where `m` and `f` hold the case counts for male and female respectively.

</details>

### Q7 Pivoting Rows to Columns Without PIVOT

Perform the same pivot without using DuckDB's `PIVOT` keyword.

<details>
<summary>Solution</summary>

Use `CASE` with aggregation:

```sql
SELECT
    country,
    year,
    SUM(CASE WHEN sex = 'm' THEN cases ELSE 0 END) AS m,
    SUM(CASE WHEN sex = 'f' THEN cases ELSE 0 END) AS f
FROM tidy_tb
GROUP BY country, year;
```

The `CASE` expression filters rows by sex, and `SUM` aggregates the cases into a single value per group. This is the standard pre-`PIVOT` approach and works in any SQL dialect.

</details>

### Q8 Splitting a Column

A `rate` column contains values like `745/19987071` (cases/population). Split this into two numeric columns: `cases` and `population`.

<details>
<summary>Solution</summary>

```sql
SELECT
    country,
    year,
    CAST(SPLIT_PART(rate, '/', 1) AS INTEGER) AS cases,
    CAST(SPLIT_PART(rate, '/', 2) AS INTEGER) AS population
FROM tb_with_rate;
```

`SPLIT_PART(rate, '/', 1)` extracts the part before the slash, and `SPLIT_PART(rate, '/', 2)` extracts the part after. The result is cast to integer.

The original `rate` column violates the tidy data principle that each cell holds one value. Splitting it fixes that.

</details>

### Q9 Concatenating Columns

Given `century` (e.g. `19`) and `year_within_century` (e.g. `99`), concatenate them back into a `year` column (e.g. `1999`).

<details>
<summary>Solution</summary>

```sql
SELECT
    country,
    CAST(century || year_within_century AS INTEGER) AS year,
    cases
FROM tb_split;
```

The `||` operator concatenates strings. If `century` and `year_within_century` are integers, cast them to strings first:

```sql
SELECT
    country,
    CAST(CAST(century AS VARCHAR) || LPAD(CAST(year_within_century AS VARCHAR), 2, '0') AS INTEGER) AS year,
    cases
FROM tb_split;
```

`LPAD` ensures single-digit years within a century are zero-padded (`9` becomes `09`, so `19` and `09` give `1909`, not `199`).

</details>

### Q10 Case Study: WHO Tuberculosis Data

The WHO tuberculosis dataset has columns `country`, `year`, `m014`, `m1524`, `m2534`, `f014`, `f1524`, `f2534`, etc. Transform it into tidy form.

<details>
<summary>Solution</summary>

Step 1: Unpivot all sex-age columns into rows:

```sql
CREATE TABLE tb_long AS
SELECT * FROM who_tb
UNPIVOT (
    cases FOR sex_age IN ("m014", "m1524", "m2534", "f014", "f1524", "f2534")
);
```

Step 2: Split `sex_age` into `sex` and `age_group`:

```sql
CREATE TABLE tb_tidy AS
SELECT
    country,
    year,
    LEFT(sex_age, 1) AS sex,
    SUBSTRING(sex_age, 2) AS age_group,
    cases
FROM tb_long;
```

Step 3 (optional): If a `rate` column like `745/19987071` exists, split it:

```sql
SELECT
    country,
    year,
    sex,
    age_group,
    CAST(SPLIT_PART(rate, '/', 1) AS INTEGER) AS cases,
    CAST(SPLIT_PART(rate, '/', 2) AS INTEGER) AS population
FROM tb_long_with_rate;
```

The final tidy table has columns: `country`, `year`, `sex`, `age_group`, `cases` (and optionally `population`). Each row is one observation. Each column is one variable. Each cell is one value.

</details>

### Q11 Tidy Data and Reproducibility

Why does tidy data matter for reproducibility?

<details>
<summary>Solution</summary>

Tidy data follows a consistent structure, so analysis scripts are simpler and less error-prone. When every column is a variable and every row is an observation, the same code works across datasets without manual adjustment. This consistency makes analysis pipelines reproducible.

Untidy data invites ad-hoc transformations that are hard to document and easy to get wrong. A column named `m014` that encodes sex and age is ambiguous. A script that hard-codes column names breaks when the data changes. Tidy data makes the data structure explicit and the transformations systematic.

</details>

## Key Takeaways

- DuckDB is an embedded column-oriented OLAP database that runs in a Docker container with no separate server.
- Tidy data: each variable is a column, each observation is a row, each value is a cell.
- `PIVOT` converts rows to columns; `UNPIVOT` converts columns to rows. Both can be done manually with `CASE`/`SUM` and `UNION ALL` respectively.
- Compound columns (like `745/19987071` or `m014`) violate tidy data and must be split.
- Concatenation with `||` recombines split columns, but watch for zero-padding with `LPAD`.
- Tidy data makes analysis scripts simpler and more reproducible.

## Related Vault Pages

- [[tidy-data]]: the principles behind this sheet's exercises
- [[reproducibility-engineering-lecture-6]]: the lecture covering tidy data concepts
- [[provenance-in-reproducibility]]: tidy data simplifies provenance tracking
