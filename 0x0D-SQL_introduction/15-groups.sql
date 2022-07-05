-- lists the number of records with the same score
SELECT score, COUNT(score) AS number GROUP BY score ORDER BY score DESC;
