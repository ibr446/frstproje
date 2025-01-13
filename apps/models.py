from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    ...



class service(models.Model):
    full_name = models.CharField(max_length=225)
    decrypt = models.CharField(max_length=225)
    price = models.CharField(max_length=225)
    image = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.full_name




class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name


