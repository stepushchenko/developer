### Constrainst 
Используются для ограничения типа данных, который может быть записан в колонку. 

**Значения Constrains:**
- `NOT NULL` - поле не может быть пустым
- `UNIQUE` - гарантирует, что значения в колонке будут уникальными.
- `PRIMARY KEY` - комбинация `NOT NULL` и `UNIQUE`
- `FOREIGN KEY` - уникальный идентификатор записи или кортежа из другой таблицы
- `CHECK` - проверка истинности условия перед добавлением данных в колонку
- `DEFAULT` - установка дефолтного значения в колонке
- `INDEX` - используется для быстрого изъятия данных в таблице

### Основные команды SQL
`show databases` показывает список существующих баз данных <br>
`create database [database name]` создание новой базы данных <br>
`use [database name]` выбор базы данных для дальнейшей работы с ней <br>
`source [path to .sql file]` позволяет выполнить несколько команд из файла .sql <br>
`drop database [table name]` позволяет уничтожить базы данных <br>
`show tables` позволяет увидеть перечень таблиц в базе данных <br>
`create table [table name] ([column title][column type])` позволяет создать новую таблицу <br>
    `CREATE TABLE instructor (ID CHAR(5), name VARCHAR(20) NOT NULL, PRIMARY KEY (ID), FOREIGN KEY (dept_name) REFERENCES department(dept_name));` <br>
`describe [table name]` позволяет увидеть сведения о таблице <br>
`insert into [table name]` вставка в таблицу <br>
    `INSERT INTO <table_name> (<col_name1>, <col_name2>, <col_name3>, …) VALUES (<value1>, <value2>, <value3>, …);` <br>
`update [table name] set where` обновление данных в таблице <br>
    `UPDATE <table_name> SET <col_name1> = <value1>, <col_name2> = <value2>, ... WHERE <condition>;` <br>
`delete * from [table name]` удаление данных из таблицы <br>
`drop table [table name]` удаление таблицы целиком <br>

### Команды SQL для выборки данных
1. начиная с SELECT https://tproger.ru/translations/sql-recap/
