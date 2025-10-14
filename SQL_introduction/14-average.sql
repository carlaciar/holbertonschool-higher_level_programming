-- script that computes the score average of all records
-- in the table second_table of the database hbtn_0c_0
SELECT
  *
  (SELECT AVG(score) FROM second_table) AS average
FROM second_table;