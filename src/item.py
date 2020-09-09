class Item:
    def __init__(self, name, description):
        super().__init__()
        self.__name = name
        self.__description = description

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description