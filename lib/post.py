class Post:
    def __init__(self, id, title, content, user_id, number_of_views):
        self.id = id
        self.title = title
        self.content = content
        self.user_id = user_id
        self.number_of_views = number_of_views

    def __repr__(self):
        return f"Post: {self.id}, {self.title}, {self.content}, {self.user_id}, {self.number_of_views}"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__