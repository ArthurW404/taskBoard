"""
Functions for serializing user's board data 
and manipulating boards
"""
import pickle
from .board import Board

CURR_BOARD = None
BOARDS = []

def load_boards(uid):
    global BOARDS
    """
    Function retrieves board from serialized file for user id uid
    If file does not exist, or is an empty list, there is no board  
    """
    file_name = "./boards/" + str(uid) + ".dump" 
    try:
        file = open(file_name, "rb")
        BOARDS = pickle.load(file)
        file.close()
        return BOARDS
    except FileNotFoundError:
        file = open(file_name, "wb")
        BOARDS = []
        pickle.dump(BOARDS, file)
        file.close()
        return BOARDS

def get_boards():
    return BOARDS

def save_boards(uid):
    """
    Function for saving the board every time seconds
    """
    global BOARDS
    print(BOARDS)
    file_name = "./boards/" + str(uid) + ".dump" 
    with open(file_name, "wb") as file:
        pickle.dump(BOARDS, file)
    
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