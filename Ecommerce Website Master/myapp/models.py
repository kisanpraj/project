from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name + " | " + self.subject


class Buyer(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.BigIntegerField()
    address = models.TextField()
    password = models.CharField(max_length=200)


    def __str__(self) -> str:
        return self.fname + " | " + self.email
