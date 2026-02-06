from lib.post import Post

class PostRepository:
    def __init__(self, db_connection):
        self._connection = db_connection
    
    def get_all_posts(self):
        rows = self._connection.execute("SELECT * FROM posts")
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["content"], row["user_id"], row["number_of_views"])
            posts.append(item)
        return posts
    
    def get_post_by_id(self, post_id):
        rows = self._connection.execute("SELECT * FROM posts WHERE id = %s", [post_id])
        result = rows[0]
        return Post(result['id'], result['title'], result['content'], result['user_id'], result['number_of_views'] )
    
    def delete_post_by_id(self, post_id):
        self._connection.execute("DELETE FROM posts WHERE id = %s", [post_id])
        return None