from django.urls import path
from wishlist.views import show_book_profile, show_book_details, add_to_wishlist, my_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', show_book_profile, name='bookprofile'),
    path('book/<int:book_id>/', show_book_details, name='show_book_details'),
    #  path('addtowishlist/<int:book_id>/', addtowishlist, name='add_to_wishlist'),
    path('add_to_wishlist/', add_to_wishlist, name='add_to_wishlist'),
    path('my_wishlist/', my_wishlist, name='my_wishlist'),

]