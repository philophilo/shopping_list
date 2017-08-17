import unittest
from app import app
from app.model.user_model import User
from app.model.application import Application


class TestApplicationRoutes(unittest.TestCase):
    """
    This class contains tests for the application routes.
    """

    def setUp(self):
        """
        This method activates the flask testing config flag, which disables
        error catching during request handling.
        The testing client always provided an interface to the application.
        :return:
        """
        app.testing = True
        self.app = app.test_client()
        self.application = Application()
        app.secret_key = "khbdfijfrfni"


if __name__ == '__main__':
    unittest.main()
