from lib.user import User

class UserRepository:
    def __init__(self, db_connection):
        self._connection = db_connection

    def get_all(self):
        user_rows = self._connection.execute("SELECT * FROM users")
        users = []
        for row in user_rows:
            user = User(row['id'], row['email_address'], row['username'])
            users.append(user)
        return users

    def find_by_id(self, user_id):
        user_rows = self._connection.execute("SELECT * FROM users WHERE id = %s", [user_id])
        user = user_rows[0]
        return User(user['id'], user['email_address'], user['username'])

    def delete_by_id(self, user_id):
        self._connection.execute("DELETE FROM users WHERE id = %s", [user_id])
        return None