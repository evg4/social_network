from lib.user_repository import UserRepository
from lib.post_repository import PostRepository
from lib.post import Post
from lib.database_connection import DatabaseConnection

conn = DatabaseConnection()
conn.connect()
conn.seed("seeds/social_network.sql")
user_repo = UserRepository(conn)
post_repo = PostRepository(conn)

# Example ways to use the app

all_users = user_repo.get_all()
print(f"All users: {all_users}")

user_id_1 = user_repo.find_by_id(1)
print(f"User with id 1 is: {user_id_1}")

user_2_posts = user_repo.get_user_with_posts(2)
print(f"User 2 and all their posts: {user_2_posts}")

all_posts = post_repo.get_all_posts()
print(f"All posts: {all_posts}")

post_id_3 = post_repo.get_post_by_id(3)
print(f"Post with id 3: {post_id_3}")

# First argument can be any integer; it will default to the next in the list when added to the database
new_post = Post(0, "New post", "Here is my new post!", 1, 6)
post_repo.create_post(new_post)
print(new_post)

# Verify that the new post was added
all_posts = post_repo.get_all_posts()
print(f"All posts: {all_posts}")

post_repo.delete_post_by_id(6)

# Verify that new post was deleted
all_posts = post_repo.get_all_posts()
print(f"All posts: {all_posts}")