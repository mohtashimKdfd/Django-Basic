#database
from functools import update_wrapper
from django.db import models

# Create your models here.

class objectss(models.Model):
    # host = 
    # topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True) # it means that this is not neccesary
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name