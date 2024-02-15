-- SQL Query to compute the average of all scores in the records

WITH average AS (SELECT AVG(score) AS avg_score FROM second_table) UPDATE second_table JOIN average SET second_table.average = average.avg_score;

