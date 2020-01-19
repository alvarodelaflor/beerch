from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    food_types = models.CharField(max_length=100)
    special_diets = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.nombre)