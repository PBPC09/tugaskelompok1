from django.urls import path
from .views import *
app_name = 'buybooks'

urlpatterns = [    
    path('create/<int:id>/', add_cart_ajax, name="add_cart"),
    path('get_cart/', get_cart_json, name="get_cart_json"),
    path('delete/<int:id>/', delete_cart_ajax, name="delete"),
    path('show_books_json', show_books_json, name="show_books_json"),
    path('show_books_json_lt', show_books_json_rating_lt, name="show_books_json"),
    path('show_books_json_gte', show_books_json_rating_gte, name="show_books_json")
]

