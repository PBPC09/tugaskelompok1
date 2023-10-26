from django.urls import path
from registerbook.views import regist_books, show_registered_books

app_name = 'registerbook'

urlpatterns = [
    path('', show_registered_books, name='show_registered_books'),
    path('regist_books', regist_books, name='regist_books'),
]