from lib.post import Post

'''
test post initialises
'''

def test_post_initialises():
    post = Post(1, 'Tuesday', 'I ate a sandwich', 2, 132)
    assert post.id == 1
    assert post.title == 'Tuesday'
    assert post.content == 'I ate a sandwich'
    assert post.user_id == 2
    assert post.number_of_views == 132

def test_formatting():
    post = Post(1, 'Tuesday', 'I ate a sandwich', 2, 132)
    assert str(post) == "Post: 1, Tuesday, I ate a sandwich, 2, 132"

def test_equality():
    post1 = Post(1, 'Tuesday', 'I ate a sandwich', 2, 132)
    post2 = Post(1, 'Tuesday', 'I ate a sandwich', 2, 132)
    assert post1 == post2