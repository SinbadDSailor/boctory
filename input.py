import logging
import sqlite3
from sqlite3 import Error
from colors import colors

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

def exec_comm(conn, create_table_sql, in_vars):
    try:
        c = conn.cursor()
        c.execute(create_table_sql, in_vars)
    except Error as e:
        logger.error(e)

def input_main():
    file_path = "storage/bots.db"

    print("Enter data value by value")
    print("If you don't want to input data, just skip input question")
    print("---------------------------------------------------------")
    platform = input("Enter platform marker: ")
    email = input("Enter email address: ")
    password = input("Enter password: ")
    acc_date = input("Enter account creation date: ")
    email_pass = input("Enter email password: ")
    

    input_vars_checker = (platform, email, password, acc_date, email_pass)
    input_vars = ()
    for val in input_vars_checker:
        if val == "":
            val = None
            input_vars = input_vars + (val,)
        else:
            input_vars = input_vars + (val,)

    ind_input_comm = """INSERT INTO bots 
    (id, 
    platform, 
    email,
    password,
    acc_date, 
    email_pass) VALUES (null, ?, ?, ?, ?, ?)"""

    conn = create_connection(file_path)

    if conn is not None:
        exec_comm(conn, ind_input_comm, input_vars)
        conn.commit()
        print(colors.BGREEN + "Successfully")
        conn.close()
    else:
        logger.error("Error while trying to individual input")

input_main()