from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    bio = models.TextField(max_length=250, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)