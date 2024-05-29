from django.db import models

# Create your models here.

class Student(models.Model) :
    name = models.CharField(max_length=200)
    email =models.EmailField(max_length=254)
    course = models.CharField(max_length=200)
    fees = models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)