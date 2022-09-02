from django.shortcuts import render
from pages.helpers import bread_crumbs
from recipe.models import (Courses_Tag,
                           Cuisine_Tag, Holiday_Tag, Ingredients_Tag,
                           Recipe, )
from article.models import Article
from .models import (Quick_Idea,
                     Featured_Recipe,
                     Index_Main_Section,
                     Index_Main_Section_Item,
                    )


# Home Page Views
def home_page(request):
  title = 'Welcome to Foodie'
  quick_ideas = Quick_Idea.objects.all()[:4]
  featured_recipe = Featured_Recipe.objects.all().order_by('created_at')[:1]
  index_main_section = Index_Main_Section.objects.all().order_by('created_at')[:1]
  index_main_section_items = Index_Main_Section_Item.objects.all().order_by('created_at')[:4]

  context = {'title':title,
             'quick_idea': quick_ideas,
             'featured_recipe': featured_recipe,
             'index_main_section': index_main_section,
             'index_main_section_items': index_main_section_items
            }

  return render(request, 'pages/index.html', context)


# Course and Courses Views
def courses_page(request):
  title = 'Courses'
  bread_crumbs = ('Home', 'Courses')
  courses_tags = Courses_Tag.objects.all().order_by('name')
  articles = Article.objects.all().order_by('-created_at')

  context = {
        'title':title,
        'crumbs': bread_crumbs,
        'courses': courses_tags,
        'articles': articles,
      }

  return render(request, 'pages/courses.html', context)

def course_page(request, course):
  title = 'Course ' + course
  bread_crumbs = ('Home', 'Courses', course.capitalize() )
  courses_tags = Courses_Tag.objects.all().order_by('name')
  recipes = Recipe.objects.filter(courses_tag__name=course)


  context = {
    'course': course,
    'title': title,
    'crumbs': bread_crumbs,
    'courses': courses_tags,
    'recipes':recipes
    }

  return render(request, 'pages/course.html', context)

# Cuisines and Cuisine View

def cuisine_page(request, cuisine):
  title = 'Cuisine ' + cuisine
  bread_crumbs = ('Home', 'Cuisine', cuisine.capitalize())
  cuisine_tags = Cuisine_Tag.objects.all().order_by('name')
  recipes = Recipe.objects.filter(cuisine_tag__name=cuisine)

  context = {
    'cuisine': cuisine,
    'title': title,
    'crumbs': bread_crumbs,
    'cuisines': cuisine_tags,
    'recipes': recipes,
    }

  return render(request, 'pages/cuisine.html', context)


def cuisines_page(request):
  title = 'Cuisine'
  bread_crumbs = ('Home', 'Cuisines')
  cuisine_tags = Cuisine_Tag.objects.all().order_by('name')
  articles = Article.objects.all().order_by('-created_at')

  context = {
    'title': title,
    'crumbs': bread_crumbs,
    'cuisines': cuisine_tags,
    'articles': articles,
    }

  return render(request, 'pages/cuisines.html', context)

# ingredients and single ingredient view
def ingredients_page(request):
  title = 'Ingredients'
  bread_crumbs = ('Home', 'Ingredients')
  ingredient_tags = Ingredients_Tag.objects.all().order_by('name')
  articles = Article.objects.all().order_by('-created_at')

  context = {
    'title':  title,
    'crumbs': bread_crumbs,
    'ingredients': ingredient_tags,
    'articles': articles,
  }

  return render(request, 'pages/ingredients.html', context)


def ingredient_page(request, ingredient):
  title = 'Ingredients ' + ingredient
  bread_crumbs = ('Home', 'Ingredients', ingredient.capitalize())
  ingredient_tag = Ingredients_Tag.objects.all().order_by('name')
  recipes = Recipe.objects.filter(ingredients_tag__name=ingredient)

  context = {
    'ingredient': ingredient,
    'title': title,
    'crumbs': bread_crumbs,
    'ingredients': ingredient_tag,
    'recipes': recipes,
  }

  return render(request, 'pages/ingredient.html', context)

# Holiday_Articles and Holiday_Recipes views
def holiday_articles(request):
  title = 'Holidays'
  bread_crumbs = ('Home', 'Holidays')
  holiday_tag = Holiday_Tag.objects.all().order_by('name')
  articles = Article.objects.all().order_by('-created_at')

  context = {
    'title': title,
    'crumbs': bread_crumbs,
    'holidays': holiday_tag,
    'articles': articles,
  }

  return render(request, 'pages/holiday_articles.html', context)


def holiday_recipes(request, holiday):
  title = "Holiday " + holiday
  bread_crumbs = ('Home', 'Holidays', holiday.capitalize())
  holiday_tag = Holiday_Tag.objects.all().order_by('name')
  recipes = Recipe.objects.filter(holiday_tag__name=holiday)

  context = {
    'holiday': holiday,
    'title': title,
    'crumbs': bread_crumbs,
    'holidays': holiday_tag,
    'recipes':recipes,
  }

  return render(request, 'pages/holiday_recipes.html', context)


# Baking_Articles and Baking_recipes views
def baking_articles(request):
  title = 'Baking'
  bread_crumbs = ('Home', 'Baking')
  baking_articles = Article.objects.filter(cuisine_tags__name='Baking').order_by('-created_at')

  context = {
    'title':title,
    'crumbs':bread_crumbs,
    'articles': baking_articles,
  }

  return render(request, 'pages/baking_articles.html', context)


# Quick Idea Views
def quick_ideas(request, idea):
  title = 'Quick Idea ' + idea

  context = {'title':title}

  return render(request, 'pages/quick_idea.html', context)