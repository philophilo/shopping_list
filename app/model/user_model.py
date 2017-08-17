class User:
    """
    User model class
    """

    def __init__(self, username, password, name=None):
        self.username = username
        self.name = name
        self.password = password
