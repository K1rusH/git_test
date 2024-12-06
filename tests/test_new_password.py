import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""
def test_password_dlina():
    for i in range(1, 25):
        assert len(generate_password(length=i)) == i
# Проверка, что пароль не состоит из одного и того же символа
def test_password_not_same_characters(password):
    assert len(password) > 1 and all(c != password[0] for c in password) == True
