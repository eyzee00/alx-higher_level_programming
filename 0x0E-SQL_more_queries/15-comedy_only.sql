-- this script lists all Comedy shows in the database hbtn_0d_tvshows
SELECT show.title FROM tv_shows AS show
        INNER JOIN tv_show_genres AS show_genre
        ON show.id = show_genre.show_id
        INNER JOIN tv_genres AS genre
        ON genre.id = show_genre.genre_id
        WHERE genre.name = 'Comedy'
	ORDER BY show.title;
