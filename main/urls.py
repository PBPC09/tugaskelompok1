from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_landing_page, name='show_landing_page'),
    path('login/', login_user, name='login'),
    path('signup/', signup, name='signup'),
]