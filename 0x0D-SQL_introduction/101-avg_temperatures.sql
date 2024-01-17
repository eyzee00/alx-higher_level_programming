-- this script groups rows by city and calculates the average temp for each one
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
