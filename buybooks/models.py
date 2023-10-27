from django.db import models
from registerbook.models import Book

class Purchase(models.Model):
    amount = models.IntegerField()
    author = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
