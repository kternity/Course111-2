import sqlite3
from flask import g #global context/temp memory

DATABASE_URL = "main.db" #defining db / exists all throughout the run time/ it's constant / 

def get_db(): 
   db = getattr(g, "database", None)
   if not db: #same as asying if db == none
      db = g.database = sqlite3.connect(DATABASE_URL)
   return db
