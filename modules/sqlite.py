import sqlite3
import os
#__file__
#sqlite3.connect(os.path.abspath(__file__+"/../../data")+"data.db")
data=sqlite3.connect(os.path.abspath(__file__+"/../../data")+"/data.db")
# data.cursor()
cursor = data.cursor()

def add_column(name_column,type_column,name_table="Users"):
    try:
        cursor.execute(f"ALTER TABLE {name_table} ADD COLUMN {name_column} {type_column}")
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
def get_value(column= "*",name_table="AdminPassword"):
    cursor.execute(f"SELECT {column} FROM {name_table}")
    return cursor.fetchall()
def set_value(columns=("name",'123'),values=[],name_table="Users"):
    text=""
    for column in range(len(columns)-1):
        text+="?,"
    text+="?"
    cursor.execute(f"INSERT INTO {name_table} {tuple(columns)} VALUES ({text})",values)