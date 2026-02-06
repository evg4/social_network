from lib.post import Post

class PostRepository:
    def __init__(self, db_connection):
        self._connection = db_connection
    
    def get_all_posts(self):
        post_rows = self._connection.execute("SELECT * FROM posts")
        return [Post(row["id"], row["title"], row["content"], row["user_id"], row["number_of_views"]) for row in post_rows]
    
    def get_post_by_id(self, post_id):
        result = self._connection.execute("SELECT * FROM posts WHERE id = %s", [post_id])[0]
        return Post(result['id'], result['title'], result['content'], result['user_id'], result['number_of_views'] )
    

    
    def delete_post_by_id(self, post_id):
        self._connection.execute("DELETE FROM posts WHERE id = %s", [post_id])
        return None
    
    def create_post(self, title, content, user_id, number_of_views):
        self._connection.execute("INSERT INTO posts (title, content, user_id, number_of_views) VALUES (%s, %s, %s, %s)", [title, content, user_id, number_of_views])

    def increment_views(self, post_id, increase_by):
        current_views = self._connection.execute("SELECT number_of_views FROM posts WHERE id = %s", [post_id])[0]['number_of_views']
        new_views = current_views + increase_by
        self._connection.execute("UPDATE posts SET number_of_views = %s WHERE id = %s", [new_views, post_id])
