from lib.post_repository import PostRepository 
from lib.post import Post

def test_get_all_posts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repo = PostRepository(db_connection)
    posts = post_repo.get_all_posts()
    assert posts == [Post(1, 'Monday', 'I went fishing', 1, 67), 
                    Post(2, 'Tuesday', 'I ate my delicious fish', 1, 153),
                    Post(3, 'Welcome', 'Thanks for visiting my page', 2, 3), 
                    Post(4, 'My favourite food', 'Cheese is my favourite food', 3, 18),
                    Post(5, 'Hello?', 'Where are all my friends?', 2, 4)]


def test_get_post_by_id(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repo = PostRepository(db_connection)
    post2 = post_repo.get_post_by_id(2)
    assert post2 == Post(2, 'Tuesday', 'I ate my delicious fish', 1, 153)


def test_delete_post_by_id(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repo = PostRepository(db_connection)
    post_repo.delete_post_by_id(3)
    assert post_repo.get_all_posts() == [Post(1, 'Monday', 'I went fishing', 1, 67), 
                    Post(2, 'Tuesday', 'I ate my delicious fish', 1, 153), 
                    Post(4, 'My favourite food', 'Cheese is my favourite food', 3, 18),
                    Post(5, 'Hello?', 'Where are all my friends?', 2, 4),]
    

def test_create_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repo = PostRepository(db_connection)
    new_post = post_repo.create_post('Title', 'Content', 1, 54)
    assert post_repo.get_post_by_id(6) == Post(6, 'Title', 'Content', 1, 54)

def test_increment_views(db_connection):
    db_connection.seed("seeds/social_network.sql")
    post_repo = PostRepository(db_connection)
    post_repo.increment_views(2, 10)
    assert post_repo.get_post_by_id(2) == Post(2, 'Tuesday', 'I ate my delicious fish', 1, 163)

