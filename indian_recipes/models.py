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

class Recipe(models.Model):
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.title}"
