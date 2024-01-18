-- this script uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT ge.name FROM tv_genres AS ge
        INNER JOIN tv_show_genres AS tv
        ON ge.id = tv.genre_id
        INNER JOIN tv_shows AS sh
        ON sh.id = tv.show_id
        WHERE sh.title = 'Dexter'
	ORDER BY ge.name;
