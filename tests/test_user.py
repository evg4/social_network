from lib.user import User

'''
user initialises
'''

def test_user_initialises():
    evg = User(1, 'evg@mail.com', 'evg')
    assert evg.email_address == 'evg@mail.com'
    assert evg.username == 'evg'

'''
printing a string of an instance has nice formatting
'''

def test_formatting():
    evg = User(1, 'evg@mail.com', 'evg')
    assert str(evg) == "User: 1, evg@mail.com, evg"

'''
identical objects are equal even if created by different means
'''

def test_equality():
    user1 = User(1, 'evg@mail.com', 'evg')
    user2 = User(1, 'evg@mail.com', 'evg')
    assert user1 == user2