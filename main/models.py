from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    ROLE_CHOICES = [('A', 'Admin'), ('B', 'Buyer')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default='B')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)

    def is_admin(self):
        return self.role == 'A'

    def is_buyer(self):
        return self.role == 'B'

    def __str__(self):
        return self.user.username