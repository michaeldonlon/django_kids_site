# galleries/management/commands/upload_kid_image.py

import shutil, os
import boto3

from botocore.exceptions import ClientError
from datetime import date
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import IntegrityError
from PIL import Image

from galleries.models import KidImage, ImageGallery



class Command(BaseCommand):
    help = 'Upload images from the command line. Argument is the path to images'

    def add_arguments(self, parser):
        parser.add_argument('images_dir', type=str, help='The full path to the images being added')
        # atm its /home/centos/website_pics (or os.path.join('home','centos','website_pics'))


    def handle(self, *args, **kwargs):
        images_dir = kwargs['images_dir']
        
        the_images = os.listdir(images_dir)

        today = date.today()
        date_formatted = today.strftime("%b-%d-%Y")

        for image in the_images:
            img_path = os.path.join(images_dir, image)
            
            try:
                with Image.open(img_path) as img:
                    exif_data = img._getexif()
                    img.close()
            except:

                with open('/home/centos/error_logs/image_error_log.txt', "a") as f:
                    f.write(date_formatted+" - Failed to get EXIF data for "+image+ "\n")
                    f.close()
                shutil.move(img_path, '/home/centos/no_exif/'+image)
                continue

            full_date = exif_data[36867] # which is Exif.Image.DateTimeOriginal
            the_year = full_date[0:4:]
            the_month = full_date[5:7:]

            gallery = the_year+'_'+the_month
            img_db_destination = os.path.join('kidimages',gallery,image)

            this_gallery = {'galleryname':gallery}
            g = ImageGallery(**this_gallery)


            this_image = {
                'thekidimage':img_db_destination,
                'gallery':g,
                # 'thumbnail':thumb_destination,
            }
            t = KidImage(**this_image)

            try:
                t.save()
                s3_client = boto3.client('s3')
                response = s3_client.upload_file(img_path, settings.AWS_STORAGE_BUCKET_NAME, os.path.join('media',img_db_destination))
                os.unlink(img_path)
            except IntegrityError as e:
                with open('/home/centos/error_logs/image_error_log.txt', "a") as f:
                    f.write(e)
                    f.close()
                shutil.move(img_path, '/home/centos/failed_uploads/'+image)
            except ClientError as e:
                with open('/home/centos/error_logs/image_error_log.txt', "a") as f:
                    f.write(e)
                    f.close()
                shutil.move(img_path, '/home/centos/failed_uploads/'+image)
            except:
                with open('/home/centos/error_logs/image_error_log.txt', "a") as f:
                    f.write("failed to upload "+image+" to s3 bucket")
                    f.close()
                shutil.move(img_path, '/home/centos/failed_uploads/'+image)

            self.stdout.write(self.style.SUCCESS('added image to media/kidimages/%s' % gallery))

        self.stdout.write(self.style.SUCCESS('done'))