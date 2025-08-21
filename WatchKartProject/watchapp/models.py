
from django.db import models

class WatchApp(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=[('Male', 'Male'), ('Female', 'Female'), ('unisex', 'Unisex')])
    category = models.CharField(max_length=50, choices=[("Analog", "Analog"),("Digital", "Digital"),("Smartwatch", "Smartwatch"),("Hybrid", "Hybrid"),])
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
