# <p align="center">SQL - More queries</p>
<img src="https://editor.analyticsvidhya.com/uploads/36882wired1.gif" width="100%">

## Introduction to SQL - More queries
SQL is a standard programming language used to manage and manipulate data in relational databases. SQL queries are instructions used to query, insert, update, and delete data in a database. However, using simple queries often isn't enough to address more complex data manipulation needs. That's why we need to go further and use advanced queries.

### Features of SQL - More queries
**SQL - More queries** include features such as:
  
- `Joins`: to extract data from multiple tables using join conditions.
- `Subqueries`: to create nested queries for more precise results.
- `Aggregates`: to group data based on certain criteria and calculate aggregates such as sum, average, maximum, etc.
- `Window functions`: to perform calculations on a subset of data within a window.
- `Regular expressions`: to perform operations on data using text patterns.

### Practical use of SQL - More queries
We'll use practical examples to illustrate the use of these features. For example:
  
- Finding duplicate data using joins and aggregate functions.
- Grouping data aggregation using aggregate functions.
- Retrieving data from linked tables using joins.
  
We'll also learn how to combine different features to solve complex data manipulation problems.

### Conclusion
SQL - More queries can help you address more complex data manipulation problems, which can save you time and improve your productivity.

## Resources
### Read or Watch:

- [How To Create a New User And Grant Permissions In MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-grant.aspx)
- [MySQL Constraints](https://zetcode.com/mysql/constraints/)
- [SQL Technique: Subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [Basic Query Operation: The Join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
- [SQL Technique: Multiple Joins And The Distinct Keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
- [SQL Technique: Join Types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
- [SQL Technique: Union And Minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
- [The Seven Types Of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
- [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
- [SQL Style Guide](https://www.sqlstyle.guide)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
  
Extra resources around relational database model design:
  
- [Design](https://www.guru99.com/database-design.html)
- [Normalization](https://www.guru99.com/database-normalization.html)
- [ER Modeling](https://www.guru99.com/er-modeling.html)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on Ubuntu 20.04 LTS using `MySQL 8.0` (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Info
### Comments For Your SQL File:

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

### Use The Sandbox To Run MySQL
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

### How To Import a SQL Dump

```sql
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```
<br>
<img src="https://user-images.githubusercontent.com/113856302/226103297-2c948fe3-66d8-49c9-82b9-f9871744d271.png" width="100%">

-------------------------

## Tasks

### [0. My Privileges!](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/0-privileges.sql)
Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
  
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'

mathieu@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
mathieu@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password: 
mathieu@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
  
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT, UPDA..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'  
```
</details>

------------------

### [1. Root User](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/1-create_user.sql)
Write a script that creates the MySQL server user `user_0d_1`.

- `user_0d_1` should have all privileges on your MySQL server
- The `user_0d_1` password should be set to `user_0d_1_pwd`
- If the user `user_0d_1` already exists, your script should not fail

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
mathieu@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
  
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, INSERT..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
```
</details>

--------------------

### [2. Read User](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/2-create_read_user.sql)
Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

- `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`
- The `user_0d_2` password should be set to `user_0d_2_pwd`
- If the database `hbtn_0d_2` already exists, your script should not fail
- If the user `user_0d_2` already exists, your script should not fail

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
mathieu@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
  
Grants for user_0d_1@localhost                                                                                                
GRANT SELECT, ..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`                                                                                                                             
GRANT APPLICATION_PASSWORD_ADMIN,...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`                                        
Grants for user_0d_2@localhost                                                                                                
GRANT USAGE ON *.* TO `user_0d_2`@`localhost`                                                                                 
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`  
```
</details>

------------------------

### [3. Always a Name](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/3-force_name.sql)
Write a script that creates the table `force_name` on your MySQL server.

- `force_name` description:
  - `id` INT
  - `name` VARCHAR(256) can’t be null
- The database name will be passed as an argument of the `mysql` command
- If the table `force_name` already exists, your script should not fail

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
mathieu@ubuntu:~/$ echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
mathieu@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
  
id  name
89  Best School
  
mathieu@ubuntu:~/$ echo 'INSERT INTO force_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
  
ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
  
mathieu@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
  
id  name
89  Best School
```
</details>

--------------------

### [4. ID Can't Be Null](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/4-never_empty.sql)
Write a script that creates the table `id_not_null` on your MySQL server.

- `id_not_null` description:
  - `id` INT with the default value `1`
  - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `id_not_null` already exists, your script should not fail

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
mathieu@ubuntu:~/$ echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
mathieu@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
  
id  name
89  Best School
  
mathieu@ubuntu:~/$ echo 'INSERT INTO id_not_null (name) VALUES ("Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
mathieu@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
  
id  name
89  Best School
1   Best
```
</details>

-------------------------

### [5. Unique ID](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/5-unique_id.sql)
Write a script that creates the table `unique_id` on your MySQL server.

- `unique_id` description:
  - `id` INT with the default value 1 and must be unique
  - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `unique_id` already exists, your script should not fail

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
mathieu@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
mathieu@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
  
id  name
89  Best School

mathieu@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
  
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'unique_id.id'
  
mathieu@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 

id  name
89  Best School
```
</details>

-------------------

### [6. States Table](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/6-states.sql)
Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.

- `states` description:
  - `id` INT unique, auto generated, can’t be null and is a primary key
  - `name` VARCHAR(256) can’t be null
- If the database `hbtn_0d_usa` already exists, your script should not fail
- If the table `states` already exists, your script should not fail

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password: 
mathieu@ubuntu:~/$ echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
mathieu@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
  
id  name
1   California
2   Arizona
3   Texas
```
</details>

-------------------

### [7. Cities Table](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/7-cities.sql)
Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.

- `cities` description:
  - `id` INT unique, auto generated, can’t be null and is a primary key
  - `state_id` INT, can’t be null and must be a `FOREIGN KEY` that references to `id` of the `states` table
  - `name` VARCHAR(256) can’t be null
- If the database `hbtn_0d_usa` already exists, your script should not fail
- If the table `cities` already exists, your script should not fail

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 7-cities.sql | mysql -hlocalhost -uroot -p
Enter password: 
mathieu@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
mathieu@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
  
id  state_id    name
1   1   San Francisco
  
mathieu@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
  
ERROR 1452 (23000) at line 1: Cannot add or update a child row: a foreign key constraint fails (`hbtn_0d_usa`.`cities`, CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`))

mathieu@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
  
id  state_id    name
1   1   San Francisco
```
</details>

----------------------

### [8. Cities Of California](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/8-cities_of_california_subquery.sql)
Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

- The `states` table contains only one record where `name` = `California` (but the `id` can be different, as per the example)
- Results must be sorted in ascending order by `cities.id`
- You are not allowed to use the `JOIN` keyword
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
  
id  name
1   California
2   Arizona
3   Texas
4   Utah
  
mathieu@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
  
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
  
mathieu@ubuntu:~/$ cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
  
id  name
1   San Francisco
2   San Jose
```
</details>

---------------------

### [9. Cities By States](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/9-cities_by_state_join.sql)
Write a script that lists all cities contained in the database `hbtn_0d_usa`.

- Each record should display: `cities.id` - `cities.name` - `states.name`
- Results must be sorted in ascending order by `cities.id`
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
  
id  name
1   California
2   Arizona
3   Texas
4   Utah
  
mathieu@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
  
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
  
mathieu@ubuntu:~/$ cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
  
id  name    name
1   San Francisco   California
2   San Jose    California
4   Page    Arizona
6   Paris   Texas
7   Houston Texas
8   Dallas  Texas
```
</details>

-------------------------

### [10. Genre ID By Show](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/10-genre_id_by_show.sql)
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

- Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
- Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
  
title   genre_id
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
```
</details>

---------------------

### [11. Genre ID For All Shows](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/11-genre_id_all_shows.sql)
Import the database dump of `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `10-genre_id_by_show.sql`)

Write a script that lists all shows contained in the database `hbtn_0d_tvshows`.

- Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
- Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
- If a show doesn’t have a genre, display `NULL`
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
  
title   genre_id
Better Call Saul    NULL
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
Homeland    NULL
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
```
</details>

---------------------

### [12. No Genre](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/12-no_genre.sql)
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `11-genre_id_all_shows.sql`)

Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

- Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
- Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
  
title   genre_id
Better Call Saul    NULL
Homeland    NULL
```
</details>

---------------------

### [13. Number Of Shows By Genre](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/13-count_shows_by_genre.sql)
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `12-no_genre.sql`)

Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

- Each record should display: `<TV Show genre>` - `<Number of shows linked to this genre>`
- First column must be called `genre`
- Second column must be called `number_of_shows`
- Don’t display a genre that doesn’t have any shows linked
- Results must be sorted in descending order by the number of shows linked
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
  
genre   number_of_shows
Drama   5
Comedy  4
Mystery 2
Crime   2
Suspense    2
Thriller    2
Adventure   1
Fantasy 1
```
</details>

------------------------

### [14. My Genres](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/14-my_genres.sql)
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `13-count_shows_by_genre.sql`)

Write a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.

- The `tv_shows` table contains only one record where `title` = `Dexter` (but the `id` can be different)
- Each record should display: `tv_genres.name`
- Results must be sorted in ascending order by the genre name
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
  
name
Crime
Drama
Mystery
Suspense
Thriller
```
</details>

----------------------

### [15. Only Comedy](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/15-comedy_only.sql)
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `14-my_genres.sql`)

Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

- The `tv_genres` table contains only one record where `name` = `Comedy` (but the `id` can be different)
- Each record should display: `tv_shows.title`
- Results must be sorted in ascending order by the show title
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
  
title
New Girl
Silicon Valley
The Big Bang Theory
The Last Man on Earth
```
</details>

------------------------

### [16. List Shows And Genres](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/16-shows_by_genre.sql)
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `15-comedy_only.sql`)

Write a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.

- If a show doesn’t have a genre, display `NULL` in the genre column
- Each record should display: `tv_shows.title` - `tv_genres.name`
- Results must be sorted in ascending order by the show title and genre name
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
  
title   name
Better Call Saul    NULL
Breaking Bad    Crime
Breaking Bad    Drama
Breaking Bad    Suspense
Breaking Bad    Thriller
Dexter  Crime
Dexter  Drama
Dexter  Mystery
Dexter  Suspense
Dexter  Thriller
Game of Thrones Adventure
Game of Thrones Drama
Game of Thrones Fantasy
Homeland    NULL
House   Drama
House   Mystery
New Girl    Comedy
Silicon Valley  Comedy
The Big Bang Theory Comedy
The Last Man on Earth   Comedy
The Last Man on Earth   Drama
```
</details>

--------------------

### [17. Not My Genre](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/100-not_my_genres.sql)
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `16-shows_by_genre.sql`)

Write a script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`

- The `tv_shows` table contains only one record where `title` = `Dexter` (but the `id` can be different)
- Each record should display: `tv_genres.name`
- Results must be sorted in ascending order by the genre name
- You can use a maximum of two `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 100-not_my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
  
name
Adventure
Comedy
Fantasy
```
</details>

------------------

### [18. No Comedy Tonight!](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/101-not_a_comedy.sql)
Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `100-not_my_genres.sql`)

Write a script that lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`.

- The `tv_genres` table contains only one record where `name` = `Comedy` (but the `id` can be different)
- Each record should display: `tv_shows.title`
- Results must be sorted in ascending order by the show title
- You can use a maximum of two `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 101-not_a_comedy.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
  
title
Better Call Saul
Breaking Bad
Dexter
Game of Thrones
Homeland
House
```
</details>

-----------------------

### [19. Rotten Tomatoes](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/102-rating_shows.sql)
Import the database `hbtn_0d_tvshows_rate` dump to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql)

Write a script that lists all shows from `hbtn_0d_tvshows_rate` by their rating.

- Each record should display: `tv_shows.title` - `rating sum`
- Results must be sorted in descending order by the rating
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
Enter password: 
  
title   rating
Better Call Saul    163
Homeland    145
Silicon Valley  82
Game of Thrones 79
Dexter  24
House   21
Breaking Bad    16
The Last Man on Earth   10
The Big Bang Theory 0
New Girl    0
```
</details>

--------------------

### [20. Best Genre](https://github.com/MathieuMorel62/holbertonschool-higher_level_programming/blob/main/0x0E-SQL_more_queries/103-rating_genres.sql)
Import the database dump from `hbtn_0d_tvshows_rate` to your MySQL server: [download](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql) (same as `102-rating_shows.sql`)

Write a script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating.

- Each record should display: `tv_genres.name` - `rating sum`
- Results must be sorted in descending order by their rating
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command

<details>
<summary>File Test</summary>
<br>

```sql
mathieu@ubuntu:~/$ cat 103-rating_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
Enter password: 
  
name    rating
Drama   150
Comedy  92
Adventure   79
Fantasy 79
Mystery 45
Crime   40
Suspense    40
Thriller    40
```
</details>

--------------------

### [21. How Do SQL Database Engines Work?](url)
Based on this video:

<a href="https://www.youtube.com/watch?v=Jib2AmRb_rk">
  <img src="https://img-0.journaldunet.com/DUu5m_FwazHaouU5Uj-D0YrMl9s=/1500x/smart/75bf752ac5654f08985c7e1d982cc3e3/ccmcms-jdn/37674443.jpg" alt="Nom de l'image">
</a>

You can find [here](https://intranet.hbtn.io/rltoken/CPI-a6rFL2BepVSNY7AvJg) the presentation used in the video.
  
Write a blog post to explain to your mother “How Do SQL Database Engines Work?”. Your blog post should contain:

- an introduction
- complete explanation
- examples (not the same as the video)
- diagrams
- a summary/conclusion

Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.
  
When done, please add all urls below (blog post, LinkedIn post, etc.)
  
Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

----------------------

## Author

- Mathieu Morel
