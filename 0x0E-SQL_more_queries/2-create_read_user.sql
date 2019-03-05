-- Creates database and user with specific permissions
-- Creates database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grants Read/SELECT privileges to user_0d_2
GRANT SELECT ON hbtn_0d_2 . * TO 'user_0d_2'@'localhost';
-- Apply and reload privileges
FLUSH PRIVILEGES;
