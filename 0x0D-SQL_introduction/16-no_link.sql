-- this script displays all rows with a non empty name from second_table
SELECT score, name FROM second_table WHERE name != "" ORDER BY score DESC;
