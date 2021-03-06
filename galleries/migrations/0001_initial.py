# Generated by Django 3.2 on 2021-07-22 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('galleryname', models.CharField(max_length=7, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='KidImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='<function KidImage.upload_kid_image at 0x7f6a35cb9430>')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='galleries.imagegallery')),
            ],
        ),
    ]
