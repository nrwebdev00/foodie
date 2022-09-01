from tkinter import CASCADE
from django.db import models
import uuid
from user.models import Profile


class Recipe(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    title_long = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(upload_to='recipe/', default='recipe/dinner-02.jpg')
    courses_tag = models.ManyToManyField('Courses_Tag', blank=True)
    cuisine_tag = models.ManyToManyField('Cuisine_Tag', blank=True)
    ingredients_tag = models.ManyToManyField('Ingredients_Tag', blank=True)
    holiday_tag = models.ManyToManyField('Holiday_Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url


class Recipe_Likes(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)



class Recipe_Comments(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.comment


class Comment_Like(models.Model):
    comment = models.ForeignKey(Recipe_Comments, on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)



class Recipe_Directions(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    direction_number = models.IntegerField()
    direction_short = models.CharField(max_length=200)
    direction_long = models.TextField(null=True, blank=True)
    time_mins = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.direction_short

class Recipe_Ingredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=500)
    measurement_unit = models.CharField(max_length=50)
    measurement_number = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.ingredient_name


class Recipe_Video(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.TextField(null=True, blank=True)
    video = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.caption

    @property
    def videoURL(self):
        try:
            url = self.video.url
        except:
            url = ''
        return url

class Recipe_Images(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    caption = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='recipe/')
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.caption

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Courses_Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Cuisine_Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Ingredients_Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Holiday_Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name