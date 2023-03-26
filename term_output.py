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

def output_print_term(): # Print output to terminal function---------->
    file_path = "storage/bots.db"

    conn = create_connection(file_path)

    print_out_comm = """SELECT * FROM bots;"""

    if conn is not None:
        table = pd.read_sql_query(print_out_comm, conn)
        print(table)
        conn.close()
    else:
        logger.error("Error while trying to output to terminal")
                         # Print output to terminal function---------/>



output_print_term()