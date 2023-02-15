-- Lists number of records wth same score
--Records are ordered b descending count
SELECT 'score', COUNT(*) AS 'number'
FROM second_table
GROUP BY 'score'
ORDER BY 'number' DESC;
