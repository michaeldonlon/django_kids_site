# galleries/management/commands/add_gallery.py

from datetime import date
from django.core.management.base import BaseCommand


from galleries.models import ImageGallery



class Command(BaseCommand):
    help = 'Creates a new gallery for the current month'

    def handle(self, *args, **kwargs):
        today = date.today()
        gallery_date = today.strftime("%Y_%m")
        the_gallery = {'galleryname':gallery_date}
        g = ImageGallery(**the_gallery)

        g.save()