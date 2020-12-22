class Column:
    def __init__(self, name, id):
        self.__name = name
        self.__items = []
        self.__id = id
    
    def get_items(self):
        """
        Returns a list of items in this column 
        """
        return self.__items

    def has_item(self, item_id):
        """
            Method checks whether it has a item with id item_id
        """
        for item in self.__items:
            if item.id == item_id:
                return True
        return False

    def remove_item(self, item_id):
        """
            Method removes item with id item_id

            returns item removed or None if item does not exist
        """
        for item in self.__items:
            if item.id == item_id:
                self.__items.remove(item)
                return item
        return None

    @property
    def name(self):
        return self.__name

    @property
    def id (self):
        return self.__id


    def append(self, item):
        self.__items.append(item)
