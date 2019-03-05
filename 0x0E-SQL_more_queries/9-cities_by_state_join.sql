-- List all cities contained in database
-- List all cities contained in hbtn_0d_usa
SELECT cities.`id`, cities.name, states.name FROM cities
       LEFT JOIN states ON cities.state_id = states.id;
