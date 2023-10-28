from django.db import models
from registerbook.models import Book
from django.contrib.auth.models import User

class Buybooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buybooks_book')  
    book = models.ForeignKey(Book, on_delete=models.CASCADE) 
    amount = models.IntegerField() 
    quantity = models.PositiveIntegerField(default=1)  
    is_ordered = models.BooleanField(default=False)

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_ordered = models.BooleanField(default=False)

def __str__(self):
    return f"{self.user.username}'s Cart - {self.book.title}"

def subtotal(self):
    return self.book.price * self.quantity