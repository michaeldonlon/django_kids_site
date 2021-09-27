# galleries/management/commands/upload_kid_image.py

import shutil, os

from datetime import date
from PIL import Image
from django.core.management.base import BaseCommand

from galleries.models import KidImage, ImageGallery



class Command(BaseCommand):
    help = 'Upload images from the command line. Argument is the path to images'

    def add_arguments(self, parser):
        parser.add_argument('images_dir', type=str, help='The path to the image being added')
        # default atm is ~/public_ftp/website_pics (or os.path.join('~','public_ftp','website_pics'))


    def handle(self, *args, **kwargs):
        images_dir = kwargs['images_dir']
        the_images = os.listdir(images_dir)

        image_objects = []

        today = date.today()
        date_formatted = today.strftime("%b-%d-%Y")

        for image in the_images:
            img_path = os.path.join(images_dir, image)
            
            try:
                img = Image.open(img_path)
                exif_data = img._getexif()
                img.close()
            except:

                with open('/home2/nishynax/public_ftp/image_error_log.txt', "a") as f:
                    f.write(date_formatted+" - Failed to get EXIF data for "+image+ "\n")
                    f.close()
                continue

            full_date = exif_data[36867] # which is Exif.Image.DateTimeOriginal
            the_year = full_date[0:4:]
            the_month = full_date[5:7:]

            gallery = the_year+'_'+the_month
            img_db_destination = os.path.join('kidimages',gallery,image)
            img_full_destination = '/home2/nishynax/public_html/media/'+img_db_destination
            shutil.move(os.path.join(images_dir, image), img_full_destination)

            this_gallery = {'galleryname':gallery}
            g = ImageGallery(**this_gallery)

            thumb_filename = thumb_name + '_thumb' + thumb_extension
            thumb_destination = os.path.join('thumbs/',thumb_filename)

            this_image = {
                'thekidimage':img_db_destination,
                'gallery':g,
                'thumbnail':thumb_destination,
            }
            t = KidImage(**this_image)
            t.save()

            self.stdout.write(self.style.SUCCESS('added image to media/kidimages/%s' % gallery))

        self.stdout.write(self.style.SUCCESS('done'))