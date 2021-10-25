from django.contrib import admin

from .models import (
    Author, 
    Cookbook,
    Recipe,
    Ingredient,
    Category,
    IngredientName,
    IngredientQty,
    IngredientUnit,
)


# register models to use in admin site
admin.site.register(Author)
admin.site.register(Cookbook)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Category)


@admin.register(
    IngredientName,
    IngredientQty,
    IngredientUnit,
)
class HideModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request): 
        return {}
