from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField
    Author = models.ForeignKey(get_user_model())
    created_date = models.DateTimeField
    published_date = models.DateTimeField
    def __str__(self) -> str:
        return self.Title