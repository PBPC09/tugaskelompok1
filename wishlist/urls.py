from django.urls import path
from wishlist.views import *

app_name = 'wishlist'

urlpatterns = [
    path('', mywishlist, name='mywishlist'),    
    path('bookprofile/', show_book_profile, name='bookprofile'),
    path('book/<int:book_id>/', show_book_details, name='show_book_details'),
    path('add_to_wishlist/', add_to_wishlist, name='add_to_wishlist'),
    path('delete_wishlist_item/<int:item_id>/', delete_wishlist_item, name='delete_wishlist_item'),
    path('get-books/', get_books, name='get_books'),
    path('mywishlist/json', mywishlist_json, name='mywishlist_json'),
    path('add_to_wishlist_flutter/', add_to_wishlist_flutter, name= 'add_to_wishlist_flutter'),
]