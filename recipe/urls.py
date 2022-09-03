from django.urls import path
from . import views


urlpatterns=[
    path('', views.recipes, name="recipes"),

    path('create-recipe/', views.create_recipe, name='create-recipe'),
    path('create-recipe-comment/<str:id>/', views.create_recipe_comment, name='create-recipe-comment'),
    path('create-recipe-directions/<str:id>/', views.create_recipe_directions, name='create-recipe-directions'),
    path('create-recipe-ingredient/<str:id>/', views.create_recipe_ingredient, name='create-recipe-ingredient'),
    path('create-recipe-video/<str:id>/', views.create_recipe_video, name='create-recipe-video'),
    path('create-recipe-image/<str:id>/', views.create_recipe_image, name='create-recipe-image'),

    path('update-recipe/<str:id>/', views.update_recipe, name='update-recipe' ),
    path('update-recipe-comment/<str:id>/', views.update_recipe_comment, name='update-recipe-comment'),
    path('update-recipe-directions/<str:id>/', views.update_recipe_directions, name='update-recipe-direction'),
    path('update-recipe-ingredients/<str:id>/', views.update_recipe_ingredients, name='update-recipe-ingredients'),
    path('update-recipe-video/<str:id>/', views.update_recipe_video, name='update-recipe-video'),
    path('update-recipe-image/<str:id>/', views.update_recipe_image, name='update-recipe-image'),


    path('delete-recipe/<str:id>/', views.delete_recipe, name='delete-recipe'),
    path('delete-recipe-comment/<str:id>/', views.delete_recipe_comment, name='delete-recipe-comment'),
    path('delete-recipe-direction/<str:id>/', views.delete_recipe_direction, name='delete-recipe-direction'),
    path('delete-recipe-ingredient/<str:id>/', views.delete_recipe_ingredients, name='delete-recipe-ingredient'),
    path('delete-recipe-video/<str:id>/', views.delete_recipe_video, name='delete-recipe-video'),
    path('delete-recipe-image/<str:id>/', views.delete_recipe_image, name='delete-recipe-image'),

]