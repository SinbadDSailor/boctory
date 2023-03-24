import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def db_main():
    file_path = "storage/bots.db"

    a_table = """CREATE TABLE IF NOT EXISTS bots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    platform TEXT,
    email TEXT,
    password TEXT,
    acc_date TEXT,
    email_pass TEXT);
    """

    conn = create_connection(file_path)

    if conn is not None:
        create_table(conn, a_table)
        conn.commit()
        print("[~] Database successfully created!")
        conn.close()
    else:
        print("Error while creating Database")


db_main()