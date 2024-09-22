from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.conf import settings
import uuid

class Token(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True, default=uuid.uuid4().hex)


class CustomUser(AbstractUser):
    ADMINISTRATOR = 'administrator'
    USER = 'user'
    CHEF = 'chef'

    ROLE_CHOICES = [
        (ADMINISTRATOR, 'Administrator'),
        (USER, 'User'),
        (CHEF, 'Chef'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class ChefProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    culinary_background = models.TextField(max_length=500)
    specialty = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.username} - Chef Profile"


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(models.Model):
    description = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return self.description


class FoodRate(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f"{self.food.description} - {self.rate}/5"



