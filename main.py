import sqlite3 as sql

db=sql.connect("shop.mdf")
cursor=db.cursor()
cursor.execute("insert into Role values ('Administrator')")
cursor.execute("insert into Role values ('User')")
db.commit()
data=cursor.execute("select*from Role")
values=data.fetchall()
for i in values:
    print(i)