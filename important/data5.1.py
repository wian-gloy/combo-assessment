import sqlite3

conn = sqlite3.connect('games.db')


print("Connected to SQLite")

conn.execute('''CREATE TABLE GAMES
             (NAME TEXT,
             ProductCode INTEGER NOT NULL UNIQUE,
             ProductId INTEGER primary key,
             Price REAL,
             NumberSales INTEGER,
             DateOfRelease, 
             StoreName TEXT DEFAULT 'Gamesville',
             AgeRestriction INTEGER NOT NULL,
             CHECK (AgeRestriction <= 18 OR (AgeRestriction = 0 AND StoreName = 'kidzone'))
             ); ''')

print("table created")


