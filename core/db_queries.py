from sqlite3 import OperationalError

from . import cursor


def get_all_goods():
    cursor.execute("""SELECT * FROM Goods""")
    return cursor.fetchall()


def get_all_goods_with_available_count():
    cursor.execute(
        """
        SELECT Goods.goods_id, Goods.name, Goods.price, WarehouseContains.warehouse_id, WarehouseContains.available 
        FROM Goods 
        JOIN WarehouseContains 
        ON Goods.goods_id = WarehouseContains.goods_id
        ORDER BY Goods.goods_id 
        """
    )
    return cursor.fetchall()


def get_data_by_query(query):
    try:
        if ('select' in query or 'SELECT' in query) and ';' not in query:
            cursor.execute(query)
            return cursor.fetchall()
        else:
            return "Error"
    except OperationalError:
        return []


def get_good(good_id):
    cursor.execute(
        """SELECT * FROM Goods WHERE Goods.goods_id = {}""".format(good_id))
    return cursor.fetchall()


def get_all_shops():
    cursor.execute("""SELECT * FROM Shops""")
    return cursor.fetchall()


def get_all_shops_with_managers():
    cursor.execute(
        """
        SELECT Shops.shop_id, Shops.name, Shops.manager_id, Managers.fio 
        FROM Shops 
        JOIN Managers 
        ON Shops.manager_id = Managers.manager_id
        """)
    return cursor.fetchall()


def get_shop(shop_id):
    cursor.execute(
        """SELECT * FROM Shops WHERE Shops.shop_id = {}""".format(shop_id))
    return cursor.fetchall()


def get_warehouse(warehouse_id):
    cursor.execute(
        """SELECT * FROM Warehouse WHERE Warehouse.warehouse_id = {}""".format(warehouse_id))
    return cursor.fetchall()


def get_shop_with_manager(shop_id):
    cursor.execute(
        """SELECT Shops.name, Shops.manager_id, Managers.fio 
            FROM Shops 
            JOIN Managers 
            ON Shops.manager_id = Managers.manager_id
            WHERE Shops.shop_id = {}""".format(shop_id))
    return cursor.fetchall()


def get_shops_warehouse_contains(warehouse_id):
    cursor.execute(
        """SELECT Goods.goods_id, Goods.name, Goods.price, WarehouseContains.available
            FROM WarehouseContains
            JOIN Goods
            ON Goods.goods_id = WarehouseContains.goods_id
            WHERE WarehouseContains.warehouse_id = {}""".format(warehouse_id))
    return cursor.fetchall()


def get_manager(manager_id):
    cursor.execute(
        """SELECT * FROM Managers WHERE Managers.manager_id = {}""".format(
            manager_id))
    return cursor.fetchall()


def get_all_warehouse():
    cursor.execute("""SELECT * FROM Warehouses""")
    return cursor.fetchall()


def get_shopping_cart(user_name):
    cursor.execute(
        """SELECT ShoppingCarts.user_name, Goods.name, Goods.price FROM ShoppingCarts JOIN Goods ON ShoppingCarts.goods_id = Goods.goods_id
        WHERE ShoppingCarts.user_name = '{}'""".format(user_name))
    return cursor.fetchall()


def get_all_shoppingcarts():
    cursor.execute("SELECT * FROM ShoppingCarts GROUP BY ShoppingCarts.phone_number")
    return cursor.fetchall()


def get_all_warehouse_contains(warehouse_id):
    cursor.execute("""SELECT Goods.name, WarehouseContains.available FROM WarehouseContains JOIN Goods on Goods.goods_id = WarehouseContains.goods_id
                   WHERE WarehouseContains.warehouse_id = {}""".format(warehouse_id))
    return cursor.fetchall()

# conn.commit()
