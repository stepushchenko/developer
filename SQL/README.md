# SQL

### Links
- Руководство по оформлению запросов SQL https://www.sqlstyle.guide/ru/ 

### Database objects 
- table
- view
- synonym
- sequence
- index
- trigger

### Aggregation functions
- avg
- count
- max
- min
- sum


### Operators 
```html
+ - * / %   <!-- arithmetic -->
& | ^  <!-- bitwise -->
= < > <= >= !> <> !=  <!-- comparison -->
+= -+ *= /= %= &= |= ^=  <!-- compound -->
AND, OR, NOT, ANY, SOME, ALL, BETWEEN, IN, EXISTS, LIKE, IS NULL, UNIQUE   <!-- logical -->
```

### Constrainst 
Используются для ограничения типа данных, который может быть записан в колонку. 

- `NOT NULL` поле не может быть пустым
- `UNIQUE` гарантирует, что значения в колонке будут уникальными.
- `PRIMARY KEY` комбинация `NOT NULL` и `UNIQUE`
- `FOREIGN KEY` уникальный идентификатор записи или кортежа из другой таблицы
- `CHECK` проверка истинности условия перед добавлением данных в колонку
- `DEFAULT` установка дефолтного значения в колонке

### Order of SQL commands
1. `SELECT` столбцы или * для выбора всех столбцов; обязательно
2. `FROM` таблица; обязательно
3. `WHERE` условие/фильтрация, например, city = 'Moscow'; необязательно
4. `GROUP BY` столбец, по которому хотим сгруппировать данные; необязательно
5. `HAVING` условие/фильтрация на уровне сгруппированных данных; необязательно
6. `ORDER BY` столбец, по которому хотим отсортировать вывод; необязательно

### COMMANDS

**DDL (Data Definition Language) Examples**

List of commands:
- **CREATE**
- **DROP**
- **ALTER**
- **TRUNCATE**
- **RENAME**
- **COMMENT**

Create a table
```html
CREATE TABLE Students {
    id int PRIMARY KEY,
    name varchar(255) NOT NUL,
    name2 varchat(255)
}
```

Drop a table
```html
DROP TABLE Students;
```

Truncate (remove all data) a Table
```html
TRUNCATE TABLE Students;
```

Modifying the data type of existing column
```html
ALTER TABLE Students
ALTER COLUMN name varchar(512);
```

Adding a new column to the Table
```html
ALTER TABLE Students
ADD email varchar(256);
```

Removing an existing column from the Table
```html
ALTER TABLE Students
DROP TABLE name
```

**DQL (Data Query Language) Examples**

List of commands:
- **SELECT**

Fetch all data from table
```html
SELECT * FROM Students;
```

Filter data from a Table
```html
SELECT * FROM Students
WHERE id = 1234;
```

```html
SELECT * FROM Students
WHERE id > 1234
AND age < 15;
```

Fetch selected columns
```html
SELECT name, name2
FROM Students
WHERE id > 1234
AND age < 15;
```

Fetch maximum 10 rows
```html
SELECT name, name2
FROM Students
WHERE id > 1234
AND age < 15
LIMIT 10;
```

Fetch count of records
```html
SELECT count(*)
FROM Students;
```

Fetch Maximum age
```html
SELECT max(age)
FROM Students;
```

Fetch Minimum Age
```html
SELECT min(age)
FROM Students;
```

Fetch Sum of Age
```html
SELECT sum(age)
FROM Students;
```

Fetch Average Age for each gender
```html
SELECT avg(age)
FROM Students
GROUP BY gender;
```

Sort (order) fetched records
```html
SELECT name, name2
FROM Students
WHERE id > 1234
AND age < 15
ORDER BY gender;
```

Sort in descending order
```html
SELECT name, name2
FROM Students
WHERE id > 1234
AND age < 15
ORDER BY gender DESC;
```

Fetch from 2 tables
```html
SELECT name, teacher
FROM Students
INNER JOIN Section
ON Students.section = Section.id;
```

**DML (Data Manipulation Language) Examples**

List of commands:
- **INSERT**
- **UPDATE**
- **DELETE**
- **LOCK**
- **CALL**
- **EXPLAIN PLAN**

Insert data (rows) into a Table
```html
INSERT INTO Students (id, name, name2)
VALUES (1235, Ivan, Senny);
```

Update data (value of column) of a Table
```html
UPDATE Students 
SET name = 'Nina'
WHERE id = 1233
```

Delete data (rows) from a Table
```html
DELETE FROM Students
WHERE id = 1234
```

Aggregate and, Filter
```html
SELECT section, count(*) AS studentcount
FROM Students
GROUP BY section
HAVING count(*) > 20;
```

Full Outer Join
```html
SELECT name, teacher
FROM Students
FULL JOIN Section
ON Students.section = Section.id;
```

### SUBQUERIES

**Single** value subqueries 
```html
SELECT name 
FROM city 
WHERE rating = (
    SELECT rating
    FROM city
); 
```

**Multiply** values subqueries

Allowed types:
- IN
- EXISTS
- ANY
- ALL

```html
SELECT name
FROM city
WHERE country_id IN (
    SELECT country_id
    FROM country
    WHERE population > 20000000
);
```

This query finds countries that have at least one city:
```html
SELECT name 
FROM country 
WHERE EXISTS (
    SELECT *
    FROM city
    WHERE country_id = country.id
);
```

### SET OPERATIONS

**UNION** combines the results of two result sets and removes duplicates. 
UNION ALL doesn't remove duplicate rows.
This query displays German cyclists together with German skaters:
```html
SELECT name
FROM cycling
WHERE country = 'DE' 
UNION
SELECT name
FROM skating
WHERE country = 'DE';
```

**INTERSECT** returns only rows that appear in both result sets.
This query displays German cyclists who are also German skaters at the same time:
```html
SELECT name
FROM cycling
WHERE country = 'DE'
INTERSECT
SELECT name
FROM skating
WHERE country = 'DE';
```

**EXCEPT** returns only the rows that appear in the first result 
set but do not appear in the second result set.
This query displays German cyclists unless they are also German skaters at the same time:
```html
SELECT name
FROM cycling
WHERE country = 'DE' 
EXCEPT
SELECT name
FROM skating
WHERE country = 'DE';
```


### JOINS

**JOIN** (or explicitly INNER JOIN) returns rows that have matching values in both tables.
```html
SELECT city.name, country.name FROM city
JOIN country
ON city.country_id = country.id;
```

**LEFT JOIN** returns all rows from the left table with corresponding rows 
from the right table. If there's no matching row, NULLs are returned as values from the second table.
```html
SELECT city.name, country.name 
FROM city
LEFT JOIN country
ON city.country_id = country.id
```

**RIGHT JOIN** returns all rows from the right table with corresponding 
rows from the left table. If there's no matching row, NULLs are 
returned as values from the left table.
```html
SELECT city.name, country.name 
FROM city
RIGHT JOIN country
ON city.country_id = country.id;
```

**FULL JOIN** (or explicitly FULL OUTER JOIN) returns all rows from both tables – 
if there's no matching row in the second table, NULLs are returned.
```html
SELECT city.name, country.name 
FROM city
FULL [OUTER] JOIN country
ON city.country_id = country.id;
```

**CROSS JOIN** returns all possible combinations of rows from both tables. 
There are two syntaxes available.
```html
SELECT city.name, country.name 
FROM city
CROSS JOIN country;
```

```html
SELECT city.name, country.name 
FROM city, country;
```

**NATURAL JOIN** will join tables by all columns with the same name.
```html
SELECT city.name, country.name 
FROM city
NATURAL JOIN country;
```