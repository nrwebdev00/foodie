from django.shortcuts import render
from .models import Recipe


def recipes(request):
    recipes = Recipe.objects.all()
    # courses_tags = Recipe.objects.filter(courses_tag__name="Lunch")

    context = {'recipes': recipes, }

    return render(request, 'recipe/recipe.html', context)