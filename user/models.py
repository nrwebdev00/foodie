from pickle import TRUE
from re import T
from tkinter import N
from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE,
                              blank=True, null=True)
  name = models.CharField(max_length=255, blank=True, null=True)
  email = models.EmailField(max_length=500, blank=True, null=True)
  location = models.CharField(max_length=255, blank=True, null=True)
  bio = models.TextField(blank=True, null=True)
  profile_image = models.ImageField( null=True, blank=True,
          upload_to='profiles/', default="profiles/user-default.png")
  facebook_url = models.CharField(max_length=500, null=True, blank=True)
  twitter_url = models.CharField(max_length=500, null=True, blank=True)
  instagram_url = models.CharField(max_length=500, null=True, blank=True)
  youtube_url = models.CharField(max_length=500, blank=True, null=True)
  linkedin_url = models.CharField(max_length=500, null=True, blank=True)
  website_url = models.CharField(max_length=500, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

  def __str__(self):
    return self.name

  @property
  def imageURL(self):
    try:
      url = self.profile_image.url
    except:
      url = ''
    return url

  class Meta:
    ordering = ['created_at']
