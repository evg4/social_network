DROP TABLE IF EXISTS test_table;

CREATE TABLE test_table (id SERIAL PRIMARY KEY, name VARCHAR(255));

INSERT INTO test_table (name) VALUES ('first_record');

--I'm pretty sure this will get created within my social_network database alongside the tables I actually want, i.e. users and posts.