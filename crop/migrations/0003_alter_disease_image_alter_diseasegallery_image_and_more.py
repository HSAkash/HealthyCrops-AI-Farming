# Generated by Django 4.1.5 on 2023-01-18 01:26

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crop', '0002_alter_disease_image_alter_diseasegallery_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='healthycrops'),
        ),
        migrations.AlterField(
            model_name='diseasegallery',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='healthycrops'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='healthycrops'),
        ),
    ]
