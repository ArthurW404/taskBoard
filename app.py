from flask import Flask, render_template
from src.board import Board, get_test_board

app = Flask(__name__)


# temp global variable, should replace with database or something 
BOARD = get_test_board()
# @app.route("/add_item")
# def add_item():
#     BOARD.add_new_colum()

@app.route("/add_column", methods=["GET"])
def add_column():
    BOARD.add_new_column()

    # DEBUGGING
    BOARD.add_item(-1, "HEllo")
    print("Fk")
    
    # Probs not a good way of doing this
    return home()

@app.route("/", methods=["GET"])
def home():
    return render_template('home.html', columns=BOARD.board)

if __name__ == "__main__":
    app.run(debug=True)