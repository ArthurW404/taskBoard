"""
Functions for serializing user's board data 
and manipulating boards
"""
import shelve
from .board import Board

CURR_BOARD = None
db_name = "boards.db"
SHELVE =  None
BOARDS = None

def close_boards():
    SHELVE.close()

def load_boards(uid):
    global SHELVE, BOARDS
    """
    Function retrieves board from serialized file for user id uid
    If file does not exist, or is an empty list, there is no board  
    """
    SHELVE = shelve.open(db_name)
    try:
        BOARDS = SHELVE[uid]
    except KeyError:
        SHELVE[uid]  = []
        BOARDS = SHELVE[uid]

def get_boards():
    return BOARDS

def save_boards(uid):
    """
    Function for saving the board every time seconds
    """
    global BOARDS, SHELVE
    print(BOARDS)
    SHELVE[uid] = BOARDS
    SHELVE.sync()

def add_new_board(name):
    """
    Function for adding new boards 
    """
    global BOARDS
    # if board name is already taken by another board, return None
    for board in BOARDS:
        if board.name == name:
            return None

    new_board = Board.new_board(name)
    BOARDS.append(new_board)
    print(BOARDS)
    return new_board

def set_curr_board(name):
    global BOARDS, CURR_BOARD
    for board in BOARDS:
        if board.name == name:
            CURR_BOARD = board
            return CURR_BOARD
    return None

def get_curr_board():
    """
    Returns None if there is no currently selected board
    """
    return CURR_BOARD