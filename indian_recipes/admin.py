from django.contrib import admin

from .models import Ingredient, Direction, Recipe

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Direction)
admin.site.register(Recipe)
