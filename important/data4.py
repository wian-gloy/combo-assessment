import sqlite3
import easygui as eg

conn = sqlite3.connect('name.db')

id=eg.enterbox("enter ID number")

name=eg.enterbox("enter name")
id=int(id)
age=eg.enterbox("enter age")
age=int(age)
city=eg.enterbox("enter city")
Salary=eg.enterbox("enter salary")
Salary=float(Salary)

conn.execute('''INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY )
             VALUES(?,?,?,?,?)''', (id,name,age,city,Salary)
             )

conn.commit()
