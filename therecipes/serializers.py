# therecipes/api/serializers.py

from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    
    cookbook = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='book_title'
     )

    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='category_name'
     )

    class Meta:
        model = Recipe
        fields = [
            "cookbook", 
            "recipe_title", 
            "category", 
            "ingredients", 
            "method", 
            "slug"
        ]


class ShortRecipeSerializer(serializers.ModelSerializer):

    cookbook = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='book_title'
     )

    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='category_name'
     )

    class Meta:
        model = Recipe
        fields = [
            "recipe_title", 
            "cookbook", 
            "category", 
            "slug"
        ]
