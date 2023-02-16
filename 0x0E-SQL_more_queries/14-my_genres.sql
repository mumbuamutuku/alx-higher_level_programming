--  lists all genres of the show Dexter
SELECT g.name
FROM tv_genres as g
INNER JOIN tv_show_genres as t
ON g.id = t.genre_id
INNER JOIN tv_shows as s
ON t.show_id = s.id
WHERE s.title = "Dexter"
ORDER BY g.name ASC;
