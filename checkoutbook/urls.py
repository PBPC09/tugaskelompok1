from django.urls import path
from checkoutbook.views import *

app_name = 'checkoutbook'

urlpatterns = [
    path('', show_checkout, name='checkout'),
    path('checkout_ajax/', checkout_ajax, name='checkout_ajax'),
    path('myorder/', show_myorder, name="myorder"),
    path('get_order_json/', get_order_json, name="get_order_json"),
    path('get_order_json_cc/', get_order_json_cc, name="get_order_json_cc"),
    path('get_order_json_dc/', get_order_json_dc, name="get_order_json_dc"),
    path('get_order_json_tf/', get_order_json_tf, name="get_order_json_tf"),
    path('get_order_json_ew/', get_order_json_ew, name="get_order_json_ew"),
]