from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'url']
    list_display_links = ('category',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['color',]
    list_display_links = ['color',]


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['producer',]


@admin.register(Yarn)
class YarnAdmin(admin.ModelAdmin):
    list_display = ['name', 'url',  'price', 'availability']
    list_display_links = ['name', ]


@admin.register(YarnImages)
class YarnImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'yarn']










