from django.contrib import admin
from .models import Picture


class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'image_tag',)


admin.site.register(Picture, PictureAdmin)
