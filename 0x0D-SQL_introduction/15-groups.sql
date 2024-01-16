-- this script that lists the number of rows with the same score in second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
