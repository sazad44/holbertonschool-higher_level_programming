-- Creates dtabase and table according to specs
-- Create database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Change referenced database
USE hbtn_0d_usa;
-- Create table cities with id, state_id, name
CREATE TABLE IF NOT EXISTS cities (
       id INT AUTO_INCREMENT UNIQUE PRIMARY KEY NOT NULL,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       FOREIGN KEY (state_id)
       REFERENCES states(id)
);
