from lib.user_repository import UserRepository
from lib.user import User
from lib.post import Post

def test_get_all_users(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = UserRepository(db_connection)
    all = repo.get_all()
    assert all == [
        User(1,'fred.smith@gmail.com', 'FS123'),
        User(2, 'alex.jones@yahoo.com', 'AJAJ'),
        User(3, 'mouse@icloud.com', 'ilovecheese')
    ]

def test_find_by_id(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = UserRepository(db_connection)
    fred = repo.find_by_id(1)
    assert fred == User(1,'fred.smith@gmail.com', 'FS123')

def test_delete_by_id(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = UserRepository(db_connection)
    repo.delete_by_id(2)
    all = repo.get_all()
    assert all == [
        User(1,'fred.smith@gmail.com', 'FS123'),
        User(3, 'mouse@icloud.com', 'ilovecheese')
    ]

def test_get_user_by_post_id(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repo = UserRepository(db_connection)
    user = user_repo.get_user_by_post_id(4)
    assert user == User(3, 'mouse@icloud.com', 'ilovecheese')

def test_update_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repo = UserRepository(db_connection)
    user_repo.update_user(1, 'fred@mail.co.uk', 'fred')
    assert user_repo.find_by_id(1) == User(1,'fred@mail.co.uk', 'fred')

def test_get_user_and_posts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    user_repo = UserRepository(db_connection)
    user_2 = user_repo.get_user_with_posts(2)
    assert user_2 == User(2, "alex.jones@yahoo.com", "AJAJ", 
        [Post(3, 'Welcome', 'Thanks for visiting my page', 2, 3), 
        Post(5, 'Hello?', 'Where are all my friends?', 2, 4)])