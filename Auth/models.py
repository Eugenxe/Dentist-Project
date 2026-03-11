from django.db import models

class Registration(models.Model):
    First_name = models.CharField(max_length=50)
    Second_name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)



class login(models.Model):
    Username = models.CharField
    Password = models.CharField
