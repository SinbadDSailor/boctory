import sqlite3
from sqlite3 import Error
from colors import colors
import logging

#Logging setup ------------------>
filenm = "storage/log.log"
fmat = "%(levelname)s: %(asctime)s | %(name)s | %(funcName)s | %(message)s"
logging.basicConfig(filename=filenm, level=logging.DEBUG, format=fmat, filemode="w")
logger = logging.getLogger(__name__)
#Logging setup -----------------/>


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        logger.error(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        logger.error(e)

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

    b_table = """CREATE TABLE IF NOT EXISTS content (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    platform TEXT,
    heading TEXT,
    paragraph TEXT,
    image TEXT);
    """

    conn = create_connection(file_path)

    if conn is not None:
        create_table(conn, a_table)
        create_table(conn, b_table)
        conn.commit()
        print(colors.BGREEN + "[~] Database successfully created!" + colors.END)
        conn.close()
    else:
        logger.error("Error while creating Database")


db_main()