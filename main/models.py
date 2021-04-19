from django.db import models
from django.utils import timezone


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class Books(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    year = models.DateField(default=timezone.now)
    date = models.DateTimeField(default=timezone.now)

    def _str_(self):
         return self.title
    
    