from django.db import models


class Recipe(models.Model):
    """Table schema to store recipes."""
    cookbook = models.ForeignKey('recipeplanner.Cookbook', on_delete=models.CASCADE)
    recipe_title = models.CharField(max_length=64)
    ingredients = models.TextField()
    method = models.TextField()
    slug = models.CharField(default='', max_length=64)

    def __str__(self):
        return '%s' % self.recipe_title


class Cookbook(models.Model):
    """Table schema to store cookbooks."""
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    slug = models.CharField(default='', max_length=64)

    def __str__(self):
        return '%s' % self.title
