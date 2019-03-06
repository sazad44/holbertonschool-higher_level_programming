-- Lists all genres in the database by rating
-- Sums and displays rating sums according to genres
SELECT tv_genres.name, SUM(`rate`) AS 'rating' FROM `tv_show_ratings`
       INNER JOIN `tv_shows` ON tv_shows.id = tv_show_ratings.show_id
       INNER JOIN `tv_show_genres` ON tv_show_genres.show_id = tv_shows.id
       INNER JOIN `tv_genres` ON tv_genres.id = tv_show_genres.genre_id
       GROUP BY tv_genres.name ORDER BY `rating` DESC;
