import sqlite3
import easygui as eg
from tabulate  import tabulate
conn=sqlite3.connect("Films.db")
cursor=conn.cursor()

sort_sql=["Film_NAME ASC","Film_NAME DESC","Film_ID ASC","Film_ID DESC","Film_Length ASC","Film_Length DESC" ,"Close"]
sort=["Name A-Z","Name Z-A","ID asc","ID desc","Time asc","Time desc","Close"]
Titles=["ID","Name","release","Rating","Length","Genre"]
genre= ["Comedy","Action","Crime","Animation","Fantasy"]


buttons=["View Database","Search Item","Add Item","Remove Item","Edit Items","Close"]
i=2
rating=["G",'PG','M','R13','R16','R18','RP13','RP16','R']


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
    search_by=eg.buttonbox("select what you want to search with.",choices=["Name","Rating","Genre"])
    if search_by== "Name":
        search=eg.enterbox(str("Enter the name of the film you are looking for"))
        output = cursor.execute(f"Select * FROM Films WHERE Film_Name LIKE '%{search}%' ") 
        eg.msgbox(tabulate(output, headers=Titles))
    
    elif search_by == "Genre":
        search=eg.buttonbox("Select the genre of the film you are looking for",choices=genre)
        output = cursor.execute(f"Select * FROM Films WHERE Film_Genre LIKE '%{search}%' ") 
        eg.msgbox(tabulate(output, headers=Titles))

    elif search_by=="Rating":
        search=eg.buttonbox("Select the rating of the film you are looking for",choices=rating)
        output = cursor.execute(f"Select * FROM Films WHERE Film_Rating LIKE '%{search}%' ")
        eg.msgbox(tabulate(output, headers=Titles))

def Add_db():
    while True:

        input_list=["Id","Name","Year","Length"]

        data=eg.multenterbox("Please enter the following details",title="data_input",fields=input_list)

        if data== None:
            eg.msgbox("canceled input.")
            break
            
        elif any(field.strip() == "" for field in data):
            eg.msgbox("Please fill all the fields")
            continue
            
        try:
            id=int(data[0])
            year=int(data[2])
            length=int(data[3])

        except ValueError:
            eg.msgbox("ID ,Year and Length must be a integer")
            continue

        query = "SELECT 1 FROM films WHERE Film_ID = ? LIMIT 1"
        cursor.execute(query, (id,))

        result = cursor.fetchone()
        if result:
            eg.msgbox("ID already exists")
            continue

        name=data[1]
        if year<1888:
            eg.msgbox("Year cannot be less than 1888")
            continue

        break

    while True:
        rating_data=eg.buttonbox("Select the rating of the film",choices=rating)
        if rating_data==None:
            eg.msgbox("Please select a rating")
            continue

        break

    while True:
        genre=eg.buttonbox("Select the genre of the film",choices=["Comedy","Action","Crime","Animation","Fantasy"])
        if genre==None:
            eg.msgbox("Please select a genre")
            continue

        break
    
    cursor.execute('''INSERT INTO Films (Film_ID, Film_NAME, Film_YEAR, Film_Rating, Film_Length, Film_Genre)
                    VALUES (?, ?, ?, ?, ?, ?)''', (id,name,year,rating_data,length,genre))
    conn.commit()
    eg.msgbox("Data added successfully")


def remove_item():
    while True: 

        search=eg.enterbox("Enter the Name of the film you want to remove")
        if search=="":
            eg.msgbox("Please enter a name")

        elif search== None:
            eg.msgbox("operation canceled")
            

        else:
            break
        
    
    cursor.execute(f"SELECT * FROM Films WHERE Film_Name LIKE '%{search}%'")
    rows = cursor.fetchall()

    output = tabulate(rows, headers=Titles)
    
    
    film_names = [row[1] for row in rows] 
    if len(film_names)<2:
        selected_film=eg.buttonbox(output,title="Remove",choices=film_names)
    else:
        selected_film = eg.choicebox(output, title="Remove", choices=film_names)
        
    confirm=eg.buttonbox(f"Are you sure you want to remove the film {selected_film}",title="Confirm",choices=["Yes","Cancel"])
    if confirm == "Yes":
        cursor.execute(f"DELETE FROM Films WHERE Film_Name LIKE '{selected_film}'")

    else:
        eg.msgbox("Operation cancelled")

    conn.commit()


def edit_item():
    search=eg.enterbox("Enter the Name of the film you want to edit")
    cursor.execute(f"SELECT * FROM Films WHERE Film_Name LIKE '%{search}%'")
    rows = cursor.fetchall()

    output = tabulate(rows, headers=Titles)
    
    
    film_names = [row[1] for row in rows] 
    if len(film_names)<2:
        selected_film=eg.buttonbox(output,title="Edit",choices=film_names)
    else:
        selected_film = eg.choicebox(output, title="Edit", choices=film_names)
    while True:
        action=eg.buttonbox("what would yuo like to edit",choices=["Name","release","Rating","Length","Genre","Close"])
        if action=="Name":
            new_name=eg.enterbox("Enter the new name")
            cursor.execute(f"UPDATE Films SET Film_Name = '{new_name}' WHERE Film_Name LIKE '{selected_film}'")
            
        if action=="release":
            new_release=eg.enterbox("Enter the new release year")
            cursor.execute(f"UPDATE Films SET Film_YEAR = '{new_release}' WHERE Film_Name LIKE '{selected_film}'")

        if action == "Rating":
            new_rating = eg.enterbox("Enter the new rating")
            cursor.execute(f"UPDATE Films SET Film_Rating = '{new_rating}' WHERE Film_Name LIKE '{selected_film}'")

        if action == "Length":
            new_length = eg.enterbox("Enter the new length")
            cursor.execute(f"UPDATE Films SET Film_Length = '{new_length}' WHERE Film_Name LIKE '{selected_film}'")

        if action == "Genre":
            new_genre = eg.buttonbox("select the new genre",choices=genre)
            cursor.execute(f"UPDATE Films SET Film_Genre = '{new_genre}' WHERE Film_Name LIKE '{selected_film}'")

        if action == "Close":
            break
        
        conn.commit()


eg.msgbox("Welcome to the movie the database.",title="Welcome")
while True:
    action=eg.buttonbox("home page",choices=buttons)

    if action==buttons[0]:
        View_db(i)

    elif action==buttons[1]:
        search_db()

    elif action==buttons[2]:
        Add_db()

    elif action == buttons[3]:
        remove_item()

    elif action == buttons[4]:
        edit_item()

    elif action==buttons[5]:
        break