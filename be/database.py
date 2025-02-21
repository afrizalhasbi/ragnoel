import sqlite3


def get_connection()
    conn = sqlite.connect('database.db')
    cursor = conn.cursor()
    return conn, cursor
