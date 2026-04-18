def login(username, password):
    """Функция авторизации пользователя."""
    if username == "admin" and password == "12345":
        return True
    return False
