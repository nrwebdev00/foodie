import re
from django.shortcuts import render,redirect
from .models import (Article,
                     Article_Comment,
                     Article_Image,
                     Article_Like
                    )
from .forms import ArticleForm, ArticleImageForm
from user.models import Profile
from recipe.models import (Recipe)

def articles(request):

  context = {}

  return render(request, 'article/article.html', context)


def single_article(request, id):
  # Article Calls - GET
  article = Article.objects.get(pk=id)
  article_images = Article_Image.objects.filter(article__id=id)
  article_comment = Article_Comment.objects.filter(article__id=id)
  article_likes = Article_Like.objects.filter(article__id=id)
  number_article_likes = len(article_likes)

  # User Info - GET
  owner = Profile.objects.get(id=article.owner.id)

  # Tags - GET
  courses_tags = article.courses_tags.all()
  cuisine_tag = article.cuisine_tags.all()
  ingredient_tag = article.ingredients_tag.all()
  holiday_tag = article.holiday_tag.all()

  # Retrieve single Recipe based on tag - GET
  courses = article.courses_tags.first()
  courses_recipe = Recipe.objects.filter(courses_tag__name=courses)[:1]

  cuisine = article.cuisine_tags.first()
  cuisine_recipe = Recipe.objects.filter(cuisine_tag__name=cuisine)[:1]

  ingredient = article.ingredients_tag.first()
  ingredient_recipe = Recipe.objects.filter(ingredients_tag__name=ingredient)[:1]

  holiday = article.holiday_tag.first()
  holiday_recipe = Recipe.objects.filter(holiday_tag__name=holiday)[:1]

  context = { 'id': id,
              'article': article,
              'article_images': article_images,
              'article_comment':article_comment,
              'article_likes':number_article_likes,
              'owner': owner,
              'courses_tags':courses_tags,
              'cuisine_tags': cuisine_tag,
              'ingredient_tags': ingredient_tag,
              'holiday_tags':holiday_tag,
              'courses_recipe': courses_recipe,
              'cuisine_recipe':cuisine_recipe,
              'ingredient_recipe':ingredient_recipe,
              'holiday_recipe':holiday_recipe,
            }

  return render(request, 'article/article-single.html', context)


def create_article(request):
  form = ArticleForm()
  form_image = ArticleImageForm()

  if request.method == 'POST':
    form = ArticleForm(request.POST)
    form_image = ArticleImageForm(request.POST)
    if form.is_valid() and form_image.is_valid():
      form.save()
      form_image.save()
      return redirect('home')

  context = {'form': form, 'form_image': form_image}

  return render(request, 'article/article_form.html', context)


def update_article(request, id):
  article = Article.objects.get(id=id)
  form = ArticleForm(instance=article)

  if request.method == 'POST':
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
      form.save()
      return redirect('home')

  context = {'form': form}

  return render(request, 'article/article_form.html', context)


# Delete Article View