import sqlite3
from sqlite3 import Error

def connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def db_setup(conn, database_setup):
    try:
        cur = conn.cursor()
        cur.execute(database_setup)
    except Error as e:
        print(e)

def db_main():
    fpath = "bot_db.db"

    sql_data = """CREATE TABLE IF NOT EXISTS portal (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    heading TEXT,
    description TEXT,
    image TEXT);"""

    conn = connection(fpath)

    db_setup(conn, sql_data)
    conn.commit()
    print("COMMIT")
    conn.close()
    print("CLOSE")

