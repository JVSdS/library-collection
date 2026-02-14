import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "library.db")


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn