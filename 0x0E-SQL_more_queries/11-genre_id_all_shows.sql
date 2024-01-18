-- this script lists all shows contained in the database hbtn_0d_tvshows
SELECT sh.title, ge.genre_id FROM tv_shows AS sh
	LEFT JOIN tv_show_genres AS ge
	ON sh.id = ge.show_id
	ORDER BY sh.title, ge.genre_id;
