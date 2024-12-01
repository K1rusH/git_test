import string
import random

def generate_password(length):
    
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(valid_characters) for i in range(length))
    return password

def test_password_characters():
    
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Generate a long password for more reliable testing
    for char in password:
        assert char in valid_characters

def test_password_length():
    
    for i in range(1, 25):
        assert len(generate_password(length=i)) == i

def test_password_uniqueness():
    
    password1 = generate_password(length=10)
    password2 = generate_password(length=10)
    assert password1 != password2
