from flask import Flask, render_template, request, redirect, g
from src.boards_handler import close_boards, set_curr_board, get_boards, get_curr_board, add_new_board, load_boards, save_boards
from src.login import add_user, debug_print, create_login_table, get_num_users, get_uid, user_exist
import sqlite3
import time
import threading

app = Flask(__name__)

DATABASE = 'users.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

uids = []

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

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('login_page.html')
    elif request.method == "POST":
        global uid
        with get_db() as db:
            c = db.cursor()
            username = request.json['name']
            password = request.json['password']
            uid = get_uid(c, username, password)        
            # add_user(c, uid, username, password)
            debug_print(c)
        #loads board from file
        load_boards(uid)
        t = threading.Thread(target=save_stuff, args=(uid,))
        t.start() 
    return {}

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template('signup_page.html')
    elif request.method == "POST":
        global uid
        print(request.json)
        with get_db() as db:
            c = db.cursor()
            username = request.json['name']
            if (user_exist(c, username)):
                return {}
            password = request.json['password']
            uid = get_num_users(c)
            add_user(c, uid, username, password)
            debug_print(c)
        #loads board from file
        load_boards(uid)
        t = threading.Thread(target=save_stuff, args=(uid,))
        t.start() 
    return {}

@app.route("/logout", methods=["GET"])
def logout():
    global uid
    uid = None
    return {}

@app.route("/home", methods=["GET"])
def home():
    return render_template('home.html', boards=get_boards())

@app.route("/", methods=["GET"])
def root():
    return redirect("/signup")
    
def save_stuff(uid):
    while True:
        save_boards(uid)
        time.sleep(3)

@app.before_first_request
def activate_job():
    global c
    with get_db() as db:
        c = db.cursor()
        try:
            create_login_table(c)
        except sqlite3.OperationalError:
            pass
        debug_print(c)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(debug=False)