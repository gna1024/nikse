from django.db import models

# Create your models here.

class Aboutcoffee(models.Model):
    name1 = models.CharField(max_length=64)
    name2 = models.CharField(max_length=64)
    text1 = models.CharField(max_length=1000)
    text2 = models.CharField(max_length=1000)
    quote = models.CharField(max_length=1000)
    photo1 = models.ImageField()
    photo2 = models.ImageField()
