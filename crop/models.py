from django.db import models
import os
from django.utils.text import slugify
from django.utils import timezone
from cloudinary.models import CloudinaryField


# create image random name
def image_upload_to(instance, filename):
    now = timezone.now()
    base, ext = os.path.splitext(filename)
    return 'images/%s%s' % (slugify(now), ext)

# Crop model
class Crop(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title


# Crop disease model
class Disease(models.Model):
    title = models.CharField(max_length=100, unique=True)
    crop = models.ForeignKey(Crop, related_name="crop_disease", on_delete=models.CASCADE)
    # image = models.ImageField(upload_to=image_upload_to)
    image = CloudinaryField('healthycrops', blank=True, null=True)
    description = models.TextField( blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.crop.title}"


# Disease gallery model
class DiseaseGallery(models.Model):
    disease = models.ForeignKey(Disease, related_name="gallery_disease", on_delete=models.CASCADE)
    image = CloudinaryField('healthycrops', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.disease} - {self.disease.crop.title}"

# Gallery model
class Gallery(models.Model):
    crop = models.ForeignKey(Crop, related_name="gallery_crop", on_delete=models.CASCADE)
    image = CloudinaryField('healthycrops', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.image}"
