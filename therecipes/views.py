# therecipes/api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import Recipe
from .serializers import RecipeSerializer, ShortRecipeSerializer


class RecipeListApiView(generics.ListAPIView):

    serializer_class = ShortRecipeSerializer

    # if method is GET, list the recipes
    def get(self, request, *args, **kwargs):
        '''
        List all the Recipe items
        '''
        queryset = self.get_queryset()
        serializer = ShortRecipeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Recipe.objects.all()
        category = self.request.query_params.get('category')
        cookbook = self.request.query_params.get('cookbook')
        if category is not None:
            queryset = queryset.filter(category__category_name__contains=category)
        elif cookbook is not None:
            queryset = queryset.filter(cookbook__book_title__contains=cookbook)
        return queryset

    # if method is POST, create a new recipe
    def post(self, request, *args, **kwargs):
        '''
        Create a new Recipe object with given recipe data
        '''
        data = {
            'recipe_title': request.data.get('recipe_title'),
            'cookbook': request.data.get('cookbook'),
            'category': request.data.get('category'),
            'ingredients': request.data.get('ingredients'),
            'method': request.data.get('method'),
        }
        serializer = RecipeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetailApiView(APIView):

    def get_object(self, slug):
        '''
        Helper method to get the object with given recipe slug
        '''
        try:
            return Recipe.objects.get(slug=slug)
        except Recipe.DoesNotExist:
            return None

    # if method is GET, show the recipe with the given ID
    def get(self, request, slug, *args, **kwargs):
        '''
        Deletes the recipe with the given recipe slug (if it exists)
        '''
        recipe_instance = self.get_object(slug)
        if not recipe_instance:
            return Response(
                {"res": "Object with that recipe slug does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = RecipeSerializer(recipe_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # if method is PUT, edit the recipe with the given ID
    def put(self, request, slug, *args, **kwargs):
        '''
        Deletes the recipe with the given recipe slug (if it exists)
        '''
        recipe_instance = self.get_object(slug)
        if not recipe_instance:
            return Response(
                {"res": "Object with recipe slug does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'recipe_title': request.data.get('recipe_title'),
            'cookbook': request.data.get('cookbook'),
            'category': request.data.get('category'),
            'ingredients': request.data.get('ingredients'),
            'method': request.data.get('method'),
        }
        serializer = RecipeSerializer(instance=recipe_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # if method is DELETE, delete the recipe with the given ID
    def delete(self, request, slug, *args, **kwargs):
        '''
        Deletes the recipe with the given recipe slug (if it exists)
        '''
        recipe_instance = self.get_object(slug)
        if not recipe_instance:
            return Response(
                {"res": "Object with recipe slug does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        recipe_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
