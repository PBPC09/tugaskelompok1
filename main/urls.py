from django.urls import path
from main.views import signup

app_name = 'main'

urlpatterns = [
    path('signup/', signup, name='signup'),
]