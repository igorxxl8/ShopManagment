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
    data_ = get_data_by_query(query)
    context = {"data": data_, "text": text, "type": search_type}
    return render(request, 'shop_management/search.html', context)


def shops(request):
    """Show all shops"""
    shops_ = get_all_shops_with_managers()
    context = {"shops": shops_}
    return render(request, 'shop_management/shops.html', context)


def shop(request, shop_id):
    shop_ = get_shop_with_manager(shop_id)[0]
    goods_ = get_shops_warehouse_contains(shop_id)
    context = {"shop": shop_, "goods": goods_}
    return render(request, 'shop_management/shop.html', context)


def goods(request):
    goods_ = get_all_goods_with_available_count()
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


def shopping_carts(request):
    shopping_carts_ = get_all_shoppingcarts()
    context = {"shopping_carts": shopping_carts_}
    return render(request, 'shop_management/shopping_carts.html', context)


def shopping_cart(request, user_name):
    shopping_cart_ = get_shopping_cart(user_name)
    total = 0
    for tup in shopping_cart_:
        total += tup[2]
    context = {"shopping_cart": shopping_cart_, "price": total}
    return render(request, 'shop_management/shopping_cart.html', context)


def warehouses(request):
    warehouses_ = get_all_warehouse()
    context = {"warehouses": warehouses_}
    return render(request, 'shop_management/warehouses.html', context)


def warehouse(request, warehouse_id):
    warehouse_ = get_all_warehouse_contains(warehouse_id)
    context = {"warehouse": warehouse_}
    return render(request, 'shop_management/warehouse.html', context)
