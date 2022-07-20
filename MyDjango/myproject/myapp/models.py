import email
from pyexpat import model
from django.db import models

# Create your models here.

class Students(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50,null=True)
    subject = models.CharField(max_length=20)
    pnumber = models.CharField(max_length=15,unique=True)

    def __str__(self) -> str:
        return self.firstname
