from django.db import models

# Create your models here.

class Review(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=64)
    review = models.FloatField(max_length=1000)
