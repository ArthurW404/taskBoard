from .column import Column
from .item import Item

class Board:
    """
    Object which contains 0 to M columns
    """
    def __init__(self, name):
        super().__init__()
        
        # list which contains all board columns 
        self.__board = []

        # used to create unique id's for all columns on this board
        self.__curr_col_id = 0
        self.__curr_issue_id = 0
        self.__bg = "/static/bg_images/default.png"
        self.__name = name

    @staticmethod
    def new_board(name):
        return Board(name)

    @property
    def bg(self):
        return self.__bg

    @property 
    def name(self):
        return self.__name

    @property
    def board(self):
        """
        Getter for board
        """
        return self.__board

    def __str__(self):
        return str(self.board)

    def add_new_column(self, col_name):
        """
        Adds new column to end of board structure
        """
        self.board.append(Column(col_name, self.__curr_col_id))
        self.__curr_col_id += 1
    
    def remove_column(self, col_id):
        """
        Removes entire column
        """
        for col in self.board:
            if col.id == col_id:
                self.board.remove(col)
                return
        print(col_id, "Does not exist")
        
        
    
    def add_item(self, col_id, issue_name, issue_descript):
        """
        Adds an item to column col of the board
        """
        # get col with same id as col_id
        for col in self.board:
            if col.id == col_id:
                col.append(Item(issue_name,issue_descript, self.__curr_issue_id))
                self.__curr_issue_id += 1
                return
        print(col_id, "Does not exist")
    
    def remove_item(self, item_id):
        """
        Removes an item to column col of the board
        """
        for col in self.board:
            if col.has_item(item_id):
                col.remove_item(item_id)
                return
                    

    def get_items(self):
        """
        Returns a list of all items in the board
        """
        return [i for col in self.board for i in col.get_items()]

    def move_column(self, col_id, is_left):
        i=0
        while i < len(self.board):
            if self.board[i].id == col_id:
                if is_left and i != 0:
                    col = self.board.pop(i)
                    self.board.insert(i - 1, col)
                    return
                elif not is_left and i != len(self.board) - 1:
                    col = self.board.pop(i)
                    self.board.insert(i + 1, col)
                    return
            i += 1


    def move_item(self, issue_id, direction):
        i=0
        while i < len(self.board):
            col = self.board[i]
            if col.has_item(issue_id):
                if direction == "left" and i != 0:
                    issue = col.remove_item(issue_id)
                    self.board[i-1].append(issue)
                    return
                elif direction == "right" and i != len(self.board) - 1:
                    issue = col.remove_item(issue_id)
                    self.board[i+1].append(issue)
                    return
            i += 1