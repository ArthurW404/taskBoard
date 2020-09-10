class Item:
    def __init__(self, name, description, id):
        super().__init__()
        self.__name = name
        self.__description = description
        self.__id = id

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def id(self):
        return self.__id
    
    