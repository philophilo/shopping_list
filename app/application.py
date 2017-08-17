import random
import string

"""
Application class handles User registration and login
"""


class Application:
    users = {}

    def register_user(self, user):
        """
        The method checks if parsed user is registed,
        if so return false otherwise add to dictionary and return True
        :param user:
        :return: bool
        """
        if user.username in self.users.keys():
            return False
        else:
            self.users[user.username] = user
        return True

    def login_user(self, username, password):
        """
        Managing authentication of user, if the password is
        similar to existing passwords then return True otherwise
        return False
        :param username: str
        :param password: str
        :return: bool
        """

        if self.users[username].password == password:
            return True
        return False

    def does_user_exist(self, username):
        """
        If username already exists in the dictionary
        as a key, return True
        :param username:
        :return bool:
        """
        print "\n doesuser>>>",username, self.users,"\n"
        if username in self.users.keys():
            return True
        return False

    def get_user(self, username):
        """
        Get user details from user dictionary based on username
        :param username:
        :return:
        """
        if username in self.users.keys():
            return self.users[username]
        return None

    def generate_random_key(self):
        """
        create a random key from string
        :return:
        """
        return ''.join(random.SystemRandom().
                       choice(string.ascii_uppercase +
                              string.digits) for _ in range(10))
