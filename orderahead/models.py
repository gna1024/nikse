from django.db import models

# Create your models here.

class Order(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=64)
    price = models.FloatField()

class Cart(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=64)
    price = models.FloatField()