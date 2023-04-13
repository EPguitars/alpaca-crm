""" Models of user data"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class Record(models.Model):
    """ Record of a user in database"""
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")


class User(AbstractUser):

    email = models.EmailField(unique=True)