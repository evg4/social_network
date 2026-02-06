class User():
    def __init__(self, id, email_address, username, posts = None):
        self.id = id
        self.email_address = email_address
        self.username = username
        self.posts = posts
    
    def __repr__(self):
        if self.posts is None:
            return f"User: {self.id}, {self.email_address}, {self.username}"
        else:
            return f"User: {self.id}, {self.email_address}, {self.username}, {self.posts}"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__