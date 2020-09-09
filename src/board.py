from .column import Column

class Board:
    """
    Object which contains 0 to M columns
    """
    def __init__(self):
        super().__init__()
        
        # list which contains all board columns 
        self.__board = []

        # used to create unique id's for all columns on this board
        self.__curr_id = 0

    @staticmethod
    def new_board():
        return Board()

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
        self.board.append(Column(col_name, self.__curr_id))
        self.__curr_id += 1
    
    def remove_column(self, index):
        """
        Removes entire column
        """
        self.board.pop(index)
    
    def add_item(self, col_id, item):
        """
        Adds an item to column col of the board
        """
        # get col with same id as col_id
        for col in self.__board:
            if col.id == col_id:
                col.append(item)
                return
        print(col_id, "Does not exist")
    
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
