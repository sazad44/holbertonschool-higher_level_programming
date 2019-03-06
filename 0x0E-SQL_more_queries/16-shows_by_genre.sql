-- List all shows and genres linked to that show
-- List all shows an their genres
SELECT tv_shows.title, tv_genres.name FROM tv_show_genres
       RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
       LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
       GROUP BY tv_shows.title, tv_genres.name ORDER BY tv_shows.title, tv_genres.name;
