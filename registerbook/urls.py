from django.urls import path
from registerbook.views import (show_registered_books, show_received_orders,
                                show_json, show_json_by_id, get_book_json, 
                                add_book_ajax, remove_book)

app_name = 'registerbook'

urlpatterns = [
    path('', show_registered_books, name='show_registered_books'),
    path('received-orders/', show_received_orders, name='show_received_orders'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('get-book/', get_book_json, name='get_book_json'),
    path('add-book-ajax/', add_book_ajax, name='add_book_ajax'),
    path('delete-book-ajax/<int:book_id>/', remove_book, name='remove_book'),
]