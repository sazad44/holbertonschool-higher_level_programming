-- Lists number of records with the same score
-- Lists number of records with same score sorted by number of records
SELECT `score`, COUNT(*) AS 'number' FROM second_table GROUP BY score ORDER BY `number` DESC;
