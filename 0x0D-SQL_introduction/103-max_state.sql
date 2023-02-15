--Displas the max temperature of each state
SELECT state, AVG(value) AS "avg_temp" FROM temperatures GROUP BY state ORDER BY state;
