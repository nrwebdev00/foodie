from django.urls import path
from . import views


urlpatterns = [
  path('', views.home_page, name='home'),

  path('quick_idea/<slug:idea>/', views.quick_ideas, name='quick_idea'),

  path('courses/', views.courses_page, name='courses'),
  path('courses/<str:course>/', views.course_page, name='course'),

  path('cuisines/', views.cuisines_page, name='cuisines'),
  path('cuisines/<str:cuisine>', views.cuisine_page, name='cuisine'),

  path('baking/', views.baking_articles, name='baking'),

  path('ingredients/', views.ingredients_page, name='ingredients'),
  path('ingredients/<str:ingredient>', views.ingredient_page, name='ingredient'),

  path('holidays/', views.holiday_articles, name='holiday_articles'),
  path('holidays/<str:holiday>', views.holiday_recipes, name='holiday_recipe'),
]