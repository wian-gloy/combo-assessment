import sqlite3
import easygui as eg

conn=sqlite3.connect("Films.db")

buttons=["View Database","Add Item","Remove Item","Edit Items","Close"]

rating=["G",'PG','M','R13','R16','R18','RP13','RP16','R']

eg.msgbox("Welcome to the movie the database.",title="Welcome")

action=eg.buttonbox("home page",choices=buttons)

if action== buttons[0]:
    print('asd')