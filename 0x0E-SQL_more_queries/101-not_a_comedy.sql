-- This script lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by the show title
SELECT title
FROM tv_shows
WHERE title NOT IN (
	SELECT tv_shows.title
		FROM tv_shows
		INNER JOIN tv_show_genres
		ON tv_shows.id = tv_show_genres.show_id
			INNER JOIN tv_genres
			ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_genres.name = 'Comedy'
)
ORDER BY title
