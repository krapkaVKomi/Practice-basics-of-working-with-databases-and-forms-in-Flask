import sqlite3

database = sqlite3.connect('data.db')
cursor = database.cursor()
database.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, note TEXT, date DATE)')
database.commit()


def connect_db():
    database = sqlite3.connect('data.db')
    cursor = database.cursor()
    return database, cursor



