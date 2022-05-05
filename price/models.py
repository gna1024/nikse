from django.db import models

# Create your models here.

class Price(models.Model):
    t = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    price = models.FloatField()
    recipe = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    quote = models.CharField(max_length=1000)
    img = models.ImageField()