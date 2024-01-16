-- lists all records of the table second_table
-- records are ordered by descending score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
