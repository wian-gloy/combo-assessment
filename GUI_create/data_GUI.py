import sqlite3
import easygui as eg
from tabulate  import tabulate
sort=["Film_NAME ASC","Film_NAME DESC"]
Titles=["ID","Name","release","Rating","Lenth","Genre"]
conn=sqlite3.connect("Films.db")
cursor=conn.cursor()
output=[]
buttons=["View Database","Add Item","Remove Item","Edit Items","Close"]
i=0
rating=["G",'PG', 'M','R13','R16','R18','RP13','RP16','R']

eg.msgbox("Welcome to the movie the database.",title="Welcome")

action=eg.buttonbox("home page",choices=buttons)

def View_db():
    for row in cursor.execute(f"Select * FROM Films ORDER BY {sort[i]}"):
        Film_ID,Film_name,Film_Year,Film_Rating,Film_Length,Film_Genre=row
        output.append(row)

    list=tabulate(output, headers=Titles)
    eg.buttonbox(list,choices="name asc")

View_db()