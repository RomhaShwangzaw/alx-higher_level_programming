-- This script lists all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter
-- Each record displays: tv_genres.name
-- sorted in ascending order by the genre name
SELECT name
FROM tv_genres
WHERE name NOT IN (
	SELECT tv_genres.name
		FROM tv_shows
		INNER JOIN tv_show_genres
		ON tv_shows.id = tv_show_genres.show_id
			INNER JOIN tv_genres
			ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_shows.title = 'Dexter'
)
ORDER BY name
