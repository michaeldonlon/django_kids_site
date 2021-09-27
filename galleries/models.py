# galleries/models.py

import os

from PIL import Image
from io import BytesIO

from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models
from django.urls import reverse



class ImageGallery(models.Model):
    

    galleryname = models.CharField(max_length=7, primary_key=True)

    def __str__(self):
        return self.galleryname

    def get_absolute_url(self):
        return reverse('gallery', kwargs={'pk': self.pk})


class KidImage(models.Model):
    

    def upload_kid_image(instance, filename):
        return 'kidimages/{0}/{1}'.format(instance.gallery.galleryname, filename)

    thekidimage = models.ImageField(upload_to=upload_kid_image, blank=True)
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE, related_name="kidimages")

    thumbnail = models.ImageField(upload_to='thumbs', editable=False, blank=True)

    def save(self, *args, **kwargs):

        if not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception('Could not create thumbnail - is the file type valid?')

        super(KidImage, self).save(*args, **kwargs)

    def make_thumbnail(self):

        image = Image.open(self.thekidimage)
        image.thumbnail(settings.THUMB_SIZE, Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(self.thekidimage.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False

        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True