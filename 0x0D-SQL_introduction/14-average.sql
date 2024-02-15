-- SQL Query to compute the average of all scores in the records

WITH average AS (SELECT AVG(score) FROM second_table) UPDATE second_table SET average = average;

