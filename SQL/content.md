### Links
- Руководство по оформлению запросов SQL https://www.sqlstyle.guide/ru/ 

### Constrainst 
Используются для ограничения типа данных, который может быть записан в колонку. 

**Значения Constrains:**
- `NOT NULL` поле не может быть пустым
- `UNIQUE` гарантирует, что значения в колонке будут уникальными.
- `PRIMARY KEY` комбинация `NOT NULL` и `UNIQUE`
- `FOREIGN KEY` уникальный идентификатор записи или кортежа из другой таблицы
- `CHECK` проверка истинности условия перед добавлением данных в колонку
- `DEFAULT` установка дефолтного значения в колонке
- `INDEX` используется для быстрого изъятия данных в таблице

### Порядок команд SQL
1. `SELECT` столбцы или * для выбора всех столбцов; обязательно
2. `FROM` таблица; обязательно
3. `WHERE` условие/фильтрация, например, city = 'Moscow'; необязательно
4. `GROUP BY` столбец, по которому хотим сгруппировать данные; необязательно
5. `HAVING` условие/фильтрация на уровне сгруппированных данных; необязательно
6. `ORDER BY` столбец, по которому хотим отсортировать вывод; необязательно

### Основные команды SQL
- `show databases` показывает список существующих баз данных <br>
- `create database <database name>` создание новой базы данных <br>
- `use <database name>` выбор базы данных для дальнейшей работы с ней <br>
- `source <path to .sql file>` позволяет выполнить несколько команд из файла .sql <br>
- `drop database <table name>` позволяет уничтожить базы данных <br>
- `show tables` позволяет увидеть перечень таблиц в базе данных <br>
- `create table <table name> (<column title><column type>)` позволяет создать новую таблицу <br>
- `describe <table name>` позволяет увидеть сведения о таблице <br>
- `insert into <table name>` вставка в таблицу <br>
- `update <table name> set where` обновление данных в таблице <br>
- `delete * from <table name>` удаление данных из таблицы <br>
- `drop table <table name>` удаление таблицы целиком <br>
- `select * from` выборка данных из таблицы
- `select distinct <col name> from` выборка без повторов
- подробности о каждой команде https://tproger.ru/translations/sql-recap/ 