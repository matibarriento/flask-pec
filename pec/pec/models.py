class Users():
    """docstring for Users"""

    def __init__(self, email, password):
        self.email = email
        self.password = password


admin = Users("admin@admin.com", "secret")
lists = [admin]


def check(email, password):
    for user in lists:
        if(user.email == email and user.password == password):
            return True
    return False
