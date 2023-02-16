-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT t.name AS genre, COUNT(*) AS 'number_shows'
FROM tv_genres as t
INNER JOIN g as tv_show_genres
ON t.id = g.genre_id
GROUP BY genre
ORDER BY number_shows DESC;
