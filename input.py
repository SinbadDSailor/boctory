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

def input_bots():
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
        print(colors.BGREEN + "Successfully executed input!" + colors.END)
        conn.close()
    else:
        logger.error("Error while trying to individual input")

def input_content():
    file_path = "storage/bots.db"

    print("Enter data value by value")
    print("If you don't want to input data, just skip input question")
    print("---------------------------------------------------------")
    platform = input("Enter platform marker: ")
    heading = input("Enter heading: ")
    paragraph = input("Enter paragraph: ")
    image = input("Enter image path: ")
    

    input_vars_checker = (platform, heading, paragraph, image)
    input_vars = ()
    for val in input_vars_checker:
        if val == "":
            val = None
            input_vars = input_vars + (val,)
        else:
            input_vars = input_vars + (val,)

    ind_input_comm = """INSERT INTO content 
    (id, 
    platform, 
    heading,
    paragraph,
    image) VALUES (null, ?, ?, ?, ?)"""

    conn = create_connection(file_path)

    if conn is not None:
        exec_comm(conn, ind_input_comm, input_vars)
        conn.commit()
        print(colors.BGREEN + "Successfully executed input!" + colors.END)
        conn.close()
    else:
        logger.error("Error while trying to individual input")

def input_main():
    print("Tables: ")
    print(colors.BRED + "[1] bots")
    print(colors.BRED + "[2] content" + colors.END)
    table_option = input("Enter your option: ")

    if int(table_option) == 1:
        input_bots()
    elif int(table_option) == 2:
        input_content()
    else:
        print(colors.BRED + "Invalid option!" + colors.END)

input_main()