import unittest
from app.model.shopping_model import Shopping, Shopping_list_item


class TestShoppinglistItems(unittest.TestCase):
    def setUp(self):
        self.shopping = Shopping("AZXDJSA", "Cooking")

    def test_user_can_create_shopping_list(self):
        item = Shopping_list_item('XZBNVLK', 'Onion',
                                  'Spicing', '2017-08-27')
        self.assertTrue(self.shopping.create_item(item))

    def test_item_already_exists_in_the_shopping_list(self):
        item = Shopping_list_item('XZBNVLK', 'Onion',
                                  'Spicing', '2017-08-27)
        self.shopping.shopping_list = {'XZBNVLK': item}
        self.assertFalse(self.shopping.create_item(item))

    def test_an_item_in_the_shopping_list_returned_when_an_id_is_specified(self):
        item = Shopping_list_item('XZBNVLK', 'Onion',
                                  'Spicing', '2017-08-27)
        self.shopping.shopping_list = {'XZBNVLK': item}
        self.assertEqual(self.shopping.get_item(item.id), item)

    def test_none_is_returned_when_an_item_is_not_found_by_its_id(self):
        self.assertIsNone(self.shopping.get_item("VBDHJFS"))

    def test_that_an_item_in_a_bucket_is_updated(self):
        item = Shopping_list_item('XZBNVLK', 'Onion',
                                  'Spicing', '2017-08-27)
        self.shopping.shopping_list = {'XZBNVLK': item}
        self.shopping.update_item('XZBNVLK', 'Onion',
                                  'Spicing', '2017-08-27)
        self.assertEqual(self.shopping.get_item('XZBNVLK').name, 'Nairobi')

    def test_item_to_be_updated_is_missing(self):
        self.assertFalse(self.shopping.update_item('AHBNVLO', 'Onion',
                                  'Spicing', '2017-08-27))

    def test_item_is_successfully_deleted(self):
        item = Shopping_list_item('XZBNVLK', 'Onion',
                                  'Spicing', '2017-08-27)
        self.shopping.shopping_list = {'XZBNVLK': item}
        self.shopping.delete_item('XZBNVLK')
        self.assertEqual(self.shopping.shopping_list, {})

    def test_an_item_that_does_not_exist_cannot_be_deleted(self):
        self.assertFalse(self.shopping.delete_item("HJJJFG"))


if __name__ == '__main':
    unittest.main()
