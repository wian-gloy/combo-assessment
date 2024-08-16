import sqlite3

conn = sqlite3.connect('Films.db')


print("Connected to SQLite")

conn.execute('''CREATE TABLE Films
             (Film_ID INTEGER primary key,
             Film_NAME TEXT,           
             Film_YEAR INTEGER NOT NULL CHECK(Film_YEAR>=1888),
             Film_Rating TEXT NOT NULL,
             Film_Length INTEGER NOT NULL CHECK(Film_Length<5100),
             Film_Genre TEXT NOT NULL)''')
            

print("table created")

conn.close()