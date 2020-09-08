class Column:
    def __init__(self, name):
        self.__name = name
        self.__items = []
    
    def get_items(self):
        """
        Returns a list of items in this column 
        """
        return self.__items

    def append(self, item):
        self.__items.append(item)