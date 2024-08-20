import sqlite3
import pandas as pd
import easygui as eg

conn=sqlite3.connect("Films.db")
cursor=conn.cursor()
output=""
buttons=["View Database","Add Item","Remove Item","Edit Items","Close"]

rating=["G",'PG', 'M','R13','R16','R18','RP13','RP16','R']

eg.msgbox("Welcome to the movie the database.",title="Welcome")

action=eg.buttonbox("home page",choices=buttons)
 
df=pd.read