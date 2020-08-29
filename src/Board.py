class Board:
    """
    2D matrix to represent a task board
    """
    def __init__(self):
        super().__init__()
        
        # list which contains all board columns 
        self.__board = []

    @property
    def board(self):
        """
        Getter for board
        """
        return self.__board

    def __str__(self):
        return str(board.board)

    def add_new_column(self):
        """
        Adds new column to end of board structure
        """
        self.board.append([])
    
    def remove_column(self, index):
        """
        Removes entire column
        """
        self.board.pop(index)
    
    def add_item(self, col, item):
        """
        Adds an item to column col of the board
        """
        self.board[col].append(item)

    def get_items(self):
        """
        Returns a list of all items in the board
        """
        return [i for col in self.board for i in col]


if __name__ == "__main__":
    board = Board()
    board.add_new_column()
    board.add_item(0, "Greetings")
    board.add_item(0, "Hello")
    board.add_new_column()
    board.add_item(1, "11")
    print (board.get_items())
    print (board)
