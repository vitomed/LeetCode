1. Ограничение целостности

* **NOT NULL** Constraint: Ensures that a column cannot have a NULL value.
* **Unique**: Ensures that all values in a column are different.
* **Primary Key**: Uniquely identified each records in a database table. It consists of a single or multiple fields.
* **Foreign Key**: Constrains data based on columns in other tables. It is used to prevent actions that would destroy links between tables.
* **Check**: Ensures that all values in a column satisfy certain conditions.
* **Exclusion**: Ensure that if any two rows are compared on the specified columns or expressions using the specified operators, at least one of these operator comparisons will return false or null.
.
```sql
CREATE TABLE Employees (
    ID INT PRIMARY KEY     NOT NULL,
    NAME           TEXT    NOT NULL,
    AGE            INT     NOT NULL,
    ADDRESS        CHAR(50),
    SALARY         REAL CHECK(SALARY > 0),
    EMAIL          TEXT    UNIQUE
);
```
.
