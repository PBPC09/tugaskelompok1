from django.urls import path
from .views import *

app_name = 'buybooks'

urlpatterns = [    
    path('', show_test, name="show_test"),
    path('show-books/', show_book, name='show_books'),
    path('filter/price/lt30/', filter_books, {'price': 'lt30'}, name='filter_price_lt30'),
    path('filter/price/gt30/', filter_books, {'price': 'gt30'}, name='filter_price_gt30'),
    path('filter/pagecount/lt100/', filter_books, {'page_count': 'lt100'}, name='filter_pagecount_lt100'),
    path('filter/pagecount/gt100/', filter_books, {'page_count': 'gt100'}, name='filter_pagecount_gt100'),
    path('filter/rating/lt3/', filter_books, {'rating': 'lt3'}, name='filter_rating_lt3'),
    path('filter/rating/gt3/', filter_books, {'rating': 'gt3'}, name='filter_rating_gt3'),
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('show-books-json/', show_book_json, name='show_books_json'),  
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
]