# therecipes/api/urls.py

from django.urls import path
from .views import RecipeListApiView, RecipeDetailApiView


urlpatterns = [
    path('recipes', RecipeListApiView.as_view()),
    path('recipes/<slug:slug>', RecipeDetailApiView.as_view()),
]
