-- this script creates a table with
-- an id field that can't be empty
CREATE TABLE IF NOT EXISTS id_not_null 
	(id INTEGER DEFAULT 1, name VARCHAR(256));
