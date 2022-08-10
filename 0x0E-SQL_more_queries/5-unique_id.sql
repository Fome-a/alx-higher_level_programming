-- a script that creates the table unique_id on your MySQL server
-- unique_id description: id INT with the default value 1 and must be unique,
-- name VARCHAR(256)
-- If the table unique_id already exists, your script should not fail
-- The database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
