# for testing out sqllite

import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

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

add_user(c, 100, "David", "Zhang")

debug_print(c)

print(get_user(c, 4))

print(get_uid(c, "David", "Zhang"))


conn.commit()
conn.close()