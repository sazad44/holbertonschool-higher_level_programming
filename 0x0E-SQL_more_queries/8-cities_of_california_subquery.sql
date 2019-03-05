-- Lists all cities in a state in the database
-- List all cities in california in hbtn_0d_usa
SELECT `id`, `name` FROM cities WHERE `state_id`=1 ORDER BY `id`;
