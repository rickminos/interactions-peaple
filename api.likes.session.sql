CREATE TABLE likes (
	id INT PRIMARY KEY,
	post_id VARCHAR ( 100 ) NOT NULL,
	user_id VARCHAR ( 100 ) NOT NULL,
	likestatus BOOLEAN NOT NULL 
	
)

CREATE TABLE coments (
	id INT PRIMARY KEY,
	post_id VARCHAR ( 100 ) NOT NULL,
	user_id VARCHAR ( 100 ) NOT NULL,
	coment VARCHAR ( 1000 ) NOT NULL
)
