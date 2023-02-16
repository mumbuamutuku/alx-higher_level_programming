-- lists all Comedy shows in the database
SELECT s.title
FROM  tv_shows as s
INNER JOIN tv_show_genres as t
ON s.id = t.show_id
INNER JOIN tv_genres as g
ON t.genre_id = g.id
WHERE g.name = "Comedy"
ORDER BY s.title ASC;
