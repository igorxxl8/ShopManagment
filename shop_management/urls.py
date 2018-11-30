"""Defines url patterns for shop_management."""

from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'shop_management'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    
    # Show all shops.
    path('shops/', views.shops, name='shops'),

    path('data/<query>', views.get_data_by_query, name='data'),

    path('shops/<shop_id>', views.shop, name='shop'),

    path('manager/<manager_id>', views.manager, name='manager'),

    path('goods/', views.goods, name='goods'),

    path('goods/<good_id>', views.good, name='good'),

    path('shopping_carts/', views.shopping_carts, name='shopping_carts'),

    path('data/', views.data, name='data'),

    path('search/<search_type>', views.search, name='search'),
]
