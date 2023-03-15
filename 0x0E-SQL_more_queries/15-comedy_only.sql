-- lists all Comedy shows in the database
SELECT s.title
FROM  tv_shows AS s
INNER JOIN tv_show_genres AS t
ON s.id = t.show_id
INNER JOIN tv_genres AS g
ON t.genre_id = g.id
WHERE g.name = "Comedy"
ORDER BY s.title ASC;
