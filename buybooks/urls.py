from django.urls import path
from .views import *
app_name = 'buybooks'

urlpatterns = [    
    path('', show_buybooks, name="show_buybooks"),
    path('cart/', show_cart, name="show_cart"),
    path('create/', add_cart_ajax, name="add_cart"),
    path('get-cart/', get_cart_json, name="get_cart"),
    path('delete/', delete_cart_ajax, name="delete"),
    path('get_cart/', get_cart_json, name="get_cart_json"),
    path('delete/', delete_cart_ajax, name="delete"),
]


