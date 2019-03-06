-- Lists all shows without a certain genre
-- Lists all shows without the comedy genre
SELECT title FROM tv_shows
       LEFT JOIN tv_show_genres ON tv_show_genres.show_id = id
       LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
       WHERE title NOT IN (SELECT title FROM tv_shows INNER JOIN tv_show_genres ON tv_show_genres.show_id = id INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.name = 'Comedy')
       GROUP BY title ORDER BY title;
