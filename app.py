from flask import Flask, render_template
from src.board import Board, get_test_board

app = Flask(__name__)

# temp global variable, should replace with database or something 
BOARD = get_test_board()

@app.route("/add_item", methods=["POST"])
def add_item():
    print("WOw")
    return {}

@app.route("/add_column", methods=["POST"])
def add_column():
    BOARD.add_new_column()

    # DEBUGGING
    BOARD.add_item(-1, "HEllo")
    print("Fk")
    
    # Probs not a good way of doing this
    # return home()
    return {}

@app.route("/", methods=["GET"])
def home():
    return render_template('home.html', columns=BOARD.board)

if __name__ == "__main__":
    app.run(debug=True)