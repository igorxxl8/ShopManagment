from django.shortcuts import render
from core.db_queries import *


def index(request):
    """The home page for Learning Log."""
    return render(request, 'shop_management/index.html')


def data(request):
    query = request.POST['sql']
    data_ = get_data_by_query(query)
    context = {"data": data_, "query": query}
    return render(request, 'shop_management/data.html', context)


def search(request, search_type):
    text = request.POST['sql']
    query = ' '.join(
        ["SELECT", "*", "FROM", search_type, "WHERE", "name", "LIKE",
         ''.join(["'%", text, "%'"])])
    print(query)
    data_ = get_data_by_query(query)
    context = {"data": data_, "text": text, "type": search_type}
    return render(request, 'shop_management/search.html', context)


def shops(request):
    """Show all shops"""
    shops_ = get_all_shops_with_managers()
    context = {"shops": shops_}
    return render(request, 'shop_management/shops.html', context)


def shop(request, shop_id):
    shop_ = get_shop(shop_id)[0]
    manager_ = get_manager(shop_[2])
    context = {"shop": shop_, "manager": manager_}
    return render(request, 'shop_management/shop.html', context)


def goods(request):
    goods_ = get_all_goods()
    context = {"goods": goods_}
    return render(request, 'shop_management/goods.html', context)


def manager(request, manager_id):
    manager_ = get_manager(manager_id)[0]
    context = {"manager": manager_}
    return render(request, 'shop_management/manager.html', context)


def good(request, good_id):
    good_ = get_good(good_id)[0]
    context = {"good": good_}
    return render(request, 'shop_management/good.html', context)


def warehouses(request):
    warehouses_ = get_all_warehouse()
    print(warehouses_)
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
