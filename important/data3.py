import sqlite3
conn = sqlite3.connect('name.db')

print("connection successful")
cursor = conn.cursor()
for row in cursor.execute("SELECT * FROM COMPANY ORDER BY ID DESC"):
    ID, NAME, AGE, ADDRESS, SALARY = row
    print(row)

print("successful")
conn.close()