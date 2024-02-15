import sqlite3
import os
#__file__
#sqlite3.connect(os.path.abspath(__file__+"/../../data")+"data.db")
data=sqlite3.connect(os.path.abspath(__file__+"/../../data")+"/data.db")
# data.cursor()
cursor = data.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Users (INTEGER PRIMARY KEY,id)")
def add_columns(name_column,type_column):
    try:
        cursor.execute(f"ALTER TABLE Users ADD COLUMN {name_column} {type_column}")
    except:
        print("Error column")

def delete_column(name_column):
    try:
        cursor.execute(f"ALTER TABLE Users DROP COLUMN {name_column}")
    except:
        print("Error column")

# [] list
# 0.0 float
# 0 int
# '' str
# True bool
# () tuple
# {} dict
def set_value(columns=("name",'123'),values=[]):
    text=""
    for column in range(len(columns)-1):
        text+="?,"
    text+="?"
    cursor.execute(f"INSERT INTO Users {columns} VALUES ({text})",values)