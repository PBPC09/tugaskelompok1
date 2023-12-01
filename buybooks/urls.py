from django.urls import path
from .views import *
app_name = 'buybooks'

urlpatterns = [    
    path('', show_buybooks, name="show_buybooks"),
    path('cart/', show_cart, name="show_cart"),
    path('create/<int:id>/', add_cart_ajax, name="add_cart"),
    path('delete/<int:id>/', delete_cart, name="delete_cart"),
    path('show_books_json', show_books_json, name="show_books_json"),
    path('show_books_json_lt', show_books_json_rating_lt, name="show_books_json_lt"),
    path('show_books_json_gte', show_books_json_rating_gte, name="show_books_json_gte"),
    path('selected/<int:id>/', selected, name="selected"),
    path('show_cart_json/<str:uname>/', show_cart_json, name="show_cart_json"),
    path('show_carts_json', show_carts_json, name="show_carts_json"),
]