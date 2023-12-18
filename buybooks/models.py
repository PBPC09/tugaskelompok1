from django.db import models
from registerbook.models import Book
from django.contrib.auth.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_ordered = models.BooleanField(default=False)

    def subtotal(self):
        return self.book.price * self.quantity
    
    def __str__(self):
        return f"{self.user.username}'s Cart - {self.book.title}"