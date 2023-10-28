from django.urls import path
from bookforum.views import *

app_name = 'bookforum'

urlpatterns = [
    path('', show_forum, name='show_forum' ),
    path('create_question/', create_question, name='create_question'),
    path('create_comments/<int:pk>', create_comments, name="create_comments"),
    path('delete_question/<str:username>/<int:id>', delete_question, name="delete_question"),
    path('delete_comments/<str:username>/<int:id>', delete_comments, name="delete_comments"),
    path('uniquecomments/json/<int:id>', show_uniquecomments_json, name="show_uniquecomments_json"),
    path('show_books_json/json/', show_books_json, name="show_books_json"),
    path('forum/json2/', show_forum_json_2, name="show_forum_json_2"),
    path('show_forumcomments/<int:id_head>/', show_forumcomments, name="show_forumcomments"),
    path('forum/json/', show_forum_json, name="show_forum_json"),
    path('comments/json/', show_comments_json, name="show_comments_json"),
    path('show_forum_json_popular_only', show_forum_json_popular_only, name="show_forum_popular_only")
]