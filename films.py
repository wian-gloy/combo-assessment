import sqlite3

conn = sqlite3.connect('Films.db')


print("Connected to SQLite")

conn.execute('''CREATE TABLE Films
             (Film_ID INTEGER primary key,
             Film_NAME TEXT UNIQUE,
             Film_Lenth TEXT NOT NULL,
             Film_YEAR INTEGER NOT NULL,
             Film_Rating INTEGER NOT NULL,
             Film_Genre TEXT NOT NULL)''')
            

print("table created")
