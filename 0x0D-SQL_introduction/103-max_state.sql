-- Displays average data ordered
-- Displays average temp by city ordered by temperature
SELECT `state`, MAX(`value`) AS 'max_temp' FROM `temperatures` GROUP BY `state` ORDER BY `state`;
