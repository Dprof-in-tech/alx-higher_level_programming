-- SQL Query to print temperature by city

SELECT city, AVG(temperature * 9/5 + 32) AS average_temperature_fahrenheit
FROM weather_data
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;
