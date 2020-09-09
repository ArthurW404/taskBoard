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

    @property
    def name(self):
        return self.__name

    @property
    def id (self):
        return self.__id


    def append(self, item):
        self.__items.append(item)
