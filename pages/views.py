from django.shortcuts import render
from pages.helpers import bread_crumbs
from recipe.models import (Courses_Tag,
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
  articles = Article.objects.all().order_by('created_at')

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

# Quick Idea Views
def quick_ideas(request, idea):
  title = 'Quick Idea ' + idea

  context = {'title':title}

  return render(request, 'pages/quick_idea.html', context)