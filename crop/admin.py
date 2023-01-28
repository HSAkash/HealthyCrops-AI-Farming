from django.contrib import admin
from .models import Crop, Disease, DiseaseGallery, Gallery
import admin_thumbnails

# Register your models here.
@admin_thumbnails.thumbnail('image')
class DiseaseGalleryInline(admin.TabularInline):
    model = DiseaseGallery
    extra = 1

# Disease admin
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'crop', 'created_at')
    search_fields = ('title', 'crop__title',)
    ordering = ('title',)
    # filter by crop
    list_filter = ('crop__title',)
    list_per_page = 10
    inlines = [DiseaseGalleryInline]

# Disease gallery admin
class DiseaseGalleryAdmin(admin.ModelAdmin):
    list_display = ('disease', 'created_at')
    



# custom admin Gallery
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image','crop', 'created_at')

admin.site.register(Crop)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(DiseaseGallery, DiseaseGalleryAdmin)
admin.site.register(Gallery, GalleryAdmin)

