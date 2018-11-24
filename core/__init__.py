import sqlite3

conn = sqlite3.connect("\\..\\ShopManagment\\db.sqlite3", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Goods (
                          goods_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                          name VARCHAR(40),
                          price INTEGER
                        );""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Warehouses (
                      warehouse_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      name VARCHAR(40)
                    );""")

cursor.execute("""CREATE TABLE IF NOT EXISTS WarehouseContains (
                      contains_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      warehouse_id INTEGER,
                      goods_id INTEGER,
                      available INTEGER,
                      FOREIGN KEY(goods_id) REFERENCES Goods(goods_id),
                      FOREIGN KEY(warehouse_id) REFERENCES Warehouses(warehouse_id)
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
                      FOREIGN KEY(manager_id) REFERENCES Managers(manager_id)
                    );""")

cursor.execute("""CREATE TABLE IF NOT EXISTS ConsumersLogs (
                      log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      message VARCHAR(50)
                    );""")


if not cursor.execute("""SELECT * FROM Goods""").fetchall():
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Mobile Phone Samsung X523', 1000);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Mobile Phone Lenovo A132', 500);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Mobile Phone LG F142', 400);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Mobile Phone HUAWEI R352', 250);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Mobile Phone iPhone 11', 300);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Mobile Phone Meizu PlusX1', 1200);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Mobile Phone Samsung S1', 300);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Mobile Phone Lenovo AA1', 1234);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Mobile Phone LG A3', 550);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Mobile Phone HUAWEI B2', 100);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Mobile Phone iPhone 12', 300);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Mobile Phone Meizu PlusXS1', 400);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Headphones Samsung XXLarge', 100);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Headphones Xiomi A1', 50);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Headphones Xiomi A2-S', 100);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Headphones Samsung ULX', 25);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Headphones Sony US12', 10);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Headphones Sony AA1', 300);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Headphones Samsung DS', 1200);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Laptop Samsung DR800', 2000);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Laptop LG AASS', 1500);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Laptop Xiomi LR5000', 1200);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Laptop Asus ZB21', 1300);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('Laptop Lenovo YAS', 1400);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('PC Asus MXS Plus', 1500);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('PC Fire AA1', 1600);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('PC Google SA', 2500);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('PC Apple ProPlusUltra BlackEdition', 2200);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('FlashDrive KINGSTON S21 200GB', 100);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('FlashDrive Samsung B1 64GB', 50);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('FlashDrive Sillicon D1 32GB', 10);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('FlashDrive SMART 32GB', 50);""")
    cursor.execute("""INSERT INTO Goods (name, price) VALUES ('FlashDrive NONSTOP 1000GB', 100);""")

    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (5, 32, 100);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (5, 1, 22);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (5, 2, 44);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (5, 3, 11);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (5, 4, 22);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (1, 5, 22);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (1, 6, 55);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (1, 7, 22);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (1, 8, 11);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (1, 9, 88);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (1, 10, 33);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (2, 11, 22);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (2, 12, 88);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (2, 13, 112);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (2, 14, 235);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (2, 15, 11);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (2, 16, 5);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (3, 17, 111);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (3, 18, 654);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (3, 19, 123);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (3, 20, 11);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (3, 21, 231);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (3, 22, 11);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (3, 23, 532);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (4, 24, 647);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (4, 25, 267);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (4, 26, 123);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (4, 27, 661);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (4, 28, 123);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (4, 29, 665);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (4, 30, 235);""")
    cursor.execute("""INSERT INTO WarehouseContains (warehouse_id, goods_id, available) VALUES (4, 31, 124);""")

    cursor.execute("""INSERT INTO Warehouses (name) VALUES ('warehouses_1');""")
    cursor.execute("""INSERT INTO Warehouses (name) VALUES ('warehouses_2');""")
    cursor.execute("""INSERT INTO Warehouses (name) VALUES ('warehouses_3');""")
    cursor.execute("""INSERT INTO Warehouses (name) VALUES ('warehouses_4');""")
    cursor.execute("""INSERT INTO Warehouses (name) VALUES ('warehouses_5');""")

    conn.commit()



