import sqlite3

conn = sqlite3.connect("\\..\\ShopManagment\\db.sqlite3")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Goods (
                      goods_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      name VARCHAR(40)
                    );""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Warehouses (
                      warehouse_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      goods_id INTEGER,
                      available INTEGER,
                      FOREIGN KEY(goods_id) REFERENCES Goods(goods_id)
                    );""")

cursor.execute("""CREATE TABLE IF NOT EXISTS ShoppingCarts (
                      bucket_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      goods_id INTEGER NOT NULL,
                      FOREIGN KEY(goods_id) REFERENCES Goods(goods_id)
                    );""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Consumers (
                      consumer_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      fio VARCHAR(80),
                      bucket_id INT NOT NULL,
                      FOREIGN KEY(bucket_id) REFERENCES ShoppingCarts(bucket_id)
                    );""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Managers (
                      manager_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      fio VARCHAR(80)
                    );""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Shops (
                      shop_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      name VARCHAR(40),
                      manager_id INTEGER,
                      FOREIGN KEY(manager_id) REFERENCES Managers(manager_id),
                    );""")

cursor.execute("""CREATE TABLE IF NOT EXISTS ConsumersLogs (
                      log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      message VARCHAR(50)
                    );""")

cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")
cursor.execute("""INSERT INTO Goods (name) VALUES ('');""")


