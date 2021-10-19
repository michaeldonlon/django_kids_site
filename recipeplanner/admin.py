from django.contrib import admin

from .models import Recipe, Cookbook 

# register models to use in admin site
admin.site.register(Recipe)
admin.site.register(Cookbook)
