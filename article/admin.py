from django.contrib import admin
from .models import (Article,
                     Article_Comment,
                     Article_Image,
                     Article_Like,
                     Article_Video,
                    )

admin.site.register(Article)
admin.site.register(Article_Comment)
admin.site.register(Article_Image)
admin.site.register(Article_Like)
admin.site.register(Article_Video)
