from django.urls import path
<<<<<<< HEAD
from main.views import show_landing_page, signup
=======
from main.views import signup
>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13

app_name = 'main'

urlpatterns = [
<<<<<<< HEAD
    path('', show_landing_page, name='show_landing_page'),
=======
>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13
    path('signup/', signup, name='signup'),
]