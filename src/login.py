# for testing out sqllite

import sqlite3

def create_login_table(c):
    c.execute("""
        CREATE TABLE users (
            uid INTEGER,
            username TEXT,
            password TEXT
        )
    """)

def add_user(c, uid, username, password):
    c.execute("INSERT INTO users VALUES(:uid, :username, :password)", {
        "uid" : uid,
        "username" : username,
        "password" : password
    })

def debug_print(c):
    """
    Used to check state of database
    """
    c.execute("SELECT * FROM users")
    print(c.fetchall())

def user_exist(c, username):
    c.execute("SELECT * FROM users WHERE username=:username", {"username": username})
    l = c.fetchall()
    if len(l) == 0:
        return False
    return True


def get_user(c, uid):
    c.execute("SELECT * FROM users WHERE uid=:uid", {"uid" : uid})
    return c.fetchone()

def get_uid(c, username, password):
    c.execute("SELECT * FROM users WHERE username=:username", {"username": username})
    user = c.fetchone()

    # check passwords are the same before giving uid
    if user[2] == password:
        return user[0]
    else:
        return None

def get_num_users(c):
    c.execute("SELECT * FROM users")
    return len(c.fetchall())