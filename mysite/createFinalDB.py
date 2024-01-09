import sqlite3

db = sqlite3.connect('schedule.db')
c = db.cursor()

db2 = sqlite3.connect('grades.db')


sql = """

    CREATE TABLE schedule (
    id INTEGER PRIMARY KEY,
    class VARCHAR(