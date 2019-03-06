-- Lists all genres not associated with a show
-- Lists all genres dexter does not fall into
SELECT tv_genres.name FROM tv_genres
       RIGHT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
       RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
       WHERE tv_genres.name <> (SELECT tv_genres.name FROM tv_genres WHERE tv_shows.title = 'Dexter')  
       GROUP BY tv_genres.name ORDER BY tv_genres.name;
