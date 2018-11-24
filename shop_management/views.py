from django.shortcuts import render
from core.db_queries import *


def index(request):
    """The home page for Learning Log."""
    return render(request, 'shop_management/index.html')


def get_data_by_query(request, query):
    data = get_data_by_query(query)
    context = {"data" : data}
    return render(request, 'shop_management/data.html', context)


def shops(request):
    """Show all shops"""
    shops_ = get_all_shops()
    context = {"shops": shops_}
    return render(request, 'shop_management/shops.html', context)


def shop(request, shop_id):
    shop_ = get_shop(shop_id)[0]
    context = {"shop": shop_}
    return render(request, 'shop_management/shop.html', context)


def goods(request):
    goods_ = get_all_goods()
    context = {"goods": goods_}
    return render(request, 'shop_management/goods.html', context)


def good(request, good_id):
    good_ = get_good(good_id)[0]
    context = {"good": good_}
    return render(request, 'shop_management/good.html', context)


def warehouses(request):
    warehouses_ = get_all_warehouse()
    context = {"warehouses": warehouses_}
    return render(request, 'shop_management/warehouses.html', context)


def warehouse(request, warehouse_id):
    warehouse_ = get_warehouse(warehouse_id)[0]
    context = {"warehouse": warehouse_}
    return render(request, 'shop_management/warehouse.html', context)


def shopping_carts(request):
    shopping_carts_ = get_all_shoppingcarts()
    context = {"warehouses": shopping_carts_}
    return render(request, 'shop_management/shopping_carts.html', context)
