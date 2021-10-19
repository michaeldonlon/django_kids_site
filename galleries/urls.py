# galleries/urls.py
from django.urls import path

from .views import GallerySelect, GalleryDetailView


urlpatterns = [
    path('', GallerySelect.as_view(), name='galleries'),
    path('<pk>/', GalleryDetailView.as_view(), name='gallery'),
]
