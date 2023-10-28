from django.db import models
from django.contrib.auth.models import User
from buybooks.models import CartItem

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    alamat = models.TextField()
    metode_pembayaran = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username}'s checkout"