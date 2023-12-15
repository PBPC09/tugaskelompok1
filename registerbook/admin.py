from django.contrib import admin
from .models import Book
from registerbook.models import Book, Notification

# Register your models here.
admin.site.register(Book)
admin.site.register(Notification)