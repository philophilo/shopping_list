import unittest
from app.model.user_model import User
from app.model.shopping_model import Shopping

class TestUserShopping(unittest.TestCase):
    def setUp(self):
        self.user = User('philo', 'pass')
        self.shopping = Shopping("AZXDJSA", "Essentials")

    def test_user_create_shopping_list(self):
        self.assertTrue(self.user.create_shopping_list(self.shopping))

    def test_user_shopping_list_exists(self):
        self.user.shopping_lists = {"AZXDJSA": self.shopping}
        self.assertFalse(self.user.create_shopping_list(self.shopping))


    def test_correct_shopping_list_returned_by_id(self):
        self.user.shopping_lists = {"AZXDJSA":self.shopping}
        self.assertEqual(self.user.get_shopping_list("AZXDJSA"),
                         self.shopping)

    def test_none_returned_if_id_is_unknown(self):
        self.assertIsNone(self.user.get_shopping_list("ABGDTAD"))


    def test_shopping_list_is_updated(self):
        self.user.shopping_lists = {"AZXDJSA":self.shopping}
        self.user.update_shopping_list("AZXDJSA", 'Expensive')
        self.assertEqual(self.user.get_shopping_list("AZXDJSA").name,
                         "Expensive")


    def test_updating_none_existsing_shopping_lists(self):
        self.assertFalse(self.user.update_shopping_list("BDBHGF", "Closet"))

    def test_shopping_list_successfully_deleted(self):
        self.user.delete_shopping_list("AZXDJSA")
        self.assertEqual(self.user.shopping_lists, {})

    def test_false_returned_when_deleting_none_existing_shopping_list(self):
        self.assertFalse(self.user.delete_shopping_list("AZXDJSA"))


if __name__ == '__main__':
        unittest.main()
