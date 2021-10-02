import sqlite3

conn = sqlite3.connect('Movies.db')

c= conn.cursor()

#c.execute("""CREATE TABLE Movies (name text, actor text, actress text, director text, year of release integer) """)

#c.execute("INSERT INTO Movies Values ('Titanic','Leonardo','Kate','James','1997')")

#c.execute("INSERT INTO Movies Values ('Avatar','Sam','Zoe','James','2009')")

#c.execute("SELECT * FROM Movies WHERE actor='Leonardo'")

c.execute("SELECT * FROM Movies")

print(c.fetchall())

conn.commit()

conn.close()