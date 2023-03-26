import logging
import os
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


def output_csv(): # Export to CSV function---------->
    csv_file = input("Enter CSV file name: ")
    csv_file_full = csv_file + ".csv"
    file_path = "storage/bots.db"
    out_parent_path = "output"
    out_csv = os.path.join(out_parent_path, csv_file_full)

    conn = create_connection(file_path)

    print_out_comm = """SELECT * FROM bots;"""

    if conn is not None:
        table = pd.read_sql_query(print_out_comm, conn)
        table.to_csv(out_csv, index=False)
        print(colors.BGREEN + f"Successfully exported to {out_csv}" + colors.END)
        conn.close()
    else:
        logger.error("Error while trying to output to CSV")
                  # Export to CSV function---------/>

output_csv()