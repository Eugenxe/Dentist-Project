from django.db import models

# Create your models here.

class Dentist(models.Model):
    First_name = models.CharField(max_length=50)
    Second_name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    id_number = models.IntegerField(max_length=12, unique=True)
    license_number = models.IntegerField(unique=True)

class Medical_facility(models.Model):
    name = models.CharField(max_length=50)
    license_number = models.CharField(max_length=100, unique=True)
