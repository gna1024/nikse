from django.db import models

# Create your models here.

class Review(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=64)
    review = models.CharField(max_length=1000)
