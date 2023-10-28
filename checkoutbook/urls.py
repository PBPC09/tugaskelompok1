from django.urls import path
from checkoutbook.views import *

app_name = 'checkoutbook'

urlpatterns = [
    path('', show_checkout, name='checkout'),
    path('checkout_ajax/', checkout_ajax, name='checkout_ajax'),
]