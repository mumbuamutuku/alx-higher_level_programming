-- lists all shows, and all genres linked to that show,
SELECT s.title, g.name
FROM  tv_shows as s
LEFT JOIN tv_show_genres as t
ON s.id = t.show_id
LEFT JOIN tv_genres as g
ON t.genre_id = g.id
ORDER BY s.title, g.name ASC;
