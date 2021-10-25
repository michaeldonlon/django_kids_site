# therecipes/api/serializers.py

from rest_framework import serializers
from .models import Ingredient, Recipe


class IngredientSerializer(serializers.ModelSerializer):
    
    ingredient_qty = serializers.StringRelatedField(many=False)
    ingredient_unit = serializers.StringRelatedField(many=False)
    ingredient_name = serializers.StringRelatedField(many=False)

    class Meta:
        model = Ingredient
        fields = [
            'ingredient_qty',
            'ingredient_unit',
            'ingredient_name'
        ]


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

    ingredients = IngredientSerializer(many=True, read_only=True)

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
        depth = 1


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
