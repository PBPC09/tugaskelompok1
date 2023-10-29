from django.urls import path
from wishlist.views import show_book_profile, show_book_details, add_to_wishlist, mywishlist, delete_wishlist_item

app_name = 'wishlist'

urlpatterns = [
    path('', mywishlist, name='mywishlist'),    
    path('bookprofile/', show_book_profile, name='bookprofile'),
    path('book/<int:book_id>/', show_book_details, name='show_book_details'),
    path('add_to_wishlist/', add_to_wishlist, name='add_to_wishlist'),
    path('delete_wishlist_item/<int:item_id>/', delete_wishlist_item, name='delete_wishlist_item'),
    # path('get-books/', get_books, name='get_books'),
]