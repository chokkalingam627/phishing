import sqlite3

conn = sqlite3.connect('todo.db')

curse = conn.cursor()

# curse.execute(" INSERT INTO todo VALUES (:c) ", {'c':'c'})
curse.execute(" DELETE FROM todo WHERE task = (?) ", ('f',))

# for x in curse.fetchall():
#     (n,) = x
#     print(n)

conn.commit()

conn.close()