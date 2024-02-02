import sqlite3 as sql
import os
name="shop.mdf"
def createDB():   
    db=sql.connect(name)
    cursor=db.cursor()
    cursor.execute("""create table if not exists Title (
        id integer primary key autoincrement,
        titleName nvarchar(20)
        )""")
    cursor.execute("""create table if not exists User (
        id integer primary key,
        userName nvarchar(20),
        password nvarchar(20),
        fullName nvarchar(50),
        address nvarchar(250),
        titleId integer,
        foreign key(titleId) references title(id)
        )""")
    db.commit()

if __name__=='__main__' and not os.path.exists(name):
    createDB()