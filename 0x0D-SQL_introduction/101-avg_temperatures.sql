-- Displays average data ordered
-- Displays average temp by city ordered by temperature
SELECT `city`, AVG(`value`) AS 'avg_temp' FROM `temperatures` GROUP BY `city` ORDER BY `avg_temp` DESC;
