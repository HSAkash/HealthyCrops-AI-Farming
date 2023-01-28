from django.urls import path


from . import views

app_name = 'crop'

urlpatterns = [
    path('croplist/', views.CropList.as_view(), name='crop-list'),
    path('diseaselist/', views.DiseaseList.as_view(), name='disease-list'),
    path('<str:title>/', views.DiseaseDetail.as_view(), name='disease-detail'),
    path('AI_Search', views.UploadImage.as_view(), name='ai-search')
]
