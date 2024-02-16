-- SQL query to write a california subquery

SET @california_id := (SELECT id FROM states WHERE name = 'California');

SELECT * FROM cities
WHERE state_id = @california_id
ORDER BY id ASC;
