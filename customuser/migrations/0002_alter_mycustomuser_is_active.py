# Generated by Django 3.2 on 2021-07-19 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycustomuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]