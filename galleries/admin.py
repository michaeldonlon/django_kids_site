# galleries/admin.py

from django.contrib import admin

from .models import ImageGallery, KidImage


class KidImageInline(admin.TabularInline):
    model = KidImage


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    inlines = [
        KidImageInline
    ]
