from . import cursor


def get_all_goods():
    cursor.execute("""SELECT * FROM Goods""")
    return cursor.fetchall()


def get_all_shops():
    cursor.execute("""SELECT * FROM Shops""")
    return cursor.fetchall()


def get_all_warehouse():
    cursor.execute("""SELECT * FROM Warehouses""")
    return cursor.fetchall()


def get_all_shoppingcarts():
    cursor.execute("SELECT * FROM ShoppingCarts")
    return cursor.fetchall()


def get_all_warehouse_contains():
    cursor.execute("SELECT * FROM WarehouseContains")
    return cursor.fetchall()


#conn.commit()
