import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    for i in range(1, 25):
        assert len(generate_password(length=i)) == i

def test_password_uniqueness():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password1 = generate_password(length=10)
    password2 = generate_password(length=10)
    assert password1 != password2
