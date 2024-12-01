import string
import random

def generate_password(length):
    """Generate a password of the given length"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(valid_characters) for i in range(length))
    return password

def test_password_characters():
    """Test that only valid characters are used when generating a password"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Generate a long password for more reliable testing
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Test that the password length matches the specified length"""
    for i in range(1, 25):
        assert len(generate_password(length=i)) == i

def test_password_uniqueness():
    """Test that two generated passwords in a row are different"""
    password1 = generate_password(length=10)
    password2 = generate_password(length=10)
    assert password1 != password2
