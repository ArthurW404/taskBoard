from flask import Flask, render_template, request
from src.board import Board
import signal

app = Flask(__name__)

# temp global variable, should replace with database or something 
BOARD = Board.new_board()


@app.route("/add_item", methods=["POST"])
def add_item():
    print("WOw")
    # print(request.json)
    issue_name = request.json['name']
    issue_descript = request.json['description']
    col_id = request.json['col_id']
    BOARD.add_item(col_id, issue_name, issue_descript)
    return {}

@app.route("/add_column", methods=["POST"])
def add_column():
    col_name = request.json['name']
    print(col_name)
    BOARD.add_new_column(col_name)

    # DEBUGGING
    # BOARD.add_item(-1, "HEllo")
    
    # Probs not a good way of doing this
    # return home()
    return {}

@app.route("/delete_issue", methods=["DELETE"])
def delete_issue():
    item_id = request.json["id"]
    BOARD.remove_item(item_id)
    return {}

@app.route("/delete_column", methods=["DELETE"])
def delete_column():
    col_id = request.json["id"]
    BOARD.remove_column(col_id)
    return {}

@app.route("/move_issue", methods=["PUT"])
def move_issue():

    return {}

@app.route("/", methods=["GET"])
def home():
    return render_template('home.html', columns=BOARD.board)


def sig_handler(signum, frame):
    print('Signal handler called with signal', signum)
    exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, sig_handler)
    app.run(debug=True)