from django.db import models
from user.models import Profile
import uuid


class Featured_Recipe(models.Model):
  owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=255, default="Featured Recipe...")
  body = models.CharField(max_length=500, default="Featured Body text...")
  img = models.ImageField(upload_to='featured_recipe/')
  alt = models.CharField(max_length=255, default='Alt text')
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return self.title

  @property
  def imageURL(self):
    try:
      url = self.img.url
    except:
      url = ''
    return url


class Quick_Idea(models.Model):
  owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=1000, default='Quick Idea... Check it Out!')
  alt = models.CharField(max_length=50, default="Quick Idea Image")
  img = models.ImageField(upload_to='quick_ideas/')
  url_name = models.CharField(max_length=100, default='page-home')
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return self.title

  @property
  def imageURL(self):
    try:
      url = self.img.url
    except:
      url = ''
    return url


class Index_Main_Section(models.Model):
  owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=1000, default='Main Section Title')
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return self.title

class Index_Main_Section_Item(models.Model):
  owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
  index_main_section = models.ForeignKey(Index_Main_Section, on_delete=models.CASCADE)
  url_name = models.CharField(max_length=200, default='home-page')
  img = models.ImageField(upload_to='index_main_section/')
  alt = models.CharField(max_length=200, default='Main Section Image')
  title = models.CharField(max_length=1000, default='Main Section Title')
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return self.title

  @property
  def imageURL(self):
    try:
      url = self.img.url
    except:
      url = ''
    return url