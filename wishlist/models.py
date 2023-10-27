from django.db import models
from django.contrib.auth.models import User
from registerbook.models import Book

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    PREFERENCE_CHOICES = [
        (1, 'Not Interested'),
        (2, 'Maybe Later'),
        (3, 'Interested'),
        (4, 'Really Want It'),
        (5, 'Must Have')
    ]
    preference = models.IntegerField(choices=PREFERENCE_CHOICES)

    def __str__(self):
        return f"{self.user.username}'s Wishlist - {self.book.title}"