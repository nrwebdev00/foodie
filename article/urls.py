from django.urls import path
from . import views

urlpatterns=[
  path('', views.articles, name='articles'),

  path('single/<str:id>/', views.single_article, name='article-single'),


  path('create-article/', views.create_article, name='create-article'),
  path('create-article-image/', views.create_article_image, name='create-article-image'),
  path('create-article-comment/', views.create_article_comment, name='create-article-comment'),

  path('update-article/<str:id>/', views.update_article, name='update-article'),
  path('update-article-image/<str:id>/', views.update_article_image, name='update_article_image'),
  path('update-article-comment/<str:id>/', views.update_article_comment, name='update_article_comment'),

  path('delete-article/<str:id>/', views.delete_article, name='delete-article'),
  path('delete-article-image/<str:id>/', views.delete_article_image, name='delete-article-image'),
  path('delete-article-comment/<str:id>/', views.delete_article_comment, name='delete-article0comment'),
]