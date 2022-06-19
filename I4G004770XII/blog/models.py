from tkinter import CASCADE
from typing_extensions import Self
from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField
    Author = models.ForeignKey(to=Self, on_delete=models.CASCADE)
    created_date = models.DateTimeField
    published_date = models.DateTimeField