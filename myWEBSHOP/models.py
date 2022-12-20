from django.db import models
from datetime import date

# Create your models here.
class Users(models.Model):
    userFirstName = models.CharField(max_length=200)
    userLastName = models.CharField(max_length=200)
    userPasswort = models.CharField(max_length=200)

class Producers(models.Model):
    producerName = models.CharField(max_length=200)

class Bikes(models.Model):
    bikeType = models.CharField(max_length=200)
    bikeDescription = models.CharField(max_length=500)
    #bikeProducerID = models.ForeignKey(Producers, on_delete=models.CASCADE)

class Rentalprocesses(models.Model):
    rentalprocessStartDate = models.DateField(default=date.today)
    rentalprocessEndDate = models.DateField()
    rentalprocessUserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    #rentalprocessBikeID = models.ForeignKey(Bikes, on_delete=models.CASCADE)

