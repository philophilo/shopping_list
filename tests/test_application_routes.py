import unittest
from app import app
#from app.model.user_model import User
#from app.model.application import Application
from app.applicationCopy import Application
from app.modelsCopy import User
#from app.models import Bucket


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
        app.secret_key = "sdgsdgsjbdvskdxljvs"

    """def test_home_status_code(self):
        response = self.app.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Request was unsuccessful")

    def test_home_page_status_code(self):
        response = self.app.get('/home', content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Request was unsuccessful")

    def test_sign_up_page_status_code(self):
        response = self.app.get('/signup', content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Request was unsuccessful")

    def test_login_page_status_code(self):
        response = self.app.get('/login', content_type="html/text")
        self.assertEqual(response.status_code, 200, msg="Request was unsuccessful")

    def test_sign_up_page_loads(self):
        response = self.app.get('/signup', content_type="html/text")
        self.assertTrue(b'Sign Up' in response.data)

    def test_login_page_loads(self):
        response = self.app.get('/login', content_type="html/text")
        self.assertTrue(b'Login' in response.data)

    def test_user_passwords_do_not_match_during_sign_up(self):
        data = {'name': 'john', 'username': 'jokamjohn', 'password': '123', 'password-confirmation': '234'}
        response = self.app.post('/signup', data=data, follow_redirects=True)
        self.assertIn(b'The passwords do not match', response.data)

    def test_user_can_sign_up(self):
        response = self.app.post('/signup', data={'username': 'jokamjohn', 'name': 'john', 'password': '123',
                                                  'password-confirmation': '123'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    """
    def test_user_can_login(self):
        user = User('jokamjohn', '123', 'john')
        self.application.users = {'jokamjohn': user}
        response = self.app.post('/login', data=dict(username='jokamjohn', password='123'), follow_redirects=True)
        self.assertIn(b'jokamjohn', response.data)
    """
    def test_invalid_login_credentials(self):
        user = User('jokamjohn', '123', 'john')
        self.application.users = {'jokamjohn': user}
        response = self.app.post('/login', data=dict(username='jokamjohn', password=''), follow_redirects=True)
        self.assertIn(b'Invalid credentials, try again', response.data)

    def test_user_login_ing_does_not_exist_credentials(self):
        response = self.app.post('/login', data=dict(username='jokam', password='123'), follow_redirects=True)
        self.assertIn(b'No account found, please sign up first', response.data)

    def test_user_log_out(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'login', response.data)

    def test_404_page(self):
        response = self.app.get('/johnkagga', follow_redirects=True)
        self.assertIn(b'Page Not Found', response.data)

    """
if __name__ == '__main__':
    unittest.main()
