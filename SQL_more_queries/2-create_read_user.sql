-- script that creates the database hbtn_0d_2 and the user user_0d_2.

-- Creates the database
CREATE DATABASE
    IF NOT EXISTS hbtn_0d_2;

-- Create the user with the password
CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';

-- Gives the user only the SELECT privilege.
GRANT SELECT
    ON hbtn_0d_2.*
    TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;
