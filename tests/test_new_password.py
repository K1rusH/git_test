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
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2

def test_password_min_length():
    """Тест на минимальную длину пароля"""
    password = generate_password(length=8)
    assert len(password) >= 8

def test_password_includes_characters():
    """Тест, что пароль содержит хотя бы один символ каждого типа"""
    password = generate_password(12)
    assert any(c.islower() for c in password), "Пароль должен содержать строчные буквы"
    assert any(c.isupper() for c in password), "Пароль должен содержать прописные буквы"
    assert any(c.isdigit() for c in password), "Пароль должен содержать цифры"
    assert any(c in string.punctuation for c in password), "Пароль должен содержать специальные символы"