-- Lists all shows contained in dataase
-- Lists all shows contained in the tv_shows table if one genre is linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
       INNER JOIN tv_show_genres WHERE tv_show_genres.genre_id IS NOT NULL
       GROUP BY tv_shows.title, tv_show_genres.genre_id ORDER BY tv_shows.title, tv_show_genres.genre_id;
