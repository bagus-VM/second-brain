---
title: "RepEng In-Class Exercise 7 — Tidy Data"
tags:
  - practice
  - reproducibility-engineering
  - semester-1
course: "Reproducibility Engineering"
status: current
last_updated: 2026-07-10
---

# In-Class Exercise Sheet 7 — Tidy Data & Metadata

Based on Hadley Wickham's "Tidy Data" and SQL for Data Science.

---

## Exercise 1 — Tidy Data Principles

**(a)** "80% of data analysis is spent on the process of cleaning and preparing the data."

**(b)** In tidy data:
- Each type of **observational unit** forms a table
- Each **observation** forms a row
- Each **variable** forms a column
- Each cell is an **individual value**

---

## Exercise 2 — Student Grades

**(a)** The compact representation (exam × student matrix) is NOT tidy because:
- Column headers (Rozz, Andrew, Susie) are **values**, not variable names
- The "student" variable is spread across columns (wide format)

**Tidy version:**

| student | exam    | grade |
| ------- | ------- | ----- |
| Rozz    | midterm | 1.3   |
| Andrew  | midterm | 2.0   |
| Susie   | midterm | 1.7   |
| Rozz    | final   | 2.3   |
| Andrew  | final   | 1.7   |
| Susie   | final   | 1.0   |

**(b)** The table with columns student, stu_number, exam, grade → **Tidy.** Each row is an observation (student × exam), each column is a variable, each cell is a value.

**(c)** The table with columns subject_id, choices, reaction_times → **NOT tidy.** The `choices` column contains multiple values (A,B,B) and `reaction_times` contains multiple values (312.3, 433.4, 365.1). Should be split into separate rows.

---

## Exercise 3 — Country Data

The three separate tables (Afghanistan, Brazil, China) are **NOT tidy** because:
- The country name is embedded in the table structure, not as a column value
- Should be one table with a `country` column:

| country     | year | cases | population |
|-------------|------|-------|------------|
| Afghanistan | 1999 | 745   | 19987071   |
| Afghanistan | 2000 | 2666  | 20595360   |
| Brazil      | 1999 | 37737 | 172006362  |
| Brazil      | 2000 | 80488 | 174504898  |
| China       | 1999 | 212258| 1272915272 |
| China       | 2000 | 213766| 1280428583 |

---

## Exercise 4 — Contingency Table SQL

### (a) Create a tidy table:
```sql
CREATE TABLE handedness (
    sex VARCHAR(10),
    handedness VARCHAR(10),
    count INTEGER
);

INSERT INTO handedness VALUES
    ('Male', 'Right-handed', 43),
    ('Male', 'Left-handed', 9),
    ('Female', 'Right-handed', 44),
    ('Female', 'Left-handed', 4);
```

### (b) Male and female counts:
```sql
SELECT sex, SUM(count) AS total FROM handedness GROUP BY sex;
-- Male: 52, Female: 48
```

### (c) Left- and right-handed counts:
```sql
SELECT handedness, SUM(count) AS total FROM handedness GROUP BY handedness;
-- Right-handed: 87, Left-handed: 13
```

### (d) Fraction of males who are left-handed:
```sql
SELECT SUM(CASE WHEN handedness = 'Left-handed' THEN count END) * 1.0 /
       SUM(count) AS fraction
FROM handedness
WHERE sex = 'Male';
-- 9/52 ≈ 0.173
```

### (e) Odds of a male being left-handed:
```sql
SELECT SUM(CASE WHEN handedness = 'Left-handed' THEN count END) * 1.0 /
       SUM(CASE WHEN handedness = 'Right-handed' THEN count END) AS odds
FROM handedness
WHERE sex = 'Male';
-- 9/43 ≈ 0.209
```

### (f) Odds ratio (male left-handed vs female left-handed):
```sql
-- Odds for males: 9/43
-- Odds for females: 4/44
-- Odds ratio: (9/43) / (4/44) = (9×44)/(43×4) = 396/172 ≈ 2.30
SELECT
  (SELECT SUM(CASE WHEN handedness='Left-handed' THEN count END) * 1.0 /
          SUM(CASE WHEN handedness='Right-handed' THEN count END)
   FROM handedness WHERE sex='Male')
  /
  (SELECT SUM(CASE WHEN handedness='Left-handed' THEN count END) * 1.0 /
          SUM(CASE WHEN handedness='Right-handed' THEN count END)
   FROM handedness WHERE sex='Female')
AS odds_ratio;
```

---

## Exercise 5 — Earthquakes Table

### (a) Tidy version:
| magnitude | year | count |
|-----------|------|-------|
| 4.0–4.9   | 2000 | 7425  |
| 4.0–4.9   | 2001 | 7456  |
| 4.0–4.9   | 2002 | 7489  |
| 5.0–5.9   | 2000 | 1318  |
| 5.0–5.9   | 2001 | 1299  |
| 5.0–5.9   | 2002 | 1312  |
| 6.0+      | 2000 | 165   |
| 6.0+      | 2001 | 174   |
| 6.0+      | 2002 | 160   |

### (b) Cross join output:
The query cross-joins earthquakes with years (2000, 2001, 2002), producing 3×3=9 rows with columns: magnitude, year, y2000, y2001, y2002. Each row has the magnitude, the year value, AND all three year columns.

### (c) CREATE TABLE earthquakesTidy:
```sql
CREATE TABLE earthquakesTidy AS
SELECT magnitude,
       year,
       CASE year
           WHEN 2000 THEN y2000
           WHEN 2001 THEN y2001
           WHEN 2002 THEN y2002
       END AS count
FROM earthquakes, (VALUES (2000), (2001), (2002)) as temp(year);
```

### (d) Reverse (pivot back):
```sql
SELECT magnitude,
       SUM(CASE WHEN year = 2000 THEN count END) AS y2000,
       SUM(CASE WHEN year = 2001 THEN count END) AS y2001,
       SUM(CASE WHEN year = 2002 THEN count END) AS y2002
FROM earthquakesTidy
GROUP BY magnitude;
```

**Why GROUP BY?** Because we're collapsing multiple rows (one per year) back into a single row per magnitude. The aggregate function `SUM` with `CASE` picks the right value for each year.

---

## Exercise 6 — Metadata & Workflows

- **Data wrangling** — the process of exploring, cleaning and preparing data
- **Workflow** — a sequence of actions applied to data, tracks how datasets are created/modified
- **Destructive mode** — data is changed and original version is lost
- **Non-destructive mode** — new dataset is created, original is kept
- **Reversible** — changes can be undone
- **Non-reversible (irreversible)** — changes cannot be undone

---

## Exercise 7 — ALTER TABLE DROP COLUMN

```sql
ALTER TABLE Customers DROP COLUMN phone;
```

→ **The action is destructive** (data in the column is permanently lost)
→ **The action is NOT reversible** (you can't undo a DROP COLUMN in standard SQL without a backup)

**Answer:** The action is destructive and non-reversible. Neither "non-destructive" nor "reversible" applies.

---

## Exercise 8 — CREATE TABLE AS SELECT

```sql
CREATE TABLE CleanCustomers AS
  SELECT id, TRIM(name) AS name, email FROM Customers;
```

→ **The action is non-destructive** (original Customers table is unchanged)
→ **The action is NOT reversible** (you can't automatically undo the CREATE; but the original data is still there)

**Answer:** The action is non-destructive ✓

---

## Exercise 9 — Destructive but Reversible

**Example:** `UPDATE Customers SET name = UPPER(name);`

This is destructive (overwrites original values) but reversible (you can recover by applying `LOWER()` — assuming the original was mixed case, and you know that).

Better example: Moving a file to trash/recycle bin. The original location is lost (destructive), but you can restore it (reversible).

---

## Exercise 10 — Destructive and Not Reversible

**Example:** `DROP TABLE Customers;`

The table and all its data are permanently gone (without a backup). There is no way to undo this with SQL alone.

---

## Related Lectures
- [[reproducibility-engineering-lecture-7]]
