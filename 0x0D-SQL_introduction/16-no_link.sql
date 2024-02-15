-- SQL query to list rows with only name values

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
