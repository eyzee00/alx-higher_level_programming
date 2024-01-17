-- lists the max values of each state in temperatures
SELECT state, MAX(value) as max_temp from temperatures GROUP BY state ORDER BY max_temp DESC;
