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

    path('goods/', views.goods, name='goods'),

    path('warehouses/', views.warehouses, name='warehouses'),

    path('shopping_carts/', views.shopping_carts, name='shopping_carts'),
]
