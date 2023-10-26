from django.urls import path
from main.views import show_landing_page, signup

app_name = 'main'

urlpatterns = [
    path('', show_landing_page, name='show_landing_page'),
    path('signup/', signup, name='signup'),
]