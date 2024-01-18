-- this script uses subqueries
SELECT name FROM cities
	WHERE state_id = 
	(SELECT state_id FROM states
	WHERE name = 'California')
	ORDER BY id;
