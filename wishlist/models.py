from django.db import models
from django.contrib.auth.models import User

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('registerbook.Book', on_delete=models.CASCADE)  # Gantikan 'main_app' dengan nama aplikasi Anda
    preference = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.user.username}'s Wishlist - {self.book.title}"
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating = models.IntegerField()
    voters = models.IntegerField()
    price = models.IntegerField()
    currency = models.CharField(max_length=20)
    decscription = models.TextField()
    publisher = models.CharField(max_length=300)
    page_count = models.IntegerField()

    def __str__(self):
        return self.title