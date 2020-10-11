from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    return render(request, "indian_recipes/index.html", {
        "recipes": Recipe.objects.all()
    })

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, "indian_recipes/recipe.html", {
        "recipe": recipe
    })
