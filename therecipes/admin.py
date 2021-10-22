from django.contrib import admin

from .models import Author, Category, Cookbook, Recipe  

# register models to use in admin site
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Cookbook)
admin.site.register(Recipe)
