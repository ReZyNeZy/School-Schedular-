
#need to create the schedular database and its commands


import sqlite3


db = sqlite3.connect('Grades.db')

c = db.cursor()

sql = """

CREATE TABLE Grades (
id INTEGER PRIMARY KEY,
class VARCHAR(20),
homework VARCHAR(20),
exam VARCHAR(20),
final VARCHAR(20),
grade VARCHAR(20)

)"""

sql2 = """DROP TABLE IF EXISTS Schedule"""



c.execute(sql)

print("DATABASE INITIALIZED")
print()

db.commit()