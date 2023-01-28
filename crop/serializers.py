from rest_framework import serializers
from .models import Crop, Disease, DiseaseGallery, Gallery

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = ('title',)
        read_only_fields = ('title',)


# Disease list serializer
class DiseaseListSerializer(serializers.ModelSerializer):
    # Crop title
    crop__title = serializers.CharField(source='crop.title', read_only=True)
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Disease
        fields = ('title', 'crop__title', 'image_url', 'created_at')
        read_only_fields = ('title', 'crop__title', 'image_url', 'created_at')

    def get_image_url(self, obj):
        return obj.image.url


# Disease gallery serializer
class DiseaseGallerySerializer(serializers.ModelSerializer):
    # image url
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = DiseaseGallery
        fields = ("image_url",)
        read_only_fields = ('image_url',)
    
    
    def get_image_url(self, obj):
        return obj.image.url


# Disease detail serializer
class DiseaseDetailSerializer(serializers.ModelSerializer):
    gallery_disease = DiseaseGallerySerializer(many=True, read_only=True)
    # Crop title
    crop__title = serializers.CharField(source='crop.title', read_only=True)
    class Meta:
        model = Disease
        fields = ('title', 'crop__title', 'gallery_disease', 'description', 'created_at')
        read_only_fields = ('title', 'crop__title', 'gallery_disease', 'description', 'created_at')


# # Gallery serializer
# class GallerySerializer(serializers.ModelSerializer):
#     crop__title = serializers.CharField(source='crop.title', read_only=True)
#     class Meta:
#         model = Gallery
#         fields = ('crop__title', 'image')
#         read_only_fields = ('crop__title', 'image')

#     def get_image_url(self, obj):
#         return obj.image.url

class GallerySerializer(serializers.Serializer):
    image = serializers.ImageField()
    crop = serializers.CharField(max_length=100)

