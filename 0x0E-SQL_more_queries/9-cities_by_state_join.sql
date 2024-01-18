-- this script that lists all cities contained in the database hbtn_0d_usa
SELECT ci.id, ci.name, st.name
	FROM cities AS ci
	INNER JOIN states AS st
	on ci.state_id = st.id
	ORDER BY ci.id ASC;
