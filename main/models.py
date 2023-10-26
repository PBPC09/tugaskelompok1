from django.db import models
from django.contrib.auth.models import User

# Create your models here.

<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

=======
>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13
class Profile(models.Model):
    ROLE_CHOICES = [('S', 'Seller'), ('B', 'Buyer')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default='B')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)

    def is_seller(self):
        return self.role == 'S'

    def is_buyer(self):
        return self.role == 'B'

    def __str__(self):
<<<<<<< HEAD
        return self.user.username
=======
        return self.user.username
>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13
