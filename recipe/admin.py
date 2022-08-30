from django.contrib import admin
from .models import (Recipe,
                     Courses_Tag,
                     Cuisine_Tag,
                     Ingredients_Tag,
                     Holiday_Tag,
                     Recipe_Images,
                     Recipe_Comments,
                     Recipe_Directions,
                     Recipe_Ingredients,
                     Recipe_Likes,
                     Recipe_Video,
                    )

admin.site.register(Recipe)
admin.site.register(Courses_Tag)
admin.site.register(Cuisine_Tag)
admin.site.register(Ingredients_Tag)
admin.site.register(Holiday_Tag)
admin.site.register(Recipe_Images)
admin.site.register(Recipe_Comments)
admin.site.register(Recipe_Directions)
admin.site.register(Recipe_Ingredients)
admin.site.register(Recipe_Likes)
admin.site.register(Recipe_Video)