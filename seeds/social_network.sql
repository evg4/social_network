-- drop child first, then parent:
DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq;

DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

-- create parent first, because the child needs the parent when to already exist when it gets created

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email_address text,
  username text
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  user_id int,
  number_of_views int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

-- populate parent first, so we have its primary key which is then used as a foreign key for the child

INSERT INTO users (email_address, username) VALUES ('fred.smith@gmail.com', 'FS123');
INSERT INTO users (email_address, username) VALUES ('alex.jones@yahoo.com', 'AJAJ');
INSERT INTO users (email_address, username) VALUES ('mouse@icloud.com', 'ilovecheese');


INSERT INTO posts (title, content, user_id, number_of_views) VALUES ('Monday', 'I went fishing', 1, 67);
INSERT INTO posts (title, content, user_id, number_of_views) VALUES ('Tuesday', 'I ate my delicious fish', 1, 153);
INSERT INTO posts (title, content, user_id, number_of_views) VALUES ('Welcome', 'Thanks for visiting my page', 2, 3);
INSERT INTO posts (title, content, user_id, number_of_views) VALUES ('My favourite food', 'Cheese is my favourite food', 3, 18);
INSERT INTO posts (title, content, user_id, number_of_views) VALUES ('Hello?', 'Where are all my friends?', 2, 4);