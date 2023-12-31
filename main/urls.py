from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_landing_page, name='show_landing_page'),
    path('landing-page/', show_landing_page_logged_in, name='show_landing_page_logged_in'),
    path('login/', login_user, name='login'),
    path('signup/', signup, name='signup'),
    path('landingpageafterlogin/', show_landing_page_logged_in, name='show_landing_page_logged_in'),
    path('logout/', logout_user, name='logout'),
    path('get-user/', get_user_json, name='get_user_json'),
]