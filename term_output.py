import logging
import pandas as pd
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

def output_term_main(): # Print output to terminal function---------->
    file_path = "storage/bots.db"

    print_term_menu()
    term_option = input("Enter your option: ")

    if int(term_option) == 1:
        tab_val = "bots"
    elif int(term_option) == 2:
        tab_val = "content"
    else:
        print(colors.BRED + "Invalid option!" + colors.END)

    conn = create_connection(file_path)

    print_out_comm = f"""SELECT * FROM {tab_val};"""

    if conn is not None:
        table = pd.read_sql_query(print_out_comm, conn)
        print(table)
        conn.close()
    else:
        logger.error("Error while trying to output to terminal")
                         # Print output to terminal function---------/>

def print_term_menu():
    print("Choose table you want to print out: ")
    print(colors.BRED + "[1] bots")
    print(colors.BRED + "[2] content" + colors.END)

output_term_main()