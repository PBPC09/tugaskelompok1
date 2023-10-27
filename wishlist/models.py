from django.db import models
from django.contrib.auth.models import User
from registerbook.models import Book

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Gantikan 'main_app' dengan nama aplikasi Anda
    preference = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.user.username}'s Wishlist - {self.book.title}"