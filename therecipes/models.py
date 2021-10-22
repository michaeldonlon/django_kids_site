# therecipes/models.py

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Ingredient(models.Model):
    """Table schema to store ingredients."""
    ingredient_name = models.CharField(max_length=64)
    ingredient_qty = models.IntegerField()
    ingredient_unit = models.CharField(max_length=16)


class Recipe(models.Model):
    """Table schema to store recipes."""
    cookbook = models.ForeignKey('Cookbook', on_delete=models.CASCADE)
    recipe_title = models.CharField(max_length=64)
    category = models.ManyToManyField('Category', blank=True)
    ingredients = models.TextField()
    method = models.TextField()
    slug = models.SlugField(null=True, blank=True, unique=True)
    prepopulated_fields = {"slug": ("recipe_title",)}

    def __str__(self):
        return '%s' % self.recipe_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.recipe_title)
        return super().save(*args, **kwargs)


class Cookbook(models.Model):
    """Table schema to store cookbooks."""
    book_title = models.CharField(max_length=64)
    author = models.ManyToManyField('Author', blank=True, related_name='authors_book')
    cover = models.ImageField(upload_to='covers', blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    prepopulated_fields = {"slug": ("book_title",)}

    def __str__(self):
        return '%s' % self.book_title

    def get_absolute_url(self):
        return reverse('cookbook_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.book_title)
        return super().save(*args, **kwargs)


class Author(models.Model):
    """Table schema to store authors."""
    author_name = models.CharField(max_length=64)
    pen_pic = models.ImageField(upload_to='author_pics', blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    prepopulated_fields = {"slug": ("author_name",)}

    def __str__(self):
        return '%s' % self.author_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.author_name)
        return super().save(*args, **kwargs)


class Category(models.Model):
    """Table schema to store categories."""
    category_name = models.CharField(max_length=64)
    slug = models.SlugField(null=True, blank=True, unique=True)
    prepopulated_fields = {"slug": ("category_name",)}

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '%s' % self.category_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)
