-- Lists all records of a table with conditions
-- Lists all rows with name value in descending order of score
SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL ORDER BY `score` DESC;
