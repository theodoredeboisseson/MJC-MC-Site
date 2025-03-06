from django.contrib import admin
from wagtail.images.models import Image
from .forms import CustomImageForm

# Unregister the default Image admin and register your custom version
# admin.site.unregister(Image)
# 
# @admin.register(Image)
# class CustomImageAdmin(admin.ModelAdmin):
#     form = CustomImageForm