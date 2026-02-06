from lib.user import User

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
        post = self._connection.execute("SELECT * FROM posts WHERE id = %s", [post_id])[0]
        user_id = post['user_id']
        user = self._connection.execute("SELECT * FROM users WHERE id = %s", [user_id])[0]
        return User(user['id'], user['email_address'], user['username'])

    def update_user(self, user_id, email, username):
        self._connection.execute("UPDATE users SET (email_address, username) = (%s, %s) WHERE id = %s", [email, username, user_id])
        return None
    