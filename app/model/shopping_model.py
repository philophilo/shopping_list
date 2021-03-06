class Shopping():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.shopping_list = {}

    def create_item(self, shopping_item):
        if shopping_item.id in self.shopping_list.keys():
            return False
        else:
            self.shopping_list[shopping_item.id] = shopping_item
            return True

    def get_all_items(self):
        return self.shopping_list

    def get_item(self, list_id):
        if list_id in self.shopping_list.keys():
            return self.shopping_list[list_id]
        return None

    def update_item(self, list_id, name, description, deadline):
        if list_id in self.shopping_list.keys():
            item = self.shopping_list[list_id]
            item.name = name
            item.description = description
            item.deadline = deadline
            return True
        return False

    def delete_item(self, list_id):
        if list_id in self.shopping_list.keys():
            self.shopping_list.pop(list_id)
            return True
        return False


class Shopping_list_item():

    def __init__(self, list_id, name, description, deadline):
        self.id = list_id
        self.name = name
        self.description = description
        self.deadline = deadline
