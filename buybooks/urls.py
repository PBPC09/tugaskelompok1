from django.urls import path
from .views import *
app_name = 'buybooks'

urlpatterns = [    
    path('', show_test, name="show_test"),

]