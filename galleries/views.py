# galleries/views.py
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import ImageGallery


class GallerySelect(PermissionRequiredMixin, TemplateView):


    permission_required = 'customuser.confirmed_user'
    template_name = 'gallery_select.html'


class GalleryDetailView(PermissionRequiredMixin, DetailView):


    permission_required = 'customuser.confirmed_user'
    model = ImageGallery
    template_name = 'picture_gallery.html'
    context_object_name='imagegallery'