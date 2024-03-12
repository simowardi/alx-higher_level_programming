-- lists all records of the second_table
-- Records are ordered by descending score.
SELECT score, name FROM second_table WHERE NOT name='' ORDER BY score DESC;`
