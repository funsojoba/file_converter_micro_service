CREATE USER 'auth_user'@'locahost' IDENTIFIED BY 'Admin1234';

CREATE DATABASE auth_db;

GRANT ALL PRIVILEGES ON auth_db.* TO 'auth_user'@'localhost';

USE auth_db;


CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO user (email, password) VALUES ('hrfunsojoba@gmail.com', 'Admin1234')

