from . import cursor


def get_all_goods():
    cursor.execute("""SELECT * FROM Goods""")
    return cursor.fetchall()


def get_data_by_query(query):
    cursor.execute(query)
    return cursor.fetchall()


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


def get_manager(manager_id):
    cursor.execute(
        """SELECT * FROM Managers WHERE Managers.manager_id = {}""".format(
            manager_id))
    return cursor.fetchall()


def get_all_warehouse():
    cursor.execute("""SELECT * FROM Warehouses""")
    return cursor.fetchall()


def get_warehouse(warehouse_id):
    cursor.execute(
        """SELECT * FROM Warehouses WHERE Warehouses.warehouse_id = {}""".format(
            warehouse_id))
    return cursor.fetchall()


def get_all_shoppingcarts():
    cursor.execute("SELECT * FROM ShoppingCarts")
    return cursor.fetchall()


def get_all_warehouse_contains():
    cursor.execute("SELECT * FROM WarehouseContains")
    return cursor.fetchall()

# conn.commit()
