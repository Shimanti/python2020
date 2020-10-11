from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    amount = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.amount} {self.name}"

class Direction(models.Model):
    step = models.TextField()

    def __str__(self):
        return f"{self.step}"

class Category(models.Model):
    subject = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.subject}"

class Recipe(models.Model):
    title = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipes")
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    directions = models.ManyToManyField(Direction, blank=True)

    def __str__(self):
        return f"{self.title}"
