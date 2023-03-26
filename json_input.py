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

def bulk_json_import():
    path_to_json = input("Enter path to JSON file: ")
    file_path = "storage/bots.db"
    conn = create_connection(file_path)

    try:
        ldata = pd.read_json(path_to_json)
        ldata.to_sql("bots", conn, if_exists="append", index=False)
        print(colors.BGREEN + "Successfully imported to database!" + colors.END)
        conn.commit()
        conn.close()
    except Error as e:
        logger.error(e)

bulk_json_import()