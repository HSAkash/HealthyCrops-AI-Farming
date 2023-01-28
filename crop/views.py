from rest_framework.response import Response
from django.shortcuts import  get_object_or_404
from PIL import Image
from crop.ML_deseases.diseasesClassification import CropDiseaseML

crop_disease_ml = CropDiseaseML()

from rest_framework import (
    generics,
    permissions,
    status,
    filters,
    pagination
)

from rest_framework.decorators import api_view

from .serializers import (
    CropSerializer,
    DiseaseListSerializer,
    DiseaseDetailSerializer,
    GallerySerializer
)


from .models import (
    Crop,
    Disease
)


class CropList(generics.ListAPIView):
    """
    Crop list view
    """
    serializer_class = CropSerializer
    queryset = Crop.objects.all()


class DiseaseList(generics.ListAPIView):
    """
    Disease list view
    """
    serializer_class = DiseaseListSerializer
    queryset = Disease.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'crop__title')
    pagination_class = pagination.PageNumberPagination
    # Category filter
    def get_queryset(self):
        queryset = Disease.objects.all()
        crop = self.request.query_params.get('crop', None)
        if crop is not None:
            queryset = queryset.filter(crop__title=crop)
        return queryset
    


class DiseaseDetail(generics.RetrieveAPIView):
    """
    Disease detail view
    """
    serializer_class = DiseaseDetailSerializer
    queryset = Disease.objects.all()
    lookup_field = 'title'


class UploadImage(generics.CreateAPIView):
    """
    Upload image
    """
    serializer_class = GallerySerializer
    # queryset = Disease.objects.all()
    # lookup_field = 'title'

    def post(self, request, *args, **kwargs):
        crop_title = request.POST.get('crop', None)
        image = request.FILES.get('image')
        disease = None
        if crop_title is not None:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            image = Image.open(serializer.validated_data['image'])
            crop = get_object_or_404(Crop, title=crop_title)
            if crop:
                disease = crop_disease_ml.predict(image, crop_title)
        if disease:
            return Response({'disease':disease}, status=status.HTTP_200_OK)
        return Response('Crop is not defined', status=status.HTTP_400_BAD_REQUEST)


# # Upload Image


# @api_view(['POST'])
# def ai_search(request):
#     data = request.data
#     crop = data['crop']
#     image = request.FILES.get('image')
#     image = Image.open(image)
#     print(type(image))

#     return Response('Image was uploaded')