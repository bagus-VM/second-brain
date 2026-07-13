---
title: "Exercise Sheet 8: Tidy Data with DuckDB"
tags: [practice, reproducibility-engineering, semester-1]
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-11
---

# Exercise Sheet 8: Tidy Data with DuckDB

## 1.2 DuckDB Setup

> [!note]- Solution
> DuckDB is an embedded column-oriented OLAP database. The simplest way to run it is via Docker Compose:
>
> ```bash
> cd LabSession8/duckdb-local
> docker compose up -d
> ```
>
> The DuckDB GUI is then available at http://localhost:4213. You can create databases and notebooks from the sidebar.
>
> **Key difference from SQLite:** SQLite is row-oriented (OLTP), DuckDB is column-oriented (OLAP). DuckDB is optimised for analytical queries over large datasets, not transactional workloads.

## 2 Data Restructuring: Tidy Data

### 2.2.1 Pivoting Rows to Columns

The table `countries_long` has columns `country`, `year`, `type`, `count` with rows like `(Afghanistan, 1999, cases, 745)` and `(Afghanistan, 1999, population, 19987071)`.

> [!note]- Solution
> **Why it's not tidy:** The `type` column contains values (`cases`, `population`) that should be variable names (column headers). Each observation (country-year) is spread across two rows instead of one.
>
> **(a) Using PIVOT:**
>
> ```sql
> SELECT * FROM countries_long
> PIVOT (
>     SUM(count) FOR type IN ('cases', 'population')
> );
> ```
>
> **(b) Without PIVOT:**
>
> ```sql
> SELECT
>     country,
>     year,
>     SUM(CASE WHEN type = 'cases' THEN count ELSE 0 END) AS cases,
>     SUM(CASE WHEN type = 'population' THEN count ELSE 0 END) AS population
> FROM countries_long
> GROUP BY country, year;
> ```
>
> The tidy result has columns: `country`, `year`, `cases`, `population`. Each row is one observation.

### 2.2.2 Pivoting Columns to Rows

The table `countries_wide` has columns `country`, `year_1999`, `year_2000`.

> [!note]- Solution
> **Why it's not tidy:** The column headers `year_1999` and `year_2000` encode values (years), not variable names. The year should be a variable in its own column.
>
> **(a) Using UNPIVOT:**
>
> ```sql
> SELECT * FROM countries_wide
> UNPIVOT (
>     cases FOR year_name IN ("year_1999", "year_2000")
> );
> ```
>
> Then clean up `year_name` to extract the actual year:
>
> ```sql
> SELECT country,
>        CAST(SUBSTRING(year_name, 6) AS INTEGER) AS year,
>        cases
> FROM countries_wide
> UNPIVOT (
>     cases FOR year_name IN ("year_1999", "year_2000")
> );
> ```
>
> **(b) Without UNPIVOT:**
>
> ```sql
> SELECT country, 1999 AS year, year_1999 AS cases FROM countries_wide
> UNION ALL
> SELECT country, 2000 AS year, year_2000 AS cases FROM countries_wide;
> ```
>
> The tidy result has columns: `country`, `year`, `cases`.

### 2.3 Splitting

The table `countries_rate` has a `rate` column with values like `745/19987071`.

> [!note]- Solution
> **Why it's not tidy:** The `rate` column encodes two values (cases and population) in one cell, violating the rule that each cell holds one value.
>
> Split the `rate` column and separate `year` into `century` and `year_within_century`:
>
> ```sql
> SELECT
>     country,
>     CAST(LEFT(CAST(year AS VARCHAR), 2) AS INTEGER) AS century,
>     CAST(SUBSTRING(CAST(year AS VARCHAR), 3) AS INTEGER) AS year_within_century,
>     CAST(LEFT(rate, STRPOS(rate, '/') - 1) AS INTEGER) AS cases,
>     CAST(SUBSTRING(rate, STRPOS(rate, '/') + 1) AS INTEGER) AS population
> FROM countries_rate;
> ```
>
> - `STRPOS(rate, '/')` finds the position of the slash.
> - `LEFT(rate, pos - 1)` extracts the part before the slash (cases).
> - `SUBSTRING(rate, pos + 1)` extracts the part after (population).
> - `LEFT(CAST(year AS VARCHAR), 2)` extracts the century (`19`), and `SUBSTRING(..., 3)` extracts the year within century (`99`).

### 2.4 Concatenation

> [!note]- Solution
> Reunite `century` and `year_within_century` back into `year`:
>
> ```sql
> SELECT
>     country,
>     CAST(CAST(century AS VARCHAR)
>         || LPAD(CAST(year_within_century AS VARCHAR), 2, '0')
>         AS INTEGER) AS year,
>     cases,
>     population
> FROM countries_split;
> ```
>
> `LPAD` ensures single-digit years are zero-padded (`9` → `09`), so `19` + `09` gives `1909`, not `199`.

### 2.5 Case Study

Transform `countries_who` (WHO tuberculosis data with columns like `new_sp_m014`, `new_sp_f65`, etc.) into tidy form.

> [!note]- Solution
> The column names encode four variables: `new/old`, `type`, `sex`, and `age_group`. Tidy form requires unpivoting and splitting.
>
> **Step 1:** Identify the columns to unpivot (all except `country`, `iso2`, `iso3`, `year`):
>
> ```sql
> -- List all the sex-age columns (abbreviated here)
> CREATE TABLE who_long AS
> SELECT * FROM countries_who
> UNPIVOT (
>     cases FOR scenario IN (
>         "new_sp_m014", "new_sp_m1524", "new_sp_m2534",
>         "new_sp_m3544", "new_sp_m4554", "new_sp_m5564",
>         "new_sp_m65", "new_sp_f014", "new_sp_f1524",
>         "new_sp_f2534", "new_sp_f3544", "new_sp_f4554",
>         "new_sp_f5564", "new_sp_f65"
>     )
> );
> ```
>
> **Step 2:** Parse the `scenario` column into components:
>
> ```sql
> CREATE TABLE countries_who_tidy AS
> SELECT
>     country,
>     iso2,
>     iso3,
>     year,
>     SPLIT_PART(scenario, '_', 1) AS new_old,
>     SPLIT_PART(scenario, '_', 2) AS type,
>     CASE
>         WHEN SUBSTRING(SPLIT_PART(scenario, '_', 3), 1, 1) = 'm' THEN 'm'
>         ELSE 'f'
>     END AS sex,
>     SUBSTRING(SPLIT_PART(scenario, '_', 3), 2) AS age_group,
>     cases
> FROM who_long;
> ```
>
> The tidy table has columns: `country`, `iso2`, `iso3`, `year`, `new_old`, `type`, `sex`, `age_group`, `cases`. Each row is one observation. Each cell is one value.

## 3 Discretization, Binarization, and Dummy Variables

Uses `countries_who_tidy` from Task 2.5.

### 3.1 Discretization

> [!note]- Solution
> ```sql
> SELECT *,
>     CASE
>         WHEN cases < 50 THEN 'Low'
>         WHEN cases < 500 THEN 'Medium'
>         ELSE 'High'
>     END AS severity_level
> FROM countries_who_tidy;
> ```
>
> This maps the numeric case count into three categorical buckets. Discretization converts continuous values into a finite set of categories.

### 3.2 Binarization and Dummy Variables

> [!note]- Solution
> **(a) Binarization** — `is_adult`: 1 if `age_group != '014'`, 0 otherwise.
>
> **(b) Dummy Variables** — `sex_m`: 1 if `sex = 'm'`, 0. `sex_f`: 1 if `sex = 'f'`, 0.
>
> ```sql
> SELECT *,
>     CASE WHEN age_group != '014' THEN 1 ELSE 0 END AS is_adult,
>     CASE WHEN sex = 'm' THEN 1 ELSE 0 END AS sex_m,
>     CASE WHEN sex = 'f' THEN 1 ELSE 0 END AS sex_f
> FROM countries_who_tidy;
> ```
>
> Binarization converts a condition into 0/1. One-hot encoding converts a categorical column into N binary columns (one per category).

## 4 Tidy Data (Multiple Choice)

> [!note]- Solution
> **Question 1:** The transformation adds a `PreferenceCategory` column based on ranges of `Rating`:
>
> ```sql
> SET PreferenceCategory = CASE
>     WHEN Rating > 4.5 THEN 'loves'
>     WHEN Rating > 2.5 THEN 'likes'
>     WHEN Rating > 0.5 THEN 'dislikes'
>     ELSE 'hates' END;
> ```
>
> This maps numeric values into categorical buckets.
>
> - Discretization
> - Pivoting
> - Creating dummy values
> - Normalization
> - Binarization
> - None of these options
>
> **Answer: Discretization** — the numeric `Rating` is being bucketed into categorical ranges (`loves`, `likes`, `dislikes`, `hates`). This is the same pattern as Task 3.1.
>
> ---
>
> **Question 2:** The table `cat_food_preference_dry_wet` has columns `cat`, `food_brand`, `rating_dry`, `rating_wet`.
>
> Is this tidy?
>
> - Yes
> - No
>
> **Answer: No** — the column headers `rating_dry` and `rating_wet` encode a variable (`food_type`: dry/wet) as part of the column name. In tidy data, `food_type` should be its own column with a single `rating` column. This is the same untidy pattern as `year_1999`/`year_2000` in Task 2.2.2.

## Key Takeaways

- Tidy data: each variable is a column, each observation is a row, each value is a cell.
- `PIVOT` converts rows to columns; `UNPIVOT` converts columns to rows. Both can be done manually with `CASE`/`SUM` and `UNION ALL`.
- Compound columns (like `745/19987071`) violate tidy data and must be split.
- Column headers that encode values (like `year_1999`, `rating_dry`) are a sign of untidy data.
- Discretization buckets continuous values; binarization converts conditions to 0/1; one-hot encoding converts categories to binary columns.

## Related Vault Pages

- [[tidy-data]]
- [[reproducibility-engineering-lecture-6]]
- [[provenance-in-reproducibility]]
