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

if action==buttons[0]:
    data = pd.read_sql_query('Select * from FILMS ORDER BY Film_ID ASC;', conn)
    
    data_str = data.to_string(index=False)

    show_msg("Show Database",data_str)

