import sqlite3

conn = sqlite3.connect("\\..\\ShopManagment\\db.sqlite3")
cursor = conn.cursor()

cursor.execute("insert into Goods (name) values ('123')")

conn.commit()

print(cursor.execute("select name from Goods;"))

