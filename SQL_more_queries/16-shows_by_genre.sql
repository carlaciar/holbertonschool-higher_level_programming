-- script that lists all shows and all genres linked to each show
-- Each record: tv_shows.title - tv_genres.name
-- Shows with no genre should display NULL
-- Results sorted by tv_shows.title and tv_genres.name

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
