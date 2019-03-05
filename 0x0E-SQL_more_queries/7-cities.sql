-- Creates dtabase and table according to specs
-- Create database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table citieswith id, state_id, name
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       state_id INT NOT NULL,
       FOREIGN KEY (state_id)
       REFERENCES `states`(`id`),
       name VARCHAR(256) NOT NULL
);
