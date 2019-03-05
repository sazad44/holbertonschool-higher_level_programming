-- Script creates table and adds multiple rows
-- Create New Table with id INT name V256 score INT
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- INSERT first record
INSERT INTO second_table (`id`, `name`, `score`) VALUES (1, "John", 10);
-- INSERT second record
INSERT INTO second_table (`id`, `name`, `score`) VALUES (2, "Alex", 3);
-- INSERT third record
INSERT INTO second_table (`id`, `name`, `score`) VALUES (3, "Bob", 14);
-- INSERT fourth record
INSERT INTO second_table (`id`, `name`, `score`) VALUES (4, "George", 8);
