from django.urls import path
from registerbook.views import (show_registered_books, show_received_orders,
                                show_json, show_json_by_id, get_book_json, 
                                add_book_ajax, remove_book, mark_notification_read,
                                remove_notification, get_notif_json,  create_book_flutter)

app_name = 'registerbook'

urlpatterns = [
    path('', show_registered_books, name='show_registered_books'),
    path('received-orders/', show_received_orders, name='show_received_orders'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('get-book/', get_book_json, name='get_book_json'),
    path('get-notif/', get_notif_json, name='get_notif_json'),
    path('add-book-ajax/', add_book_ajax, name='add_book_ajax'),
    path('delete-book-ajax/<int:book_id>/', remove_book, name='remove_book'),
    path('delete-notification/<int:notif_id>/', remove_notification, name='remove_notification'),
    path('mark-notification-read/<int:notif_id>/', mark_notification_read, name='mark_notification_read'),
    path('create-book-flutter/', create_book_flutter, name='create_book_flutter'),
]