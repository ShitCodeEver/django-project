from django.contrib import admin
from .models import News, Projects, ImageProject

class ImageProjectInline(admin.TabularInline):
    model = ImageProject
    extra = 2
    max_num = 4
    min_num = 2
    validate_min = True

@admin.register(News)
class AdminNews(admin.ModelAdmin):
    fields = ['name', 'anons', 'slug','full_text']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Projects)
class AdminNews(admin.ModelAdmin):
    fields = ['name', 'country', 'full_text', 'slug', 'MainImage']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageProjectInline]

# Register your models here.
