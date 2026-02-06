from lib.user import User
from lib.post import Post

class UserRepository:
    def __init__(self, db_connection):
        self._connection = db_connection

    def get_all(self):
        user_rows = self._connection.execute("SELECT * FROM users")
        return [User(row['id'], row['email_address'], row['username']) 
                for row in user_rows]

    def find_by_id(self, user_id):
        user = self._connection.execute("SELECT * FROM users WHERE id = %s", [user_id])[0]
        return User(user['id'], user['email_address'], user['username'])

    def delete_by_id(self, user_id):
        self._connection.execute("DELETE FROM users WHERE id = %s", [user_id])
        return None
    
    def get_user_by_post_id(self, post_id):
        # post = self._connection.execute("SELECT * FROM posts WHERE id = %s", [post_id])[0]
        # user_id = post['user_id']
        # user = self._connection.execute("SELECT * FROM users WHERE id = %s", [user_id])[0]
        # return User(user['id'], user['email_address'], user['username'])
        user = self._connection.execute("SELECT user_id, email_address, username FROM users JOIN posts ON users.id = posts.user_id WHERE posts.id = %s", [post_id])[0]
        return User(user['user_id'], user['email_address'], user['username'])

    
    def get_user_with_posts(self, user_id):
        rows = self._connection.execute("SELECT posts.id AS post_id, title, content,user_id, number_of_views, email_address, username FROM posts JOIN users ON users.id = posts.user_id WHERE posts.user_id = %s", [user_id])
        posts = [Post(row["post_id"], row["title"], row["content"], row["user_id"], row["number_of_views"]) for row in rows]
        return User(rows[0]["user_id"], rows[0]["email_address"], rows[0]["username"], posts)

    # this can be refactored to pass in a User object instead of each attribute individually (although the SQL query will still need all 3. See PostRepository for example).
    def update_user(self, user_id, email, username):
        self._connection.execute("UPDATE users SET (email_address, username) = (%s, %s) WHERE id = %s", [email, username, user_id])
        return None
    