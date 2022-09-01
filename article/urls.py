from django.urls import path
from . import views

urlpatterns=[
  path('', views.articles, name='articles'),

  path('single/<str:id>/', views.single_article, name='article-single'),
]