from flask import Flask, render_template, request
from src.board import Board
import signal

app = Flask(__name__)

# Each user have their own collection of boards
BOARDS = []
# temp global variable, should replace with database or something 
BOARD = Board.new_board("My crappy board")
BOARDS.append(BOARD)
BOARDS.append(Board.new_board("Test_board n2"))

@app.route("/board/add_item", methods=["POST"])
def add_item():
    print("WOw")
    issue_name = request.json['name']
    issue_descript = request.json['description']
    col_id = request.json['col_id']
    BOARD.add_item(col_id, issue_name, issue_descript)
    return {}

@app.route("/board/add_column", methods=["POST"])
def add_column():
    col_name = request.json['name']
    print(col_name)
    BOARD.add_new_column(col_name)
    return {}

@app.route("/board/delete_issue", methods=["DELETE"])
def delete_issue():
    item_id = request.json["id"]
    BOARD.remove_item(item_id)
    return {}

@app.route("/board/delete_column", methods=["DELETE"])
def delete_column():
    col_id = request.json["id"]
    BOARD.remove_column(col_id)
    return {}

@app.route("/board/move_column", methods=["PUT"])
def move_column():
    col_id = request.json["id"]
    is_left = request.json["left"]
    BOARD.move_column(col_id, is_left)
    return {}

@app.route("/board/move_issue", methods=["PUT"])
def move_issue():
    issue_id = request.json["id"]
    direction = request.json["direction"]
    BOARD.move_item(issue_id, direction)
    return {}

@app.route("/board", methods=["GET"])
def board():
    return render_template('board_page.html', boards=BOARDS, board=BOARD, columns=BOARD.board)

@app.route("/", methods=["GET"])
def home():
    return render_template('home.html', boards=BOARDS, board=BOARD, columns=BOARD.board)


def sig_handler(signum, frame):
    print('Signal handler called with signal', signum)
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, sig_handler)
    app.run(debug=True)