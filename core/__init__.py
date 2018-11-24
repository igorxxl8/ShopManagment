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
                      user_name VARCHAR(40),
                      phone_number VARCHAR(40),
                      goods_id INTEGER NOT NULL,
                      manager_id INTEGER NOT NULL,
                      FOREIGN KEY(goods_id) REFERENCES Goods(goods_id),
                      FOREIGN KEY(manager_id) REFERENCES Managers(manager_id)
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

    cursor.execute("""INSERT INTO Managers (fio) VALUES ('Matthews John');""")
    cursor.execute("""INSERT INTO Managers (fio) VALUES ('McKenzie Ronald');""")
    cursor.execute("""INSERT INTO Managers (fio) VALUES ('Thompson Edwin');""")
    cursor.execute("""INSERT INTO Managers (fio) VALUES ('Howard Horatio');""")
    cursor.execute("""INSERT INTO Managers (fio) VALUES ('Harris Noel');""")
    cursor.execute("""INSERT INTO Managers (fio) VALUES ('Cole August');""")
    cursor.execute("""INSERT INTO Managers (fio) VALUES ('Wilcox Charles');""")
    cursor.execute("""INSERT INTO Managers (fio) VALUES ('Wilkerson David');""")
    cursor.execute("""INSERT INTO Managers (fio) VALUES ('Jacobs Ethan');""")
    cursor.execute("""INSERT INTO Managers (fio) VALUES ('Whitehead Kerry');""")

    cursor.execute("""INSERT INTO Shops (name, manager_id) VALUES ('E-Shop', 1);""")
    cursor.execute("""INSERT INTO Shops (name, manager_id) VALUES ('Only-E-Shop', 2);""")
    cursor.execute("""INSERT INTO Shops (name, manager_id) VALUES ('Shop of Electro', 3);""")
    cursor.execute("""INSERT INTO Shops (name, manager_id) VALUES ('Electro Shop', 4);""")
    cursor.execute("""INSERT INTO Shops (name, manager_id) VALUES ('Super-E Shop', 5);""")
    cursor.execute("""INSERT INTO Shops (name, manager_id) VALUES ('Ultra Electronic Shop', 6);""")
    cursor.execute("""INSERT INTO Shops (name, manager_id) VALUES ('Thunder Shop', 7);""")
    cursor.execute("""INSERT INTO Shops (name, manager_id) VALUES ('Goods is good', 8);""")
    cursor.execute("""INSERT INTO Shops (name, manager_id) VALUES ('Only E-Shop', 9);""")
    cursor.execute("""INSERT INTO Shops (name, manager_id) VALUES ('Keks Shop', 10);""")

    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
            ('Alex', '291112233', 1, 1);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Alex', '291112233', 3, 1);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Alex', '291112233', 10, 1);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('John', '292223562', 2, 2);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('John', '292223562', 15, 2);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('John', '292223562', 30, 2);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Ben', '444713565', 2, 3);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Ben', '444713565', 17, 3);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Ben', '444713565', 13, 3);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Harry', '238472411', 11, 4);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Harry', '238472411', 8, 4);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Harry', '238472411', 4, 4);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Oliver', '456228836', 31, 5);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Jack', '532225123', 16, 6);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Jack', '532225123', 20, 6);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Charlie', '884563422', 24, 7);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Thomas', '573356714', 31, 8);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Thomas', '573356714', 24, 8);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Thomas', '573356714', 23, 8);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Thomas', '573356714', 11, 8);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Jacob', '746664689', 1, 9);"""
    )
    cursor.execute(
        """INSERT INTO ShoppingCarts (user_name, phone_number, goods_id, manager_id) VALUES
        ('Alfie ', '66354567', 27, 10);"""
    )

    conn.commit()
