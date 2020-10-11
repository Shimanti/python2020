from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:recipe_id>", views.recipe, name="recipe"),
    path("<int:recipe_id>/add_recipe", views.add_recipe, name="add_recipe"),
    path("<int:recipe_id>/add_ingredients", views.add_ingredients, name="add_ingredients"),
    path("<int:recipe_id>/edit", views.edit, name="edit"),
]
