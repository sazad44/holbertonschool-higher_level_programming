-- Creates database and a table with specific values
-- Creates database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table states with id and name specs
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT AUTO_INCREMENT UNIQUE PRIMARY KEY NOT NULL, name VARCHAR(256) NOT NULL);
