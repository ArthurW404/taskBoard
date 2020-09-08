from flask import Flask, render_template, request
from src.board import Board, get_test_board
import signal

app = Flask(__name__)

# temp global variable, should replace with database or something 
BOARD = get_test_board()


@app.route("/add_item", methods=["POST"])
def add_item():
    print("WOw")
    return {}

@app.route("/add_column", methods=["POST"])
def add_column():
    BOARD.add_new_column(request.json['name'])

    # DEBUGGING
    BOARD.add_item(-1, "HEllo")
    
    # Probs not a good way of doing this
    # return home()
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