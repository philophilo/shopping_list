import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.application = Application()
        app.secret_key = "wehuejbjbawe"
        self.user = User('philo', 'pass', 'philo philo')

    def test_landing_page_status_code(self):
        response = self.app.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200,
                         msg="Request was successful")

    def test_passwords_not_matching(self):
        data = {'name':'philo philo', 'username':'philo', 'password':
                'pass', 'password-confirm':'pass123'}
        response = self.app.post('/', data=data, follow_redirests=True)
        self.assertIn(b'Passwords do not match', response.data)

    def test_user_can_login(self):
        self.application.users = {'philophilo', self.user}
        response = self.app.post('/', data=dict(username='philo',
                                                password='pass'),
                                 follow_redirects=True)
        self.assertIn(b'philo', response.data)

    def test_invalid_login(self):
        self.application.users = {'philophilo', self.user}
        response = self.app.post('/', data=dict(username='philo',
                                                password='pass123'),
                                 follow_redirects=True)
        self.assertIn(b'Incorrect password or username, please try again',
                      response.data)

    def test_unkown_user_account(self):
        response = self.app.post('/', data=dict(username='phil',
                                                password='123'),
                                 follow_redirects=True)
        self.assertIn(b'login', response.data)

    def test_user_loging_out(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'login', response.data)

if __name__ == '__main__':
    unittest.main()
