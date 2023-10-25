from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating = models.IntegerField()
    voters = models.IntegerField()
    price = models.IntegerField()
    currency = models.TextField()
    decscription = models.CharField(max_length=500)
    publisher = models.CharField(max_length=300)
    page_count = models.IntegerField()
    
    def __str__(self):
        return self.title