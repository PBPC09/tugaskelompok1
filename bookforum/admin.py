from django.contrib import admin
from .models import ForumHead, ForumComment

# Register your models here.
admin.site.register(ForumHead)
admin.site.register(ForumComment)