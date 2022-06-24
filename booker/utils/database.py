import sqlite3
import os

FILENAME = "database.db"


def ensure_tables_are_created():
    con = sqlite3.connect(FILENAME)
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS desk
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               desk_id text NOT NULL, person text NOT NULL)''')

    con.commit()
    con.close()


def get_bookings(desk_id):
    con = sqlite3.connect(FILENAME)
    cur = con.cursor()
    result = cur.execute(
        "SELECT * FROM desk WHERE desk_id = ?",
        (desk_id,)).fetchall()
    con.close()
    return result


def add_booking(desk_id, person):
    con = sqlite3.connect(FILENAME)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO desk(desk_id, person) VALUES(?, ?)",
        [desk_id, person])
    id = cur.lastrowid
    con.commit()
    con.close()
    return id


def delete_bookings(desk_id):
    con = sqlite3.connect(FILENAME)
    cur = con.cursor()
    result = cur.execute("DELETE FROM desk where desk_id = ?", (desk_id,))
    deleted = result.rowcount
    con.commit()
    con.close()
    return deleted == 1


def get_db_status():
    # It's always running perfectly, as long as it exists of course! :)
    return os.path.exists(FILENAME)
