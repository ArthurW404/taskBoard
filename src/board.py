from .column import Column

class Board:
    """
    Object which contains 0 to M columns
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

    def add_new_column(self, col_name):
        """
        Adds new column to end of board structure
        """
        self.board.append(Column(col_name))
    
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
    
    def remove_item(self, col, item):
        """
        Removes an item to column col of the board
        """
        self.board[col].remove(item)

    def get_items(self):
        """
        Returns a list of all items in the board
        """
        return [i for col in self.board for i in col.get_items()]

def get_test_board():
    board = Board()
    board.add_new_column("Test")
    board.add_item(0, "Greetings")
    board.add_item(0, "Hello")
    board.add_new_column("Test2")
    board.add_item(1, "11")
    return board

if __name__ == "__main__":
    board = get_test_board()
    print (board.get_items())
    print (board)
