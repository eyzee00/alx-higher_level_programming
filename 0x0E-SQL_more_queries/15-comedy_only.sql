-- this script lists all Comedy shows in the database hbtn_0d_tvshows
SELECT sh.title FROM tv_shows AS sh
        INNER JOIN tv_show_genres AS ge
        ON sh.id = ge.show_id
        INNER JOIN tv_genres AS tv
	ON tv.id = ge.genre_id
	WHERE tv.name = 'Comedy'
	ORDER BY t.`title`;
