from django.db import models

# Create your models here.
class Buybooks(models.Model):
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
    amount = models.IntegerField()

    def __str__(self):
        return self.title
