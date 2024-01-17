-- lists the max values of each state in temperatures
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
