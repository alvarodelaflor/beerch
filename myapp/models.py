from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    food_types = models.CharField(max_length=100)
    special_diets = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.nombre)

class User(models.Model):
    photo = models.URLField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTv_p3auZIO-jK7XWsgmAOwOLrSL7GcJ4JT1CQsdJl391lPu8vj&s')
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{0}".format(self.nombre)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    rate = models.IntegerField()
    visit_date = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

       
    def __str__(self):
        return "{0}".format(self.nombre)