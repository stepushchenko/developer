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

### Joins
- inner join
- left [outer] join
- right [outer] join
- full [outer] join

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

### Commands

**DDL (Data Definition Language) Examples**

List of commands:
- CREATE
- DROP
- ALTER
- TRUNCATE
- RENAME
- COMMENT

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
- SELECT

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
- INSERT
- UPDATE
- DELETE
- LOCK
- CALL
- EXPLAIN PLAN

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