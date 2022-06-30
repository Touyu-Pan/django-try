from pydoc import describe
from venv import create
from django.db import models

# Create your models here.

class Room(models.Model):
    #host = 
    #topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True) # auto_now takes a snapshot on every time we save
    created = models.DateTimeField(auto_now_add=True) # auto_now_add takes a time stamp when we first create this instance

    def __str__(self):
        return self.name