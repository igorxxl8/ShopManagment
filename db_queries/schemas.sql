CREATE TABLE Goods (
  goods_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(40)
);
DROP TABLE Goods;

CREATE TABLE Warehouses (
  warehouse_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  goods_id INTEGER,
  available INTEGER,
  FOREIGN KEY(goods_id) REFERENCES Goods(goods_id)
);

CREATE TABLE ShoppingCarts (
  bucket_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  goods_id INTEGER NOT NULL,
  FOREIGN KEY(goods_id) REFERENCES Goods(goods_id)

);

CREATE TABLE Consumers (
  consumer_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  fio VARCHAR(80),
  bucket_id INT NOT NULL,
  FOREIGN KEY(bucket_id) REFERENCES ShoppingCarts(bucket_id)
);

CREATE TABLE Managers(
  manager_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  fio VARCHAR(80)
  --shop_id INTEGER
);

CREATE TABLE Sellers (
  seller_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  fio VARCHAR(80),
  manager_id INTEGER,
  FOREIGN KEY(manager_id) REFERENCES Managers(manager_id)
);

CREATE TABLE Shops (
  shop_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(40),
  manager_id INTEGER,
  seller_id INTEGER,
  FOREIGN KEY(manager_id) REFERENCES Managers(manager_id),
  FOREIGN KEY(seller_id) REFERENCES Sellers(seller_id)
);

-- ALTER TABLE Managers
-- ADD FOREIGN KEY(shop_id) REFERENCES Shops(shop_id)
-- ON DELETE SET NULL;


-- ACTIVITY JOURNALS(LOGS)
CREATE TABLE ConsumersLogs (
  log_id INTEGER PRIMARY KEY AUTOINCREMENT,
  message VARCHAR(50)
);
