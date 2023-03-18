# <p align="center">SQL - Introduction</p>
<img src="https://media3.giphy.com/media/vISmwpBJUNYzukTnVx/giphy.gif" width="100%">

## SQL - Introduction

`SQL (Structured Query Language)` is a programming language used to manage and manipulate relational databases. It is a standard language used by database management systems (DBMS) such as **MySQL**, **Oracle**, **Microsoft SQL Server**, and **PostgreSQL**.
  
`SQL` is a declarative language, which means that you tell it what you want to do, and it figures out how to do it. The language is used to interact with databases and perform operations such as creating, modifying, and deleting tables and data. SQL is also used to retrieve data from databases using queries.
  
`SQL` consists of several components, including:
  
- `Data Definition Language (DDL)`: used to define the structure of databases, including creating, altering, and dropping tables, indexes, and other objects.
- `Data Manipulation Language (DML)`: used to manipulate data in databases, including inserting, updating, and deleting rows in tables.
- `Data Query Language (DQL)`: used to retrieve data from databases using queries, including selecting, filtering, and sorting data.
- `Transaction Control Language (TCL)`: used to manage transactions in databases, including committing or rolling back changes.
  
`SQL` is an important skill for anyone working with databases or data analysis. It allows users to efficiently manage large amounts of data and extract valuable insights from it.

## Concepts

*For this project, we expect you to look at this concept:*

- [Databases](https://intranet.hbtn.io/concepts/864)

## Resources
### Read or Watch:

- [What Is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
- [Install MySQL (MySQL Server)](https://www.youtube.com/watch?v=9h3ctGFTz9w)
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
- [Basic SQL Statements: DDL And DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php) (*no need to read the chapter “Privileges”*)
- [Basic Queries: SQL And RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
- [SQL Technique: Functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
- [SQL Technique: Subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [What Makes The Big Difference Between a Backtick And An Apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Info
### Comments for your SQL file:

```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

### Install MySQL 8.0 on Ubuntu 20.04 LTS

```sql
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

Connect to your MySQL server:

```sql
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

## Use the sandbox to run MySQL

**In the container, credentials are `root/root`**

- Ask for container `Ubuntu 20.04`
- Connect via SSH
- OR connect via the Web terminal
- In the container, you should start MySQL before playing with it:

```sql
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```

**In the container, credentials are `root/root`**

-----------------------

## Tasks

### [0. List Databases](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/0-list_databases.sql)
Write a script that lists all databases of your MySQL server.

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
  
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys       
```
</details>

--------------------------

### [1. Create a Database](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/1-create_database_if_missing.sql)
Write a script that creates the database `hbtn_0c_0` in your MySQL server.

- If the database `hbtn_0c_0` already exists, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements

<details>
<summary>File Test</summary>
<br>
  
```mysql
mathieu@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password:
mathieu@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 

Database
information_schema
hbtn_0c_0
mysql
performance_schema 
```
</details>

----------------------

### [2. Delete a Database](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/2-remove_database.sql)
Write a script that deletes the database `hbtn_0c_0` in your MySQL server.

- If the database `hbtn_0c_0` doesn’t exist, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
  
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys  
  
mathieu@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
mathieu@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
  
Database                                                                                                                                                                  
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
```
</details>

-----------------------

### [3. List Tables](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/3-list_tables.sql)
Write a script that lists all the tables of a database in your MySQL server.

- The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 

Tables_in_mysql                                                                              
columns_priv                                                                                 
component                                                                                    
db                                                                                           
default_roles                                                                                
engine_cost                                                                                  
func                                                                                         
general_log                                                                                  
global_grants                                                                                
gtid_executed                                                                                
help_category                                                                                
help_keyword                                                                                 
help_relation                                                                                
help_topic                                                                                   
innodb_index_stats                                                                           
innodb_table_stats                                                                           
password_history                                                                             
plugin                                                                                       
procs_priv                                                                                   
proxies_priv                                                                                 
replication_asynchronous_connection_failover                                                 
replication_asynchronous_connection_failover_managed                                         
role_edges                                                                                   
server_cost                                                                                  
servers                                                                                      
slave_master_info                                                                            
slave_relay_log_info                                                                         
slave_worker_info                                                                            
slow_log                                                                                     
tables_priv                                                                                  
time_zone                                                                                    
time_zone_leap_second                                                                        
time_zone_name                                                                               
time_zone_transition                                                                         
time_zone_transition_type                                                                    
user
```
</details>

--------------------------

### [4. First Table](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/4-first_table.sql)
Write a script that creates a table called `first_table` in the current database in your MySQL server.

- `first_table` description:
  - `id` INT
  - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `first_table` already exists, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
mathieu@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
Tables_in_hbtn_0c_0
first_table
```
</details>

-------------------

### [5. Full Description](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/5-full_table.sql)
Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

- The database name will be passed as an argument of the `mysql` command
- You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
Table   Create Table                                                                         
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci 
```
</details>

---------------------

### [6. List All In Table](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/6-list_values.sql)
Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

- All fields should be printed
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
```
</details>

-----------------------

### [7. First Add](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/7-insert_value.sql)
Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.

- New row:
  - `id` = `89`
  - `name` = `Best School`
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
mathieu@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
id  name
89  Best School
  
mathieu@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
mathieu@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:  
mathieu@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
id  name
89  Best School
89  Best School
89  Best School
```
</details>

--------------------

### [8. Count 89](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/8-count_89.sql)
Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.

- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 

3
```
</details>

----------------------

### [9. Full Creation](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/9-full_creation.sql)
Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.

- `second_table` description:
  - `id` INT
  - `name` VARCHAR(256)
  - `score` INT
- The database name will be passed as an argument to the `mysql` command
- If the table `second_table` already exists, your script should not fail
- You are not allowed to use the `SELECT` and `SHOW` statements
- Your script should create these records:
  - `id` = 1, `name` = “John”, `score` = 10
  - `id` = 2, `name` = “Alex”, `score` = 3
  - `id` = 3, `name` = “Bob”, `score` = 14
  - `id` = 4, `name` = “George”, `score` = 8

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
```
</details>

------------------

### [10. List By Best](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/10-top_score.sql)
Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
score   name
14  Bob
10  John
8   George
3   Alex
```
</details>

--------------------

### [11. Select The Best](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/11-best_score.sql)
Write a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
score   name
14  Bob
10  John
```
</details>

-------------------

### [12. Cheating Is Bad](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/12-no_cheating.sql)
Write a script that updates the score of Bob to `10` in the table `second_table`.

You are not allowed to use Bob’s id value, only the `name` field
The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
mathieu@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
score   name
10  John
10  Bob
8   George
3   Alex
```
</details>

--------------------

### [13. Score Too Low](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/13-change_class.sql)
Write a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
mathieu@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
score   name
10  John
10  Bob
8   George
```
</details>

-------------------

### [14. Average](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/14-average.sql)
Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

- The result column name should be `average`
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
average
9.3333
```
</details>

--------------------

### [15. Number By Score](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/15-groups.sql)
Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

- The result should display:
  - the `score`
  - the number of records for this `score` with the label `number`
- The list should be sorted by the number of records (descending)
- The database name will be passed as an argument to the `mysql` command

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
score   number
10  2
8   1
```
</details>

---------------------

### [16. Say My Name](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/16-no_link.sql)
Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

- Don’t list rows without a `name` value
- Results should display the score and the name (in this order)
- Records should be listed by descending score
- The database name will be passed as an argument to the `mysql` command
  
In this example, new data have been added to the table `second_table`.

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
score   name
18  Aria
12  Aria
10  John
10  Bob
```
</details>

------------

### [17. Go To UTF8](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/100-move_to_utf8.sql)
Write a script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in your MySQL server.
  
You need to convert all of the following to `UTF8`:

- Database `hbtn_0c_0`
- Table `first_table`
- Field `name` in `first_table`

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 
Enter password: 
mathieu@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
```
</details>

----------------------

### [18. Temperatures #0](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/101-avg_temperatures.sql)
Import in `hbtn_0c_0` database this table dump: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/272/temperatures.sql)

Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
city    avg_temp
Chandler    72.8627
Gilbert 71.8088
Pismo beach 71.5147
San Francisco   71.4804
Sedona  70.7696
Phoenix 70.5882
Oakland 70.5637
Sunnyvale   70.5245
Chicago 70.4461
San Diego   70.1373
Glendale    70.1225
Sonoma  70.0392
Yuma    69.3873
San Jose    69.2990
Tucson  69.0245
Joliet  68.6716
Naperville  68.1029
Tempe   67.0441
Peoria  66.5392
```
</details>

-------------------

### [19. Temperatures #1](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/102-top_city.sql)
Import in `hbtn_0c_0` database this table dump: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as `Temperatures #0`)
  
Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
city    avg_temp
Naperville  76.9412
San Diego   73.7941
Sunnyvale   73.2353
```
</details>

--------------------

### [20. Temperatures #2](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0D-SQL_introduction/103-max_state.sql)
Import in `hbtn_0c_0` database this table dump: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as `Temperatures #0`)
  
Write a script that displays the max temperature of each state (ordered by State name).

<details>
<summary>File Test</summary>
<br>
  
```sql
mathieu@ubuntu:~/$ cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
  
state   max_temp
AZ  110
CA  110
IL  110
```
</details>

-------------------

## Author

- Mathieu Morel
