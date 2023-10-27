from django.urls import path
from registerbook.views import regist_books_json, show_registered_books, add_book

app_name = 'registerbook'

urlpatterns = [
    path('', show_registered_books, name='show_registered_books'),
    path('add-book', add_book, name='add_book'),
    path('json/', regist_books_json, name='regist_books_json'),
]