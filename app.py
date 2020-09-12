from flask import Flask, render_template, request, redirect
from src.boards_handler import close_boards, set_curr_board, get_boards, get_curr_board, add_new_board, load_boards, save_boards
import signal
import time
import threading

app = Flask(__name__)

# uid is unique to each user
# should be retrieved after user successfully logs in 
uid = 'test'

#loads board from file
load_boards(uid)

# # Each user have their own collection of boards
# BOARDS = []
# # temp global variable, should replace with database or something 
# BOARD = Board.new_board("My crappy board")
# BOARDS.append(BOARD)
# BOARDS.append(Board.new_board("Test_board n2"))

@app.route("/board/add_item", methods=["POST"])
def add_item():
    issue_name = request.json['name']
    issue_descript = request.json['description']
    col_id = request.json['col_id']
    get_curr_board().add_item(col_id, issue_name, issue_descript)
    return {}

@app.route("/board/add_column", methods=["POST"])
def add_column():
    col_name = request.json['name']
    print(col_name)
    get_curr_board().add_new_column(col_name)
    return {}

@app.route("/board/delete_issue", methods=["DELETE"])
def delete_issue():
    item_id = request.json["id"]
    get_curr_board().remove_item(item_id)
    return {}

@app.route("/board/delete_column", methods=["DELETE"])
def delete_column():
    col_id = request.json["id"]
    get_curr_board().remove_column(col_id)
    return {}

@app.route("/board/move_column", methods=["PUT"])
def move_column():
    col_id = request.json["id"]
    is_left = request.json["left"]
    get_curr_board().move_column(col_id, is_left)
    return {}

@app.route("/board/move_issue", methods=["PUT"])
def move_issue():
    issue_id = request.json["id"]
    direction = request.json["direction"]
    get_curr_board().move_item(issue_id, direction)
    return {}

@app.route("/add_board", methods=["POST"])
def add_board():
    print(request.json)
    name = request.json['name']
    add_new_board(name)
    return {}

@app.route("/change_board", methods=["PUT"])
def change_board():
    name = request.json['name']
    set_curr_board(name)
    return {}

@app.route("/board", methods=["GET"])
def board():
    user_board = get_curr_board()
    if user_board is None:

        return redirect("/")
    return render_template('board_page.html', boards=get_boards(), board=get_curr_board(), columns=get_curr_board().board)

@app.route("/", methods=["GET"])
def home():
    return render_template('home.html', boards=get_boards())

def sig_handler(signum, frame):
    print('Signal handler called with signal', signum)

    # close data before exiting
    close_boards()
    exit(0)

def save(uid):
    while True:
        save_boards(uid)
        time.sleep(3)
        
if __name__ == "__main__":
    signal.signal(signal.SIGINT, sig_handler)
    t = threading.Thread(target=save, args=(uid,))
    t.daemon = True
    t.start()
    app.run(debug=False)