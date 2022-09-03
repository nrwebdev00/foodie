from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import ( Recipe,
                      Recipe_Comments,
                      Recipe_Directions,
                      Recipe_Ingredients,
                      Recipe_Video,
                      Recipe_Images
                  )

# RecipeForm
class RecipeForm(ModelForm):

  class Meta:
    model = Recipe
    fields = ['title', 'title_long', 'description',
              'featured_image', 'alt_image','courses_tag',
              'cuisine_tag', 'ingredients_tag', 'holiday_tag']
    widgets = {
      'courses_tag': forms.CheckboxSelectMultiple(),
      'cuisine_tag': forms.CheckboxSelectMultiple(),
      'ingredients_tag': forms.CheckboxSelectMultiple(),
      'holiday_tag': forms.CheckboxSelectMultiple(),
    }

  def __init__(self, *args, **kwargs):
    super(RecipeForm, self).__init__(*args, **kwargs)

    for name, field in self.fields.items():
      field.widget.attrs.update({'class':'recipe-input input'})


# RecipeCommentForm
class RecipeCommentForm(ModelForm):

  class Meta:
    model = Recipe_Comments
    fields = ['comment']
    labels = {
      'comment': 'Leave Your Comment'
    }

    def __init__(self, *args, **kwargs):
      super(RecipeCommentForm, self).__init__(*args, **kwargs)

      for name, field in self.fields.items():
        field.widget.attrs.update({'class':'recipe-input input'})


# RecipeDirectionsForm
class RecipeDirectionsForm(ModelForm):

  class Meta:
    model = Recipe_Directions
    fields = ['direction_number', 'direction_short',
              'direction_long', 'time_mins']
    labels = {
      'direction_number': 'Order of Direction Number',
      'direction_short': 'Short Direction',
      'direction_long': 'Detailed Direction',
      'time_mins': 'Time To Complete in Minutes'
    }

  def __init__(self, *args, **kwargs):
    super(RecipeDirectionsForm, self).__init__(*args, **kwargs)

    for name, field in self.fields.items():
      field.widget.attrs.update({'class':'recipe-input input'})


# RecipeIngredientsForm
class RecipeIngredientsForm(ModelForm):

  class Meta:
    model = Recipe_Ingredients
    fields = ['ingredient_name', 'measurement_unit', 'measurement_number']
    labels = {
      'ingredient_name':'Ingredient',
      'measurement_unit':'Measurement Type',
      'measurement_number': 'Measurement'
    }

  def __init__(self, *args, **kwargs):
    super(RecipeIngredientsForm, self).__init__(*args, **kwargs)

    for name, field in self.fields.items():
      field.widget.attrs.update({'class':'recipe-input input'})


# RecipeVideoForm
class RecipeVideoForm(ModelForm):

  class Meta:
    model = Recipe_Video
    fields = ['caption', 'video', 'alt']
    labels = {
      'alt' : 'Alt Tag'
    }

  def __init__(self, *args, **kwargs):
    super(RecipeVideoForm, self).__init__(*args, **kwargs)

    for name, field in self.fields.items():
      field.widget.attrs.update({'class':'recipe-input input'})


# RecipeImageForm
class RecipeImageForm(ModelForm):

  class Meta:
    model = Recipe_Images
    fields = ['caption', 'image', 'alt']
    labels = {
      'alt' : 'Alt Tag'
    }

  def __init__(self, *args, **kwargs):
    super(RecipeImageForm, self).__init__(*args, **kwargs)

    for name, field in self.fields.items():
      field.widget.attrs.update({'class':'recipe-input input'})
