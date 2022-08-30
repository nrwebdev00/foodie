import uuid
from django.db import models
from recipe.models import (Courses_Tag,
                           Cuisine_Tag,
                           Ingredients_Tag,
                           Holiday_Tag,
                          )
from user.models import Profile


class Article(models.Model):
  owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
  title = models.CharField(max_length=1000)
  body = models.TextField()
  courses_tags = models.ManyToManyField(Courses_Tag, blank=True)
  cuisine_tags = models.ManyToManyField(Cuisine_Tag, blank=True)
  ingredients_tag = models.ManyToManyField(Ingredients_Tag, blank=True)
  holiday_tag = models.ManyToManyField(Holiday_Tag, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return self.title


class Article_Image(models.Model):
  owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  image = models.ImageField(upload_to="article/")
  caption = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
     return self.caption


class Article_Video(models.Model):
  owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  caption = models.TextField(blank=True, null=True)
  video = models.FileField(upload_to='videos/')
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return self.caption

class Article_Comment(models.Model):
  owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  comment = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return self.comment


class Article_Like(models.Model):
  owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)
