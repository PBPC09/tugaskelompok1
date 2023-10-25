from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)


    def __str__(self):
        return self.title

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    preference = models.IntegerField()  # Seberapa suka Anda dengan buku ini, misalnya dari 1-5

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
