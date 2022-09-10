from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings





class Task(models.Model):
    title = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default=None, on_delete=models.CASCADE)
    

    
    def __str__(self):
        return self.title

class City(models.Model):
    city = models.CharField(max_length=30)
    user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.city



