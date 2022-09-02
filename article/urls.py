from django.urls import path
from . import views

urlpatterns=[
  path('', views.articles, name='articles'),

  path('single/<str:id>/', views.single_article, name='article-single'),


  path('create-article/', views.create_article, name='create-article'),
  path('update-article/<str:id>/', views.update_article, name='update-article'),
]