from django.db import models
from registerbook.models import Book
from django.contrib.auth.models import User
# Create your models here.
class ForumHead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(null=True)
    title = models.CharField(max_length=100)
    question = models.TextField()
    
class ForumComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment_to = models.ForeignKey(ForumHead, on_delete=models.CASCADE,)
    date = models.DateField(null=True)
    answer = models.TextField()