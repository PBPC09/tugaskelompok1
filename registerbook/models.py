from django.db import models
from registerbook.models import Book

class Purchase(models.Model):
    amount = models.IntegerField()

    def __str__(self):
        return self.title