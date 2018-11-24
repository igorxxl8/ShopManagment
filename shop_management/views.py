from django.shortcuts import render
from core.db_queries import *


def index(request):
    """The home page for Learning Log."""
    return render(request, 'shop_management/index.html')


def shops(request):
    """Show all shops"""
    shops_ = get_all_shops()
    context = {"shops": shops_}
    return render(request, 'shop_management/shops.html', context)


def goods(request):
    goods_ = get_all_goods()
    context = {"goods": goods_}
    return render(request, 'shop_management/goods.html', context)


def warehouses(request):
    warehouses_ = get_all_warehouse()
    context = {"warehouses": warehouses_}
    return render(request, 'shop_management/warehouses.html', context)


def shopping_carts(request):
    shopping_carts_ = get_all_shoppingcarts()
    context = {"warehouses": shopping_carts_}
    return render(request, 'shop_management/shopping_carts.html', context)
