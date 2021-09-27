# galleries/forms.py

from django import forms

from .models import ImageGallery, KidImage



class ImageGalleryForm(forms.ModelForm):
    class Meta:
        model = ImageGallery
        fields = ('galleryname',)


class KidImageForm(forms.ModelForm):
    class Meta:
        model = KidImage
        fields = ('thekidimage',)