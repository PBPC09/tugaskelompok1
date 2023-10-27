from django.urls import path
from registerbook.views import regist_books_json, show_registered_books, add_book, get_book_json, add_book_ajax, remove_book, show_received_orders

app_name = 'registerbook'

urlpatterns = [
    path('', show_registered_books, name='show_registered_books'),
    path('add-book', add_book, name='add_book'),
    path('json/', regist_books_json, name='regist_books_json'),
    path('get-book/', get_book_json, name='get_book_json'),
    path('add-book-ajax/', add_book_ajax, name='add_book_ajax'),
    path('delete-book-ajax/<int:book_id>/', remove_book, name='remove_book'),
    path('received-orders/', show_received_orders, name='show_received_orders'),
]