import sqlite3

# Connect to the database
conn = sqlite3.connect('Films.db')

# Insert data into the Films table
movies = [
    (1, 'Ghostbusters', 2016, 'PG', 116, 'Comedy'),
    (2, 'The Legend of Tarzan', 2016, 'M', 109, 'Action'),
    (3, 'Jason Bourne', 2016, 'M', 123, 'Action'),
    (4, 'The Nice Guys', 2016, 'R16', 116, 'Crime'),
    (5, 'The Secret Life of Pets', 2016, 'PG', 91, 'Animation'),
    (6, 'Star Trek Beyond', 2016, 'M', 120, 'Action'),
    (7, 'Batman v Superman', 2016, 'M', 151, 'Action'),
    (8, 'Finding Dory', 2016, 'PG', 103, 'Animation'),
    (9, 'Zootopia', 2016, 'PG', 108, 'Animation'),
    (10, 'The BFG', 2016, 'PG', 90, 'Fantasy'),
    (11, 'A Monster Calls', 2016, 'M', 108, 'Fantasy'),
    (12, 'Independence Day: Resurgence', 2016, 'M', 120, 'Action'),
    (13, 'The Green Room', 2016, 'R16', 94, 'Crime'),
    (14, 'Doctor Strange', 2016, 'M', 130, 'Fantasy'),
    (15, 'The Jungle Book', 2016, 'PG', 105, 'Fantasy'),
    (16, 'Alice Through the Looking Glass', 2016, 'PG', 118, 'Fantasy'),
    (17, 'Imperium', 2016, 'R16', 109, 'Crime'),
    (18, 'The Infiltrator', 2016, 'R16', 127, 'Crime'),
    (19, 'Mad Max: Fury Road', 2015, 'R16', 120, 'Action'),
    (20, 'Spectre', 2015, 'M', 145, 'Action'),
    (21, 'Jurassic World', 2015, 'M', 100, 'Action'),
    (22, 'The Intern', 2015, 'M', 121, 'Comedy'),
    (23, 'Ted 2', 2015, 'R16', 121, 'Comedy'),
    (24, 'Trainwreck', 2015, 'R16', 122, 'Comedy'),
    (25, 'Inside Out', 2015, 'PG', 94, 'Animation'),
    (26, 'The Good Dinosaur', 2015, 'PG', 101, 'Animation'),
    (27, 'Divergent', 2014, 'M', 121, 'Action'),
    (28, 'The Maze Runner', 2014, 'M', 115, 'Action'),
    (29, 'Birdman', 2014, 'R16', 119, 'Comedy'),
    (30, 'Guardians of the Galaxy', 2014, 'M', 121, 'Fantasy'),
    (31, 'The Lego Movie', 2014, 'PG', 100, 'Animation'),
    (32, 'Big Hero 6', 2014, 'PG', 108, 'Animation'),
    (33, 'The Drop', 2014, 'R16', 106, 'Crime')
    ]

conn.executemany('INSERT INTO Films VALUES (?, ?, ?, ?, ?, ?)', movies)

# Commit the transaction
conn.commit()

print("Data inserted successfully")

# Close the connection
conn.close()
