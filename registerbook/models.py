from django.db import models
from main.models import Profile
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    voters = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=20)
    description = models.TextField()
    publisher = models.CharField(max_length=300)
    page_count = models.IntegerField()
    genres = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orders')
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='purchased')
    #seller = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sold')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - Book {self.book.title} - Buyer {self.buyer.user.username}"