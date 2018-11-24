"""Defines url patterns for shop_management."""

from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'shop_management'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    
    # Show all topics.
    path('shops/', views.shops, name='shops'),
    
    # Detail page for a single topic.
    path('shops/<int:topic_id>/', views.shop, name='shop'),
    
    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),
    
    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
