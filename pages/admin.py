from django.contrib import admin
from .models import ( Quick_Idea,
                      Featured_Recipe,
                      Index_Main_Section,
                      Index_Main_Section_Item
                    )

admin.site.register(Quick_Idea)
admin.site.register(Featured_Recipe)
admin.site.register(Index_Main_Section)
admin.site.register(Index_Main_Section_Item)
