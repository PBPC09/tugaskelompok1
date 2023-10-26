from django.urls import path
from wishlist.views import bookprofile

app_name = 'wishlist'

urlpatterns = [
    # path('book/<int:book_id>/', views.book_profile, name='book_profile'),
    # path('wishlist/', views.wishlist_page, name='wishlist_page'),
    # path('add/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('bookprofile/', bookprofile, name='bookprofile'),

]