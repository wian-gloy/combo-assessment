import sqlite3
import pandas as pd
import easygui as eg
import tkinter as tk 
from tkinter.scrolledtext import ScrolledText


def show_msg(title,message):
    root = tk.Tk()
    root.title(title)

    text_widget = ScrolledText(root, wrap=tk.WORD, width=100, height=30)
    text_widget.pack(fill=tk.BOTH, expand=True)
    
    text_widget.insert(tk.END, message)
    text_widget.config(state=tk.DISABLED)
    

    root.mainloop()


conn=sqlite3.connect("Films.db")
cursor=conn.cursor()
output=""
buttons=["View Database","Add Item","Remove Item","Edit Items","Close"]

rating=["G",'PG', 'M','R13','R16','R18','RP13','RP16','R']

eg.msgbox("Welcome to the movie the database.",title="Welcome")

action=eg.buttonbox("home page",choices=buttons)
sort=["Name","ID","Time"]

if action==buttons[0]:
    how=eg.buttonbox("How would you like to sort the data",choices=sort)

    #If how == Name it asks user if it should be sorted A-Z or Z-A
    if how==sort[0]:
        how1=eg.buttonbox("how would you like it to be ordered",choices=["A-Z","Z-A"])
        if how1=="A-Z":
            data = pd.read_sql_query("SELECT * FROM FILMS ORDER BY Film_NAME ASC;",conn)
        else:
            data = pd.read_sql_query("SELECT * FROM FILMS ORDER BY Film_NAME DESC;",conn)
    #if how == ID it asks user how it should be sorted asc or desc
    elif how==sort[1]:
        how1=eg.buttonbox("how would you like it to be sorted",choices=["Ascending","Descending"])
        if how1=="Ascending":
            data = pd.read_sql_query("SELECT * FROM FILMS ORDER BY Film_ID ASC;",conn)
        
        else:
            data = pd.read_sql_query("SELECT * FROM FILMS ORDER BY Film_ID DESC;",conn)

    elif how ==sort[2]:
        how1=eg.buttonbox("how would you like it to be sorted",choices=["Ascending","Descending",])
        

    
    data_str = data.to_string(index=False)

    show_msg("Show Database",data_str)

