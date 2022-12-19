from django.db import models

# Create your models here.
class Users(models.Model):
    userFirstName = models.CharField(max_length=200)
    userLastName = models.CharField(max_length=200)
    userPasswort = models.CharField(max_length=200)
