# Generated by Django 4.1.5 on 2023-01-17 18:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='healthycrops'),
        ),
        migrations.AlterField(
            model_name='diseasegallery',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='healthycrops'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='healthycrops'),
        ),
    ]
