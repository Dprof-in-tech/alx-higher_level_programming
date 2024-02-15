-- SQL Query to compute the average of all scores in the records

ALTER TABLE second_table ADD COLUMN average FLOAT;

SET @avg_score := (SELECT AVG(score) FROM second_table);

UPDATE second_table SET average = @avg_score;
