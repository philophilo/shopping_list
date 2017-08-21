class User:
    """
    User model class
    """

    def __init__(self, username, password, name=None):
        self.username = username
        self.name = name
        self.password = password
        self.shopping_lists = dict()

    def create_shopping_list(self, shopping):
        if shopping.id in self.shopping_lists.keys():
            return False
        else:
            self.shopping_lists[shopping.id] = shopping

        print self.shopping_lists.values()
        return True


    def get_shopping_list(self, list_id):
        print self.shopping_lists.values(), list_id
        if list_id in self.shopping_lists.keys():
            return self.shopping_lists[list_id]
        return None


    def update_shopping_list(self, list_id, name):
        if list_id in self.shopping_lists.keys():
            shop_list = self.shopping_lists[list_id]
            shop_list.name = name
            return True
        return False

    def delete_shopping_list(self, list_id):
        if list_id in self.shopping_lists.keys():
            self.shopping_lists.pop(list_id)
            return True
        return False
