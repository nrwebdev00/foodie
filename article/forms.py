from dataclasses import fields
from django.forms import ModelForm
from .models import Article, Article_Image, Article_Comment

class ArticleForm(ModelForm):

  class Meta:
    model = Article
    fields = '__all__'


class ArticleImageForm(ModelForm):

  class Meta:
    model = Article_Image
    fields = '__all__'


class ArticleCommentForm(ModelForm):

  class Meta:
    model = Article_Comment
    fields = '__all__'
