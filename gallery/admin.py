from django.contrib import admin
from .models import Picture
from sorl.thumbnail.admin import AdminImageMixin




# admin.site.register(Picture)

@admin.register(Picture)
class PictureAdmin(AdminImageMixin ,admin.ModelAdmin):
    list_display = ('title', 'created_date', 'picture')
#     ordering = ('-created_date')
