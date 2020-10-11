from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *

# Create your views here.
def index(request):
    return render(request, "indian_recipes/index.html", {
        "recipes": Recipe.objects.all()
    })

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, "indian_recipes/recipe.html", {
        "recipe": recipe,
        "ingredients": recipe.ingredients.all(),
        "non_ingredients": Ingredient.objects.exclude(recipes=recipe).all(),
        "directions": recipe.directions.all(),
        "non-directions": Direction.objects.exclude(recipes=recipe).all()
    })

def add_recipe(request, recipe_id):
    pass

def add_ingredients(request, recipe_id):
    if request.method=="POST":
        recipe = Recipe.objects.get(pk=recipe_id)
        ingredient = Ingredient.objects.get(pk=int(request.POST["ingredient"]))
        recipe.ingredients.add(ingredient)
        return HttpResponseRedirect(reverse("recipe", args=(recipe.id,)))

def edit(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, "indian_recipes/edit.html" , {
        "recipe": recipe,
    })
