from django.contrib import admin
from .models import Book
from registerbook.models import Book

# Register your models here.
admin.site.register(Book)