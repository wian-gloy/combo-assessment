import sqlite3
import easygui as eg
from tabulate  import tabulate
conn=sqlite3.connect("Films.db")
cursor=conn.cursor()

sort_sql=["Film_NAME ASC","Film_NAME DESC","Film_ID ASC","Film_ID DESC","Film_Length ASC","Film_Length DESC" ,"Close"]
sort=["Name A-Z","Name Z-A","ID asc","ID desc","Time asc","Time desc","Close"]
Titles=["ID","Name","release","Rating","Length","Genre"]



buttons=["View Database","Search Item","Remove Item","Edit Items","Close"]
i=2
rating=["G",'PG','M','R13','R16','R18','RP13','RP16','R']

eg.msgbox("Welcome to the movie the database.",title="Welcome")

action=eg.buttonbox("home page",choices=buttons)

def View_db(i):
    while not i == 6:
        output=[]
        for row in cursor.execute(f"Select * FROM Films ORDER BY {sort_sql[i]}"):
            Film_ID,Film_name,Film_Year,Film_Rating,Film_Length,Film_Genre=row
            output.append(row)

        list=tabulate(output, headers=Titles)
        sortby=eg.buttonbox(list,choices=sort)
        if sortby == sort[0]:
            i=0
            
        elif sortby == sort[1]:
            i=1
            
        elif sortby == sort[2]:
            i=2
            
        elif sortby == sort[3]:
            i=3
            
        elif sortby == sort[4]:
            i=4
            
        elif sortby == sort[5]:
            i=5
        
        elif sortby == sort[6]:
            i=6
            
        
def search_db():
    search_by=eg.buttonbox("select what you want to search with.",choices=["Name","ID","Year","Rating",'Genre'])
    if search_by== "Name":
        search=eg.enterbox(str("Enter the name of the film you are looking for"))
        output = cursor.execute(f"Select * FROM Films WHERE Film_Name LIKE '%{search}%' ") 
    eg.msgbox(tabulate(output, headers=Titles))
if action==buttons[0]:
    View_db(i)

elif action==buttons[1]:
    search_db()
