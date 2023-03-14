-- script that creates the MySQL server user user_0d_1.

-- Creates a new user with the name user_0d_1 and a password user_0d_1_pwd
CREATE USER 
    IF NOT EXISTS 'user_0d_1'@'localhost' 
    IDENTIFIED BY 'user_0d_1_pwd';

-- Gives the user all privileges on all databases ('.') using the host 'localhost
GRANT ALL PRIVILEGES 
    ON *.* 
    TO 'user_0d_1'@'localhost';

-- Updates user privileges to take into account the changes we have just made.
FLUSH PRIVILEGES;
